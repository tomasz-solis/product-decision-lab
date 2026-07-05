# Product Decision Lab

A guided index to my public work in product data science. I work on the
decision layer of product analytics: measurement readiness, experimentation and
causal inference, and decision analysis when the evidence is incomplete.

The projects here are not isolated technical demos. Each one starts from a
decision a product team has to make, states its assumptions, quantifies the
uncertainty, tests the claims that can be tested, and ends with something the
team could operate without me.

## The thesis

Most product decisions are made on incomplete evidence. There is often no clean
experiment, the metrics don't answer the real question, and the business case
rests on assumptions nobody wrote down. The uncertainty doesn't go away. The
useful work is making the tradeoffs clear enough that a team can decide well
anyway.

Three questions organize the portfolio, and together they trace one product
decision from start to finish:

1. **Can we trust our metrics enough to decide?** (measurement readiness)
2. **How do we get evidence when experiments are imperfect?** (experimentation
   and causal inference)
3. **How do we decide when the evidence is still incomplete?** (decision
   analysis under uncertainty)

Measure, test, decide. The three headline projects below map onto those
questions.

---

## Headline projects

### Product Decision Under Uncertainty
[Repo](https://github.com/tomasz-solis/product-decision-under-uncertainty) ·
[Live app](https://beforeyouship.streamlit.app/)

A decision-analysis case study for one irreversible platform investment. It
models the competing options with Monte Carlo simulation, tracked assumption
provenance, correlated risk, an explicit guardrail policy, and a policy
frontier. The output is a recommendation a leadership team can review, plus the
answer point estimates can't give: how far the assumptions would have to be
wrong before the recommendation changes.

### Experiment Architect
[Repo](https://github.com/tomasz-solis/experiment-architect) ·
[Live app](https://testarchitect.streamlit.app/)

A toolkit for planning and reading product experiments: A/B sizing, reverse
MDE, causal method selection, difference-in-differences and regression
discontinuity with their diagnostics, and both frequentist and Bayesian
analysis with loss-aware ship/hold decisions. It covers the calls that come
before and after the arithmetic: whether an experiment is feasible at all,
which causal fallback to use when it isn't, and whether the evidence is strong
enough to ship on.

### Measurement Maturity Framework
[Repo](https://github.com/tomasz-solis/measurement-maturity-framework) ·
[Live app](https://metricready.streamlit.app/)

A decision-readiness audit for product metrics. It models a product area as a
measurement graph (metrics, the decisions they feed, guardrails,
instrumentation, ownership, review rhythm) and reports how many of the area's
key decisions are backed by trusted, owned, instrumented metrics. The failure
modes it counts are orphaned metrics, missing owners, and decisions with no
metric behind them.

---

## The rest of the portfolio

The three above are the spine. These show the same thinking in other settings.

- **[Trackside Labs](https://github.com/tomasz-solis/trackside-labs)**: a live
  Formula 1 prediction system that updates as each race weekend produces new
  evidence. Applied ML and forecasting under sparse, fast-changing signals,
  with calibration and evaluation built in.
- **[Public Signals Mislead](https://github.com/tomasz-solis/public-signals-mislead)**:
  a strategy case study on why public signals (search interest, online
  sentiment) should trigger investigation rather than drive decisions. The core
  distinction is between a signal and the outcome it is taken to stand for.
- **[Dial In](https://github.com/tomasz-solis/dial-in)**: a small
  operator-facing tool for café prep planning under uncertain demand, where
  stockouts hide true demand and waste is costly.

Also here: an agent-orchestrated experiment-decision pipeline
([product-referee](https://github.com/tomasz-solis/product-referee)), and a few
earlier causal-inference studies listed in the map below.

---

## How I'd read it

If you have five minutes:

1. **Product Decision Under Uncertainty**, the clearest example of decision
   science applied to a senior product call.
2. **Experiment Architect** for experimentation and causal product-data work.
3. **Measurement Maturity Framework** for reusable analytical systems that
   others can operate.

By the kind of role:

- **Product Data Scientist / Decision Scientist:** Experiment Architect, then
  Product Decision Under Uncertainty, then Public Signals Mislead.
- **Staff / Principal Product Analyst:** Product Decision Under Uncertainty,
  then Measurement Maturity Framework, then Public Signals Mislead.
- **Applied ML / Decision Systems:** Trackside Labs, then Product Decision
  Under Uncertainty, then Dial In.

---

## How I work

A few patterns run through all of it.

- Define the decision before the method. The first question is what decision
  the analysis will inform, and what would change our mind.
- Keep signals and outcomes separate. Search interest is not adoption, backlash
  is not churn, dashboard usage is not decision quality, and statistical
  significance is not business value.
- Make assumptions reviewable. Incomplete evidence makes assumptions
  unavoidable, so the goal is to write them down and make them easy to argue
  with.
- Treat uncertainty as an input. Which assumptions drive the recommendation,
  where the downside sits, and what evidence would change the call.
- End on a policy: ship if, hold if, test if, roll back if. It doesn't have to
  be perfect, but it has to be explicit enough to review.

---

## What's public, and what isn't

These projects are built on synthetic and public data, and they are generalized
on purpose. The production versions ran against real OKRs, telemetry, and
stakeholders that NDAs keep private. What's public here is the reusable engine,
and generalizing it well was harder than the original builds. Where a project
uses a public dataset, it says so and explains what it is standing in for.

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

I'm a senior product data scientist working on the decision layer of product
analytics: experimentation, causal inference, and decision analysis under
uncertainty. The problems I look for are the ones where the signal is noisy,
the data is incomplete, and the right answer is a decision system rather than
a dashboard.

- GitHub: [github.com/tomasz-solis](https://github.com/tomasz-solis)
- LinkedIn: [linkedin.com/in/tomaszsolis](https://www.linkedin.com/in/tomaszsolis)
