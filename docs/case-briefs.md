# Anonymized case briefs

Method docs show I can build something. A short case brief shows I've used it in a
real room, with real stakes. Each headline app gets one, 250–400 words, written
decision-first and safe to publish under NDA.

The three below are drafts to edit, not to publish as they stand. Replace the
bracketed parts with the real, anonymized specifics. They're written to be safe even
if I change nothing, but they're far stronger with the actual texture of the decision.

---

## NDA-safety checklist (apply to every brief)

- No company name, product name, or recognizable feature.
- No sector detail specific enough to identify the place (say "a platform team", not
  "a payments team at a Series-C fintech").
- No dates, no headcounts, no org-chart specifics that narrow it to one company.
- Outcomes stay directional ("shifted the decision", "avoided a likely write-off"),
  never exact figures.
- Never tie a situation to an employer — not here, not online, anywhere.
- When unsure, generalize one more level. The point is the judgment, not the case.

## Structure (reuse for each)

1. **Situation** — the decision at stake, anonymized, in a line or two.
2. **Why the standard approach fell short** — the default move, and why it was wrong
   here. This is where the judgment shows.
3. **What I did** — the move, in plain language, naming the method once.
4. **What changed** — how the decision or the conversation moved. Directional only.
5. **What I'd do differently** — one honest reflection.

---

## Brief 1 — Product Decision Under Uncertainty (`beforeyouship`)

**Choosing between irreversible options when there's no clean experiment.**

A team faced a set of mutually exclusive, hard-to-reverse options under a fixed
deadline. There was no way to run a clean experiment first. The choice had to be made
on assumptions, and once made it couldn't be cheaply undone.

The default was a business case with one payoff number per option, maybe three if the
author was careful. That framing quietly assumed everyone would trade expected value
against tail risk one-for-one, and it hid the fact that the options had very different
downside shapes. The debate kept circling the point estimates, which were the least
trustworthy numbers in the room.

I reframed the choice as a decision under uncertainty: explicit, reviewable
assumptions; a Monte Carlo model of the joint world instead of a spreadsheet of
midpoints; and the part that actually moved people, a guardrail policy plus a frontier
showing how far the assumptions would have to be wrong before the recommendation
flipped. As it happened, no option cleared every guardrail, so the honest
recommendation was an explicit expected-value fallback rather than a confident winner.

The conversation moved off whose point estimate was right and onto which assumptions
the decision actually turned on, and what guardrails would make a choice safe enough
to commit to. The recommendation carried its own "here's what would change our mind" —
that's what let leadership sign off.

Next time I'd elicit the guardrail thresholds from stakeholders before showing any
result. Anchoring the risk appetite first would have shortened the debate and made the
fallback land as a finding rather than a surprise.

> *Edit points:* what the options were (one level abstract), the deadline pressure, the
> one assumption that turned out to dominate, and the real "what changed".

---

## Brief 2 — Experiment Architect (`testarchitect`)

**Knowing when an experiment is feasible, and when to ship on something other than a p-value.**

A team wanted to A/B test a change, but the realistic traffic and baseline rate meant a
properly powered test would have run far longer than the decision window. The pressure
was to run it anyway and read the result early.

Running underpowered and peeking early is the classic way to ship on noise; the result
would have been directional at best and misleading at worst. But "we can't test, so go
with your gut" was the other bad option on the table. Neither the naive frequentist
read nor abandoning rigor was acceptable.

A reverse-MDE check made the real constraint legible first: the smallest effect this
test could detect in the time we had was larger than any effect we'd plausibly see, so
a clean A/B was the wrong tool. From there, I scoped the test to a
guardrail question it could answer, and framed the ship decision on a Bayesian read —
posterior probability of a positive lift and expected loss if we were wrong — instead
of a binary significance verdict. Where randomization wasn't possible at all, the job
was to pick the right causal fallback rather than pretend an A/B existed.

The decision stopped depending on a test that couldn't deliver in time. We shipped on
an explicit, loss-aware rule the team agreed to in advance, with guardrails watched
rather than ignored, and everyone understood what we were and weren't sure about.

Next time I'd bring the loss-aware framing into planning, not read-out. Agreeing on the
acceptable cost of being wrong is much easier before anyone has a result they like.

> *Edit points:* the metric, the real constraint (traffic vs. effect size), the method
> you actually used, and the agreed decision rule.

---

## Brief 3 — Measurement Maturity Framework (`MetricReady`)

**Catching that a metric isn't decision-ready before it drives a decision.**

A product area was about to start steering recurring decisions — targets, planning,
ship/hold calls — off a set of metrics that looked finished. The dashboards were
polished and the numbers were precise.

The instinct in the room was to debate methodology: the right way to define the
headline metric. But the real risk was structural, not analytical. Some metrics had no
clear owner, the SQL lived in someone's notebook rather than anywhere reviewable, and
several key decisions weren't backed by a trusted, instrumented metric at all. A
polished chart on top of an unowned, untested definition is exactly how a wrong number
reaches a board deck before anyone notices.

I ran the area through a decision-readiness audit instead of a methodology debate:
model it as a measurement graph — metrics, the decisions they feed, the guardrails, the
instrumentation, the ownership and review rhythm — and report the decision-centric
result: how many of this area's key decisions are backed by trusted, owned,
instrumented metrics, reported as a band rather than a false-precise score. Metric count
was never the measure; the problems were counted as orphaned metrics, missing owners,
and decisions with no metric.

The team stopped arguing definitions and fixed the cheap structural gaps first —
ownership, written-down SQL, basic tests — closing the readiness gaps while they were
still cheap, instead of discovering them live in a planning meeting.

Next time I'd run the audit at the start of the planning cycle, not once the metrics
were already being wired into targets. The framework is cheapest exactly when it feels
least urgent.

> *Edit points:* the structural gap that mattered most, the decision that would have
> been made on a shaky metric, and what the team fixed first.

---

## Where these go

One brief per headline app, in an "In practice" box on that app's card. Keep it visually
separate from the method docs — this is the human layer. If you record a short
walkthrough, narrate the brief over the live app.
