# Know Before You Deploy: hands-on network CI/CD with Forward Predict

The AutoCon6 workshop WS:A4 (Tucson, November 16, 2026), as the room ran it. Four routers, six host subnets, a pull
request, and a test stage that asks what the **network** will do after a change, before any router is touched.

**Baseline → Change → Predict → Approve → Deploy → Verify**

The change is small on purpose: retire two stale BGP advertisements on r4. The obvious version of that change also takes
out the live service, two routers away, and it's perfectly valid config. Catching that before it ships is the whole point.

## What's here

| Path | What it is |
|---|---|
| [`docs/exercises/`](docs/exercises/README.md) | The exercises, start to finish, plus [how it works and where it stops](docs/exercises/how-it-works.md), [what to do when you're stuck](docs/exercises/stuck.md) and [where to read further](docs/exercises/go-deeper.md) |
| `src/workshop/` | The `workshop` command: each step is a few calls to netlab, NAPALM, the Forward headless collector, the Forward Python SDK and Git, and it prints every one |
| `lab/` | The netlab topology and the templates that build the four-router diamond |
| `requirements/`, `nqe/` | The tests: what must stay reachable, what must stay blocked, which path traffic takes |
| `candidate/`, `intent.md` | The change, and what it's supposed to do |
| `.github/workflows/forward-predict.yml` | The pull request check: the three predict steps as three job steps |
| `examples/` | A GitLab CI sketch, and the predict and upload steps written out by hand |
| `slides/deck.md` | The deck's source, with the speaker notes inline |

## Running it yourself

You need three things the workshop handed out on the day:

1. **A Forward network and an API key for it.** The workshop talks to Forward only through
   [forward-python-sdk](https://github.com/forwardnetworks/forward-python-sdk). Put these in `.env` (or, in a Codespace,
   as Codespaces secrets on your fork; the pull request check wants the same ones as Actions secrets):
   ```
   FORWARD_URL=https://fwd.app
   FORWARD_USERNAME=<API key>
   FORWARD_PASSWORD=<API secret>
   FORWARD_NETWORK_ID=<your network's id>
   WORKSHOP_LAB_ID=my-lab
   ```
2. **The Arista cEOS image, version 4.36.0.1F.** We can't redistribute it. Download the 64-bit cEOS-lab 4.36.0.1F image from
   Arista with your own account, then `docker import <that file> ceos:4.36.0.1F`.
3. **A machine with Docker, 4 CPUs and 16 GB of memory** (Debian or Ubuntu; containerlab needs sudo, and your user in
   the `clab_admins` group), or a 4-core GitHub Codespace on your fork.

Then, with the cEOS image imported first:

```
bash .devcontainer/bootstrap.sh     # uv, netlab, containerlab (a Codespace runs this for you; run it again after importing cEOS)
uv run workshop collector           # the headless collector, matching your Forward server's release
uv run workshop doctor              # fix anything it flags
uv run workshop up                  # netlab builds and configures the lab: 3 to 10 minutes
```

`workshop doctor` expects the API key to see exactly one network, the lab's: use a user scoped to that network (that's
how every seat was set up). In a Codespace the `workshop` command is already on your path. The **Your lab** page
(`uv run workshop ui`, port 8765) shows where you are and what to run next. Then follow
[`docs/exercises/`](docs/exercises/README.md) from exercise 1.

**On a fork,** to get the pull request gate too: enable Actions, add the five settings above as Actions secrets, and add a
ruleset on `main` that requires the `forward/predict` check (without it, nothing stops a red pull request from merging).
Deploying outside a Codespace needs `GITHUB_TOKEN` and `GITHUB_REPOSITORY` set, or use `--no-github` and a local
prediction, as exercise 5 shows.

## What isn't here

The event's own plumbing: the service that handed out seats, the room board, the Slack bot, and the tooling that
provisioned 64 repositories and Forward networks. None of it is needed to run the loop.

## Honest notes

This ran on four cEOS routers, one change at a time, one person per lab. It hasn't been tested bigger, on other
platforms, or with many changes in flight; [Beyond the lab](docs/exercises/06-beyond.md) says what to check before you
believe it at work. And Predict got one case wrong while we built this; [the story](docs/exercises/how-it-works.md#b-a-time-the-model-was-wrong)
is why the loop doesn't stop at Predict.

Questions or fixes: open an issue. MIT licensed (`LICENSE`). Arista cEOS is Arista's, under Arista's terms, and is not
included.
