<!-- .slide: class="cover" -->
<div class="kicker">AutoCon6 · WS:A4 · For remote participants only</div>

## Not in the room? Join on Zoom

{{REMOTE}}

<p style="margin-top:.8em"><b>In the room? No Zoom!</b> Zoom is for remote participants only: the room's network is for your lab.</p>

<p class="small">The session is recorded for everyone who couldn't be online.</p>

Note:
Up while people arrive. Remote participants only: anyone in the room stays off the call. Start the recording before the welcome. A proctor watches the Zoom chat for remote questions and relays them. NAF feeds the presenter microphone into the call.

---

<!-- .slide: class="cover" -->
<img class="logo-naf" alt="Network Automation Forum" src="{{NAF}}">
<div class="kicker">AutoCon6 · WS:A4 · Monday, November 16, 2026</div>

# Know Before You Deploy

## Hands-on network CI/CD with Forward Predict

<div class="pipe" style="justify-content:center;margin:.9em auto 0;font-size:.8em"><span class="on">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span class="on">Approve</span><span class="on">Deploy</span><span class="on">Verify</span></div>

<p class="small" style="margin-top:1em"><em>Craig Johnson · Sean Deveci · Mike Lossmann</em></p>

<img class="logo-ac6" alt="AutoCon 6, the network automation conference" src="{{AC6}}">

Note:
Welcome. Four hours, mostly hands-on. Lab first: no long talk this morning, the why comes in short pieces between lab blocks. Introduce the three proctors, say where the helpers sit, and that raising a hand is always fine.

---

<div class="kicker">Before we start</div>

## Four hours, and your hands are on the keyboard

- **Into the lab first.** The talk comes in short pieces between lab work. Most of today is you at a terminal
- **Stuck? Raise a hand.** Three of us are walking the room: Craig, Sean and Mike
- **Slack:** `#ac6-ws-a4`. Ask `@wsa4` anything about the lab: it knows the exercises and, once you link your seat, your last `workshop` results
- **The projector** shows the room's progress during work time. Nicknames only
- **Helpers can see** your terminal commands and `workshop` results, to find where you're stuck; `@wsa4` sees only your `workshop` results, and only once you link your seat. Secrets are masked
- **One rule:** you type the commands, we point at the line to read
- **What we keep:** your GitHub username (to hand you a seat), the nickname you pick, and your seat's commands and results (for the helpers). We never ask for your email. All of it is deleted Sunday, November 22, 8 PM Tucson. Nobody from sales will contact you about today

Note:
Housekeeping, under two minutes. Name the three proctors and where they are standing. Say the break is 10:45 to 11:15 and we finish at 1:00. Say plainly that helpers can see each seat's recent commands (the notice is on the claim page and in the seat README), and that it is only to help. If they fall behind it is fine: every exercise has a way back (`workshop reset --to N`) and nobody is graded. Then, in your own words: this isn't a sales session. We never ask for your email, nobody will follow up, and everything you build today is yours to take: the repository goes public when we finish.

---

### Today

{{AGENDA_GANTT}}

Note:
Point out that nearly all of this is keyboard time. The projector shows this deck during talks and the room board during work time.

---

<!-- .slide: class="section" -->
<div class="num">1</div>
<div class="kicker">9:00 · Section 1 of 6</div>

## Into the lab

<div class="pipe"><span class="on">Pre-change</span><span>Change</span><span>Post-change</span><span>Verify</span></div>

<div class="goal">A lab of your own, running, and Forward's model of it. The talk comes later, in short pieces between lab work.</div>

<p><b>By 1:00:</b> you'll have caught a broken change before it touched a router, and you'll know exactly how.</p>

<div class="finish">By 9:30 you have: <code>workshop doctor</code> READY, the lab up, and a baseline in Forward with <code>workshop baseline check</code> at PASS.</div>

<p class="small muted">Presenting: {{WHO:launch}}</p>

Note:
Craig opens. Exercise 0, then the four baseline steps (the start of exercise 1). Keep the talk to the slides in this section: the why comes at 9:30, once everyone has a lab and a model. Watch the board: tiles go dashed → claimed → baseline.

---

<div class="kicker">Your lab</div>

## Four routers, a client, a service, and four more hosts

<svg viewBox="0 0 1500 520" style="width:100%;max-height:600px;font-family:'Space Mono',ui-monospace,monospace">
<g stroke="#555555" stroke-width="6" fill="none"><line x1="760" y1="130" x2="1100" y2="260"/><line x1="420" y1="260" x2="760" y2="390"/><line x1="760" y1="390" x2="1100" y2="260"/></g>
<g stroke="#92c968" stroke-width="10" fill="none"><line x1="130" y1="260" x2="420" y2="260"/><line x1="420" y1="260" x2="760" y2="130"/><line x1="1100" y1="260" x2="1370" y2="260"/></g>
<g fill="#141414" stroke="#eeff41" stroke-width="4"><rect x="330" y="215" width="180" height="90" rx="14"/><rect x="670" y="85" width="180" height="90" rx="14"/><rect x="670" y="345" width="180" height="90" rx="14"/><rect x="1010" y="215" width="180" height="90" rx="14"/></g>
<g fill="#141414" stroke="#bdbdbd" stroke-width="4"><rect x="40" y="215" width="180" height="90" rx="14"/><rect x="1280" y="215" width="180" height="90" rx="14"/></g>
<g fill="#fff" font-size="34" font-weight="600" text-anchor="middle"><text x="130" y="252">client</text><text x="420" y="252">r1</text><text x="760" y="122">r2</text><text x="760" y="382">r3</text><text x="1100" y="252">r4</text><text x="1370" y="252">service</text></g>
<g fill="#bdbdbd" font-size="24" text-anchor="middle"><text x="130" y="285">10.10.10.10</text><text x="420" y="285">AS 65001</text><text x="760" y="155">AS 65002</text><text x="760" y="415">AS 65003</text><text x="1100" y="285">AS 65004</text><text x="1370" y="285">10.20.20.20</text></g>
<g font-size="26" font-weight="600"><text x="150" y="205" fill="#92c968">TCP 8080 ✓ open</text><text x="60" y="350" fill="#ff5252">TCP 2222 ✗ blocked (ACL on r1)</text></g>
<g stroke="#555555" stroke-width="3" fill="none" stroke-dasharray="6 6"><line x1="625" y1="45" x2="670" y2="115"/><line x1="625" y1="105" x2="670" y2="140"/><line x1="625" y1="415" x2="670" y2="380"/><line x1="625" y1="475" x2="670" y2="405"/></g>
<g fill="#141414" stroke="#757575" stroke-width="3"><rect x="455" y="22" width="170" height="46" rx="10"/><rect x="455" y="82" width="170" height="46" rx="10"/><rect x="455" y="392" width="170" height="46" rx="10"/><rect x="455" y="452" width="170" height="46" rx="10"/></g>
<g fill="#bdbdbd" font-size="19" text-anchor="middle"><text x="540" y="52">branch .30.30</text><text x="540" y="112">branch2 .30.31</text><text x="540" y="422">dc .40.40</text><text x="540" y="482">dc2 .40.41</text></g>
<g font-size="24" fill="#bdbdbd"><text x="1010" y="345">r4 advertises:</text><text x="1010" y="378" fill="#92c968">10.20.20.0/24  (the service)</text><text x="1010" y="408" fill="#f7b654">10.20.30.0/24  (stale?)</text><text x="1010" y="438" fill="#f7b654">10.20.40.0/24  (stale?)</text></g>
</svg>

Note:
The green path is the primary one, through r2. Two of r4's three advertisements have no route behind them; retiring those is today's change request. The third carries the service. The four grey hosts (10.30.30.0/24 and 10.30.31.0/24 behind r2, 10.40.40.0/24 and 10.40.41.0/24 behind r3) give Forward more to show: get the change wrong and five places lose the service, not one.

---

<div class="kicker">Where things live</div>

## Three places, one loop

<div class="cols3">
<div class="card"><h4>This Codespace</h4><p>The lab: four cEOS routers, a client, a service and four more hosts. The <code>workshop</code> command. Your <b>Your lab</b> tab.</p></div>
<div class="card"><h4>Your Forward network</h4><p>Forward's model of your lab, on fwd.app. Reached only through your seat's token. <b>Your work never needs the Forward UI</b>; between sections we'll look at what you just did, on the projector.</p></div>
<div class="card"><h4>Your GitHub repo</h4><p><code>candidate/</code> is the change. <code>intent.md</code> says what we want. Later today, a check on your pull request decides what may merge.</p></div>
</div>

Note:
Three boxes; the attendee only ever touches the first and the third directly. Forward is driven through the CLI and the pipeline.

---

<div class="kicker">Three rules</div>

## The rules of the game

- **PASS is the only green.** FAIL, ERROR, INCONCLUSIVE and STALE all stop a deploy. An empty answer is never a pass.
- **AI advises, the tests decide.** Forward AI can draft, review and explain. Your requirements, checked by Forward, are the judge.
- **You type the deploy.** A person approves and confirms. Nothing deploys itself.

Note:
These three rules come back in the investigation talk and the wrap-up.

---

<!-- .slide: class="title" -->
<div class="kicker">Let's go</div>

## Open your Codespace

1. Go to <code>tinyurl.com/wsa4go</code> (or scan the QR code on the board) and sign in with GitHub
2. Press **Get a seat**, then **accept the invitation**
3. **Open in Codespaces**, then wait for the **Your lab** tab
4. In the terminal: <code>workshop doctor</code>, then <code>workshop up</code>
5. **Then the baseline:** four steps as soon as `workshop up` finishes (it takes 3 to 10 minutes)

<p class="small muted" style="margin-top:1.2em">On your seat page: pick an icon and a nickname (they show on the board), and link Slack with <code>@wsa4 i am CODE</code> so the bot knows your seat.<br>Stuck? Ask <code>@wsa4</code> in Slack first · raise a hand if it can't sort it out · the board shows the whole room</p>

Note:
The short link is <code>tinyurl.com/wsa4go</code> and the QR code is on the board (switch the projector to it). Read the link out. Target: `workshop up` started by 9:08. No long talk now: while `up` builds, the three short slides about the lab play (your lab, three places, the rules), then everyone takes a baseline. Helpers walk the room for anyone stuck (the "Four fixes" slide is the cheat sheet). Icons and nicknames are optional and friendly; a helper can clear one from the helpers' desk. The Slack bot is in the channel only (no DMs).

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 9:05 → 9:15</div>

## Launch your lab

- Seat page: **Get a seat**, **accept the invitation**, **Open in Codespaces**
- `workshop doctor` says **READY**, then `workshop up`: 3 to 10 minutes, keep listening while it builds
- Can't push to your seat repository? Accept the invitation, then reopen the Codespace

<p class="small"><b>Why:</b> a lab of your own means you can break things on purpose, which you can't do in production.</p>

<p class="small muted">Exercise 0 · <b>Behind?</b> The only must-do is <code>workshop up</code> running. Raise a hand, or <code>@wsa4 help seat-NN</code>.</p>

Note:
Leave this up for a minute or two, then talk through the next three slides while the labs build.

---

<div class="kicker">While it builds: what you just launched</div>

## Your lab is a page of YAML

<div class="cols">
<div>

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

</div>
<div>

<pre><code>{# lab/stale-adverts.j2: today's problem #}
router bgp &#123;&#123; bgp.as &#125;&#125;
   address-family ipv4
      network 10.20.30.0/24
      network 10.20.40.0/24</code></pre>

<p class="small"><code>workshop up</code> runs <b>netlab</b>: addresses, BGP sessions and policy come from this file; the custom bits are small templates like this one. Change the YAML, rebuild the lab.</p>

</div>
</div>

Note:
Shortened from the real lab/topology.yml (it also has four more hosts and the addressing plan); it's in their repository, open it. The point: a realistic multi-AS lab is a page of text you can review in a pull request. The stale-adverts template is the "decommissioned segment" they'll retire all morning.

---

<div class="kicker">Take it home</div>

## Every piece is open source, except Forward

<table class="small">
<tr><th>Piece</th><th>What it does today</th></tr>
<tr><td><b>netlab</b></td><td>builds and configures the lab from YAML (<code>workshop up</code>)</td></tr>
<tr><td><b>containerlab</b></td><td>runs the routers and hosts as containers</td></tr>
<tr><td><b>Netmiko</b></td><td>netlab's config push at bring-up</td></tr>
<tr><td><b>NAPALM</b> (+ pyeapi)</td><td>every change after that: the router's own diff, an atomic commit</td></tr>
<tr><td><b>PyGithub, GitPython, Docker SDK</b></td><td>the glue in <code>src/workshop/</code>: pull requests, commits, containers</td></tr>
<tr><td><b>This workshop</b></td><td>MIT, public: every command, YAML file and test you use today</td></tr>
<tr><td class="muted">Not open source</td><td class="muted">Arista cEOS-lab (free download) · GitHub Codespaces and Actions · <b>Forward</b>: the model, the queries, Predict</td></tr>
</table>

<p class="small muted">github.com/forwardnetworks/autocon6-know-before-you-deploy</p>

Note:
Say it plainly: everything except the router image, GitHub's hosting and Forward is open source, and you can take all of it home today. Forward is the one product in the loop: the network model and what you ask of it. Pinned versions are in pyproject.toml.

---

<div class="kicker">Two ways through. Same finish line</div>

## Pick your path

<div class="cols">
<div class="card"><h4>I'm Too Young to Die</h4><p class="small">New to CI, Git or automation? Good.</p><ul class="small">
<li>The <b>Your lab</b> page: every step is a button, with its command shown underneath</li>
<li>Commit and open the PR from the editor's panels. No Git commands</li>
<li>Each exercise's <b>Behind?</b> line is your shortcut</li>
<li>Ask <code>@wsa4</code> for a hint. Then another one</li>
</ul></div>
<div class="card good"><h4>Hold My Beer</h4><p class="small">You live in a terminal.</p><ul class="small">
<li>Terminal only: every step by hand. Read the <code>→</code> calls it prints, and open their HTTP</li>
<li>Git from the CLI. Read <code>src/workshop/</code> as you go</li>
<li>Side quests: write your own test, try to cheat the gate, deploy a FAIL on purpose and back it out, or give Copilot Forward's tools</li>
<li><code>workshop yolo</code> exists. Try it</li>
</ul></div>
</div>

<p class="small muted">Both end at <code>workshop verify compare</code> saying <b>MATCH</b>. Switch whenever you like: the page and the terminal run the same commands.</p>

Note:
Ten seconds, with a smile. Neither path is the lesser one: the Too Young to Die crowd see the same evidence, and plenty of experts will end up clicking at 12:15. `workshop yolo` is a hidden joke command: it always refuses, and explains why. Don't spoil what it says.

---

<div class="kicker">Exercise 0 · Your editor</div>

## Everything is in the Codespace

- **Explorer:** the candidate, the requirements, the exercises
- **Source Control:** commit and push your change
- **GitHub Pull Requests:** open the PR, watch its check
- **Terminal:** every `workshop` command
- **Ports:** *Your lab* on 8765, if its pane is blank

Note:
Point at each one on the projector. The Pull Requests panel is on the left bar; the Ports tab is next to the terminal. If the Your lab pane is blank, Ports, port 8765, the globe icon.

---

<!-- .slide: data-nobuild -->
<div class="kicker">If your lab won't start</div>

## Four fixes, in this order

1. **Run `workshop doctor`.** It names what is missing. Read the last line.
2. **It says settings are missing?** You opened the Codespace from the wrong place. **Delete it**, accept the GitHub invitation, then reopen from **your seat page**.
3. **Can't push?** Same cause: accept the invitation, then reopen the Codespace.
4. **Still stuck?** Ask <code>@wsa4</code> in Slack: once your seat is linked it sees your last <code>workshop</code> results and gives you the next command. Raise a hand if it can't sort it out.

<p class="small muted">Don't open a Codespace from the "repo" link on a helper's screen. That one is read only.</p>

Note:
Show this only if a few people are stuck at 9:15. It is the same fix the helpers use: delete the Codespace, accept the invitation, reopen from the seat page. The usual cause is a Codespace opened before the invitation was accepted, or from a read-only repository link. Helpers: the desk shows the last commands for the seat.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 9:15 → 9:30</div>

## Give Forward a baseline

<div class="pipe"><span class="on">Pre-change</span><span>Change</span><span>Post-change</span><span>Verify</span></div>

- When `workshop up` finishes: `workshop probe` says **8080 open**, 8443 and 2222 blocked
- `workshop baseline collect` → `upload` → `wait` → `check` (or the four buttons on the **Your lab** page)
- `check`: every requirement **PASS**: the lab is the network it should be
- Each step prints an **Evidence** line: what it just proved

<p class="small"><b>Why:</b> every change is judged against a known “before”.</p>

<p class="small muted">Exercise 0, then exercise 1's "Take the baseline" · <b>Behind?</b> <code>workshop up</code> still running is fine: take the baseline when it's done. <b>Early?</b> Side quest: walk the route on r1.</p>

---

<!-- .slide: class="checkpoint" -->
<div class="kicker">Checkpoint · 9:30</div>

## Lab running, baseline PASS?

- Codespace open, with the <b>Your lab</b> tab
- <code>workshop doctor</code> says <b>READY</b>
- <code>workshop baseline check</code> says <b>PASS</b>

<div class="behind"><b>Behind?</b> A FAIL on the baseline usually means <code>baseline</code> ran before <code>up</code> finished: <code>workshop up</code> again, then the baseline steps from <code>collect</code>. Still building? Carry on listening; take the baseline when it's done.</div>

Note:
Most tiles should be blue (baseline) by now. If a Codespace will not start: release the seat (helpers' desk) and they press Get a seat again. If they opened it before accepting the invitation, `workshop doctor` says so: accept, then reopen from the seat page.

---

<!-- .slide: data-nobuild -->
<div class="kicker">Side quests</div>

## Ahead? Pick a side quest

<table>
<tr><th>When you can start</th><th>Side quest</th><th>About</th></tr>
<tr><td>Lab running</td><td><b>Walk the route</b>: the real router's two paths</td><td>5 min</td></tr>
<tr><td>Baseline PASS</td><td><b>Interrogate the model</b> · <b>Ask Forward AI</b>, then check it · <b>Ask Forward anything (NQE)</b></td><td>10 · 5 · 10</td></tr>
<tr><td>First check back</td><td><b>Write your own test</b></td><td>10 min</td></tr>
<tr><td>Seen a red check</td><td><b>Which lines are stale?</b> · <b>Blast radius</b>, before and after · every way of retiring them · let an adviser draft it</td><td>5 · 10 · 10 · 10</td></tr>
<tr><td>Verified</td><td><b>Cheat the gate</b> · <b>Catch the drift</b> · <b>Deploy it anyway, then back it out</b></td><td>10 · 10 · 15</td></tr>
</table>

<p class="small muted">Never blocks the core steps. Behind? Skip them. They are in <code>docs/exercises/side-quests.md</code>, and the <b>Go further</b> card on your lab page tracks four of them.</p>

Note:
Say it once, now: the point of the day is stick time. If you finish a section early, do not wait for the room, pick one of these. They are optional, they start from where you already are, and none changes your core state except the last two, which reset first. Proctors: nudge anyone idle toward the row for where they are. Do not offer "Which lines are stale?" before someone has seen a red check; it spoils exercise 3.

---

<!-- .slide: class="section" -->
<div class="num">2</div>
<div class="kicker">9:30 · Section 2 of 6</div>

## The missing test stage

<div class="goal">Why a syntax check and a diff aren't enough, then find your way around Forward's model and see a change the Forward way.</div>

<div class="finish">By 10:05 you have: a path and a query you ran yourself, and a baseline at PASS.</div>

<p class="small muted">Presenting: {{WHO:baseline}}</p>

Note:
Five slides of why, then hands back on keyboards. Proctors: anyone without a PASS baseline yet, help them now (the talk doesn't need them).

---

<div class="kicker">The problem</div>

## Automation executes changes well.

<div class="big" style="margin-top:.8em">What tests them first?</div>

<ul><li class="fragment">A syntax check</li><li class="fragment">A code review</li><li class="fragment">Hope</li></ul>

Note:
Let the room answer out loud. The point: we have good tools to push a change and weak tools to know what it will do.

---

<div class="kicker">Two kinds of validation</div>

## Is it well formed? vs. What will it do?

<div class="cols">
<div class="card"><h4>Configuration validation</h4><ul><li>Syntax and schema</li><li>Linting and style</li><li>Is the config legal?</li></ul></div>
<div class="card hot"><h4>Behavioral validation</h4><ul><li>Is the service still reachable?</li><li>Are the routes still there?</li><li>Is what must stay blocked still blocked?</li></ul></div>
</div>

Note:
Both matter. Only the second one tells you about an outage before you cause it.

---

<div class="kicker">A realistic change</div>

## Valid configuration can still cut off a service.

```
router bgp 65004
   address-family ipv4
      no network 10.20.20.0/24
```

<ul><li class="fragment">Valid EOS. One line. A syntax check passes it.</li><li class="fragment">It stops r4 advertising the subnet your <b>service</b> lives on.</li></ul>

Note:
Foreshadowing: later today they write a change like this on purpose and watch it get stopped.

---

<div class="kicker">What catches this today</div>

## Four checks, and what each one can't see

<table>
<tr><th>Check</th><th>It sees</th><th>It can't see</th></tr>
<tr><td><b>Syntax and lint</b></td><td>the config is legal</td><td>what it does</td></tr>
<tr><td><b>Peer review</b></td><td>a diff of one device</td><td>the effect on the others</td></tr>
<tr><td><b>Change window</b></td><td>nothing yet</td><td>you find out by deploying</td></tr>
<tr><td><b>A lab copy</b></td><td>the lab you built</td><td>whether it still matches production</td></tr>
</table>

Note:
Ask who relies on each one. None of them is wrong. None of them answers "what will the network do after this change?"

---

<div class="kicker">Why review misses it</div>

## The line is on r4. The damage is on r1.

<svg class="diamond" viewBox="0 0 1500 500" style="width:100%;max-height:560px">
<g class="lnk idle"><line x1="1370" y1="250" x2="1100" y2="250"/><line x1="1100" y1="250" x2="760" y2="120"/><line x1="760" y1="120" x2="420" y2="250"/><line x1="420" y1="250" x2="130" y2="250"/><line x1="1100" y1="250" x2="760" y2="380"/><line x1="760" y1="380" x2="420" y2="250"/></g>
<g class="fragment fade-out" data-fragment-index="2"><g class="lnk live"><line x1="1100" y1="250" x2="760" y2="120"/><line x1="760" y1="120" x2="420" y2="250"/><line x1="420" y1="250" x2="130" y2="250"/><line x1="1100" y1="250" x2="760" y2="380"/><line x1="760" y1="380" x2="420" y2="250"/></g></g>
<g class="fragment" data-fragment-index="2"><g class="lnk gone"><line x1="1100" y1="250" x2="760" y2="120"/><line x1="760" y1="120" x2="420" y2="250"/><line x1="420" y1="250" x2="130" y2="250"/><line x1="1100" y1="250" x2="760" y2="380"/><line x1="760" y1="380" x2="420" y2="250"/></g></g>
<g fill="#141414" stroke="#eeff41" stroke-width="4"><rect x="330" y="205" width="180" height="90" rx="14"/><rect x="670" y="75" width="180" height="90" rx="14"/><rect x="670" y="335" width="180" height="90" rx="14"/><rect x="1010" y="205" width="180" height="90" rx="14"/></g>
<g fill="#141414" stroke="#bdbdbd" stroke-width="4"><rect x="40" y="205" width="180" height="90" rx="14"/><rect x="1280" y="205" width="180" height="90" rx="14"/></g>
<g fill="#fff" font-size="34" font-weight="600" text-anchor="middle"><text x="130" y="262">client</text><text x="420" y="262">r1</text><text x="760" y="132">r2</text><text x="760" y="392">r3</text><text x="1100" y="262">r4</text><text x="1370" y="262">service</text></g>
<g class="fragment" data-fragment-index="1"><rect class="pulse" x="1010" y="205" width="180" height="90" rx="14" fill="none" stroke="#ff5252" stroke-width="8"/><text x="1100" y="180" fill="#ff5252" font-size="28" font-weight="600" text-anchor="middle">one line removed</text><text x="1100" y="352" fill="#ff5252" font-size="24" text-anchor="middle">no network 10.20.20.0/24</text></g>
<g class="fragment" data-fragment-index="2"><text x="760" y="262" fill="#ff5252" font-size="28" font-weight="600" text-anchor="middle">route withdrawn</text></g>
<g class="fragment" data-fragment-index="3"><rect class="pulse" x="330" y="205" width="180" height="90" rx="14" fill="none" stroke="#ff5252" stroke-width="8"/><text x="420" y="340" fill="#ff5252" font-size="28" font-weight="600" text-anchor="middle">r1: no route</text><text x="420" y="372" fill="#ff5252" font-size="28" font-weight="600" text-anchor="middle">to the service</text></g>
<g class="fragment" data-fragment-index="4"><rect class="pulse" x="40" y="205" width="180" height="90" rx="14" fill="none" stroke="#ff5252" stroke-width="8"/><text x="130" y="180" fill="#ff5252" font-size="30" font-weight="600" text-anchor="middle">TCP 8080 ✗ fails</text></g>
</svg>

A reviewer reading r4's diff sees one removed line. Nothing in the diff says *r1 loses a route*.

Note:
This is exactly what they will see in exercise 3. Plant it now: the cause and the symptom are on different devices.

---

<div class="kicker">Before you open it</div>

## What Forward does with what it collects

<div class="flow">
<div class="step"><b>Collect</b>config and state from every device, read-only (your ZIP)</div><div class="arrow">›</div>
<div class="step"><b>Normalize</b>one vendor-neutral model: devices, interfaces, routes, ACLs, BGP</div><div class="arrow">›</div>
<div class="step hot"><b>Compute</b>every path a packet could take, worked out from the model, not sampled</div><div class="arrow">›</div>
<div class="step ok"><b>Ask</b>path searches, diffs, and NQE queries (2,000+ built in), against that model</div>
</div>

- **Normalized config and state:** the same question works on Arista, Cisco or Juniper: `workshop data routes`
- **Mathematical verification:** not a ping from one place. Forward computes the forwarding behavior of the whole network: `workshop path`
- **A query language:** anything else about the network, as an NQE query: `workshop nqe` (and later today, your path searches become intent checks)

Note:
Two minutes, then hands back on keyboards. The point: Forward doesn't log in to routers to answer questions. It collected once (that's the ZIP they uploaded), turned every vendor's config and state into one model, and computes answers from it, so "can the client reach the service?" is answered for every path, not by sending one packet. The three bullets are the three commands they run next. Keep it plain: no product tour, the UI stays closed.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 9:35 → 9:45</div>

## Meet Forward

<div class="pipe"><span class="on">Pre-change</span><span>Change</span><span>Post-change</span><span>Verify</span></div>

- `workshop data inventory`, `data topology`, `data vulns` (which CVEs hit these routers), `data routes --prefix 10.20.20.0/24`
- `workshop path`: follow the service path hop by hop. `workshop path --port 2222`: delivered, but denied at r1
- Forward's own NQE library (2,000+ ready-made queries): `workshop nqe "/L3/BGP/Established BGP Peerings"`, `"/Interfaces/Interface Status Query"`, `"/L2/CDP and LLDP"`

<p class="small"><b>Why:</b> none of this touched a router. It is Forward's model, built from the ZIP you uploaded.</p>

<p class="small muted">Exercise 1 · <b>Behind?</b> <code>workshop path</code> and the NQE query; skip the rest. <b>Early?</b> Side quests: interrogate the model, or ask Forward AI.</p>

Note:
Point out the library queries ship with Forward and work on any network; writing their own (and meeting today's change request) is lab 2.

---

<div class="kicker">What changes</div>

## Test the result, not the diff

- Say what must stay true, **once**, as tests: reachable, blocked, the path
- Ask Forward what the network will do **after** the change, not what the text says
- Run the same tests on every change, and again on the real network after deploy

<p class="small muted">The tests are files in a repository. They are reviewed, versioned and reused.</p>

Note:
The shift: from reading configuration to stating intent. The tests are the part you keep.

---

<div class="kicker">The honest limit</div>

## A test you didn't write can't fail

- A check is only as good as your requirements
- And a model can be wrong: we caught one modelling an ACL edit no real router would accept
- That is why the baseline step matters: it's where you write down what must stay true
- AI can draft a change and explain a failure. Only the requirements decide

<p class="small muted">Start small: three requirements for one kind of change beats a perfect model you never finish.</p>

Note:
Be straight about this. The value is not magic in the tool; it's that "what must stay true" becomes executable, and gets checked every time. The ACL story (docs/exercises/how-it-works.md, section b): on an early development build, Predict accepted a duplicate ACL sequence number that real cEOS rejects, and modelled both entries. We switched scenarios. It's why deploy render compares the model's diff with the router's, and why verify collects again.

---

<div class="kicker">The change loop most teams run</div>

## Pre-change → change → post-change → verify

<div class="flow">
<div class="step"><b>Pre-change</b>collect the network as it is: your baseline<br><span class="small muted">NAF: Collector → Observability</span></div><div class="arrow">›</div>
<div class="step"><b>Change</b>push the config to the router<br><span class="small muted">NAF: Executor</span></div><div class="arrow">›</div>
<div class="step"><b>Post-change</b>collect it again<br><span class="small muted">NAF: Collector → Observability</span></div><div class="arrow">›</div>
<div class="step hot"><b>Verify</b>compare: what moved, who lost reach, does it still work?<br><span class="small muted">NAF: Observability</span></div>
</div>

You'll run this loop next with Forward. Good loop. One catch: you only learn the answer **after** the change is live.

Note:
One minute. This is the operational loop most teams already have, mapped to the NAF framework blocks. Exercise 1's "See a change" is exactly this loop, and at 10:10 they'll run it with a real (bad) change. Don't mention Predict yet: the gap ("you only learn after") is the setup for 10:20.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 9:50 → 10:05</div>

## See a change the Forward way

<div class="pipe"><span class="on">Pre-change</span><span class="on">Change</span><span class="on">Post-change</span><span class="on">Verify</span></div>

- **Make a change: shut r2's link to r4** (or `workshop link down`), then the four baseline steps: ROUTE-SERVICE and PATH-SERVICE **FAIL**, on purpose
- **What changed: everything Forward sees** (`workshop data changes`): links, configs, interfaces, routes, ARP/MAC, ACLs, site reachability, and Forward's own BGP and LLDP queries, before against after
- Then the detail: **routes** (what moved) · **reachability** (Branches ↔ Service) · `workshop path` (still works, now via r3. Is that OK? Hold that thought)
- **Undo the change**, then the four baseline steps once more: every line **PASS**

<p class="small"><b>Why:</b> Forward tells you what moved and who lost reach. Whether it matters is your intent: lab 2.</p>

<p class="small muted">Exercise 1 · <b>Behind?</b> Skip it: a PASS baseline is all exercise 2 needs. If you shut the link, undo it and take the baseline again.</p>

---

<!-- .slide: class="checkpoint" -->
<div class="kicker">Checkpoint · 10:05</div>

## Ready for a change?

<div class="pipe"><span class="on">Pre-change</span><span>Change</span><span>Post-change</span><span>Verify</span></div>

- You followed one path hop by hop and ran one NQE query
- Made the change? It's undone, and your newest baseline says <b>PASS</b>
- <code>workshop baseline check</code> says <b>PASS</b>

<div class="behind"><b>Behind?</b> A FAIL on the baseline usually means <code>baseline</code> ran before <code>up</code> finished. Run <code>workshop up</code> again, then the baseline steps from <code>workshop baseline collect</code>.</div>

Note:
Most tiles should be blue (baseline). Hands up for anyone with a FAIL on the baseline. Ask someone to read out their 2222 path: DELIVERED but DENIED at r1. Fill time: the router CLI tour (`netlab connect r1`) and the Forward AI prompts (exercise 1 extras).

---

<!-- .slide: class="section" -->
<div class="num">3</div>
<div class="kicker">10:05 · Section 3 of 6</div>

## Build and run the change pipeline

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

<div class="goal">Send a one-prefix change through Git, CI and Forward Predict, and read the result.</div>

<div class="finish">By 10:45 you have: a pull request open, the <b>forward/predict</b> check run, and its verdict read. A red here is expected: not done yet.</div>

<p class="small muted">Presenting: {{WHO:baseline}} (the hint), then {{WHO:pipeline}}</p>

Note:
Exercise 2. Open .github/workflows/forward-predict.yml and src/workshop/forward.py on the projector. Code and requirements come from main, so a PR cannot weaken its own test.

---

<!-- .slide: class="meme" data-nobuild -->
<div class="kicker">A true story, probably yours</div>

<div class="cap">Friday, 4:55 PM. The diff is three lines.</div>
<div class="pic">🙂👍 → 🔥📟</div>
<div class="cap bottom">"It's just removing some old network statements."</div>

Note:
Five seconds, let them laugh. Then: "Hands up if you've been paged by a three-line change." Next slide: when do you find out?

---

<div class="kicker">Three ways to find out</div>

## When do you learn the change broke something?

<table class="small">
<tr><th></th><th>What runs</th><th>What tells you</th><th>When</th></tr>
<tr><td><b>1</b></td><td>Deploy <b>without Predict</b>, collect before and after, diff</td><td>3 routes deleted on r1, r2, r3; Branches, Data centre and Client edge lose the Service. Is that bad? You have to know.</td><td>After it's live</td></tr>
<tr><td><b>2</b></td><td>Same, with the intent checks</td><td>Forward says APP-EXISTING and PATH-SERVICE FAIL, in the change ticket. Back it out.</td><td>After it's live</td></tr>
<tr><td><b>3</b></td><td>Predict, with the intent checks, then deploy, then verify</td><td>The same FAILs, on the predicted network</td><td><b>Before any router changes</b></td></tr>
</table>

<p class="small muted">Next ten minutes: <b>you</b> do 1 and 2, with Predict overridden (please don't do this at work). Then the rest of the morning is 3.</p>

Note:
Craig, one minute, before handing to {{WHO:pipeline}}. Don't demo it: tease it. "The next ten minutes, you'll do what a lot of us do on a Tuesday: push a change nobody checked first. Then Forward will tell you how it went. Spoiler: you won't like it." They run it themselves (next slide); proctors watch for anyone who forgets to back it out.

---

<div class="kicker">The story starts here</div>

## Your critical flows become Forward intent checks

<table class="small">
<tr><th>Requirement (Git)</th><th>Forward intent check</th><th>On your baseline</th></tr>
<tr><td><b>APP-EXISTING</b> 8080 must get through</td><td>Existential path check</td><td class="p">PASS</td></tr>
<tr><td><b>MGMT-DENY</b> 2222 must be blocked</td><td>Isolation path check</td><td class="p">PASS</td></tr>
<tr><td><b>PATH-SERVICE</b> via r1 → r2 → r4</td><td>Existential, through r2</td><td class="p">PASS</td></tr>
<tr><td><b>STALE-CLEARED</b> no inert BGP statements</td><td>NQE check (the query, in Forward's library)</td><td class="f">FAIL: the 2 stale lines, the finding to fix</td></tr>
</table>

<p class="small"><code>workshop intent</code> (or the page's button) turns your lab 1 path searches into these checks, and Forward judges every snapshot from then on: the baseline, every change you make, the network after a deploy. <b>Forward is the Collector here</b> (NAF): the headless collector's ZIP, named by its SHA-256 in every change record, is the snapshot it models.</p>

Note:
This is the spine of the day: the flows you care about are written once, in Git, and Forward holds them as intent checks. From now on every snapshot answers "do my critical flows still work?" Point out that STALE-CLEARED failing is the point: it's the finding the change request will clear. Ask: in your network, what are the three flows you'd put here first?

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 10:10 → 10:20 · don't try this at work</div>

## Ship it. What could go wrong?

<p style="margin:.2em 0 .9em"><span class="stamp">PREDICT OVERRIDDEN</span></p>

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span>Predict</span><span>Approve</span><span class="on">Deploy</span><span class="on">Verify</span></div>

- **First:** your own question, `workshop nqe nqe/stale_bgp_advertisements.nqe`: **today's change request**. Then turn your path searches into intent checks (`workshop intent`, or the Deploy stage's button)
- **Propose:** retire **all three** statements (tick them on the Propose stage, or edit the file). Don't commit
- **Deploy without Predict** (the Deploy stage, or `workshop deploy apply --without-predict --confirm HASH`): it opens a change ticket
- **Verify**, five steps: **FAIL**. Open the ticket (your repo's **Issues** tab): Forward says what broke, after the fact
- **Back it out:** Revert: plan → apply → the baseline steps → compare: **MATCH**. Then empty the candidate

<p class="small"><b>Why:</b> so you know exactly what the next two hours are saving you from.</p>

<p class="small muted">Exercise 2, first part · <b>Behind?</b> Skip it: the pipeline is the core.</p>

---

<div class="kicker">Add a loop in front</div>

## Design → predict → test, then the loop you know

<div class="flow">
<div class="step"><b>Design</b>the change, and the tests it must pass, in Git<br><span class="small muted">NAF: Intent</span></div><div class="arrow">›</div>
<div class="step hot"><b>Predict</b>Forward models the network <i>with</i> the change. No router touched<br><span class="small muted">NAF: Observability</span></div><div class="arrow">›</div>
<div class="step"><b>Test</b>your requirements on the predicted network: only PASS goes on<br><span class="small muted">NAF: Orchestrator, with a person</span></div>
</div>

<div class="flow" style="margin-top:.5em">
<div class="step"><b>Pre-change</b>still current?</div><div class="arrow">›</div>
<div class="step"><b>Change</b>exactly the bytes that passed<br><span class="small muted">NAF: Executor</span></div><div class="arrow">›</div>
<div class="step"><b>Post-change</b>collect again</div><div class="arrow">›</div>
<div class="step ok"><b>Verify</b>reality matches the prediction</div>
</div>

Same questions you asked at 10:10. Now you ask them **before** the change.

Note:
The turn of the morning. The design loop (NAF Intent → Observability → Orchestrator) is new; the operational loop below is the one they just ran by hand, now gated. Predict appears here for the first time. Hand over to {{WHO:pipeline}} after this slide.

---

<div class="kicker">Your morning, step by step</div>

## Same loop, two ways to drive it

<table class="small">
<tr><th>Stage</th><th>I'm Too Young to Die: click</th><th>Hold My Beer: type</th></tr>
<tr><td><b>0 Start</b></td><td><b>Start the lab</b>, then <b>Check my setup</b></td><td><code>workshop up</code>, <code>workshop doctor</code></td></tr>
<tr><td><b>1 Baseline</b></td><td><b>1. Collect</b> → <b>2. Upload</b> → <b>3. Wait for the model</b> → <b>4. Check</b></td><td><code>workshop baseline collect</code>, <code>upload</code>, <code>wait</code>, <code>check</code></td></tr>
<tr><td><b>2 Propose</b></td><td>tick what to retire, <b>Write candidate/r4-bgp.eos</b>, <b>Open pull request</b></td><td>edit <code>candidate/r4-bgp.eos</code>, branch, commit, push, open the PR</td></tr>
<tr><td><b>3 Predict</b></td><td>watch <b>forward/predict</b> on your PR (or <b>1. Change set</b> → <b>2. Predict</b> → <b>3. Check</b>)</td><td><code>workshop predict changeset</code>, <code>run</code>, <code>check</code></td></tr>
<tr><td><b>4 Approve</b></td><td colspan="2">merge the pull request on GitHub, only when the check is green</td></tr>
<tr><td><b>5 Deploy</b></td><td><b>1. Gates</b> → <b>2. Render</b> → <b>3. Apply</b> → <b>4. Read back</b></td><td><code>workshop deploy gates</code>, <code>render</code>, <code>apply</code>, <code>readback</code> with <code>--pr N --confirm HASH</code></td></tr>
<tr><td><b>6 Verify</b></td><td><b>1. Probe</b> → <b>2. Collect</b> → <b>3. Upload</b> → <b>4. Wait for the model</b> → <b>5. Compare</b></td><td><code>workshop verify probe</code>, <code>collect</code>, <code>upload</code>, <code>wait</code>, <code>compare</code></td></tr>
</table>

<p class="small muted">Finish line, either way: <b>MATCH</b>. Every button runs the command next to it, and shows it under the button.</p>

Note:
Talk it through top to bottom, once, about a minute: this is the whole morning. Point out that each row is a section of the day (into the lab 9:00, the why at 9:30, the pipeline 10:05, break it 11:15, fix it 12:00, deploy and verify 12:30). The buttons and the commands are the same thing: a Too Young to Die person who peeks under a button is reading the Hold My Beer column. Nobody needs to remember this slide: the Your lab page always shows the next step.

---

<div class="kicker">The software pattern</div>

## CI/CD, for the network

<div class="flow">
<div class="step"><b>Propose</b>a pull request</div><div class="arrow">›</div>
<div class="step hot"><span class="n">the missing stage</span><b>Tests</b>of network behavior</div><div class="arrow">›</div>
<div class="step"><b>Gate</b>only PASS gets through</div><div class="arrow">›</div>
<div class="step"><b>Deploy</b>exactly what was tested</div><div class="arrow">›</div>
<div class="step"><b>Verify</b>reality matches</div>
</div>

Pull requests, automated tests and gates are familiar. What was missing was a test stage that *understands the network*, and a last stage that checks reality against the prediction. That last check is what closes the loop.

Note:
Everyone in software knows this picture. Networks had the pipeline but not the tests.

---

<div class="kicker">How it works</div>

## A model of your network

<div class="flow">
<div class="step"><b>Your network</b>configs and state, collected</div><div class="arrow">›</div>
<div class="step"><b>Forward model</b>a snapshot you can query</div><div class="arrow">›</div>
<div class="step hot"><b>Predict</b>apply a proposed change to the model</div><div class="arrow">›</div>
<div class="step"><b>Predicted network</b>no device touched</div><div class="arrow">›</div>
<div class="step ok"><b>Your tests</b>pass or fail</div>
</div>

Test the *result* of a change before it exists.

Note:
Forward builds a model from what it collects. Predict applies candidate changes to that model and lets you run the same tests on the outcome. No router is touched.

---

<div class="kicker">The pipeline you will run</div>

## Six stages. Only a PASS moves on.

<div class="pipeline">
<div class="pipe"><span class="on">1 Baseline</span><span class="on">2 Propose</span><span class="on">3 Predict</span><span class="on">4 Approve</span><span class="on">5 Deploy</span><span class="on">6 Verify</span></div>

<div class="lane"><div class="label">Where it runs</div>
<div>Your terminal</div><div>Your editor, then a pull request</div><div>GitHub Actions, with Forward</div><div>GitHub</div><div>Your terminal, then r4</div><div>Your terminal, with Forward</div></div>

<div class="lane"><div class="label">What it checks</div>
<div>A known start, fingerprinted</div><div>Only <code>candidate/</code> changes</div><div class="gate">Your tests, on the predicted network</div><div>A person merges a green check</div><div>Exactly the predicted lines, if nothing drifted</div><div>Reality agrees with the prediction</div></div>

<div class="lane"><div class="label">The steps you type</div>
<div><code>baseline collect</code> … <code>check</code></div><div>edit, commit, open the PR</div><div>runs for you on every PR</div><div>Squash and merge</div><div><code>deploy gates</code> … <code>readback</code></div><div><code>verify probe</code> … <code>compare</code></div></div>
</div>

Note:
Walk left to right once. Each stage checks one thing; we come back to those, and their limits, at the end. Every stage is a few commands you run one at a time: each prints the real call it makes and the evidence it leaves.

---

<div class="kicker">Why a change workflow, and where it fits</div>

## Automation made changes fast. A workflow makes them safe

<table class="small">
<tr><th>Stage</th><th>NAF Framework block</th><th>What it adds</th></tr>
<tr><td><b>Propose</b></td><td>Intent</td><td>The change and the tests it must pass, in Git: reviewable, versioned, one source</td></tr>
<tr><td><b>Baseline, Predict</b></td><td>Collector → Observability</td><td>A model of the real network, and the change applied to it before any router is touched</td></tr>
<tr><td><b>Approve</b></td><td>Orchestrator, with a person</td><td>Only a PASS can merge, and a person merges it</td></tr>
<tr><td><b>Deploy</b></td><td>Executor</td><td>Exactly the lines that were predicted, and only if nothing drifted</td></tr>
<tr><td><b>Verify</b></td><td>Collector → Observability</td><td>The real network checked against the prediction: the loop closes</td></tr>
</table>

<p class="small muted">Swap any block for the tool you use; the workflow is the part that carries over. Nothing reaches the network without evidence, and nothing is done until the network agrees.</p>

Note:
The point to land: pushing config is a solved problem; knowing what it will do is not. A valid, reviewed change can still take out a service two routers away (you'll do exactly that at 11:15). The workflow is what puts evidence between "I wrote it" and "it's live", and the NAF Framework (reference.networkautomation.forum) gives us shared names for the parts. We come back to this map at the wrap-up with what you actually ran.

---

<div class="kicker">Live walkthrough · 10:20</div>

## How a change becomes a verdict

<div class="flow">
<div class="step"><b>Pull request</b>changes <code>candidate/r4-bgp.eos</code></div><div class="arrow">›</div>
<div class="step"><b>CI job</b>code and tests come from <code>main</code></div><div class="arrow">›</div>
<div class="step"><b>Baseline check</b>yours, unchanged</div><div class="arrow">›</div>
<div class="step hot"><b>Predict</b>a change set on your baseline</div><div class="arrow">›</div>
<div class="step ok"><b>Judge</b>your tests, on the predicted network</div>
</div>

**Why does the CI job take the tests from `main`, not from the pull request?**

Note:
Open `.github/workflows/forward-predict.yml` and `src/workshop/predict.py` on the screen. Answer: a pull request must not be able to weaken its own test. Only the candidate file comes from the PR.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 10:25 → 10:45</div>

## Your first change through the pipeline

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

- Retire **one** stale advertisement on a new branch, and open a pull request
- Watch **forward/predict**. Expect only `STALE-CLEARED` to fail: that's "not done yet"
- Read the workflow and `predict.py` while you wait

<p class="small"><b>Why:</b> this puts a test inside the pull request review you already do.</p>

<p class="small muted">Exercise 2 · <b>Behind?</b> This one is skippable: go straight to exercise 3. <b>Early?</b> Side quest: write your own test.</p>

---

<div class="kicker">Predict is an API call</div>

## From Python, a few lines

```python
handle = client.change_sets.create(name, snapshot_id=baseline_id)
handle.set_commands("r4", candidate_text)        # the exact lines you will deploy
snapshot = handle.predict_and_wait(label)         # Forward builds the predicted network
report = evaluate(requirements, observer(snapshot.id))   # your tests, on that network
```

<p class="tiny">Simplified from <code>src/workshop/forward.py</code> and <code>predict.py</code>. The Forward Python SDK makes every call.</p>

Note:
Emphasise "programmable part of a pipeline, not a UI walkthrough". The candidate text is the same bytes NAPALM later sends to the router.

---

<div class="kicker">Tests are code</div>

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

<p class="small muted">Four kinds: <b>flow</b>, <b>route</b>, <b>path</b> and <b>nqe</b> (a query over the network). Reviewed and versioned like any code.</p>

Note:
Show requirements/candidate.yml. Five tests today. They can write their own in the stretch work.

---

<div class="kicker">The evidence</div>

## What was predicted, against what

<div class="cols">
<div><ul><li>the candidate's hash</li><li>the baseline it was predicted against, and its fingerprint</li><li>the requirements' hash</li><li>the change set and predicted snapshot</li><li>every result, with what Forward observed</li></ul></div>
<div class="card"><h4>Why it matters</h4><p>Deploy refuses unless the evidence matches: the same candidate, the same tests, the same baseline, and routers that haven't drifted.</p></div>
</div>

Note:
This is the bridge to the deploy guards later. `evidence/evidence.json` on the Codespace.

---

<!-- .slide: class="checkpoint" -->
<div class="kicker">Checkpoint · 10:45</div>

## Did your pull request get a verdict?

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

- Your pull request is open from its own branch (not <code>main</code>)
- The <b>forward/predict</b> check ran, and you read its summary
- You know which requirement failed, and why

<div class="behind"><b>Behind?</b> The check can queue for a few minutes while GitHub starts it: the page and the PR say so. Read the pipeline code while you wait.</div>

Note:
Tiles show predicting, then red. This red is expected. Watch how long tiles stay predicting; if fwd.app queues, tell the room it is the wave and keep reading code. If GitHub Actions is slow, see the handbook runbook.

---

<!-- .slide: class="title" -->
<div class="kicker">10:45 → 11:15</div>

## Break

<p class="muted">Back at 11:15. If your Codespace naps while you're away, <code>workshop up</code> wakes it. Coffee does the same for you.</p>

---

<!-- .slide: class="section" -->
<div class="num">4</div>
<div class="kicker">11:15 · Section 4 of 6</div>

## Break it before you deploy it

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

<div class="goal">Make a change that looks valid, and watch Predict catch the damage before any router is touched.</div>

<div class="finish">By 12:00 you have: a predicted FAIL, the line responsible found, and proof the real network is untouched.</div>

<p class="small muted">Presenting: {{WHO:breakit}}</p>

Note:
Handoff: {{WHO:pipeline}} → {{WHO:breakit}}. Exercise 3. All three network statements look the same: finish the job. The retire-all PR goes red (APP-EXISTING, ROUTE-SERVICE and PATH-SERVICE fail). `workshop probe` proves the live network is untouched. At 11:40 walk the investigation on the projector.

---

<div class="kicker">11:15 · Break it before you deploy it</div>

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

Note:
Set up the exercise: they make this change on purpose. Remind them to run `workshop probe` afterwards to see the real network is unchanged.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 11:15 → 11:40</div>

## Break it, and read why

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

- Make the change above, open the PR, watch **forward/predict** go red
- Which tests failed? What did Forward observe?
- `workshop probe`: the real network is unchanged

<p class="small"><b>Why:</b> valid, short, looks right, and it cuts off the service. The cause is on r4, the damage on r1.</p>

<p class="small muted">Exercise 3 · <b>Behind?</b> Steps 1 to 3 and read the summary. Skip the AI discussion. <b>Early?</b> Once you have seen a red check: which lines are stale?</p>

---

<div class="kicker">11:40 · Investigation</div>

## Read the verdict

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

<table class="verdict">
<tr><th>Requirement</th><th>Result</th><th>Forward observed</th></tr>
<tr><td>APP-EXISTING</td><td class="f">FAIL</td><td>BLACKHOLE</td></tr>
<tr><td>MGMT-DENY</td><td class="p">PASS</td><td>still blocked</td></tr>
<tr><td>ROUTE-SERVICE</td><td class="f">FAIL</td><td>r1 has no route to 10.20.20.0/24</td></tr>
<tr><td>PATH-SERVICE</td><td class="f">FAIL</td><td>not delivered</td></tr>
<tr><td>STALE-CLEARED</td><td class="p">PASS</td><td>0 stale advertisements</td></tr>
</table>

The stale advertisements are gone, and the service is gone with them. On your pull request: the **Change analysis**. It opens as a change request: **why** (Forward's finding on your baseline), **the risks Forward already saw** (every host reaches the service through r4; 2222 stays blocked), **the exact config**, **when**. Then every host's reach, before and after, and which sites lose the Service.

Note:
Have them scroll the PR's Conversation to the Change analysis comment: it's the wow moment. Start at "1 · The change request": Forward named the risk (5 of 5 hosts reach the service through r4) before anyone wrote a line of config; the reviewer reads the same page. The "Every host to the service" table shows all five hosts losing the service from one line on r4. Read a real red check from the room if someone volunteers. The "stale cleared" pass is the trap: the change achieved its goal and broke the network.

---

<div class="kicker">Follow the evidence</div>

## Why does the whole diamond lose the route?

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

<div class="flow">
<div class="step hot"><b>r4</b>stops advertising <code>10.20.20.0/24</code></div><div class="arrow">›</div>
<div class="step"><b>r2, r3</b>lose the route</div><div class="arrow">›</div>
<div class="step"><b>r1</b>has no route to the service</div><div class="arrow">›</div>
<div class="step hot"><b>client</b>TCP 8080 blackholed</div>
</div>

Which of the three statements carried the service? How could you have known **before** the change?

Note:
Let a couple of people answer. The service prefix is directly connected on r4; its network statement is what puts it into BGP. The stale two have no route behind them.

---

<div class="kicker">AI advises, Predict decides</div>

## Ask Forward AI, then check it

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

<div class="cols">
<div class="card"><h4>Asked with no context</h4><p>"Why can the client no longer reach the service?"</p><p class="small bad">Blames r1 and suggests a static route there. Right symptom, wrong cause.</p></div>
<div class="card good"><h4>Given the facts</h4><p>"This change removes these three statements. With it, the client can't reach the service. Which caused that?"</p><p class="small ok">Names <code>network 10.20.20.0/24</code> as the culprit.</p></div>
</div>

**Framing matters. The requirements, on the predicted network, are the judge.**

<p class="small muted">It shows its work: when it ran NQE queries, <b>How it got that</b> under the answer lists them. Run one yourself with <code>workshop nqe</code>.</p>

Note:
From our own rehearsal on fwd.app. The lesson is not "AI is bad" but "AI output is advice to be checked". Prediction is the check. The "How it got that" fold on the lab page (and the end of `workshop ask`) shows the queries Forward AI wrote: running its query is one way to check what it said; the requirements on the predicted network are still the judge.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 11:40 → 12:00</div>

## Find the line responsible

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

- Compare with your first pull request: what's different?
- `workshop explain` (after the local predict steps)
- Finished early? `workshop matrix` predicts every combination

<p class="small muted">Exercise 3, continued</p>

---

<!-- .slide: class="checkpoint" -->
<div class="kicker">Checkpoint · 12:00</div>

## Did Predict catch it?

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="on">Predict</span><span>Approve</span><span>Deploy</span><span>Verify</span></div>

- Predict said <b>FAIL</b> on your change
- You can say which requirements broke, and why
- <code>workshop probe</code> still shows 8080 open: nothing was deployed

<div class="behind"><b>Behind?</b> Run the predict steps on your change (<code>workshop predict changeset</code>, <code>run</code>, <code>check</code>), then <code>workshop explain</code> for the plain-words reason, or ask a proctor to walk it with you.</div>

Note:
About 11:35 most tiles are red and the feed shows a change was held at the gate before deploy. Discussion: the chat that blames r1. AI advises, Predict decides.

---

<div class="kicker">And a time it didn't</div>

## Predict got one wrong while we built this

- Our first scenario changed an ACL line on r1 by resending sequence 10 with a new port
- Real cEOS rejects that: <code>% Error: Duplicate sequence number</code>, and keeps the old entry
- Predict, on the development build we were using, accepted it and modelled both entries. No router could hold that config
- So we changed scenarios. And it's why the loop doesn't stop at Predict: <code>deploy render</code> shows Forward's diff next to the router's own, and <code>verify</code> collects the real network again

<p class="small muted">That was a from-source build, not the fwd.app release, and we didn't retest it on the release. The whole story: How it works, section b.</p>

Note:
Tell it straight, no spin. The point isn't "the model is bad". Any model is a model, and a good pipeline assumes it will be wrong sometimes and checks. That's why render and verify exist. If someone asks whether it's fixed: we don't know, we didn't retest that case on the release.

---

<!-- .slide: class="section" -->
<div class="num">5</div>
<div class="kicker">12:00 · Section 5 of 6</div>

## Fix it and prove it

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span class="on">Approve</span><span>Deploy</span><span>Verify</span></div>

<div class="goal">Finish the job safely, let it through the gate, and merge.</div>

<div class="finish">By 12:30 you have: a candidate Predict judges PASS, and the pull request merged.</div>

<p class="small muted">Presenting: {{WHO:fixit}}</p>

Note:
Exercise 4. Fix, push, green, merge. Show a merge refused on the red retire-one PR. Fill: workshop agent on a scratch branch.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 12:00 → 12:30</div>

## Fix it, and let it through the gate

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span class="on">Approve</span><span>Deploy</span><span>Verify</span></div>

- Keep the live advertisement. Push the fix to the same branch
- **forward/predict** re-runs: a regression test on every commit
- Green? **Merge** (Squash and Merge). Only a green check can

<p class="small"><b>Why:</b> the fix goes through the same gate. No shortcuts, for anyone.</p>

<p class="small muted">Exercise 4 · <b>Behind?</b> Retire only the two stale advertisements, open the PR, merge when green. <b>Early?</b> Side quest: every way of retiring the lines, or let an adviser draft it.</p>

---

<!-- .slide: class="checkpoint" -->
<div class="kicker">Checkpoint · 12:30</div>

## Is it green and merged?

<div class="pipe"><span class="done">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span class="on">Approve</span><span>Deploy</span><span>Verify</span></div>

- <b>forward/predict</b> says PASS on the fixed change
- The pull request is <b>merged</b> into main
- Your lab is still at its baseline: nothing deployed yet

<div class="behind"><b>Behind?</b> Stuck on red? Pair with a finished neighbor, or use <b>Behind or stuck? Catch me up</b> on your lab page.</div>

Note:
About 12:20 tiles go green, then approved. Help anyone still red and pair them with a finished neighbor.

---

<!-- .slide: class="section" -->
<div class="num">6</div>
<div class="kicker">12:30 · Section 6 of 6</div>

## Deploy and verify

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="done">Predict</span><span class="done">Approve</span><span class="on">Deploy</span><span class="on">Verify</span></div>

<div class="goal">Send exactly what Predict approved, then check that reality matched the prediction.</div>

<div class="finish">By 12:50 you have: the change deployed to r4, and <code>workshop verify compare</code> saying MATCH.</div>

<p class="small muted">Presenting: {{WHO:deploy}}</p>

Note:
Handoff: {{WHO:fixit}} → {{WHO:deploy}}. Exercise 5. `workshop deploy gates`, `render`, `apply`, `readback` (with `--pr N --confirm HASH`), then the five verify steps. Put `deploy render` on the projector: one change, the same lines in Forward's model and in r4's own diff. Then the change window (optional, 3 minutes): `workshop deploy apply ... --at <now+2>`, and while it counts down `workshop link down` in a second terminal: at the window, NOT DEPLOYED (STALE). The approval is for the network Forward predicted, not whatever it has become. Then `workshop link up` (the fingerprint matches again) before deploying for real. Fill: the drift experiment (hand edit, verify MISMATCH), then `workshop restore` and the baseline steps.

---

<!-- .slide: class="work" -->
<div class="kicker">Work time · 12:30 → 12:50</div>

## Deploy, collect, compare

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="done">Predict</span><span class="done">Approve</span><span class="on">Deploy</span><span class="on">Verify</span></div>

- Copy the deploy command from the top of the green check's summary
- `workshop deploy gates` → `render` → `apply` → `readback`: you type the hash
- `workshop verify probe` … `compare` → **MATCH**
- Real changes wait for a window: **Apply at the window** (or `--at HH:MM`) checks every gate now and again when it opens. Change a router in between: **STALE**, nothing sent

<p class="small"><b>Why:</b> approval only counts if what you deploy is what was approved, against the network Forward predicted, and you check that reality agreed.</p>

<p class="small muted">Exercise 5 · <b>Behind?</b> Three steps: sync <code>main</code>, deploy, verify. <b>Early?</b> Side quests: cheat the gate, catch the drift.</p>

---

<!-- .slide: class="checkpoint" -->
<div class="kicker">Checkpoint · 12:50</div>

## Did reality match the prediction?

<div class="pipe"><span class="done">Baseline</span><span class="done">Propose</span><span class="done">Predict</span><span class="done">Approve</span><span class="on">Deploy</span><span class="on">Verify</span></div>

- <code>workshop deploy</code> applied the change to r4
- <code>workshop verify compare</code> says <b>MATCH</b>
- The real flows agree: 8080 open, 2222 blocked

<div class="behind"><b>Behind?</b> Deploy needs the merged pull request number and the 7-character hash: <code>workshop deploy gates --pr N --confirm HASH</code>, then <code>render</code>, <code>apply</code>, <code>readback</code> with the same flags.</div>

Note:
About 12:45 tiles are solid green and the board total for re-checked climbs. Then the wrap-up.

---

<div class="kicker">12:50 · Wrap-up</div>

## What you ran today

<div class="pipe"><span class="on">Baseline</span><span class="on">Propose</span><span class="on">Predict</span><span class="on">Approve</span><span class="on">Deploy</span><span class="on">Verify</span></div>

<table>
<tr><th>Stage</th><th>The step you ran</th></tr>
<tr><td><b>Baseline</b></td><td><code>workshop baseline collect</code> → <code>upload</code> → <code>wait</code> → <code>check</code></td></tr>
<tr><td><b>Propose, Predict</b></td><td>a pull request, then <code>workshop predict changeset</code> → <code>run</code> → <code>check</code> in CI</td></tr>
<tr><td><b>Approve</b></td><td>you merged a green <code>forward/predict</code> check, and only that</td></tr>
<tr><td><b>Deploy</b></td><td><code>workshop deploy gates</code> → <code>render</code> → <code>apply</code> → <code>readback</code></td></tr>
<tr><td><b>Verify</b></td><td><code>workshop verify probe</code> → <code>collect</code> → <code>upload</code> → <code>wait</code> → <code>compare</code></td></tr>
</table>


Note:
Handoff: {{WHO:deploy}} → {{WHO:wrapup}}. Quick recap, one row per stage. The point to land: every stage was a separate step with its own evidence, and the only thing that could deploy was a PASS.

---

<div class="kicker">12:50 · Wrap-up</div>

## What we checked, and what we didn't

<table>
<tr><th>Stage</th><th>What we checked</th><th>What it doesn't cover</th></tr>
<tr><td><b>Baseline</b></td><td>a known start, its configs fingerprinted</td><td>operational state: links, sessions</td></tr>
<tr><td><b>Predict</b></td><td>your requirements, on the modelled result</td><td>what you didn't write; timing; the model's own mistakes</td></tr>
<tr><td><b>Approve</b></td><td>a person merges a green check</td><td>review: zero reviewers were required</td></tr>
<tr><td><b>Deploy</b></td><td>the predicted lines, only if no config drifted</td><td>a change in the second between gate and write</td></tr>
<tr><td><b>Verify</b></td><td>a new collection agreed, live probes agreed</td><td>anything you didn't probe or require</td></tr>
</table>

Note:
Tie each row back to something they did today. The right-hand column is the honest part: docs/exercises/how-it-works.md has the detail for anyone who asks.

---

<div class="kicker">The NAF Framework</div>

## Where today's steps sit in the framework

- **Intent:** the candidate and the requirements, in Git
- **Collector** and **Observability:** Forward reads the network and judges it, before and after
- **Orchestrator:** the pull request and its check. It never touches a router
- **Executor:** NAPALM, writing exactly what Predict judged

<p class="small muted">Swap any one block and the loop still works. Today the Executor and the candidate's syntax are EOS-specific.</p>

Note:
The callback to the map at the start, now with what they ran. Point at reference.networkautomation.forum/Framework/Framework. The hand-off to land is Observability to Orchestrator: the pipeline continues only on PASS. Forward covers two blocks, the collector and the model, and that is why they are named separately. The full map is in docs/exercises/framework.md.

---

<!-- .slide: class="meme" data-nobuild -->
<div class="kicker">What you did today</div>

<div class="cap">Diff looked fine. Syntax check passed. A reviewer would have approved it.</div>
<div class="pic">🤖🔮🛑</div>
<div class="cap bottom">Forward: "5 of 5 hosts lose the service." Before a single router changed.</div>

Note:
The whole morning in one slide. Pause on it.

---

<div class="kicker">With or without Forward</div>

## Five rules worth stealing

1. **Deploy exactly what you tested.** Same bytes, checked by hash
2. **Approval is for one change.** Bound to that candidate, that baseline, those requirements
3. **"Couldn't tell" is not a pass.** Empty, unknown or stale never turns green
4. **Check for drift before you write.** The configs you predicted against are the ones you change
5. **Verify against the prediction.** Not against hope, and not against "no alarms"

<p class="small muted">Predict needs a model of the network. These rules don't: they work in any pipeline you run today.</p>

Note:
This is the slide to land if they forget everything else. Each rule is something they watched the workshop enforce: deploy refused a hash that didn't match, a STALE wouldn't deploy, the drift side quest, verify MATCH. Ask the room which one their pipeline breaks today.

---

<div class="kicker">Monday morning</div>

## You don't need the whole pipeline to start

1. Pick **one kind of change** you make often
2. Write **three requirements** for it: reachable, blocked, the path
3. Run Predict on every pull request, **report-only** at first
4. Make the check **required** once you trust it

<p class="small muted">Keep AI as an adviser. The requirements decide.</p>

Note:
Make it small and concrete. The aim is one requirement file and one check on one pull request by next week.

---

<div class="kicker">Where this goes</div>

## The same pattern, bigger

- **More tests, same gate.** A regression suite is more requirements, run on every change
- **Any pipeline.** The gate is a command with exit codes; put it in the CI you already run
- **More autonomy.** Agents that draft and iterate while people approve
- **Not tested here.** Bigger networks, other platforms, many changes in flight: validate those first

<p class="small muted">Only PASS deploys. That doesn't change when the author is an agent.</p>

Note:
Mention the advisers (ask, propose, explain, agent) they could try in stretch work, and that they're welcome to bring their own coding agent; AGENTS.md gives it the rules.

---

<div class="kicker">The room, by the numbers</div>

## What we did together

<div class="score" id="score">
<div class="tiles">
<div class="stat big" data-k="caught"><div class="num">–</div><div class="lbl">changes held at the gate before deploy</div></div>
<div class="stat" data-k="predictions"><div class="num">–</div><div class="lbl">predictions run</div></div>
<div class="stat" data-k="verified"><div class="num">–</div><div class="lbl">networks re-checked after a change</div></div>
</div>
<div class="funnel">
<div class="muted">how far each seat got</div>
<div class="f-row" data-k="claimed"><span>took a seat</span><span class="f-track"><span class="f-bar"></span></span><span class="f-n">–</span></div>
<div class="f-row" data-k="baselines"><span>baselined</span><span class="f-track"><span class="f-bar"></span></span><span class="f-n">–</span></div>
<div class="f-row" data-k="merged"><span>merged</span><span class="f-track"><span class="f-bar"></span></span><span class="f-n">–</span></div>
<div class="f-row" data-k="verified"><span>verified</span><span class="f-track"><span class="f-bar"></span></span><span class="f-n">–</span></div>
</div>
</div>

<p class="offline" id="score-offline">Live from the room board when this page is served by the claim service. Offline, read the three totals off the board.</p>

Note:
Open the board and read the totals aloud (after 12:50 its wrap-up scoreboard shows all three). This is the proof point: every held change was stopped before it could merge.

---

<div class="kicker">Take it home</div>

## What you have

- The exercises and `AGENTS.md` in your seat repository
- A requirement you wrote (or can write) in `requirements/`
- **Go deeper** (`docs/exercises/go-deeper.md`): Forward's docs for each feature you used, netlab, NAPALM, GitHub rulesets, and where to look when a tool breaks
- The loop: **Baseline → Propose → Predict → Approve → Deploy → Verify**

**Your seat stays up until Sunday, November 22, 8 PM Tucson.** Finish at your own pace, then keep a copy: on your repository's page, **Code → Download ZIP** (or `git clone` it). After that the seat, its Forward network and its repository are removed.

**All of it, public now:** <code>github.com/forwardnetworks/autocon6-know-before-you-deploy</code>: the exercises, the lab, the <code>workshop</code> command and these slides. No sign-up.

Note:
Read the date on the slide out loud: seats stay up a week (agenda.json, teardown). Tell them to download their repository before then. The repository is public (made public the night before, MIT licensed). Read the address out.

---

<!-- .slide: class="title" -->
# Questions?

<p style="margin-top:1em">One thing that didn't work, or confused you? Post it in <code>#ac6-ws-a4</code> or open an issue on the repository. Fixes go in this week, in the open.</p>

<p class="muted" style="margin-top:1em">Craig Johnson · Sean Deveci · Mike Lossmann<br>Slack: <code>#ac6-ws-a4</code> · <code>@wsa4</code> in the channel</p>

<p class="small muted">Fixes and questions: issues on github.com/forwardnetworks/autocon6-know-before-you-deploy</p>
