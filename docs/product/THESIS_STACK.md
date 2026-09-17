# SOPHROSYNE Thesis Stack

## Purpose

SOPHROSYNE must not depend on one heroic claim such as “AI predicts markets”, “persistent memory is a moat”, or “retail investors will pay for better explanations”. Those claims can fail independently.

This document separates the project into layers with explicit falsification boundaries so that one failed hypothesis kills only the claim it actually contradicts.

The goal is not an unfalsifiable thesis. The goal is a thesis architecture that is **hard to fool, easy to narrow, and impossible to rescue by rhetoric after evidence turns negative**.

---

# T0 — Methodological invariant

> **Evidence must have more authority than conviction, implementation sunk cost, model sophistication, engagement or narrative quality.**

This is not an empirical market claim. It is the governing method of the project.

Consequences:
- a negative result may remove a feature, model, market, persona, pricing tier or business model;
- no failed empirical claim is rescued because implementation already exists;
- `INCONCLUSIVE`, `PIVOT_REQUIRED` and `STOP_CURRENT_CONFIGURATION` are valid outcomes;
- simpler baselines may defeat more sophisticated systems;
- evidence that contradicts the product is a successful MK0 output.

T0 changes only through an explicit governance/ADR reversal.

---

# T1 — Problem thesis

> **Some self-directed investors make worse decisions than necessary because market information is fragmented, uncertainty is poorly represented, and outcomes are often confused with decision-process quality.**

T1 does **not** claim:
- that all retail investors need SOPHROSYNE;
- that users need more information;
- that AI is required;
- that trading more frequently is desirable;
- that better process guarantees higher returns.

### T1 dies if

Target users show no meaningful decision-process problem under controlled tasks, or a trivial existing workflow already eliminates it with negligible cost/friction.

---

# T2 — Causal intervention thesis

> **A point-in-time intervention that records expectations, confidence, evidence, opposing evidence, invalidators and later process/outcome feedback can improve at least one preregistered dimension of probabilistic decision quality versus an equivalent low-cost baseline.**

Candidate dimensions include:
- calibration;
- discrimination;
- contradiction detection;
- recognition of uncertainty;
- separation of process quality from outcome luck;
- avoidance of unjustified action;
- transfer to novel scenarios.

T2 deliberately does not require persistent long-term memory, ML, LLMs, multimodal data or backtesting.

### T2 dies if

A simple friction/checklist or stateless baseline captures the pre-registered economically meaningful effect, or if observed gains disappear under hidden-rubric, transfer, outcome-blind or dependency-adjusted analysis.

---

# T3 — Product thesis

> **The validated intervention can be packaged into a product experience that users prefer to the best realistic substitute because it reduces time-to-sound-reasoning without hiding uncertainty or materially increasing cognitive burden.**

The product category remains **Financial Decision Intelligence**.

T3 may use:
- Market Translator;
- Evidence View;
- Decision Records;
- Strategy Sandbox;
- portfolio context;
- progressive disclosure;
- point-in-time feedback.

None of these is assumed to be the reason the product works.

### T3 dies if

The causal benefit exists in the lab but users do not repeatedly use the product, the cognitive/interaction cost cancels the benefit, or a free/cheap substitute provides effectively equivalent value.

---

# T4 — Economic thesis

> **A promotable configuration exists where willingness-to-pay and retention support the full cost of legal/compliance, licensed data, infrastructure, support, security and acquisition at acceptable margins.**

T4 is independent from T2/T3: a useful product can still be a bad business.

### T4 dies if

The price users will actually commit to cannot structurally cover mandatory cost and acquisition economics, after excluding vanity intent and subsidized behavior.

Possible outcome: B2C dies while a separately validated B2B configuration remains testable. B2B is not an automatic rescue.

---

# T5 — Defensibility thesis

> **If SOPHROSYNE becomes defensible, defensibility will emerge from a validated compound system and accumulated evidence/learning assets, not from any single commodity feature.**

Potential compound assets may include:
- point-in-time evidence/provenance corpus;
- process-vs-outcome labels;
- calibration/error taxonomy;
- validated intervention policy;
- longitudinal decision-quality evidence;
- domain/regulatory/data-rights execution discipline;
- trust history that competitors cannot recreate instantly.

Explicitly **not moat by itself**:
- translation;
- Spanish language;
- LLM chat;
- persistent memory;
- multi-source ingestion;
- backtesting;
- natural-language strategy building;
- Decision Records;
- progressive disclosure.

### T5 dies if

The valued experience is cheaply reproducible by a broker, frontier-model wrapper or simple workflow before accumulation creates measurable switching/learning advantage, or if accumulated data creates more legal/privacy/licensing liability than defensibility.

---

# Non-transitive proof rule

Passing one layer does not prove the next:

```text
T1 problem exists
    != T2 intervention works
    != T3 product is preferred
    != T4 business is viable
    != T5 business is defensible
```

Likewise, failure is scoped:

```text
ML failure           -> does not kill T2
memory failure       -> does not kill T2
B2C economics failure-> kills T4 B2C, not automatically T2
moat failure         -> kills T5, not automatically product utility
causal-value failure -> kills current SOPHROSYNE core configuration
```

---

# Minimum viable claim

The smallest empirical claim SOPHROSYNE is allowed to defend before stronger evidence exists is:

> **Structured point-in-time feedback may help some users evaluate decisions under uncertainty more rigorously than an equivalent baseline.**

Anything stronger requires receipts.

---

# Core kill rule

The current independent-product thesis must be stopped or materially reformulated if all are true:

1. the simple-friction baseline captures >= 80% of the measured causal benefit;
2. the best free/cheap substitute is non-inferior on the primary product outcomes;
3. no meaningful transfer effect exists outside the assisted workflow;
4. WTP cannot cover the promotable cost structure; and
5. no compound asset shows evidence of durable accumulation advantage.

No amount of implementation quality overrides this rule.

---

# What “solid” means

A solid SOPHROSYNE thesis is not one that cannot lose.

It is one where:
- every important claim names its evidence burden;
- every test has a baseline capable of defeating it;
- negative results narrow the system instead of being reinterpreted as success;
- no commodity capability is mislabeled as a moat;
- product utility, business viability and defensibility are never conflated;
- the project can stop cleanly when the evidence says it should.

> **SOPHROSYNE earns complexity one validated layer at a time.**
