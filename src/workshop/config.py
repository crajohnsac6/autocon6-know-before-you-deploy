"""Settings for one lab, from the environment (Codespaces or Actions secrets), a local ``.env``, or ``FORWARD_LAB``: one
secret holding a whole ``.env`` (what a fork's pull request check gets, since a Codespace can't set Actions secrets). Forward credentials are read by forward-sdk itself (``FORWARD_URL``,
``FORWARD_USERNAME``, ``FORWARD_PASSWORD``, ``FORWARD_VERIFY_TLS``); nothing here prints them.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values, load_dotenv

LAB_SECRET = "FORWARD_LAB"  # one Actions secret: the whole .env that `workshop connect` wrote
LAB_KEYS = ("FORWARD_URL", "FORWARD_USERNAME", "FORWARD_PASSWORD", "FORWARD_NETWORK_ID", "WORKSHOP_LAB_ID")  # all it may set


class SettingsError(RuntimeError):
    """A required setting is missing."""


@dataclass(frozen=True)
class Settings:
    repo_root: Path
    lab_id: str
    network_id: str
    state_dir: Path
    collector_home: Path
    device_username: str
    device_password: str
    enable_password: str

    def state(self, name: str) -> Path:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        return self.state_dir / name


def repo_root(start: Path | None = None) -> Path:
    here = (start or Path.cwd()).resolve()
    for candidate in (here, *here.parents):
        if (candidate / "requirements" / "candidate.yml").is_file() and (candidate / "lab").is_dir():
            return candidate
    raise SettingsError("run workshop from inside the workshop repository")


def from_secret() -> None:
    """Fill in the lab's settings from FORWARD_LAB (a whole .env as one secret); a variable already set wins. Only LAB_KEYS:
    a machine-local line in a pasted .env (a CA path, a collector folder) must not reach CI. In Actions, the key and
    secret are registered as log masks: GitHub masks the multi-line secret as a whole, not these values on their own."""
    import io

    text = os.environ.get(LAB_SECRET, "")
    if not text.strip():
        return
    for key, value in dotenv_values(stream=io.StringIO(text)).items():
        if key not in LAB_KEYS or not (value or "").strip() or os.environ.get(key, "").strip():
            continue
        os.environ[key] = value.strip()
        if key in ("FORWARD_USERNAME", "FORWARD_PASSWORD") and os.environ.get("GITHUB_ACTIONS") == "true":
            print(f"::add-mask::{value.strip()}", flush=True)


def load(start: Path | None = None) -> Settings:
    root = repo_root(start)
    load_dotenv(root / ".env", override=False)
    from_secret()
    lab_id = os.environ.get("WORKSHOP_LAB_ID", "").strip()
    network_id = os.environ.get("FORWARD_NETWORK_ID", "").strip()
    missing = [name for name, value in (("WORKSHOP_LAB_ID", lab_id), ("FORWARD_NETWORK_ID", network_id)) if not value]
    for name in ("FORWARD_URL", "FORWARD_USERNAME", "FORWARD_PASSWORD"):
        if not os.environ.get(name, "").strip():
            missing.append(name)
    if missing:
        what = "missing settings: " + ", ".join(missing)
        if os.environ.get("GITHUB_ACTIONS") == "true":
            raise SettingsError(what + f"\nThis repository needs one Actions secret, {LAB_SECRET}: the whole .env that `workshop connect` "
                                "wrote in your Codespace (Settings > Secrets and variables > Actions > New repository secret; README step 5).")
        if os.environ.get("CODESPACES") == "true":
            raise SettingsError(what + "\nNo Forward lab here yet. Run `workshop connect`: it gets you one of your own (free, 14 days).")
        raise SettingsError(what + " (in a Codespace: `workshop connect`; on your own machine: .env, see README.md)")
    state = Path(os.path.expanduser(os.environ.get("WORKSHOP_STATE_DIR", "~/.local/state/autocon6"))) / lab_id
    collector = Path(os.path.expanduser(os.environ.get("FWD_HEADLESS_HOME", "~/.cache/autocon6/collector")))
    return Settings(
        repo_root=root,
        lab_id=lab_id,
        network_id=network_id,
        state_dir=state,
        collector_home=collector,
        device_username=os.environ.get("LAB_DEVICE_USERNAME", "admin"),
        device_password=os.environ.get("LAB_DEVICE_PASSWORD", "admin"),
        enable_password=os.environ.get("LAB_ENABLE_PASSWORD", "admin"),
    )
