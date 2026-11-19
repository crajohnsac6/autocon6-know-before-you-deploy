# Know Before You Deploy: hands-on network CI/CD with Forward Predict

First run as an AutoCon6 workshop (Tucson, November 2026). Four routers, six host subnets, a pull
request, and a test stage that asks what the **network** will do after a change, before any router is touched.

**Baseline → Propose → Predict → Approve → Deploy → Verify**

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
| [`slides/`](slides/README.md) | The slides, readable on GitHub with their speaker notes ([`deck.md`](slides/deck.md) is the reveal.js source) |

## Running it yourself

### In a GitHub Codespace (easiest)

1. **Fork this repository**, then on your fork: **Code → Codespaces → Create codespace** (4 cores). When VS Code asks whether you
   trust the authors of the files, choose **Trust Folder & Continue** (it's this repository; the terminal needs it).
2. **Import Arista's cEOS image, version 4.36.0.1F.** We can't redistribute it: download the 64-bit cEOS-lab image from
   Arista with your own account, drag it into the Codespace, then `docker import <that file> ceos:4.36.0.1F` and
   `bash .devcontainer/bootstrap.sh`.
3. **Get a Forward lab:** `workshop connect`. It opens a one-click "Forward lab request" issue on this repository; GitHub
   Actions makes you a Forward network and an API key that sees only that network, and replies encrypted so only your
   Codespace can read it. A minute later the key is in your Codespace's `.env` (and, where GitHub allows it, in your
   fork's `FORWARD_LAB` Actions secret for the pull request check, step 5). The lab is free and lasts 14 days; run it again after that for a
   fresh one.
4. Then:
   ```
   workshop collector     # Forward's headless collector, matching the server's release
   workshop doctor        # fix anything it flags
   workshop up            # netlab builds and configures the lab: 3 to 10 minutes
   ```
   and follow [`docs/exercises/`](docs/exercises/README.md) (exercise 0's first steps are these). The **Your lab** page
   (port 8765; `workshop status` prints its address) shows where you are and what to run next.
5. **Before exercise 2, turn on the pull request check.** GitHub keeps a fork's workflows off until you enable them:
   your fork's **Actions** tab → **I understand my workflows, go ahead and enable them**. The check needs your lab's key
   as one Actions secret: GitHub usually doesn't let a Codespace set it, and then `workshop connect` prints the link. **Settings →
   Secrets and variables → Actions → New repository secret**, name `FORWARD_LAB`, and paste the whole of `.env` (open it
   in the editor, select all, copy). Do it again after `workshop connect --renew`. Then, to make the
   gate binding, **Settings → Rules → Rulesets → New branch ruleset** on `main`: require a pull request and the
   `forward/predict` status check. Without the ruleset the check still runs, but nothing stops a red pull request from merging.

### On your own machine, with your own Forward

You need Docker, 4 CPUs and 16 GB of memory (Debian or Ubuntu; containerlab needs sudo, and your user in the
`clab_admins` group), the cEOS image above, and a Forward network with an API key that sees only that network. Put these
in `.env`:

```
FORWARD_URL=https://fwd.app
FORWARD_USERNAME=<API key>
FORWARD_PASSWORD=<API secret>
FORWARD_NETWORK_ID=<your network's id>
WORKSHOP_LAB_ID=my-lab
```

then `bash .devcontainer/bootstrap.sh`, `uv run workshop collector`, `uv run workshop doctor`, `uv run workshop up`.

**The pull request gate on your fork:** enable Actions, add the Forward settings above as Actions secrets (each on its
own, or the five lines as one secret named `FORWARD_LAB`; where both are set, the separate ones win), and add a ruleset on `main` that requires the `forward/predict` check (without
it, nothing stops a red pull request from merging). Deploying outside a Codespace needs `GITHUB_TOKEN` and
`GITHUB_REPOSITORY` set, or use `--no-github` and a local prediction, as exercise 5 shows.

## What isn't here

What the first run at AutoCon6 used to hand out 64 labs at once: the sign-up service, the room's progress board, a Slack
bot, and the provisioning tooling. None of it is needed to run the loop: `workshop connect` replaces all of it.

## Honest notes

This ran on four cEOS routers, one change at a time, one person per lab. It hasn't been tested bigger, on other
platforms, or with many changes in flight; [Beyond the lab](docs/exercises/06-beyond.md) says what to check before you
believe it at work. And Predict got one case wrong while we built this; [the story](docs/exercises/how-it-works.md#b-a-time-the-model-was-wrong)
is why the loop doesn't stop at Predict.

Questions or fixes: open an issue. MIT licensed (`LICENSE`). Arista cEOS is Arista's, under Arista's terms, and is not
included.
