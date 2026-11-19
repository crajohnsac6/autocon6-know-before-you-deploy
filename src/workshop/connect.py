"""Forward labs on request: a Forward lab of your own for working through the workshop (owner decision 2026-11-18).

Who it's for: anyone in a GitHub Codespace on their own fork of the public repository, with no Forward account. They
run ``workshop connect``; a minute later their Codespace has a Forward network in the AutoCon6 org and an API key that
can see only that network, in ``.env``. Nobody hands out credentials, and there is no server: GitHub Actions on the
public repository does the work.

How it works, in four steps:

1. **The Codespace asks.** ``workshop connect`` makes a one-time key pair (kept in the state directory), and opens a
   prefilled issue on the public repository, "Forward lab request", carrying only the public half. The person presses Create.
2. **GitHub Actions answers.** The issue starts a workflow on the public repository (the code on its default branch,
   with the AutoCon6 org admin's API key as an Actions secret, which nobody can read back). ``python -m workshop.connect
   issue`` reads who opened the issue from GitHub's own event, makes or renews their lab with forward-python-sdk, and
   replies on the issue with the credentials **encrypted to that public key**. The thread is public; the reply is
   readable only by the Codespace that asked.
3. **The Codespace reads the reply,** decrypts it with its private half, and writes ``.env`` (0600).
4. **A weekly workflow reaps** (``python -m workshop.connect reap``): labs older than 14 days are deleted, network,
   user and keys. Asking again after that gives a fresh lab.

Safety rules (from the design review):

- Every Forward name comes from the requester's GitHub numeric id (``autocon6-lab-<id>``), never the login, which can be
  renamed and reused by someone else. The id comes from the issue event, so nobody can ask for someone else's lab.
- The lab's user holds ADMIN on its one network and no org role; every new key is checked to see only that network
  before it is handed out.
- A first issue never adopts an existing user. The reaper touches only the exact names ``autocon6-lab-<digits>`` (network)
  and ``autocon6-lab-<digits>@autocon6.invalid`` (user).
- Forward is the record: the network's name carries the GitHub id and its creation time the age. No database.

The encryption (``seal``/``unseal``): X25519 key agreement with a one-time sender key, HKDF-SHA256, AES-256-GCM, from the
``cryptography`` library. Encoded as ``forward-lab:v1:<base64url(sender public key, nonce, ciphertext)>``.
"""

from __future__ import annotations

import base64
import itertools
import json
import os
import re
import secrets
import string
import sys
import time
import urllib.parse
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

PREFIX = "autocon6-lab"
EMAIL_DOMAIN = "autocon6.invalid"
PUBLIC_REPO = "forwardnetworks/autocon6-know-before-you-deploy"
TITLE = "Forward lab request"
MARKER = "<!-- autocon6-forward-lab v1 -->"
REPLY = "forward-lab:v1:"
LIFETIME = timedelta(days=14)
MAX_LABS = 200
AGAIN = timedelta(minutes=10)

OWN_NETWORK = re.compile(rf"{PREFIX}-(\d+)")  # always used with fullmatch: exact names only
OWN_EMAIL = re.compile(rf"{PREFIX}-(\d+)@{re.escape(EMAIL_DOMAIN)}")
KEY_LINE = re.compile(r"^Key: ([A-Za-z0-9_-]{43}=?)\s*$", re.MULTILINE)


def names(github_id: int) -> tuple[str, str, str]:
    """(lab id, network name, user email) for a GitHub account id."""
    network = f"{PREFIX}-{github_id}"
    return f"lab-{github_id}", network, f"{network}@{EMAIL_DOMAIN}"


# ---------------------------------------------------------------------------------------------------------------------
# Encryption: the reply on a public issue is readable only by the Codespace that asked.

_INFO = b"autocon6-forward-lab v1"


def keypair() -> tuple[bytes, str]:
    """A new one-time key pair: (private key bytes, public key as base64url text)."""
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey

    priv = X25519PrivateKey.generate()
    raw = serialization.Encoding.Raw
    return (priv.private_bytes(raw, serialization.PrivateFormat.Raw, serialization.NoEncryption()),
            _b64(priv.public_key().public_bytes(raw, serialization.PublicFormat.Raw)))


def _b64(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode().rstrip("=")


def _unb64(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def _key(shared: bytes, salt: bytes) -> bytes:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF

    return HKDF(algorithm=hashes.SHA256(), length=32, salt=salt, info=_INFO).derive(shared)


def seal(public_key: str, message: bytes) -> str:
    """Encrypt message to public_key (base64url X25519): only its private half opens it."""
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    recipient = _unb64(public_key)
    eph = X25519PrivateKey.generate()
    eph_pub = eph.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    key = _key(eph.exchange(X25519PublicKey.from_public_bytes(recipient)), eph_pub + recipient)
    nonce = secrets.token_bytes(12)
    return REPLY + _b64(eph_pub + nonce + AESGCM(key).encrypt(nonce, message, _INFO))


def unseal(private_key: bytes, sealed: str) -> bytes:
    """Open what seal made for this private key. Raises on anything else (a wrong key or a tampered reply)."""
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    if not sealed.startswith(REPLY):
        raise ValueError("not a Forward lab reply")
    blob = _unb64(sealed[len(REPLY):].strip())
    eph_pub, nonce, body = blob[:32], blob[32:44], blob[44:]
    priv = X25519PrivateKey.from_private_bytes(private_key)
    mine = priv.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    key = _key(priv.exchange(X25519PublicKey.from_public_bytes(eph_pub)), eph_pub + mine)
    return AESGCM(key).decrypt(nonce, body, _INFO)


# ---------------------------------------------------------------------------------------------------------------------
# GitHub Actions side: make, renew and reap labs (needs the AutoCon6 org admin's API key).


class Refused(Exception):
    """An answer for the requester, in plain words (posted on their issue)."""


@dataclass
class Lab:
    network_id: str
    network_name: str
    created_at: datetime | None


def _when(text: Any) -> datetime | None:
    if not text:
        return None
    if isinstance(text, datetime):
        return text if text.tzinfo else text.replace(tzinfo=UTC)
    try:
        got = datetime.fromisoformat(str(text))
    except ValueError:
        return None
    return got if got.tzinfo else got.replace(tzinfo=UTC)


def _password() -> str:
    """24 characters with every class Forward's password policy may ask for."""
    sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!#%+-=?@^_"]
    chars = [secrets.choice(s) for s in sets] + [secrets.choice("".join(sets)) for _ in range(20)]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


class Admin:
    """The org admin's view of Forward, through forward-python-sdk. Every call `workshop connect` makes is here."""

    def __init__(self, url: str, key: str, secret: str) -> None:
        from forward_sdk import ForwardClient

        self.url = url
        self.c = ForwardClient(url, username=key, password=secret, user_agent="autocon6-forward-lab")

    def networks(self) -> list[Lab]:
        return [Lab(str(n.id), n.name, _when(getattr(n, "created_at", None))) for n in self.c.networks.list()]

    def users(self) -> list[tuple[str, str]]:
        """(user id, email) for every user in the org."""
        out = []
        for row in self.c.user_accounts.list_users_with_roles():
            u = getattr(row, "user", None) or row
            out.append((str(getattr(u, "id", "")), str(getattr(u, "email", "") or getattr(u, "username", "")).lower()))
        return out

    def create_network(self, name: str) -> str:
        return str(self.c.networks.create(name).id)

    def create_user(self, email: str) -> tuple[str, str]:
        password = _password()
        user = self.c.user_accounts.create_user(body={"email": email, "password": password, "enabled": True})
        return str(user.id), password

    def reset_password(self, user_id: str) -> str:
        password = _password()
        self.c.user_accounts.update_user(user_id=user_id, body={"password": password})
        return password

    def grant(self, user_id: str, network_id: str) -> None:
        """ADMIN on this one network; no other network, no org role."""
        roles = self.c.user_accounts.get_user_roles(user_id=user_id)
        if getattr(roles, "org", None):
            raise RuntimeError(f"user {user_id} holds org roles; a lab user must hold none")
        current = getattr(roles, "network", None) or {}
        for other in current:
            if str(other) != network_id:
                self.c.user_accounts.clear_user_network_roles(user_id=user_id, network_id=str(other))
        have = current.get(network_id)
        if "ADMIN" not in str(getattr(have, "roles", have) or ""):
            self.c.user_accounts.set_user_network_role(user_id=user_id, network_id=network_id, role="ADMIN")

    def mint(self, email: str, password: str, name: str, *, retried: bool = False) -> tuple[str, str]:
        """(access key, secret) of a new API key for the lab user: Forward mints a key only for the signed-in user."""
        from forward_sdk import ForwardClient

        with ForwardClient(self.url, username=email, password=password, user_agent="autocon6-forward-lab") as me:
            current = me.user_accounts.get_current_user()
            extra = (current.model_extra or {}) | ((current.user.model_extra or {}) if current.user else {})
            if extra.get("mustSetPassword"):
                if retried:
                    raise RuntimeError(f"Forward keeps asking {email} to set a password")
                fresh = _password()
                me.user_accounts.change_current_user_password(body={"password": password, "newPassword": fresh})
                return self.mint(email, fresh, name, retried=True)
            got = me.user_accounts.create_current_user_api_token(name=name, body={"password": password})
        return str(got.token.access_key), got.secret

    def tokens(self, user_id: str) -> list[tuple[str, datetime | None]]:
        listed = self.c.user_accounts.list_user_api_tokens(user_id=user_id)
        return [(t.name, _when(t.created_at)) for t in listed.tokens]

    def delete_token(self, user_id: str, name: str) -> None:
        self.c.user_accounts.delete_user_api_token(user_id=user_id, token_name=name)

    def fence(self, key: str, secret: str, network_id: str) -> None:
        """The new key sees exactly its own network and cannot list the org's users."""
        from forward_sdk import ForwardClient
        from forward_sdk.errors import ForwardPermissionError

        with ForwardClient(self.url, username=key, password=secret, user_agent="autocon6-forward-lab") as lab:
            seen = [str(n.id) for n in lab.networks.list()]
            if seen != [network_id]:
                raise RuntimeError(f"the new key sees {len(seen)} networks, not just {network_id}")
            try:
                lab.user_accounts.list_users_with_roles()
            except ForwardPermissionError:
                return
            raise RuntimeError("the new key can list the org's users")

    def delete_user(self, user_id: str) -> None:
        from forward_sdk.errors import ForwardNotFoundError

        try:
            for name, _ in self.tokens(user_id):
                self.delete_token(user_id, name)
            self.c.user_accounts.delete_user(user_id=user_id)
        except ForwardNotFoundError:
            pass

    def delete_network(self, network_id: str) -> None:
        from forward_sdk.errors import ForwardNotFoundError

        try:
            self.c.networks.delete(network_id)
        except ForwardNotFoundError:
            pass


def issue(admin: Admin, github_id: int, now: datetime | None = None) -> dict[str, Any]:
    """Make or renew the lab for this GitHub account; return the credentials for its .env. Raises Refused."""
    now = now or datetime.now(UTC)
    if github_id <= 0:
        raise Refused("no GitHub account on the request")
    lab_id, network_name, email = names(github_id)
    nets = admin.networks()
    mine = [n for n in nets if n.network_name == network_name]
    count = sum(1 for n in nets if OWN_NETWORK.fullmatch(n.network_name))
    if len(mine) > 1:
        raise RuntimeError(f"{len(mine)} networks are named {network_name}")
    user = next((uid for uid, mail in admin.users() if mail == email), None)
    lab = mine[0] if mine else None
    if lab and lab.created_at and now - lab.created_at >= LIFETIME:  # expired, not reaped yet: start over
        if user:
            admin.delete_user(user)
        admin.delete_network(lab.network_id)
        lab, user, count = None, None, count - 1
    new = lab is None
    if new:
        if count >= MAX_LABS:
            raise Refused(f"every Forward lab is in use ({MAX_LABS}): please try again in a few days")
        if user:  # a user with no network is a leftover: never adopt it
            admin.delete_user(user)
        network_id = admin.create_network(network_name)
        try:
            user, password = admin.create_user(email)
        except Exception:
            admin.delete_network(network_id)
            raise
        created = now
    else:
        network_id, created = lab.network_id, lab.created_at or now
        if user is None:
            user, password = admin.create_user(email)
        else:
            newest = max((t for _, t in admin.tokens(user) if t), default=None)
            if newest and now - newest < AGAIN:
                raise Refused(f"a key for your lab was made {int((now - newest).total_seconds() // 60)} minute(s) ago and still works "
                              f"(in the .env of the Codespace that asked for it). For a new key, ask again after {(newest + AGAIN):%H:%M} UTC.")
            password = admin.reset_password(user)
    admin.grant(user, network_id)
    token_name = f"{network_name}-{int(now.timestamp())}"
    key, secret = admin.mint(email, password, token_name)
    try:
        admin.fence(key, secret, network_id)
    except Exception:
        admin.delete_token(user, token_name)  # never hand out a key that sees more than its lab
        raise
    for name, _ in admin.tokens(user):
        if name != token_name:
            admin.delete_token(user, name)
    return {"FORWARD_URL": admin.url, "FORWARD_USERNAME": key, "FORWARD_PASSWORD": secret, "FORWARD_NETWORK_ID": network_id,
            "WORKSHOP_LAB_ID": lab_id, "expires_at": (created + LIFETIME).isoformat(timespec="minutes"), "new": new}


def reap(admin: Admin, now: datetime | None = None) -> dict[str, list[str]]:
    """Delete Forward labs older than LIFETIME, and lab users whose network is gone."""
    now = now or datetime.now(UTC)
    users = {}
    for uid, mail in admin.users():
        if m := OWN_EMAIL.fullmatch(mail):
            users[m.group(1)] = uid
    out: dict[str, list[str]] = {"labs": [], "users": [], "errors": []}
    live = set()
    for lab in sorted(admin.networks(), key=lambda n: n.network_name):
        m = OWN_NETWORK.fullmatch(lab.network_name)
        if not m:
            continue
        if lab.created_at is None:  # unknown age: never delete on a guess, but say so
            live.add(m.group(1))
            out["errors"].append(f"{lab.network_name}: Forward gave no creation time; not reaped")
            continue
        if now - lab.created_at < LIFETIME:
            live.add(m.group(1))
            continue
        try:
            if m.group(1) in users:
                admin.delete_user(users.pop(m.group(1)))
            admin.delete_network(lab.network_id)
            out["labs"].append(lab.network_name)
        except Exception as exc:  # noqa: BLE001 - report it and carry on with the others
            live.add(m.group(1))
            out["errors"].append(f"{lab.network_name}: {exc}")
    for gid, uid in sorted(users.items()):
        if gid in live:
            continue
        try:
            admin.delete_user(uid)
            out["users"].append(f"{PREFIX}-{gid}@{EMAIL_DOMAIN}")
        except Exception as exc:  # noqa: BLE001
            out["errors"].append(f"user {uid}: {exc}")
    return out


def _answer_issue(event_path: str) -> int:
    """The issue workflow: read the event, issue, reply (encrypted) and close. Secrets come from the environment."""
    from github import Auth, Github

    event = json.loads(Path(event_path).read_text())
    issue_ = event.get("issue") or {}
    body = issue_.get("body") or ""
    if MARKER not in body or issue_.get("pull_request"):
        print("not a lab request: nothing to do")
        return 0
    gh = Github(auth=Auth.Token(os.environ["GITHUB_TOKEN"]))
    thread = gh.get_repo(os.environ["GITHUB_REPOSITORY"]).get_issue(int(issue_["number"]))
    match = KEY_LINE.search(body)
    try:
        if not match:
            raise Refused("the request has no public key: open it with `workshop connect` from your Codespace")
        try:
            seal(match.group(1), b"check")  # a key that can't be sealed to is refused before Forward is touched
        except Exception as exc:
            raise Refused("the request's key is not valid: open it with `workshop connect` from your Codespace") from exc
        creds = issue(Admin(os.environ["FORWARD_URL"], os.environ["FORWARD_ADMIN_KEY"], os.environ["FORWARD_ADMIN_SECRET"]),
                      int((issue_.get("user") or {}).get("id") or 0))
        sealed = seal(match.group(1), json.dumps(creds).encode())
        thread.create_comment(f"Your lab is ready (it expires {creds['expires_at'][:10]}). Your Codespace picks this up by itself.\n\n"
                              f"```\n{sealed}\n```")
        print(f"issued lab {creds['WORKSHOP_LAB_ID']} ({'new' if creds['new'] else 'renewed'})")
    except Refused as exc:
        thread.create_comment(f"No lab this time: {exc}")
        print(f"refused: {exc}")
    except Exception as exc:  # noqa: BLE001 - a short public line; the details stay in the workflow log
        thread.create_comment("Something went wrong making your lab; a maintainer has been told. Try `workshop connect` again later.")
        print(f"error: {type(exc).__name__}: {exc}")
        thread.edit(state="closed")
        return 1
    thread.edit(state="closed")
    return 0


def _reap_now() -> int:
    got = reap(Admin(os.environ["FORWARD_URL"], os.environ["FORWARD_ADMIN_KEY"], os.environ["FORWARD_ADMIN_SECRET"]))
    print(json.dumps(got, indent=2))
    return 1 if got["errors"] else 0


# ---------------------------------------------------------------------------------------------------------------------
# Codespace side: ask, wait for the reply, write .env.

CREDENTIAL_KEYS = ("FORWARD_URL", "FORWARD_USERNAME", "FORWARD_PASSWORD", "FORWARD_NETWORK_ID", "WORKSHOP_LAB_ID")
EXPIRES_KEY = "FORWARD_LAB_EXPIRES_AT"  # written with the credentials, so an expired lab asks again


def have_credentials(root: Path, now: datetime | None = None) -> bool:
    """Forward credentials already set and still good: Codespaces secrets, or a Forward lab in .env that hasn't expired."""
    env = root / ".env"
    text = env.read_text() if env.is_file() else ""
    if all(os.environ.get(k) for k in CREDENTIAL_KEYS[1:4]):
        return True  # Codespaces secrets win over .env (python-dotenv never overrides them): an expiry in .env is irrelevant
    if not all(re.search(rf"^{k}=.+$", text, re.MULTILINE) for k in CREDENTIAL_KEYS[1:4]):
        return False
    m = re.search(rf"^{EXPIRES_KEY}=(.+)$", text, re.MULTILINE)
    if not m:
        return True  # your own Forward: no expiry
    expires = _when(m.group(1).strip())
    return expires is not None and (now or datetime.now(UTC)) < expires  # an unreadable date counts as expired


def request_url(public_key: str, repo: str) -> str:
    body = f"{MARKER}\nKey: {public_key}\nFrom: {repo}\n\nOpened by `workshop connect`. Press **Create**: a lab is made for you and the reply goes to your Codespace."
    return f"https://github.com/{PUBLIC_REPO}/issues/new?" + urllib.parse.urlencode({"title": TITLE, "body": body})


def write_env(root: Path, creds: dict[str, Any]) -> Path:
    """Set the credentials in .env (0600), keeping any other lines."""
    env = root / ".env"
    keys = (*CREDENTIAL_KEYS, EXPIRES_KEY)
    keep = [line for line in (env.read_text().splitlines() if env.is_file() else []) if line.split("=", 1)[0] not in keys]
    lines = [f"{k}={creds[k]}" for k in CREDENTIAL_KEYS] + ([f"{EXPIRES_KEY}={creds['expires_at']}"] if creds.get("expires_at") else [])
    env.write_text("\n".join(keep + lines) + "\n")
    env.chmod(0o600)
    return env


def find_reply(issues: list[Any], public_key: str, since: datetime | None = None) -> str | None:
    """The sealed reply to a request carrying public_key, posted by GitHub Actions; None while there is none.

    A sealed reply on any of the matching requests wins: submitting the request twice is easy (each `workshop connect`
    reopens the same link), and the second one is refused ("still works") while the first holds the real reply. Only
    when no request has a reply does a refusal count, and then only one posted since this run began (``since``): an old
    refusal must not block asking again later."""
    refusal = None
    for it in issues:
        if f"Key: {public_key}" not in (it.body or ""):
            continue
        for c in it.get_comments():
            if getattr(c.user, "login", "") != "github-actions[bot]":  # only the workflow can post as this account
                continue
            body = c.body or ""
            when = _when(getattr(c, "created_at", None))
            fresh = since is None or (when is not None and when >= since)
            if REPLY in body:
                return next(line.strip() for line in body.splitlines() if line.strip().startswith(REPLY))
            if fresh and body.startswith("No lab this time") and refusal is None:
                refusal = body.removeprefix("No lab this time: ")
            if fresh and body.startswith("Something went wrong") and refusal is None:
                refusal = "the lab couldn't be made (a maintainer has been told). Try `workshop connect` again later."
    if refusal:
        raise Refused(refusal)
    return None


def run(root: Path, state_dir: Path, log, *, wait: float = 300, poll: float = 10, renew: bool = False) -> int:
    """``workshop connect``: ask for a lab, wait for the reply, write .env. Exit 0 when .env holds credentials."""
    if not renew and have_credentials(root):
        log("Your Forward lab is set (in .env, or Codespaces secrets) and hasn't expired: nothing to do. "
            "`workshop connect --renew` asks for a new key.")
        return 0
    login, repo = os.environ.get("GITHUB_USER", ""), os.environ.get("GITHUB_REPOSITORY", "")
    if not (os.environ.get("CODESPACES") and login and repo):
        log("`workshop connect` runs in a GitHub Codespace on your fork of "
            f"{PUBLIC_REPO}: fork it on GitHub, open a Codespace on your fork, then run this there.")
        return 2
    state_dir.mkdir(parents=True, exist_ok=True)
    keyfile = state_dir / "forward-lab.key"
    if keyfile.is_file():
        private, public, asked = _reload(keyfile)
    else:
        private, public = keypair()
        asked = datetime.now(UTC)
        _save(keyfile, private, public, asked)
    url = request_url(public, repo)
    log("1. Open this link (it opens by itself in a Codespace) and press Create (it asks for a Forward lab of your own, free for 14 days):")
    log(f"   {url}")
    if os.environ.get("BROWSER"):
        import webbrowser

        webbrowser.open(url)  # $BROWSER: Codespaces opens it in your own browser
    log("2. Waiting for the reply (usually under a minute) ...")
    from github import Auth, Github, GithubException

    gh = Github(auth=Auth.Token(os.environ.get("GITHUB_TOKEN", ""))) if os.environ.get("GITHUB_TOKEN") else Github()
    public_repo = gh.get_repo(PUBLIC_REPO)
    deadline = time.monotonic() + wait
    while time.monotonic() < deadline:
        try:
            # islice, not [:5]: PyGithub's list raises IndexError when slicing an empty result (no request yet)
            recent = list(itertools.islice(public_repo.get_issues(creator=login, state="all", sort="created", direction="desc"), 5))
            sealed = find_reply(recent, public, since=asked)
        except GithubException as exc:  # GitHub busy or briefly unreachable: keep waiting
            log(f"   (GitHub didn't answer this time: {exc.status}; still waiting)")
            time.sleep(poll)
            continue
        except Refused as exc:
            log(f"No lab: {exc}")
            # Shown now: from here on this refusal is old news, and the next run waits for a new answer (the key stays, so a
            # reply to an earlier request can still be read). A refusal that arrived after a run gave up is still shown.
            _save(keyfile, private, public, datetime.now(UTC))
            return 1
        if sealed:
            try:
                creds = json.loads(unseal(private, sealed))
            except Exception:  # noqa: BLE001 - never a traceback; a reply for another key is not ours
                log("The reply couldn't be opened with this Codespace's key. Run `workshop connect` again to make a new request.")
                keyfile.unlink(missing_ok=True)
                return 1
            path = write_env(root, creds)
            keyfile.unlink(missing_ok=True)
            fork_secrets(gh, repo, creds, log)
            log(f"3. Your lab is ready: network {creds['FORWARD_NETWORK_ID']}, lab {creds['WORKSHOP_LAB_ID']}, until {creds['expires_at'][:10]}.")
            log(f"   Saved in {path} (only you can read it). Next: workshop collector (downloads Forward's collector), then workshop doctor")
            return 0
        time.sleep(poll)
    log("No reply yet. If you pressed Create, run `workshop connect` again in a minute (it keeps waiting for the same request).")
    return 2


def fork_secrets(gh: Any, repo: str, creds: dict[str, Any], log) -> bool:
    """Give the fork's pull request check the same credentials, as Actions secrets. GitHub may not let a Codespace's token
    do that; then say how to do it by hand (the values are in .env)."""
    try:
        target = gh.get_repo(repo)
        for k in CREDENTIAL_KEYS:
            target.create_secret(k, str(creds[k]), secret_type="actions")
    except Exception as exc:  # noqa: BLE001 - optional: the lab works without it
        log("   For the pull request check on your fork, add the five FORWARD_*/WORKSHOP_LAB_ID values from .env as Actions secrets")
        why = getattr(exc, "status", type(exc).__name__)
        log(f"   (your fork > Settings > Secrets and variables > Actions). GitHub didn't let this Codespace do it ({why}).")
        return False
    log(f"   Your fork's pull request check has them too (Actions secrets on {repo}).")
    return True


def _save(keyfile: Path, private: bytes, public: str, asked: datetime) -> None:
    """The one-time key pair, and since when an answer counts (the request, or the last refusal shown)."""
    keyfile.write_text(json.dumps({"private": _b64(private), "public": public, "asked_at": asked.isoformat()}))
    keyfile.chmod(0o600)


def _reload(keyfile: Path) -> tuple[bytes, str, datetime]:
    data = json.loads(keyfile.read_text())
    asked = _when(data.get("asked_at")) or datetime.fromtimestamp(keyfile.stat().st_mtime, UTC)
    return _unb64(data["private"]), data["public"], asked


if __name__ == "__main__":  # GitHub Actions: python -m workshop.connect issue|reap
    what = sys.argv[1] if len(sys.argv) > 1 else ""
    if what == "issue":
        sys.exit(_answer_issue(os.environ["GITHUB_EVENT_PATH"]))
    if what == "reap":
        sys.exit(_reap_now())
    sys.exit("usage: python -m workshop.connect issue|reap")
