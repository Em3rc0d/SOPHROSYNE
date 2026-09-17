# Q00 — Core Causal Value Falsification Gate

## Purpose

Q00 exists to answer one question before SOPHROSYNE is allowed to interpret user enthusiasm, pricing intent, memory effects or moat narratives as product validation:

> **Does SOPHROSYNE create material incremental decision-process value over simpler and cheaper substitutes?**

Q00 is an umbrella causal gate. It does not replace Q01–Q05; it constrains how Q03/Q04/Q05 evidence may be interpreted.

---

## Primary null hypothesis

> A simple low-cost baseline can reproduce enough of SOPHROSYNE's measured benefit that the additional product complexity is not justified.

The project must try to fail to reject this null.

---

# Required baseline arms

At minimum, the preregistered trial compares:

### A — Raw-information control
Relevant information with no structured intervention.

### B — Stateless structured assistant
Same data and task support, but no longitudinal memory.

### C — Dumb friction baseline
A minimal checklist:
1. What do you expect?
2. What probability/confidence do you assign?
3. What evidence opposes your view?
4. What would invalidate it?
5. When/how will the outcome be evaluated?

### D — Simple feedback
Prediction + confidence + later outcome/process feedback, without full decision memory.

### E — Short-memory SOPHROSYNE
Recent rolling context only.

### F — Full candidate SOPHROSYNE
The currently proposed evidence/decision-feedback system.

Where available and legally/research-operationally appropriate, a realistic free/cheap external substitute may be added as a comparator, but Q00 must not depend on access to a specific broker account.

---

# Primary outcomes

Q00 must preregister a small set of primary outcomes. Candidate outcomes:
- calibration error;
- discrimination between stronger/weaker scenarios;
- contradiction detection;
- uncertainty recognition;
- process/outcome separation;
- unnecessary-action rate;
- transfer to novel hidden-outcome scenarios.

No primary outcome may be selected after seeing results.

Financial profit is not a required primary endpoint for Q00 because market noise can swamp decision-process effects over small samples.

---

# Destructive tests

## T00-1 — Simple-friction ablation

Question: does the five-question checklist capture most of the benefit?

Default kill threshold for complex intervention advantage:

```text
(effect_F - effect_control) <= 1.25 * (effect_C - effect_control)
```

or equivalently the simple-friction arm captures >= 80% of the pre-specified benefit of the full arm, subject to the preregistered outcome direction and uncertainty rule.

If true across the primary outcome bundle, full-complexity causal advantage is not established.

## T00-2 — Memory ablation

Compare stateless, simple feedback, short memory and full memory.

Possible conclusions:
- `MEMORY_EXCLUDED` — no material advantage over stateless/simple feedback;
- `SHORT_MEMORY_SUFFICIENT` — long-history accumulation adds no material value;
- `FULL_MEMORY_SUPPORTED` — long-history arm clears the minimum meaningful effect;
- `INCONCLUSIVE`.

Persistent memory is never assumed to be a moat.

## T00-3 — Outcome-blind process test

Hold ex-ante information/process constant while varying revealed outcomes.

If process-quality ratings materially track lucky/unlucky outcomes, the intervention has not adequately separated process from outcome bias.

## T00-4 — Hidden-rubric test

Users are not told the exact scoring rubric.

If measured improvement disappears when users cannot optimize directly for the rubric, the claimed learning effect is not established.

## T00-5 — Transfer test

Use novel scenarios/tasks not structurally identical to training interactions.

Separate:
- assisted performance;
- immediate unassisted transfer;
- delayed unassisted transfer where feasible.

If only assisted performance improves, the product may still be a cognitive prosthetic, but claims of improving the user's independent reasoning are rejected.

## T00-6 — Regime/context transfer

Where the evidence domain permits, vary market regime, asset/horizon or evidence composition.

A benefit that appears only in one narrow context must be scoped to that context rather than generalized.

## T00-7 — Effective-sample correction

Correlated decisions/scenarios must not be treated as independent observations.

Participant-level and scenario-cluster dependence must be handled under `STATISTICAL_DECISION_RULES.md`.

## T00-8 — Cognitive-cost test

Measure time-to-decision, task completion, burden/abandonment and comprehension.

A small decision-quality gain may be rejected if it requires disproportionate cognitive cost relative to the target use case.

## T00-9 — Zero-price/cheap-substitute test

Compare the full candidate experience against the strongest realistic cheap/free substitute available for the same task.

SOPHROSYNE must demonstrate material incremental value, not merely parity with an already-owned tool.

## T00-10 — Economic bridge

Q00 does not prove willingness-to-pay, but Q03 pricing evidence may not be interpreted as strong product support if Q00 shows no meaningful incremental causal/product effect.

---

# Anti-gaming rules

- no universal public “decision intelligence score” is required or assumed;
- do not optimize users toward a single composite score;
- expose specific feedback rather than a gamified rank where possible;
- rubric versions are frozen before outcome inspection;
- process-quality labels distinguish observable behavior from inferred cognition;
- self-reported reasoning is `ATTRIBUTED`, not ground-truth causality;
- `NO CONCLUSION` cannot become the dominant strategy merely because it avoids penalties; discrimination/utility outcomes must detect trivial conservatism.

---

# Minimum economically meaningful effect

Statistical significance alone is insufficient.

Before data collection, each primary outcome must define:
- direction of improvement;
- minimum practically meaningful effect;
- acceptable uncertainty interval;
- sample/exclusion policy;
- multiplicity handling where applicable.

A tiny but statistically detectable advantage does not justify a large architectural, privacy, licensing or UX burden.

---

# Decision vocabulary

Q00 uses the project-wide terminal vocabulary:
- `CLOSED_PASS`;
- `CLOSED_CONDITIONAL`;
- `PIVOT_REQUIRED`;
- `STOP_CURRENT_CONFIGURATION`;
- `INCONCLUSIVE`.

Possible scoped component outcomes such as `MEMORY_EXCLUDED` or `SHORT_MEMORY_SUFFICIENT` are subordinate findings and do not replace the terminal Q00 decision.

---

# Promotion rules

### Q00 CLOSED_PASS
The full candidate or a narrower evidence-derived configuration demonstrates material incremental decision-process value versus required baselines, without unacceptable cognitive cost or obvious rubric gaming.

### Q00 CLOSED_CONDITIONAL
A narrower intervention works, but one or more assumed components (for example persistent memory, ML, multi-source complexity) must be excluded/deferred.

### Q00 PIVOT_REQUIRED
The problem exists, but the current mechanism/product thesis is not the correct intervention.

### Q00 STOP_CURRENT_CONFIGURATION
Simple/cheap substitutes capture the meaningful effect, or the intervention creates no material decision-process benefit after robust controls.

### Q00 INCONCLUSIVE
Evidence quality/sample/dependence does not support a decision.

---

# Relationship to Q01–Q05

```text
Q00 causal value
    ↓ constrains interpretation of
Q03 user value / WTP
Q04 optional quantitative components
Q05 defensibility

Q01 legal/compliance and Q02 data rights remain independently fatal where applicable.
```

A Q03 pricing signal cannot rescue failed Q00 causal value.
A Q05 moat narrative cannot rescue failed Q00 causal value.
A sophisticated Q04 model cannot rescue failed Q00 causal value.

---

## Final invariant

> SOPHROSYNE must beat a deliberately competent simple baseline before complexity is allowed to count as product value.
