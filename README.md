# Product Decision Lab

A portfolio of decision science, product analytics, experimentation, and applied ML projects.

I build analytical systems for product teams operating under uncertainty: when experiments are limited, signals are noisy, and teams still need to make a call.

This repository is a guided index to my public work. The goal is not to show isolated technical demos, but to show how I approach ambiguous product and business problems: framing the decision, making assumptions explicit, quantifying uncertainty, testing claims, and turning evidence into something a team could actually use.

---

## Operating thesis

Most product decisions are made with incomplete evidence.

Sometimes there is no clean experiment.
Sometimes public signals are misleading.
Sometimes metrics exist, but do not answer the real decision.
Sometimes the business case depends on assumptions nobody has written down.
Sometimes the model is less important than the decision policy around it.

My work focuses on the space between analysis and action:

```text
messy inputs → explicit assumptions → uncertainty model → tradeoff analysis → decision-ready recommendation
```

The projects in this portfolio are grouped around three questions:

1. **How should we decide when the future is uncertain?**
2. **How should we test or infer impact when experiments are imperfect?**
3. **How do we know whether a product area is measurement-ready enough to make good recurring decisions?**

---

## Featured projects

### 1. Product Decision Under Uncertainty

**Repo:** [product-decision-under-uncertainty](https://github.com/tomasz-solis/product-decision-under-uncertainty)

A decision-analysis case study for an irreversible product/platform investment.

The project models competing strategic options using Monte Carlo simulation, assumption provenance, correlated uncertainty, guardrails, and a policy frontier. The point is not to predict the future perfectly. The point is to make the tradeoffs visible enough that a product or leadership team can review the recommendation.

**What it demonstrates**

* Decision framing under uncertainty
* Assumption provenance and auditability
* Monte Carlo simulation
* Correlated risk modeling
* Guardrail-based decision policy
* Translating analysis into a recommendation

**Why it matters**

Many product business cases hide uncertainty behind a single expected-value number. This project treats uncertainty as part of the decision, not an appendix.

---

### 2. Trackside Labs

**Repo:** [trackside-labs](https://github.com/tomasz-solis/trackside-labs)

A live Formula 1 prediction system that updates forecasts as new race-weekend evidence becomes available.

The domain is F1, but the underlying problem is broader: how do you make predictions under sparse, noisy, and fast-changing evidence? The project combines historical baselines, current-session signals, uncertainty bands, evaluation reports, and production-style update flows.

**What it demonstrates**

* Applied ML system design
* Forecasting under noisy evidence
* Incremental model updates
* Calibration and evaluation discipline
* Production-oriented project structure
* Separating baseline signal from live evidence

**Why it matters**

This is a practical example of building a prediction system, not just a notebook. It shows how I think about evidence quality, uncertainty, and model behavior over time.

---

### 3. Experiment Architect

**Repo:** [experiment-architect](https://github.com/tomasz-solis/experiment-architect)

A product experimentation toolkit for planning, diagnosing, and interpreting product tests.

It covers A/B test sizing, reverse MDE, causal method selection, Bayesian and frequentist analysis, guardrail metrics, and loss-aware ship/hold decisions.

**What it demonstrates**

* Experiment design
* A/B test planning
* Causal method selection
* Bayesian and frequentist analysis
* Guardrail thinking
* Decision-aware interpretation of results

**Why it matters**

Experimentation maturity is not just sample-size calculation. It is knowing when an experiment is feasible, when causal inference is needed, and when the evidence is not strong enough to ship on.

---

### 4. Public Signals Mislead

**Repo:** [public-signals-mislead](https://github.com/tomasz-solis/public-signals-mislead)

A product strategy case study on why public signals should trigger investigation, not drive decisions directly.

The project studies subscription-product features using external signals such as search interest and public discussion. It shows why public attention, backlash, or trend decay can be useful inputs, but weak standalone proxies for adoption, retention, revenue, or strategic value.

**What it demonstrates**

* Product judgment
* Signal vs outcome separation
* External-data limitations
* Analytical storytelling
* Decision caveats
* Executive-style case framing

**Why it matters**

Product teams are often tempted to overreact to loud public signals. This project shows how to use those signals responsibly: as prompts for deeper investigation, not as product verdicts.

---

### 5. Measurement Maturity Framework

**Repo:** [measurement-maturity-framework](https://github.com/tomasz-solis/measurement-maturity-framework)

A decision-readiness audit for product metrics and measurement systems.

The project evaluates whether a product area has the metric structure, ownership, instrumentation, guardrails, and review rhythm needed to support recurring product decisions.

**What it demonstrates**

* Metric system design
* Product measurement maturity
* Decision-readiness assessment
* Metric risk scoring
* Structured diagnostics
* Reusable product analytics frameworks

**Why it matters**

Good measurement is not about having more dashboards. It is about whether a team can make reliable decisions from the metrics they already use.

---

### 6. Dial In

**Repo:** [dial-in](https://github.com/tomasz-solis/dial-in)

An applied business decision app for small specialty coffee shops.

The project focuses on café prep planning: estimating how much sweet and savoury food to prepare when demand is uncertain, stockouts hide true demand, and waste is costly.

**What it demonstrates**

* Turning data thinking into an operator-facing product
* Demand uncertainty
* Censored-demand reasoning
* Practical decision support
* Lightweight business app design
* Product thinking outside a corporate setting

**Why it matters**

Not every valuable data product needs a huge data platform. Sometimes the value is in helping a small business make one recurring decision better.

---

## How to read this portfolio

For a quick review, start with:

1. **Product Decision Under Uncertainty**
   Best example of decision science and Staff-level product judgment.

2. **Experiment Architect**
   Best example of experimentation and causal product-data thinking.

3. **Trackside Labs**
   Best example of applied ML, system design, and production discipline.

4. **Public Signals Mislead**
   Best example of analytical storytelling and product judgment.

5. **Measurement Maturity Framework**
   Best example of reusable product analytics operating models.

6. **Dial In**
   Best example of practical productization and business-facing data work.

---

## Decision patterns used across the projects

### 1. Make the decision explicit

Before choosing a method, define the decision.

Bad framing:

```text
Can we analyze this?
```

Better framing:

```text
What decision will this analysis inform, and what would change our mind?
```

---

### 2. Separate signals from outcomes

A signal is something observable.
An outcome is what the business actually cares about.

Examples:

```text
Search interest ≠ adoption
Reddit backlash ≠ churn
Dashboard usage ≠ decision quality
Experiment significance ≠ business value
Forecast accuracy ≠ operational usefulness
```

A lot of bad product decisions happen when signals are treated as outcomes.

---

### 3. Make assumptions reviewable

When evidence is incomplete, assumptions are unavoidable.

The goal is not to remove assumptions. The goal is to make them explicit, traceable, and easy to challenge.

```text
hidden assumptions → fragile confidence
visible assumptions → reviewable decision
```

---

### 4. Use uncertainty as an input, not an excuse

Uncertainty should not paralyze decisions. It should shape them.

Useful questions:

```text
What has to be true for this option to be best?
Where is the downside risk?
Which assumptions drive the recommendation?
Which guardrails would make this safe enough to try?
What evidence would change the decision?
```

---

### 5. Connect analysis to a policy

A good analysis does not end with “it depends.”

It should help define a policy:

```text
ship if...
hold if...
test if...
invest if...
rollback if...
escalate if...
```

The policy does not need to be perfect. It needs to be explicit enough to review.

---

## Skills demonstrated

### Product analytics

* Product opportunity framing
* Metric system design
* Adoption, retention, and usage thinking
* Product feedback interpretation
* Decision-readiness assessment
* Executive-style analytical storytelling

### Experimentation and causal inference

* A/B test planning
* Minimum detectable effect
* Bayesian and frequentist interpretation
* Difference-in-differences
* Regression discontinuity
* Guardrail metrics
* Loss-aware decision rules

### Applied ML and forecasting

* Prediction under noisy evidence
* Feature engineering
* Model evaluation
* Calibration
* Uncertainty bands
* Incremental forecast updates
* Production-oriented project structure

### Decision science

* Monte Carlo simulation
* Scenario analysis
* Assumption provenance
* Risk modeling
* Policy frontiers
* Tradeoff analysis
* Decision recommendations under uncertainty

### Product and system design

* Streamlit apps
* Reusable frameworks
* Business-facing tools
* Documentation for different audiences
* Reproducible analysis structure
* Portfolio-ready case studies

---

## What this portfolio is meant to prove

This portfolio is designed to show that I can operate beyond dashboard delivery.

The common thread across the projects is the ability to:

* frame ambiguous product and business problems;
* identify what evidence is actually needed;
* use statistical and ML methods pragmatically;
* explain assumptions and limitations clearly;
* translate analysis into decision-ready recommendations;
* build reusable artifacts that other people could adopt.

In short:

```text
I help product teams make better decisions when the evidence is incomplete.
```

---

## Suggested review paths

### For Product Data Scientist / Business Data Scientist roles

Start with:

1. [Experiment Architect](https://github.com/tomasz-solis/experiment-architect)
2. [Product Decision Under Uncertainty](https://github.com/tomasz-solis/product-decision-under-uncertainty)
3. [Public Signals Mislead](https://github.com/tomasz-solis/public-signals-mislead)

Focus areas:

* experimentation;
* causal inference;
* product judgment;
* decision recommendations;
* business tradeoffs.

---

### For Staff / Principal Product Analyst roles

Start with:

1. [Product Decision Under Uncertainty](https://github.com/tomasz-solis/product-decision-under-uncertainty)
2. [Measurement Maturity Framework](https://github.com/tomasz-solis/measurement-maturity-framework)
3. [Public Signals Mislead](https://github.com/tomasz-solis/public-signals-mislead)

Focus areas:

* ambiguous problem framing;
* reusable analytical systems;
* metric and decision readiness;
* strategic product judgment;
* cross-functional communication.

---

### For Applied ML / Decision Systems roles

Start with:

1. [Trackside Labs](https://github.com/tomasz-solis/trackside-labs)
2. [Product Decision Under Uncertainty](https://github.com/tomasz-solis/product-decision-under-uncertainty)
3. [Dial In](https://github.com/tomasz-solis/dial-in)

Focus areas:

* forecasting;
* uncertainty handling;
* production-style project structure;
* practical decision support;
* model evaluation.

---

## Repository map

```text
product-decision-lab
├── decision-science
│   ├── product-decision-under-uncertainty
│   ├── public-signals-mislead
│   └── measurement-maturity-framework
│
├── experimentation-and-causal-inference
│   ├── experiment-architect
│   ├── causal-guardian
│   ├── rdd-free-shipping
│   ├── ipo-lockup-did-analysis
│   └── product-referee
│
└── applied-ml-and-product-systems
    ├── trackside-labs
    ├── dial-in
    └── decant
```

---

## About me

I am a Senior Product Data Analyst moving toward Product Data Science, Decision Science, and Staff/Principal-level product analytics work.

My background is in product analytics, experimentation, business-facing analysis, and building practical tools that help teams make better decisions.

I am especially interested in problems where:

* the signal is noisy;
* the decision is high-impact;
* the data is incomplete;
* the assumptions matter;
* the best answer is not a dashboard, but a decision system.

---

## Contact

* GitHub: [github.com/tomasz-solis](https://github.com/tomasz-solis)
* LinkedIn: [linkedin.com/in/tomaszsoli](https://www.linkedin.com/in/tomaszsoli)
