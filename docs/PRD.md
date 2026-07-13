# PRD — Product Decision Lab (landing page)

**Author:** Tomasz Solis
**Status:** Draft v0.3 — for iteration
**Last updated:** 2026-07-05

Companion docs: [`identity-block.md`](identity-block.md) (copy) and
[`case-briefs.md`](case-briefs.md) (the "in practice" layer). Settled decisions are in
§3; open questions are in §11.

---

## 1. Purpose

One fast, role-routable page that gets a recruiter or hiring manager to want a
conversation within about a minute, and gives someone in my network a single link they
can forward when they vouch for me.

## 2. What the page is optimized for

Getting the interview, not winning the role. Legibility and low friction matter
more than analytical depth here, because depth only pays off once someone has
decided to look closely.

The path a reviewer takes, and where portfolios usually lose them:

| Step | The question in their head | Where most portfolios lose them |
|---|---|---|
| 1. Discovery | (they have to find it) | The page exists, but nothing routes to it |
| 2. Ten-second read | "Is this person at my level?" | Level has to be inferred, so they leave |
| 3. One-minute skim | "Real substance, or filler?" | Too dense and it intimidates; too thin and it's dismissed |
| 4. Reach out | "Is a 30-minute call worth it?" | No specific hook; no sense of a real operator |

The work already wins step 3. The page exists to stop losing steps 1, 2, and 4,
which are framing and distribution problems rather than building problems.

## 3. Settled decisions

- **Positioning:** Product Decision Scientist (see `identity-block.md`). Systems
  thinking is the thesis, shown by the work, not the title.
- **Three headline apps**, read as one system: Measurement Maturity (can we trust our
  metrics?), then Experiment Architect (how do we get evidence?), then Decision Under
  Uncertainty (how do we decide when the evidence is still incomplete?). Measure, test,
  decide.
- **`product-referee` is a footnote, not a headline.** It overlaps Experiment
  Architect's ship/hold logic and would dilute the arc.
- **The page stays thin; the apps stay deep.** If the wrapper reads as the main
  piece of work, it works against a senior candidate.
- **NDA framing is matter-of-fact, not defensive** (see `identity-block.md`). The page
  never ties work to a named employer. One shared paragraph after the app cards,
  not repeated per card.
- **The one thing to read first is Product Decision Under Uncertainty.**
- **Host and URL (settled 2026-07-04):** GitHub Pages, branch deploy from `main`
  root, at `tomasz-solis.github.io/product-decision-lab`. A custom domain can be
  added later without rework.
- **Off-thesis repos stay off the page (settled 2026-07-04):** the footer's link
  to the full README index covers them.

## 4. Audience

| Reader | Time | Wants | What the page owes them |
|---|---|---|---|
| Recruiter | ~30s | Level and fit, plus a sign of seniority | Thesis and a paste-ready level line, in plain language |
| Hiring manager | 2–3 min | One strong piece of work, and evidence of judgment | The start-here app, the systems arc, one case brief |
| Technical interviewer | deep | Real depth, code, methods | Direct links to repos, narrative and methods docs, live apps |

## 5. Goals and non-goals

**Goals**
- Level and thesis clear in the first ten seconds, above the fold, paste-ready for a recruiter.
- The measure–test–decide arc is stated, not left to be inferred.
- One anonymized case brief on each headline app.
- Every app reachable in a click, each with a static fallback for when it's asleep.
- One memorable URL that LinkedIn, the CV, and GitHub all point to.

**Non-goals**
- Not a blog, and not a rebuild of the README (link to it instead).
- Not a per-app deep dive; that's each repo's job.
- No auth, no backend, no CMS.
- Winning the role is the interview's job, not the page's.

## 6. What success looks like

The criteria are qualitative. The one number that matters is replies and
interview invites per batch of outreach, tracked by hand.

- A peer can repeat the measure–test–decide arc after one read.
- A non-technical reader can say what each app is for, in plain terms.
- Time to grasp the thesis is under ten seconds (test it on three people).
- No broken or asleep first impressions during a skim.

## 7. Page structure (single page, thin)

1. **Hero**: name, title, thesis line, one "Start here" link to Product Decision
   Under Uncertainty.
2. **The system**: the three apps as one diagram (measure, test, decide), a sentence
   each on the decision it improves. This is the centerpiece.
3. **Three app cards**: spec in §8.
4. **Read one thing**: Decision Under Uncertainty, with the honest hook that no option
   clears the guardrails, and why that is the interesting result.
5. **Routes by role**: three short columns reusing the README's review paths.
6. **A note on reuse**: one paragraph making clear these are tools other people can
   operate, not one-off analyses.
7. **Footer**: GitHub, LinkedIn, the full README index, the `product-referee` footnote.

## 8. App card spec

- One line on the decision it improves, in plain language, not a feature list.
- An "In practice" box with the anonymized case brief.
- Two links: the live app, and the written case (the durable fallback).
- A static screenshot that renders even when the app is asleep.
- Three or four method tags.
- A quiet "wakes in about 10s" note on the live link.
- The shared NDA paragraph sits once after the cards (see §3).
- Optional: a short walkthrough clip.

## 9. Requirements

**Functional**
- Static single page, no build complexity.
- Every live-app link paired with a static fallback.
- Legible on mobile; the thesis readable without scrolling on desktop.
- A plain-language top layer, with the technical depth one click down.

**Non-functional**
- Keep-awake on all three apps. A scheduled Playwright workflow in this repo
  visits each app every six hours with a real browser session; a plain HTTP GET
  returns 200 without counting as viewer activity, which is why the earlier
  curl-based workflow was removed as broken.
- Fallback-first: the page holds its value even if all three apps are down.
- Any headline numbers match each repo's published artifacts. The repos already
  content-address their artifacts, so reuse those rather than restating by hand.
- GitHub disables schedule-triggered workflows after 60 days of repo
  inactivity, which would silently stop the keep-awake job and let all three
  apps hibernate. A GITHUB_TOKEN/Actions-bot commit does not reset that clock,
  so the mitigation is a periodic manual re-trigger or a real commit.

## 10. Risks

| # | Risk | How it's handled |
|---|---|---|
| R1 | Reads as a link farm | The system arc is the hero, not the tiles |
| R2 | Polish reads as "built for the portfolio" | Scar-tissue detail, the NDA framing, the case briefs |
| R3 | Three live apps, three things that can be asleep | Keep-awake plus static fallbacks |
| R4 | Wrapper thicker than the apps | Keep the page thin; depth one click down |
| R5 | Nothing routes to it | LinkedIn, GitHub README, and CV all point here; forward it to warm contacts |

## 11. Open questions

- **Q4 — Walkthrough clips:** fast follow after launch, not v1.

Resolved and moved to §3: host and URL (Q1, Q2), off-thesis repos (Q3), NDA
placement (Q5).

## 12. Milestones

1. ~~Lock the thesis and the three-app arc copy.~~ Done (`identity-block.md`).
2. ~~Write and edit the three case briefs.~~ Done as drafts with edit points
   (`case-briefs.md`); real anonymized specifics still to be filled in.
3. ~~Capture screenshots; confirm a fallback artifact exists per app.~~ Done
   (`assets/`, all three fallback links verified).
4. ~~Build the static page.~~ Done (`index.html`).
5. Keep-awake on all three apps; check links and fallbacks. Keep-awake workflow
   is in place; links and fallbacks were checked manually (no automated
   link-checker exists). Verify the first scheduled runs after deploy.
6. Point LinkedIn, the GitHub README, and the CV at the lab.
7. Test with three peers against the ten-second and "repeat the arc" checks; revise.
8. Forward it to at least ten warm contacts with a one-line ask.

## Changelog

- **v0.3 (2026-07-05)** — Page built (index.html, screenshots, keep-awake
  workflow), prepared for deploy on GitHub Pages. Q1–Q3 and Q5 settled and moved
  to §3. Prose pass to the house voice.
- **v0.2 (2026-07-02)** — Positioning set to Product Decision Scientist; prose pass.
- **v0.1 (2026-06-28)** — First draft. Objective set to getting the interview; three-app
  arc and `product-referee`-as-footnote settled; companion copy and case-brief docs created.
