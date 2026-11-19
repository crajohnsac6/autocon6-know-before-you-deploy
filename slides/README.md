# Know Before You Deploy: the slides

The deck from the AutoCon6 workshop, one slide per section below, readable on GitHub. Each slide's speaker notes are
folded underneath it. It is generated from [`deck.md`](deck.md) (the reveal.js source) by `slides/build_github.py`, so the
layout is simplified: step pipelines read as `A → B → C`, and the two drawn diagrams are marked where they appear.

---

<sub>Slide 1</sub>

*AutoCon6 · WS:A4 · Monday, November 16, 2026*

# Know Before You Deploy

## Hands-on network CI/CD with Forward Predict

Baseline → Propose → Predict → Approve → Deploy → Verify

*Craig Johnson · Sean Deveci · Mike Lossmann*

<details><summary>Speaker notes</summary>

Welcome. Four hours, mostly hands-on. Lab first: no long talk this morning, the why comes in short pieces between lab blocks. Introduce the three proctors, say where the helpers sit, and that raising a hand is always fine.

</details>

---

<sub>Slide 2</sub>

*Before we start*

## Four hours, and your hands are on the keyboard

- **Into the lab first.** The talk comes in short pieces between lab work. Most of today is you at a terminal
- **Stuck? Raise a hand.** Three of us are walking the room: Craig, Sean and Mike
- **Slack:** `#ac6-ws-a4`. Ask `@wsa4` anything about the lab: it knows the exercises and, once you link your seat, your last `workshop` results
- **The projector** shows the room's progress during work time. Nicknames only
- **Helpers can see** your terminal commands and `workshop` results, to find where you're stuck; `@wsa4` sees only your `workshop` results, and only once you link your seat. Secrets are masked
- **One rule:** you type the commands, we point at the line to read
- **What we keep:** your GitHub username (to hand you a seat), the nickname you pick, and your seat's commands and results (for the helpers). We never ask for your email. All of it is deleted Sunday, November 22, 8 PM Tucson. Nobody from sales will contact you about today

<details><summary>Speaker notes</summary>

Housekeeping, under two minutes. Name the three proctors and where they are standing. Say the break is 10:45 to 11:15 and we finish at 1:00. Say plainly that helpers can see each seat's recent commands (the notice is on the claim page and in the seat README), and that it is only to help. If they fall behind it is fine: every exercise has a way back (`workshop reset --to N`) and nobody is graded. Then, in your own words: this isn't a sales session. We never ask for your email, nobody will follow up, and everything you build today is yours to take: the repository goes public when we finish.

</details>

---

<sub>Slide 3</sub>

### Today

| Time | Section | Exercise |
|---|---|---|
| 9:00 | Into the lab | [0 · Launch, and take a baseline](../docs/exercises/00-launch.md) |
| 9:30 | The missing test stage | [1 · What must remain true](../docs/exercises/01-baseline.md) |
| 10:05 | Build and run the change pipeline | [2 · First change through the pipeline](../docs/exercises/02-pipeline.md) |
| 10:45 | *Break* | |
| 11:15 | Break it before you deploy it | [3 · A change that looks safe](../docs/exercises/03-break-it.md) |
| 12:00 | Fix it and prove it | [4 · Fix it](../docs/exercises/04-fix-it.md) |
| 12:30 | Deploy and verify | [5 · Deploy, collect, compare](../docs/exercises/05-deploy-verify.md) |
| 12:50 | Wrap-up and Q&A | [6 · Beyond the lab](../docs/exercises/06-beyond.md) |

<details><summary>Speaker notes</summary>

Point out that nearly all of this is keyboard time. The projector shows this deck during talks and the room board during work time.

</details>

---

<sub>Slide 4</sub>

*9:00 · Section 1 of 6*

## Into the lab

**Pre-change** → Change → Post-change → Verify

A lab of your own, running, and Forward's model of it. The talk comes later, in short pieces between lab work.

**By 1:00:** you'll have caught a broken change before it touched a router, and you'll know exactly how.

By 9:30 you have: `workshop doctor` READY, the lab up, and a baseline in Forward with `workshop baseline check` at PASS.

Presenting: Craig

<details><summary>Speaker notes</summary>

Craig opens. Exercise 0, then the four baseline steps (the start of exercise 1). Keep the talk to the slides in this section: the why comes at 9:30, once everyone has a lab and a model. Watch the board: tiles go dashed → claimed → baseline.

</details>

---

<sub>Slide 5</sub>

*Your lab*

## Four routers, a client, a service, and four more hosts

*(A drawn diagram on the presented slide.)*

<details><summary>Speaker notes</summary>

The green path is the primary one, through r2. Two of r4's three advertisements have no route behind them; retiring those is today's change request. The third carries the service. The four grey hosts (10.30.30.0/24 and 10.30.31.0/24 behind r2, 10.40.40.0/24 and 10.40.41.0/24 behind r3) give Forward more to show: get the change wrong and five places lose the service, not one.

</details>

---

<sub>Slide 6</sub>

*Where things live*

## Three places, one loop

#### This Codespace

The lab: four cEOS routers, a client, a service and four more hosts. The `workshop` command. Your **Your lab** tab.

#### Your Forward network

Forward's model of your lab, on fwd.app. Reached only through your seat's token. **Your work never needs the Forward UI**; between sections we'll look at what you just did, on the projector.

#### Your GitHub repo

`candidate/` is the change. `intent.md` says what we want. Later today, a check on your pull request decides what may merge.

<details><summary>Speaker notes</summary>

Three boxes; the attendee only ever touches the first and the third directly. Forward is driven through the CLI and the pipeline.

</details>

---

<sub>Slide 7</sub>

*Three rules*

## The rules of the game

- **PASS is the only green.** FAIL, ERROR, INCONCLUSIVE and STALE all stop a deploy. An empty answer is never a pass.
- **AI advises, the tests decide.** Forward AI can draft, review and explain. Your requirements, checked by Forward, are the judge.
- **You type the deploy.** A person approves and confirms. Nothing deploys itself.

<details><summary>Speaker notes</summary>

These three rules come back in the investigation talk and the wrap-up.

</details>

---

<sub>Slide 8</sub>

*Let's go*

## Open your Codespace

1. Go to <code>tinyurl.com/wsa4go</code> (or scan the QR code on the board) and sign in with GitHub
2. Press **Get a seat**, then **accept the invitation**
3. **Open in Codespaces**, then wait for the **Your lab** tab
4. In the terminal: <code>workshop doctor</code>, then <code>workshop up</code>
5. **Then the baseline:** four steps as soon as `workshop up` finishes (it takes 3 to 10 minutes)

On your seat page: pick an icon and a nickname (they show on the board), and link Slack with `@wsa4 i am CODE` so the bot knows your seat.  
Stuck? Ask `@wsa4` in Slack first · raise a hand if it can't sort it out · the board shows the whole room

<details><summary>Speaker notes</summary>

The short link is `tinyurl.com/wsa4go` and the QR code is on the board (switch the projector to it). Read the link out. Target: `workshop up` started by 9:08. No long talk now: while `up` builds, the three short slides about the lab play (your lab, three places, the rules), then everyone takes a baseline. Helpers walk the room for anyone stuck (the "Four fixes" slide is the cheat sheet). Icons and nicknames are optional and friendly; a helper can clear one from the helpers' desk. The Slack bot is in the channel only (no DMs).

</details>

---

<sub>Slide 9</sub>

*Work time · 9:05 → 9:15*

## Launch your lab

- Seat page: **Get a seat**, **accept the invitation**, **Open in Codespaces**
- `workshop doctor` says **READY**, then `workshop up`: 3 to 10 minutes, keep listening while it builds
- Can't push to your seat repository? Accept the invitation, then reopen the Codespace

**Why:** a lab of your own means you can break things on purpose, which you can't do in production.

Exercise 0 · **Behind?** The only must-do is `workshop up` running. Raise a hand, or `@wsa4 help seat-NN`.

<details><summary>Speaker notes</summary>

Leave this up for a minute or two, then talk through the next three slides while the labs build.

</details>

---

<sub>Slide 10</sub>

*While it builds: what you just launched*

## Your lab is a page of YAML

```yaml
# lab/topology.yml (netlab)
provider: clab
module: [ bgp ]
nodes:
  r1: { bgp.as: 65001, config: [ client-in ] }
  r2: { bgp.as: 65002 }
  r3: { bgp.as: 65003 }
  r4: { bgp.as: 65004, config: [ stale-adverts ] }
  client:  { device: linux }
  service: { device: linux }
links:
- r1: { bgp.locpref: 200 }   # prefer the path via r2
  r2:
- r1-r3
- r2-r4
- r3-r4
```

```
{# lab/stale-adverts.j2: today's problem #}
router bgp {{ bgp.as }}
   address-family ipv4
      network 10.20.30.0/24
      network 10.20.40.0/24
```

`workshop up` runs **netlab**: addresses, BGP sessions and policy come from this file; the custom bits are small templates like this one. Change the YAML, rebuild the lab.

<details><summary>Speaker notes</summary>

Shortened from the real lab/topology.yml (it also has four more hosts and the addressing plan); it's in their repository, open it. The point: a realistic multi-AS lab is a page of text you can review in a pull request. The stale-adverts template is the "decommissioned segment" they'll retire all morning.

</details>

---

<sub>Slide 11</sub>

*Take it home*

## Every piece is open source, except Forward

| Piece | What it does today |
| --- | --- |
| **netlab** | builds and configures the lab from YAML (`workshop up`) |
| **containerlab** | runs the routers and hosts as containers |
| **Netmiko** | netlab's config push at bring-up |
| **NAPALM** (+ pyeapi) | every change after that: the router's own diff, an atomic commit |
| **PyGithub, GitPython, Docker SDK** | the glue in `src/workshop/`: pull requests, commits, containers |
| **This workshop** | MIT, public: every command, YAML file and test you use today |
| Not open source | Arista cEOS-lab (free download) · GitHub Codespaces and Actions · **Forward**: the model, the queries, Predict |

github.com/forwardnetworks/autocon6-know-before-you-deploy

<details><summary>Speaker notes</summary>

Say it plainly: everything except the router image, GitHub's hosting and Forward is open source, and you can take all of it home today. Forward is the one product in the loop: the network model and what you ask of it. Pinned versions are in pyproject.toml.

</details>

---

<sub>Slide 12</sub>

*Two ways through. Same finish line*

## Pick your path

#### I'm Too Young to Die

New to CI, Git or automation? Good.

- The **Your lab** page: every step is a button, with its command shown underneath
- Commit and open the PR from the editor's panels. No Git commands
- Each exercise's **Behind?** line is your shortcut
- Ask `@wsa4` for a hint. Then another one

#### Hold My Beer

You live in a terminal.

- Terminal only: every step by hand. Read the `→` calls it prints, and open their HTTP
- Git from the CLI. Read `src/workshop/` as you go
- Side quests: write your own test, try to cheat the gate, deploy a FAIL on purpose and back it out, or give Copilot Forward's tools
- `workshop yolo` exists. Try it

Both end at `workshop verify compare` saying **MATCH**. Switch whenever you like: the page and the terminal run the same commands.

<details><summary>Speaker notes</summary>

Ten seconds, with a smile. Neither path is the lesser one: the Too Young to Die crowd see the same evidence, and plenty of experts will end up clicking at 12:15. `workshop yolo` is a hidden joke command: it always refuses, and explains why. Don't spoil what it says.

</details>

---

<sub>Slide 13</sub>

*Exercise 0 · Your editor*

## Everything is in the Codespace

- **Explorer:** the candidate, the requirements, the exercises
- **Source Control:** commit and push your change
- **GitHub Pull Requests:** open the PR, watch its check
- **Terminal:** every `workshop` command
- **Ports:** *Your lab* on 8765, if its pane is blank

<details><summary>Speaker notes</summary>

Point at each one on the projector. The Pull Requests panel is on the left bar; the Ports tab is next to the terminal. If the Your lab pane is blank, Ports, port 8765, the globe icon.

</details>

---

<sub>Slide 14</sub>

*If your lab won't start*

## Four fixes, in this order

1. **Run `workshop doctor`.** It names what is missing. Read the last line.
2. **It says settings are missing?** You opened the Codespace from the wrong place. **Delete it**, accept the GitHub invitation, then reopen from **your seat page**.
3. **Can't push?** Same cause: accept the invitation, then reopen the Codespace.
4. **Still stuck?** Ask <code>@wsa4</code> in Slack: once your seat is linked it sees your last <code>workshop</code> results and gives you the next command. Raise a hand if it can't sort it out.

Don't open a Codespace from the "repo" link on a helper's screen. That one is read only.

<details><summary>Speaker notes</summary>

Show this only if a few people are stuck at 9:15. It is the same fix the helpers use: delete the Codespace, accept the invitation, reopen from the seat page. The usual cause is a Codespace opened before the invitation was accepted, or from a read-only repository link. Helpers: the desk shows the last commands for the seat.

</details>

---

<sub>Slide 15</sub>

*Work time · 9:15 → 9:30*

## Give Forward a baseline

**Pre-change** → Change → Post-change → Verify

- When `workshop up` finishes: `workshop probe` says **8080 open**, 8443 and 2222 blocked
- `workshop baseline collect` → `upload` → `wait` → `check` (or the four buttons on the **Your lab** page)
- `check`: every requirement **PASS**: the lab is the network it should be
- Each step prints an **Evidence** line: what it just proved

**Why:** every change is judged against a known “before”.

Exercise 0, then exercise 1's "Take the baseline" · **Behind?** `workshop up` still running is fine: take the baseline when it's done. **Early?** Side quest: walk the route on r1.

---

<sub>Slide 16</sub>

*Checkpoint · 9:30*

## Lab running, baseline PASS?

- Codespace open, with the <b>Your lab</b> tab
- <code>workshop doctor</code> says <b>READY</b>
- <code>workshop baseline check</code> says <b>PASS</b>

**Behind?** A FAIL on the baseline usually means `baseline` ran before `up` finished: `workshop up` again, then the baseline steps from `collect`. Still building? Carry on listening; take the baseline when it's done.

<details><summary>Speaker notes</summary>

Most tiles should be blue (baseline) by now. If a Codespace will not start: release the seat (helpers' desk) and they press Get a seat again. If they opened it before accepting the invitation, `workshop doctor` says so: accept, then reopen from the seat page.

</details>

---

<sub>Slide 17</sub>

*Side quests*

## Ahead? Pick a side quest

| When you can start | Side quest | About |
| --- | --- | --- |
| Lab running | **Walk the route**: the real router's two paths | 5 min |
| Baseline PASS | **Interrogate the model** · **Ask Forward AI**, then check it · **Ask Forward anything (NQE)** | 10 · 5 · 10 |
| First check back | **Write your own test** | 10 min |
| Seen a red check | **Which lines are stale?** · **Blast radius**, before and after · every way of retiring them · let an adviser draft it | 5 · 10 · 10 · 10 |
| Verified | **Cheat the gate** · **Catch the drift** · **Deploy it anyway, then back it out** | 10 · 10 · 15 |

Never blocks the core steps. Behind? Skip them. They are in `docs/exercises/side-quests.md`, and the **Go further** card on your lab page tracks four of them.

<details><summary>Speaker notes</summary>

Say it once, now: the point of the day is stick time. If you finish a section early, do not wait for the room, pick one of these. They are optional, they start from where you already are, and none changes your core state except the last two, which reset first. Proctors: nudge anyone idle toward the row for where they are. Do not offer "Which lines are stale?" before someone has seen a red check; it spoils exercise 3.

</details>

---

<sub>Slide 18</sub>

*9:30 · Section 2 of 6*

## The missing test stage

Why a syntax check and a diff aren't enough, then find your way around Forward's model and see a change the Forward way.

By 10:05 you have: a path and a query you ran yourself, and a baseline at PASS.

Presenting: Craig

<details><summary>Speaker notes</summary>

Five slides of why, then hands back on keyboards. Proctors: anyone without a PASS baseline yet, help them now (the talk doesn't need them).

</details>

---

<sub>Slide 19</sub>

*The problem*

## Automation executes changes well.

What tests them first?

- A syntax check
- A code review
- Hope

<details><summary>Speaker notes</summary>

Let the room answer out loud. The point: we have good tools to push a change and weak tools to know what it will do.

</details>

---

<sub>Slide 20</sub>

*Two kinds of validation*

## Is it well formed? vs. What will it do?

#### Configuration validation

- Syntax and schema
- Linting and style
- Is the config legal?

#### Behavioral validation

- Is the service still reachable?
- Are the routes still there?
- Is what must stay blocked still blocked?

<details><summary>Speaker notes</summary>

Both matter. Only the second one tells you about an outage before you cause it.

</details>

---

<sub>Slide 21</sub>

*A realistic change*

## Valid configuration can still cut off a service.

```
router bgp 65004
   address-family ipv4
      no network 10.20.20.0/24
```

- Valid EOS. One line. A syntax check passes it.
- It stops r4 advertising the subnet your **service** lives on.

<details><summary>Speaker notes</summary>

Foreshadowing: later today they write a change like this on purpose and watch it get stopped.

</details>

---

<sub>Slide 22</sub>

*What catches this today*

## Four checks, and what each one can't see

| Check | It sees | It can't see |
| --- | --- | --- |
| **Syntax and lint** | the config is legal | what it does |
| **Peer review** | a diff of one device | the effect on the others |
| **Change window** | nothing yet | you find out by deploying |
| **A lab copy** | the lab you built | whether it still matches production |

<details><summary>Speaker notes</summary>

Ask who relies on each one. None of them is wrong. None of them answers "what will the network do after this change?"

</details>

---

<sub>Slide 23</sub>

*Why review misses it*

## The line is on r4. The damage is on r1.

*(A drawn diagram on the presented slide.)*

A reviewer reading r4's diff sees one removed line. Nothing in the diff says *r1 loses a route*.

<details><summary>Speaker notes</summary>

This is exactly what they will see in exercise 3. Plant it now: the cause and the symptom are on different devices.

</details>

---

<sub>Slide 24</sub>

*Before you open it*

## What Forward does with what it collects

**Collect**config and state from every device, read-only (your ZIP)→**Normalize**one vendor-neutral model: devices, interfaces, routes, ACLs, BGP→**Compute**every path a packet could take, worked out from the model, not sampled→**Ask**path searches, diffs, and NQE queries (2,000+ built in), against that model

- **Normalized config and state:** the same question works on Arista, Cisco or Juniper: `workshop data routes`
- **Mathematical verification:** not a ping from one place. Forward computes the forwarding behavior of the whole network: `workshop path`
- **A query language:** anything else about the network, as an NQE query: `workshop nqe` (and later today, your path searches become intent checks)

<details><summary>Speaker notes</summary>

Two minutes, then hands back on keyboards. The point: Forward doesn't log in to routers to answer questions. It collected once (that's the ZIP they uploaded), turned every vendor's config and state into one model, and computes answers from it, so "can the client reach the service?" is answered for every path, not by sending one packet. The three bullets are the three commands they run next. Keep it plain: no product tour, the UI stays closed.

</details>

---

<sub>Slide 25</sub>

*Work time · 9:35 → 9:45*

## Meet Forward

**Pre-change** → Change → Post-change → Verify

- `workshop data inventory`, `data topology`, `data vulns` (which CVEs hit these routers), `data routes --prefix 10.20.20.0/24`
- `workshop path`: follow the service path hop by hop. `workshop path --port 2222`: delivered, but denied at r1
- Forward's own NQE library (2,000+ ready-made queries): `workshop nqe "/L3/BGP/Established BGP Peerings"`, `"/Interfaces/Interface Status Query"`, `"/L2/CDP and LLDP"`

**Why:** none of this touched a router. It is Forward's model, built from the ZIP you uploaded.

Exercise 1 · **Behind?** `workshop path` and the NQE query; skip the rest. **Early?** Side quests: interrogate the model, or ask Forward AI.

<details><summary>Speaker notes</summary>

Point out the library queries ship with Forward and work on any network; writing their own (and meeting today's change request) is lab 2.

</details>

---

<sub>Slide 26</sub>

*What changes*

## Test the result, not the diff

- Say what must stay true, **once**, as tests: reachable, blocked, the path
- Ask Forward what the network will do **after** the change, not what the text says
- Run the same tests on every change, and again on the real network after deploy

The tests are files in a repository. They are reviewed, versioned and reused.

<details><summary>Speaker notes</summary>

The shift: from reading configuration to stating intent. The tests are the part you keep.

</details>

---

<sub>Slide 27</sub>

*The honest limit*

## A test you didn't write can't fail

- A check is only as good as your requirements
- And a model can be wrong: we caught one modelling an ACL edit no real router would accept
- That is why the baseline step matters: it's where you write down what must stay true
- AI can draft a change and explain a failure. Only the requirements decide

Start small: three requirements for one kind of change beats a perfect model you never finish.

<details><summary>Speaker notes</summary>

Be straight about this. The value is not magic in the tool; it's that "what must stay true" becomes executable, and gets checked every time. The ACL story (docs/exercises/how-it-works.md, section b): on an early development build, Predict accepted a duplicate ACL sequence number that real cEOS rejects, and modelled both entries. We switched scenarios. It's why deploy render compares the model's diff with the router's, and why verify collects again.

</details>

---

<sub>Slide 28</sub>

*The change loop most teams run*

## Pre-change → change → post-change → verify

**Pre-change**collect the network as it is: your baseline  
NAF: Collector → Observability→**Change**push the config to the router  
NAF: Executor→**Post-change**collect it again  
NAF: Collector → Observability→**Verify**compare: what moved, who lost reach, does it still work?  
NAF: Observability

You'll run this loop next with Forward. Good loop. One catch: you only learn the answer **after** the change is live.

<details><summary>Speaker notes</summary>

One minute. This is the operational loop most teams already have, mapped to the NAF framework blocks. Exercise 1's "See a change" is exactly this loop, and at 10:10 they'll run it with a real (bad) change. Don't mention Predict yet: the gap ("you only learn after") is the setup for 10:20.

</details>

---

<sub>Slide 29</sub>

*Work time · 9:50 → 10:05*

## See a change the Forward way

Pre-change → Change → Post-change → Verify

- **Make a change: shut r2's link to r4** (or `workshop link down`), then the four baseline steps: ROUTE-SERVICE and PATH-SERVICE **FAIL**, on purpose
- **What changed: everything Forward sees** (`workshop data changes`): links, configs, interfaces, routes, ARP/MAC, ACLs, site reachability, and Forward's own BGP and LLDP queries, before against after
- Then the detail: **routes** (what moved) · **reachability** (Branches ↔ Service) · `workshop path` (still works, now via r3. Is that OK? Hold that thought)
- **Undo the change**, then the four baseline steps once more: every line **PASS**

**Why:** Forward tells you what moved and who lost reach. Whether it matters is your intent: lab 2.

Exercise 1 · **Behind?** Skip it: a PASS baseline is all exercise 2 needs. If you shut the link, undo it and take the baseline again.

---

<sub>Slide 30</sub>

*Checkpoint · 10:05*

## Ready for a change?

**Pre-change** → Change → Post-change → Verify

- You followed one path hop by hop and ran one NQE query
- Made the change? It's undone, and your newest baseline says <b>PASS</b>
- <code>workshop baseline check</code> says <b>PASS</b>

**Behind?** A FAIL on the baseline usually means `baseline` ran before `up` finished. Run `workshop up` again, then the baseline steps from `workshop baseline collect`.

<details><summary>Speaker notes</summary>

Most tiles should be blue (baseline). Hands up for anyone with a FAIL on the baseline. Ask someone to read out their 2222 path: DELIVERED but DENIED at r1. Fill time: the router CLI tour (`netlab connect r1`) and the Forward AI prompts (exercise 1 extras).

</details>

---

<sub>Slide 31</sub>

*10:05 · Section 3 of 6*

## Build and run the change pipeline

Baseline → **Propose** → **Predict** → Approve → Deploy → Verify

Send a one-prefix change through Git, CI and Forward Predict, and read the result.

By 10:45 you have: a pull request open, the **forward/predict** check run, and its verdict read. A red here is expected: not done yet.

Presenting: Craig (the hint), then Sean

<details><summary>Speaker notes</summary>

Exercise 2. Open .github/workflows/forward-predict.yml and src/workshop/forward.py on the projector. Code and requirements come from main, so a PR cannot weaken its own test.

</details>

---

<sub>Slide 32</sub>

*A true story, probably yours*

Friday, 4:55 PM. The diff is three lines.🙂👍 → 🔥📟"It's just removing some old network statements."

<details><summary>Speaker notes</summary>

Five seconds, let them laugh. Then: "Hands up if you've been paged by a three-line change." Next slide: when do you find out?

</details>

---

<sub>Slide 33</sub>

*Three ways to find out*

## When do you learn the change broke something?

|  | What runs | What tells you | When |
| --- | --- | --- | --- |
| **1** | Deploy **without Predict**, collect before and after, diff | 3 routes deleted on r1, r2, r3; Branches, Data centre and Client edge lose the Service. Is that bad? You have to know. | After it's live |
| **2** | Same, with the intent checks | Forward says APP-EXISTING and PATH-SERVICE FAIL, in the change ticket. Back it out. | After it's live |
| **3** | Predict, with the intent checks, then deploy, then verify | The same FAILs, on the predicted network | **Before any router changes** |

Next ten minutes: **you** do 1 and 2, with Predict overridden (please don't do this at work). Then the rest of the morning is 3.

<details><summary>Speaker notes</summary>

Craig, one minute, before handing to Sean. Don't demo it: tease it. "The next ten minutes, you'll do what a lot of us do on a Tuesday: push a change nobody checked first. Then Forward will tell you how it went. Spoiler: you won't like it." They run it themselves (next slide); proctors watch for anyone who forgets to back it out.

</details>

---

<sub>Slide 34</sub>

*The story starts here*

## Your critical flows become Forward intent checks

| Requirement (Git) | Forward intent check | On your baseline |
| --- | --- | --- |
| **APP-EXISTING** 8080 must get through | Existential path check | PASS |
| **MGMT-DENY** 2222 must be blocked | Isolation path check | PASS |
| **PATH-SERVICE** via r1 → r2 → r4 | Existential, through r2 | PASS |
| **STALE-CLEARED** no inert BGP statements | NQE check (the query, in Forward's library) | FAIL: the 2 stale lines, the finding to fix |

`workshop intent` (or the page's button) turns your lab 1 path searches into these checks, and Forward judges every snapshot from then on: the baseline, every change you make, the network after a deploy. **Forward is the Collector here** (NAF): the headless collector's ZIP, named by its SHA-256 in every change record, is the snapshot it models.

<details><summary>Speaker notes</summary>

This is the spine of the day: the flows you care about are written once, in Git, and Forward holds them as intent checks. From now on every snapshot answers "do my critical flows still work?" Point out that STALE-CLEARED failing is the point: it's the finding the change request will clear. Ask: in your network, what are the three flows you'd put here first?

</details>

---

<sub>Slide 35</sub>

*Work time · 10:10 → 10:20 · don't try this at work*

## Ship it. What could go wrong?

PREDICT OVERRIDDEN

Baseline → **Propose** → Predict → Approve → **Deploy** → **Verify**

- **First:** your own question, `workshop nqe nqe/stale_bgp_advertisements.nqe`: **today's change request**. Then turn your path searches into intent checks (`workshop intent`, or the Deploy stage's button)
- **Propose:** retire **all three** statements (tick them on the Propose stage, or edit the file). Don't commit
- **Deploy without Predict** (the Deploy stage, or `workshop deploy apply --without-predict --confirm HASH`): it opens a change ticket
- **Verify**, five steps: **FAIL**. Open the ticket (your repo's **Issues** tab): Forward says what broke, after the fact
- **Back it out:** Revert: plan → apply → the baseline steps → compare: **MATCH**. Then empty the candidate

**Why:** so you know exactly what the next two hours are saving you from.

Exercise 2, first part · **Behind?** Skip it: the pipeline is the core.

---

<sub>Slide 36</sub>

*Add a loop in front*

## Design → predict → test, then the loop you know

**Design**the change, and the tests it must pass, in Git  
NAF: Intent→**Predict**Forward models the network *with* the change. No router touched  
NAF: Observability→**Test**your requirements on the predicted network: only PASS goes on  
NAF: Orchestrator, with a person

**Pre-change**still current?→**Change**exactly the bytes that passed  
NAF: Executor→**Post-change**collect again→**Verify**reality matches the prediction

Same questions you asked at 10:10. Now you ask them **before** the change.

<details><summary>Speaker notes</summary>

The turn of the morning. The design loop (NAF Intent → Observability → Orchestrator) is new; the operational loop below is the one they just ran by hand, now gated. Predict appears here for the first time. Hand over to Sean after this slide.

</details>

---

<sub>Slide 37</sub>

*Your morning, step by step*

## Same loop, two ways to drive it

| Stage | I'm Too Young to Die: click | Hold My Beer: type |
| --- | --- | --- |
| **0 Start** | **Start the lab**, then **Check my setup** | `workshop up`, `workshop doctor` |
| **1 Baseline** | **1. Collect** → **2. Upload** → **3. Wait for the model** → **4. Check** | `workshop baseline collect`, `upload`, `wait`, `check` |
| **2 Propose** | tick what to retire, **Write candidate/r4-bgp.eos**, **Open pull request** | edit `candidate/r4-bgp.eos`, branch, commit, push, open the PR |
| **3 Predict** | watch **forward/predict** on your PR (or **1. Change set** → **2. Predict** → **3. Check**) | `workshop predict changeset`, `run`, `check` |
| **4 Approve** | merge the pull request on GitHub, only when the check is green | |
| **5 Deploy** | **1. Gates** → **2. Render** → **3. Apply** → **4. Read back** | `workshop deploy gates`, `render`, `apply`, `readback` with `--pr N --confirm HASH` |
| **6 Verify** | **1. Probe** → **2. Collect** → **3. Upload** → **4. Wait for the model** → **5. Compare** | `workshop verify probe`, `collect`, `upload`, `wait`, `compare` |

Finish line, either way: **MATCH**. Every button runs the command next to it, and shows it under the button.

<details><summary>Speaker notes</summary>

Talk it through top to bottom, once, about a minute: this is the whole morning. Point out that each row is a section of the day (into the lab 9:00, the why at 9:30, the pipeline 10:05, break it 11:15, fix it 12:00, deploy and verify 12:30). The buttons and the commands are the same thing: a Too Young to Die person who peeks under a button is reading the Hold My Beer column. Nobody needs to remember this slide: the Your lab page always shows the next step.

</details>

---

<sub>Slide 38</sub>

*The software pattern*

## CI/CD, for the network

**Propose**a pull request→the missing stage**Tests**of network behavior→**Gate**only PASS gets through→**Deploy**exactly what was tested→**Verify**reality matches

Pull requests, automated tests and gates are familiar. What was missing was a test stage that *understands the network*, and a last stage that checks reality against the prediction. That last check is what closes the loop.

<details><summary>Speaker notes</summary>

Everyone in software knows this picture. Networks had the pipeline but not the tests.

</details>

---

<sub>Slide 39</sub>

*How it works*

## A model of your network

**Your network**configs and state, collected→**Forward model**a snapshot you can query→**Predict**apply a proposed change to the model→**Predicted network**no device touched→**Your tests**pass or fail

Test the *result* of a change before it exists.

<details><summary>Speaker notes</summary>

Forward builds a model from what it collects. Predict applies candidate changes to that model and lets you run the same tests on the outcome. No router is touched.

</details>

---

<sub>Slide 40</sub>

*The pipeline you will run*

## Six stages. Only a PASS moves on.

1 Baseline → 2 Propose → 3 Predict → 4 Approve → 5 Deploy → 6 Verify

Where it runsYour terminalYour editor, then a pull requestGitHub Actions, with ForwardGitHubYour terminal, then r4Your terminal, with Forward

What it checksA known start, fingerprintedOnly `candidate/` changesYour tests, on the predicted networkA person merges a green checkExactly the predicted lines, if nothing driftedReality agrees with the prediction

The steps you type`baseline collect` … `check`edit, commit, open the PRruns for you on every PRSquash and merge`deploy gates` … `readback``verify probe` … `compare`

<details><summary>Speaker notes</summary>

Walk left to right once. Each stage checks one thing; we come back to those, and their limits, at the end. Every stage is a few commands you run one at a time: each prints the real call it makes and the evidence it leaves.

</details>

---

<sub>Slide 41</sub>

*Why a change workflow, and where it fits*

## Automation made changes fast. A workflow makes them safe

| Stage | NAF Framework block | What it adds |
| --- | --- | --- |
| **Propose** | Intent | The change and the tests it must pass, in Git: reviewable, versioned, one source |
| **Baseline, Predict** | Collector → Observability | A model of the real network, and the change applied to it before any router is touched |
| **Approve** | Orchestrator, with a person | Only a PASS can merge, and a person merges it |
| **Deploy** | Executor | Exactly the lines that were predicted, and only if nothing drifted |
| **Verify** | Collector → Observability | The real network checked against the prediction: the loop closes |

Swap any block for the tool you use; the workflow is the part that carries over. Nothing reaches the network without evidence, and nothing is done until the network agrees.

<details><summary>Speaker notes</summary>

The point to land: pushing config is a solved problem; knowing what it will do is not. A valid, reviewed change can still take out a service two routers away (you'll do exactly that at 11:15). The workflow is what puts evidence between "I wrote it" and "it's live", and the NAF Framework (reference.networkautomation.forum) gives us shared names for the parts. We come back to this map at the wrap-up with what you actually ran.

</details>

---

<sub>Slide 42</sub>

*Live walkthrough · 10:20*

## How a change becomes a verdict

**Pull request**changes `candidate/r4-bgp.eos`→**CI job**code and tests come from `main`→**Baseline check**yours, unchanged→**Predict**a change set on your baseline→**Judge**your tests, on the predicted network

**Why does the CI job take the tests from `main`, not from the pull request?**

<details><summary>Speaker notes</summary>

Open `.github/workflows/forward-predict.yml` and `src/workshop/predict.py` on the screen. Answer: a pull request must not be able to weaken its own test. Only the candidate file comes from the PR.

</details>

---

<sub>Slide 43</sub>

*Work time · 10:25 → 10:45*

## Your first change through the pipeline

Baseline → **Propose** → **Predict** → Approve → Deploy → Verify

- Retire **one** stale advertisement on a new branch, and open a pull request
- Watch **forward/predict**. Expect only `STALE-CLEARED` to fail: that's "not done yet"
- Read the workflow and `predict.py` while you wait

**Why:** this puts a test inside the pull request review you already do.

Exercise 2 · **Behind?** This one is skippable: go straight to exercise 3. **Early?** Side quest: write your own test.

---

<sub>Slide 44</sub>

*Predict is an API call*

## From Python, a few lines

```python
handle = client.change_sets.create(name, snapshot_id=baseline_id)
handle.set_commands("r4", candidate_text)        # the exact lines you will deploy
snapshot = handle.predict_and_wait(label)         # Forward builds the predicted network
report = evaluate(requirements, observer(snapshot.id))   # your tests, on that network
```

Simplified from `src/workshop/forward.py` and `predict.py`. The Forward Python SDK makes every call.

<details><summary>Speaker notes</summary>

Emphasise "programmable part of a pipeline, not a UI walkthrough". The candidate text is the same bytes NAPALM later sends to the router.

</details>

---

<sub>Slide 45</sub>

*Tests are code*

## Each requirement is a behavioral test

```yaml
- id: APP-EXISTING
  kind: flow
  port: 8080
  expect: permit
  title: The existing application still works

- id: ROUTE-SERVICE
  kind: route
  device: r1
  prefix: 10.20.20.0/24
  next_hop: 10.255.0.2
```

Four kinds: **flow**, **route**, **path** and **nqe** (a query over the network). Reviewed and versioned like any code.

<details><summary>Speaker notes</summary>

Show requirements/candidate.yml. Five tests today. They can write their own in the stretch work.

</details>

---

<sub>Slide 46</sub>

*The evidence*

## What was predicted, against what

- the candidate's hash
- the baseline it was predicted against, and its fingerprint
- the requirements' hash
- the change set and predicted snapshot
- every result, with what Forward observed

#### Why it matters

Deploy refuses unless the evidence matches: the same candidate, the same tests, the same baseline, and routers that haven't drifted.

<details><summary>Speaker notes</summary>

This is the bridge to the deploy guards later. `evidence/evidence.json` on the Codespace.

</details>

---

<sub>Slide 47</sub>

*Checkpoint · 10:45*

## Did your pull request get a verdict?

Baseline → **Propose** → **Predict** → Approve → Deploy → Verify

- Your pull request is open from its own branch (not <code>main</code>)
- The <b>forward/predict</b> check ran, and you read its summary
- You know which requirement failed, and why

**Behind?** The check can queue for a few minutes while GitHub starts it: the page and the PR say so. Read the pipeline code while you wait.

<details><summary>Speaker notes</summary>

Tiles show predicting, then red. This red is expected. Watch how long tiles stay predicting; if fwd.app queues, tell the room it is the wave and keep reading code. If GitHub Actions is slow, see the handbook runbook.

</details>

---

<sub>Slide 48</sub>

*10:45 → 11:15*

## Break

Back at 11:15. If your Codespace naps while you're away, `workshop up` wakes it. Coffee does the same for you.

---

<sub>Slide 49</sub>

*11:15 · Section 4 of 6*

## Break it before you deploy it

Baseline → **Propose** → **Predict** → Approve → Deploy → Verify

Make a change that looks valid, and watch Predict catch the damage before any router is touched.

By 12:00 you have: a predicted FAIL, the line responsible found, and proof the real network is untouched.

Presenting: Mike

<details><summary>Speaker notes</summary>

Handoff: Sean → Mike. Exercise 3. All three network statements look the same: finish the job. The retire-all PR goes red (APP-EXISTING, ROUTE-SERVICE and PATH-SERVICE fail). `workshop probe` proves the live network is untouched. At 11:40 walk the investigation on the projector.

</details>

---

<sub>Slide 50</sub>

*11:15 · Break it before you deploy it*

## All three look alike. Finish the job.

```
router bgp 65004
   address-family ipv4
      no network 10.20.20.0/24
      no network 10.20.30.0/24
      no network 10.20.40.0/24
```

- Valid EOS. Three lines. A syntax check passes it.
- Open the pull request and watch the gate.
- Your routers are **not touched**.

<details><summary>Speaker notes</summary>

Set up the exercise: they make this change on purpose. Remind them to run `workshop probe` afterwards to see the real network is unchanged.

</details>

---

<sub>Slide 51</sub>

*Work time · 11:15 → 11:40*

## Break it, and read why

Baseline → **Propose** → **Predict** → Approve → Deploy → Verify

- Make the change above, open the PR, watch **forward/predict** go red
- Which tests failed? What did Forward observe?
- `workshop probe`: the real network is unchanged

**Why:** valid, short, looks right, and it cuts off the service. The cause is on r4, the damage on r1.

Exercise 3 · **Behind?** Steps 1 to 3 and read the summary. Skip the AI discussion. **Early?** Once you have seen a red check: which lines are stale?

---

<sub>Slide 52</sub>

*11:40 · Investigation*

## Read the verdict

Baseline → Propose → **Predict** → Approve → Deploy → Verify

| Requirement | Result | Forward observed |
| --- | --- | --- |
| APP-EXISTING | FAIL | BLACKHOLE |
| MGMT-DENY | PASS | still blocked |
| ROUTE-SERVICE | FAIL | r1 has no route to 10.20.20.0/24 |
| PATH-SERVICE | FAIL | not delivered |
| STALE-CLEARED | PASS | 0 stale advertisements |

The stale advertisements are gone, and the service is gone with them. On your pull request: the **Change analysis**. It opens as a change request: **why** (Forward's finding on your baseline), **the risks Forward already saw** (every host reaches the service through r4; 2222 stays blocked), **the exact config**, **when**. Then every host's reach, before and after, and which sites lose the Service.

<details><summary>Speaker notes</summary>

Have them scroll the PR's Conversation to the Change analysis comment: it's the wow moment. Start at "1 · The change request": Forward named the risk (5 of 5 hosts reach the service through r4) before anyone wrote a line of config; the reviewer reads the same page. The "Every host to the service" table shows all five hosts losing the service from one line on r4. Read a real red check from the room if someone volunteers. The "stale cleared" pass is the trap: the change achieved its goal and broke the network.

</details>

---

<sub>Slide 53</sub>

*Follow the evidence*

## Why does the whole diamond lose the route?

Baseline → Propose → **Predict** → Approve → Deploy → Verify

**r4**stops advertising `10.20.20.0/24`→**r2, r3**lose the route→**r1**has no route to the service→**client**TCP 8080 blackholed

Which of the three statements carried the service? How could you have known **before** the change?

<details><summary>Speaker notes</summary>

Let a couple of people answer. The service prefix is directly connected on r4; its network statement is what puts it into BGP. The stale two have no route behind them.

</details>

---

<sub>Slide 54</sub>

*AI advises, Predict decides*

## Ask Forward AI, then check it

Baseline → Propose → **Predict** → Approve → Deploy → Verify

#### Asked with no context

"Why can the client no longer reach the service?"

Blames r1 and suggests a static route there. Right symptom, wrong cause.

#### Given the facts

"This change removes these three statements. With it, the client can't reach the service. Which caused that?"

Names `network 10.20.20.0/24` as the culprit.

**Framing matters. The requirements, on the predicted network, are the judge.**

It shows its work: when it ran NQE queries, **How it got that** under the answer lists them. Run one yourself with `workshop nqe`.

<details><summary>Speaker notes</summary>

From our own rehearsal on fwd.app. The lesson is not "AI is bad" but "AI output is advice to be checked". Prediction is the check. The "How it got that" fold on the lab page (and the end of `workshop ask`) shows the queries Forward AI wrote: running its query is one way to check what it said; the requirements on the predicted network are still the judge.

</details>

---

<sub>Slide 55</sub>

*Work time · 11:40 → 12:00*

## Find the line responsible

Baseline → Propose → **Predict** → Approve → Deploy → Verify

- Compare with your first pull request: what's different?
- `workshop explain` (after the local predict steps)
- Finished early? `workshop matrix` predicts every combination

Exercise 3, continued

---

<sub>Slide 56</sub>

*Checkpoint · 12:00*

## Did Predict catch it?

Baseline → Propose → **Predict** → Approve → Deploy → Verify

- Predict said <b>FAIL</b> on your change
- You can say which requirements broke, and why
- <code>workshop probe</code> still shows 8080 open: nothing was deployed

**Behind?** Run the predict steps on your change (`workshop predict changeset`, `run`, `check`), then `workshop explain` for the plain-words reason, or ask a proctor to walk it with you.

<details><summary>Speaker notes</summary>

About 11:35 most tiles are red and the feed shows a change was held at the gate before deploy. Discussion: the chat that blames r1. AI advises, Predict decides.

</details>

---

<sub>Slide 57</sub>

*And a time it didn't*

## Predict got one wrong while we built this

- Our first scenario changed an ACL line on r1 by resending sequence 10 with a new port
- Real cEOS rejects that: <code>% Error: Duplicate sequence number</code>, and keeps the old entry
- Predict, on the development build we were using, accepted it and modelled both entries. No router could hold that config
- So we changed scenarios. And it's why the loop doesn't stop at Predict: <code>deploy render</code> shows Forward's diff next to the router's own, and <code>verify</code> collects the real network again

That was a from-source build, not the fwd.app release, and we didn't retest it on the release. The whole story: How it works, section b.

<details><summary>Speaker notes</summary>

Tell it straight, no spin. The point isn't "the model is bad". Any model is a model, and a good pipeline assumes it will be wrong sometimes and checks. That's why render and verify exist. If someone asks whether it's fixed: we don't know, we didn't retest that case on the release.

</details>

---

<sub>Slide 58</sub>

*12:00 · Section 5 of 6*

## Fix it and prove it

Baseline → **Propose** → **Predict** → **Approve** → Deploy → Verify

Finish the job safely, let it through the gate, and merge.

By 12:30 you have: a candidate Predict judges PASS, and the pull request merged.

Presenting: Mike

<details><summary>Speaker notes</summary>

Exercise 4. Fix, push, green, merge. Show a merge refused on the red retire-one PR. Fill: workshop agent on a scratch branch.

</details>

---

<sub>Slide 59</sub>

*Work time · 12:00 → 12:30*

## Fix it, and let it through the gate

Baseline → **Propose** → **Predict** → **Approve** → Deploy → Verify

- Keep the live advertisement. Push the fix to the same branch
- **forward/predict** re-runs: a regression test on every commit
- Green? **Merge** (Squash and Merge). Only a green check can

**Why:** the fix goes through the same gate. No shortcuts, for anyone.

Exercise 4 · **Behind?** Retire only the two stale advertisements, open the PR, merge when green. **Early?** Side quest: every way of retiring the lines, or let an adviser draft it.

---

<sub>Slide 60</sub>

*Checkpoint · 12:30*

## Is it green and merged?

Baseline → **Propose** → **Predict** → **Approve** → Deploy → Verify

- <b>forward/predict</b> says PASS on the fixed change
- The pull request is <b>merged</b> into main
- Your lab is still at its baseline: nothing deployed yet

**Behind?** Stuck on red? Pair with a finished neighbor, or use **Behind or stuck? Catch me up** on your lab page.

<details><summary>Speaker notes</summary>

About 12:20 tiles go green, then approved. Help anyone still red and pair them with a finished neighbor.

</details>

---

<sub>Slide 61</sub>

*12:30 · Section 6 of 6*

## Deploy and verify

Baseline → Propose → Predict → Approve → **Deploy** → **Verify**

Send exactly what Predict approved, then check that reality matched the prediction.

By 12:50 you have: the change deployed to r4, and `workshop verify compare` saying MATCH.

Presenting: Sean

<details><summary>Speaker notes</summary>

Handoff: Mike → Sean. Exercise 5. `workshop deploy gates`, `render`, `apply`, `readback` (with `--pr N --confirm HASH`), then the five verify steps. Put `deploy render` on the projector: one change, the same lines in Forward's model and in r4's own diff. Then the change window (optional, 3 minutes): `workshop deploy apply ... --at `, and while it counts down `workshop link down` in a second terminal: at the window, NOT DEPLOYED (STALE). The approval is for the network Forward predicted, not whatever it has become. Then `workshop link up` (the fingerprint matches again) before deploying for real. Fill: the drift experiment (hand edit, verify MISMATCH), then `workshop restore` and the baseline steps.

</details>

---

<sub>Slide 62</sub>

*Work time · 12:30 → 12:50*

## Deploy, collect, compare

Baseline → Propose → Predict → Approve → **Deploy** → **Verify**

- Copy the deploy command from the top of the green check's summary
- `workshop deploy gates` → `render` → `apply` → `readback`: you type the hash
- `workshop verify probe` … `compare` → **MATCH**
- Real changes wait for a window: **Apply at the window** (or `--at HH:MM`) checks every gate now and again when it opens. Change a router in between: **STALE**, nothing sent

**Why:** approval only counts if what you deploy is what was approved, against the network Forward predicted, and you check that reality agreed.

Exercise 5 · **Behind?** Three steps: sync `main`, deploy, verify. **Early?** Side quests: cheat the gate, catch the drift.

---

<sub>Slide 63</sub>

*Checkpoint · 12:50*

## Did reality match the prediction?

Baseline → Propose → Predict → Approve → **Deploy** → **Verify**

- <code>workshop deploy</code> applied the change to r4
- <code>workshop verify compare</code> says <b>MATCH</b>
- The real flows agree: 8080 open, 2222 blocked

**Behind?** Deploy needs the merged pull request number and the 7-character hash: `workshop deploy gates --pr N --confirm HASH`, then `render`, `apply`, `readback` with the same flags.

<details><summary>Speaker notes</summary>

About 12:45 tiles are solid green and the board total for re-checked climbs. Then the wrap-up.

</details>

---

<sub>Slide 64</sub>

*12:50 · Wrap-up*

## What you ran today

Baseline → Propose → Predict → Approve → Deploy → Verify

| Stage | The step you ran |
| --- | --- |
| **Baseline** | `workshop baseline collect` → `upload` → `wait` → `check` |
| **Propose, Predict** | a pull request, then `workshop predict changeset` → `run` → `check` in CI |
| **Approve** | you merged a green `forward/predict` check, and only that |
| **Deploy** | `workshop deploy gates` → `render` → `apply` → `readback` |
| **Verify** | `workshop verify probe` → `collect` → `upload` → `wait` → `compare` |

<details><summary>Speaker notes</summary>

Handoff: Sean → Craig. Quick recap, one row per stage. The point to land: every stage was a separate step with its own evidence, and the only thing that could deploy was a PASS.

</details>

---

<sub>Slide 65</sub>

*12:50 · Wrap-up*

## What we checked, and what we didn't

| Stage | What we checked | What it doesn't cover |
| --- | --- | --- |
| **Baseline** | a known start, its configs fingerprinted | operational state: links, sessions |
| **Predict** | your requirements, on the modelled result | what you didn't write; timing; the model's own mistakes |
| **Approve** | a person merges a green check | review: zero reviewers were required |
| **Deploy** | the predicted lines, only if no config drifted | a change in the second between gate and write |
| **Verify** | a new collection agreed, live probes agreed | anything you didn't probe or require |

<details><summary>Speaker notes</summary>

Tie each row back to something they did today. The right-hand column is the honest part: docs/exercises/how-it-works.md has the detail for anyone who asks.

</details>

---

<sub>Slide 66</sub>

*The NAF Framework*

## Where today's steps sit in the framework

- **Intent:** the candidate and the requirements, in Git
- **Collector** and **Observability:** Forward reads the network and judges it, before and after
- **Orchestrator:** the pull request and its check. It never touches a router
- **Executor:** NAPALM, writing exactly what Predict judged

Swap any one block and the loop still works. Today the Executor and the candidate's syntax are EOS-specific.

<details><summary>Speaker notes</summary>

The callback to the map at the start, now with what they ran. Point at reference.networkautomation.forum/Framework/Framework. The hand-off to land is Observability to Orchestrator: the pipeline continues only on PASS. Forward covers two blocks, the collector and the model, and that is why they are named separately. The full map is in docs/exercises/framework.md.

</details>

---

<sub>Slide 67</sub>

*What you did today*

Diff looked fine. Syntax check passed. A reviewer would have approved it.🤖🔮🛑Forward: "5 of 5 hosts lose the service." Before a single router changed.

<details><summary>Speaker notes</summary>

The whole morning in one slide. Pause on it.

</details>

---

<sub>Slide 68</sub>

*With or without Forward*

## Five rules worth stealing

1. **Deploy exactly what you tested.** Same bytes, checked by hash
2. **Approval is for one change.** Bound to that candidate, that baseline, those requirements
3. **"Couldn't tell" is not a pass.** Empty, unknown or stale never turns green
4. **Check for drift before you write.** The configs you predicted against are the ones you change
5. **Verify against the prediction.** Not against hope, and not against "no alarms"

Predict needs a model of the network. These rules don't: they work in any pipeline you run today.

<details><summary>Speaker notes</summary>

This is the slide to land if they forget everything else. Each rule is something they watched the workshop enforce: deploy refused a hash that didn't match, a STALE wouldn't deploy, the drift side quest, verify MATCH. Ask the room which one their pipeline breaks today.

</details>

---

<sub>Slide 69</sub>

*Monday morning*

## You don't need the whole pipeline to start

1. Pick **one kind of change** you make often
2. Write **three requirements** for it: reachable, blocked, the path
3. Run Predict on every pull request, **report-only** at first
4. Make the check **required** once you trust it

Keep AI as an adviser. The requirements decide.

<details><summary>Speaker notes</summary>

Make it small and concrete. The aim is one requirement file and one check on one pull request by next week.

</details>

---

<sub>Slide 70</sub>

*Where this goes*

## The same pattern, bigger

- **More tests, same gate.** A regression suite is more requirements, run on every change
- **Any pipeline.** The gate is a command with exit codes; put it in the CI you already run
- **More autonomy.** Agents that draft and iterate while people approve
- **Not tested here.** Bigger networks, other platforms, many changes in flight: validate those first

Only PASS deploys. That doesn't change when the author is an agent.

<details><summary>Speaker notes</summary>

Mention the advisers (ask, propose, explain, agent) they could try in stretch work, and that they're welcome to bring their own coding agent; AGENTS.md gives it the rules.

</details>

---

<sub>Slide 71</sub>

*The room, by the numbers*

## What we did together

changes held at the gate before deploypredictions runnetworks re-checked after a changehow far each seat gottook a seat–baselined–merged–verified–

Live from the room board when this page is served by the claim service. Offline, read the three totals off the board.

<details><summary>Speaker notes</summary>

Open the board and read the totals aloud (after 12:50 its wrap-up scoreboard shows all three). This is the proof point: every held change was stopped before it could merge.

</details>

---

<sub>Slide 72</sub>

*Take it home*

## What you have

- The exercises and `AGENTS.md` in your seat repository
- A requirement you wrote (or can write) in `requirements/`
- **Go deeper** (`docs/exercises/go-deeper.md`): Forward's docs for each feature you used, netlab, NAPALM, GitHub rulesets, and where to look when a tool breaks
- The loop: **Baseline → Propose → Predict → Approve → Deploy → Verify**

**Your seat stays up until Sunday, November 22, 8 PM Tucson.** Finish at your own pace, then keep a copy: on your repository's page, **Code → Download ZIP** (or `git clone` it). After that the seat, its Forward network and its repository are removed.

**All of it, public now:** <code>github.com/forwardnetworks/autocon6-know-before-you-deploy</code>: the exercises, the lab, the <code>workshop</code> command and these slides. No sign-up.

<details><summary>Speaker notes</summary>

Read the date on the slide out loud: seats stay up a week (agenda.json, teardown). Tell them to download their repository before then. The repository is public (made public the night before, MIT licensed). Read the address out.

</details>

---

<sub>Slide 73</sub>

# Questions?

One thing that didn't work, or confused you? Post it in `#ac6-ws-a4` or open an issue on the repository. Fixes go in this week, in the open.

Craig Johnson · Sean Deveci · Mike Lossmann  
Slack: `#ac6-ws-a4` · `@wsa4` in the channel

Fixes and questions: issues on github.com/forwardnetworks/autocon6-know-before-you-deploy
