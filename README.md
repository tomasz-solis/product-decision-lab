# Product Decision Lab

I build the systems product teams use to decide under uncertainty — measurement
readiness, experimentation, and decision analysis for the common case where the
experiment is imperfect, the signal is noisy, and a call still has to be made.

This repository is a guided index to my public work. It isn't a set of isolated
technical demos. It's meant to show how I approach ambiguous product problems: frame the
decision, make the assumptions explicit, quantify the uncertainty, test the claims, and
turn the result into something a team could actually use.

## The thesis

Most product decisions are made on incomplete evidence. Sometimes there's no clean
experiment. Sometimes the public signals mislead. Sometimes the metrics exist but don't
answer the real question. Sometimes the business case rests on assumptions nobody wrote
down. The work I care about lives between the analysis and the decision it's supposed to
serve.

Three questions organize the portfolio, and together they trace one product decision
from start to finish:

1. **Can we trust our metrics enough to decide?** — measurement readiness.
2. **How do we get evidence when experiments are imperfect?** — experimentation and
   causal inference.
3. **How do we decide when the evidence is still incomplete?** — decision analysis under
   uncertainty.

Measure, test, decide. The three headline projects below map onto those three questions.

---

## Headline projects

### Product Decision Under Uncertainty
[Repo](https://github.com/tomasz-solis/product-decision-under-uncertainty) ·
[Live app](https://beforeyouship.streamlit.app/)

A decision-analysis case study for one irreversible platform investment. It models the
competing options with Monte Carlo simulation, tracked assumption provenance, correlated
risk, an explicit guardrail policy, and a policy frontier. The point isn't to predict the
future. It's to make the tradeoffs visible enough that a leadership team can review the
call — and to answer the question point estimates can't: how far would we have to be
wrong for the recommendation to change?

### Experiment Architect
[Repo](https://github.com/tomasz-solis/experiment-architect) ·
[Live app](https://testarchitect.streamlit.app/)

A toolkit for planning and reading product experiments: A/B sizing, reverse MDE, causal
method selection, difference-in-differences and regression discontinuity with their
diagnostics, and both frequentist and Bayesian analysis with loss-aware ship/hold
decisions. Experimentation maturity isn't sample-size arithmetic. It's knowing when an
experiment is feasible, when causal inference is the right fallback, and when the evidence
isn't strong enough to ship on.

### Measurement Maturity Framework
[Repo](https://github.com/tomasz-solis/measurement-maturity-framework)

A decision-readiness audit for product metrics. It checks whether a product area has the
ownership, instrumentation, guardrails, and review rhythm to make reliable recurring
decisions — and reports how many of the area's key decisions are actually backed by
trusted, owned metrics. Good measurement isn't more dashboards. It's whether a team can
rely on the numbers it already has.

---

## The rest of the portfolio

The three above are the spine. These show the same thinking in other settings.

- **[Trackside Labs](https://github.com/tomasz-solis/trackside-labs)** — a live Formula 1
  prediction system that updates as each race weekend produces new evidence. Applied ML
  and forecasting under sparse, fast-changing signals, with calibration and evaluation
  built in.
- **[Public Signals Mislead](https://github.com/tomasz-solis/public-signals-mislead)** — a
  strategy case study on why public signals (search interest, online sentiment) should
  trigger investigation, not drive decisions. Separating a signal from the outcome it's
  taken to stand for.
- **[Dial In](https://github.com/tomasz-solis/dial-in)** — a small operator-facing tool for
  café prep planning under uncertain demand, where stockouts hide true demand and waste is
  costly. Not every useful data product needs a platform behind it.

Also here: an agent-orchestrated experiment-decision pipeline
([product-referee](https://github.com/tomasz-solis/product-referee)), and a few earlier
causal-inference studies listed in the map below.

---

## How I'd read it

If you have five minutes:

1. **Product Decision Under Uncertainty** — the clearest example of decision science and
   senior product judgment.
2. **Experiment Architect** — experimentation and causal product-data thinking.
3. **Measurement Maturity Framework** — reusable analytical systems others can operate.

By the kind of role:

- **Product Data Scientist / Decision Scientist:** Experiment Architect, then Product
  Decision Under Uncertainty, then Public Signals Mislead.
- **Staff / Principal Product Analyst:** Product Decision Under Uncertainty, then
  Measurement Maturity Framework, then Public Signals Mislead.
- **Applied ML / Decision Systems:** Trackside Labs, then Product Decision Under
  Uncertainty, then Dial In.

---

## How I work

A few patterns run through all of it.

**Define the decision before the method.** The useful question isn't "can we analyze
this?" It's "what decision will this inform, and what would change our mind?"

**Keep signals and outcomes separate.** Search interest isn't adoption, backlash isn't
churn, dashboard usage isn't decision quality, and statistical significance isn't business
value. A lot of bad calls come from treating a signal as the outcome.

**Make assumptions reviewable.** When evidence is incomplete, assumptions are
unavoidable. The goal isn't to remove them but to make them explicit and easy to argue
with.

**Treat uncertainty as an input, not an excuse.** What has to be true for this option to
win? Where's the downside? Which assumptions drive the recommendation, and what evidence
would change it?

**End on a policy, not on "it depends."** Ship if, hold if, test if, roll back if. The
policy doesn't have to be perfect. It has to be explicit enough to review.

---

## What's public, and what isn't

These projects are built on synthetic and public data, and they're generalized on
purpose. The production versions run against real OKRs, telemetry, and stakeholders that
NDAs keep private. What's here is the reusable engine — and generalizing it well took more
judgment than the original build. Where a project uses a public dataset, it says so and
explains what it's standing in for.

---

## Repository map

```
product-decision-lab
├── decision science
│   ├── product-decision-under-uncertainty
│   ├── public-signals-mislead
│   └── measurement-maturity-framework
├── experimentation and causal inference
│   ├── experiment-architect
│   ├── causal-guardian
│   ├── rdd-free-shipping
│   ├── ipo-lockup-did-analysis
│   └── product-referee
└── applied ML and product systems
    ├── trackside-labs
    ├── dial-in
    └── decant
```

---

## About me

I'm a senior product data scientist working on the decision layer of product analytics —
experimentation, causal inference, and decision analysis under uncertainty. I'm drawn to
the problems where the signal is noisy, the decision is high-impact, the data is
incomplete, the assumptions matter, and the right answer is a decision system rather than
a dashboard.

- GitHub: [github.com/tomasz-solis](https://github.com/tomasz-solis)
- LinkedIn: [linkedin.com/in/tomaszsolis](https://www.linkedin.com/in/tomaszsolis)
