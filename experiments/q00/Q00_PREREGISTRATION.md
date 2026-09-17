# Q00 Pre-Registration — Core Causal Value Against Simple Baselines

## Status

`DRAFT`

This document is not evidence and does not close Q00. It freezes the experiment design that may become `PRE_REGISTERED` only after materials, reviewer, sample plan and execution version are finalized before outcome inspection.

Canonical authorities:
- `docs/validation/Q00_CORE_CAUSAL_VALUE.md`;
- `docs/product/THESIS_STACK.md`;
- `adr/ADR-0014-THESIS-STACK-AND-Q00.md`;
- `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`;
- `contracts/validation_graph.yaml`.

---

## 1. Identity

```yaml
experiment_id: Q00-CORE-CAUSAL-V1
version: 1
status: DRAFT
lock_ids: [Q00]
owner: Em3rc0d
independent_reviewer: TBD
created_at: 2026-09-17
pre_registered_at: null
supersedes: null
```

## 2. Question

Does the full candidate SOPHROSYNE intervention create material incremental decision-process value over simpler and cheaper substitutes under controlled, non-production tasks?

## 3. Hypothesis and failure hypothesis

**Primary hypothesis:** the full candidate configuration improves preregistered decision-process outcomes by materially more than competent simple baselines, without imposing disproportionate cognitive/time cost.

**Failure hypothesis:** most measured benefit is captured by simple friction, stateless structure, simple feedback or short memory; any remaining gain is too small, too unstable, too costly or too dependent on assisted use to justify full product complexity.

Positive Q03 willingness-to-pay, Q04 modeling sophistication or Q05 defensibility evidence cannot rescue a failed Q00 result.

## 4. Scope

```yaml
population: adults 18+ who independently research/manage their own investments
promotion_geography: Peru
interaction_version: frozen Q00 study prototype/material set
tasks: historical, synthetic or paper-analysis only
real_money_trading_required: false
personalized_live_recommendations_required: false
```

The study evaluates decision-process quality, not whether participants earn money in live markets.

## 5. Required comparison arms

Every promotable run must include, or explicitly justify the inapplicability of, these arms:

- **A — Raw-information control:** relevant source material without SOPHROSYNE structuring.
- **B — Stateless structured assistant:** structured explanation without longitudinal memory.
- **C — Five-question friction checklist:** minimal deliberate-friction intervention.
- **D — Simple feedback:** prediction/confidence/outcome feedback without the full system.
- **E — Short-memory SOPHROSYNE:** only bounded recent decision context.
- **F — Full candidate SOPHROSYNE:** complete candidate intervention being tested.
- **G — Strongest realistic cheap/free substitute:** required when a credible operational comparator can be frozen before execution.

Arm labels and materials become immutable at `PRE_REGISTERED`.

## 6. Destructive tests

The run must support the following analyses:

- `T00-1` simple-friction ablation;
- `T00-2` memory ablation;
- `T00-3` outcome-blind process evaluation;
- `T00-4` hidden-rubric evaluation;
- `T00-5` assisted vs unassisted transfer;
- `T00-6` regime/context transfer;
- `T00-7` effective-sample/dependence correction;
- `T00-8` cognitive/time-cost comparison;
- `T00-9` zero-price/cheap-substitute comparison;
- `T00-10` economic bridge to Q03.

## 7. Sample and assignment plan

Before `PRE_REGISTERED`, freeze:

```yaml
target_sample_size: TBD
minimum_usable_sample: TBD
primary_peru_minimum: TBD
recruitment_channels: TBD
randomization_or_counterbalancing: TBD
repeated_task_structure: TBD
missing_data_policy: TBD
withdrawal_policy: TBD
```

If the minimum usable sample is not reached, the result is `INCONCLUSIVE`; favorable descriptive results cannot override that state.

## 8. Primary outcomes

Before outcome inspection, freeze a small primary set selected from the following candidate families:

- calibration quality;
- scenario discrimination;
- contradiction/opposing-evidence detection;
- uncertainty recognition;
- process-vs-outcome separation;
- unnecessary-action avoidance in paper scenarios;
- transfer to novel hidden-outcome tasks;
- cognitive/time cost.

For each selected primary measure the final manifest must define:

```yaml
name:
definition:
unit:
direction_of_better:
aggregation:
minimum_practically_meaningful_effect:
uncertainty_interval_rule:
```

Secondary measures may explain a result but cannot rescue a failed primary decision rule.

## 9. Frozen decision rules

### Simple-friction destruction rule

If arm C captures at least **80% of the preregistered benefit** attributable to arm F on the mandatory primary decision rule, full-complexity causal advantage is not established for the tested scope.

Equivalent formulation when improvement ratios are used: if the full candidate produces no more than `1.25x` the improvement of the friction baseline on the registered aggregate decision rule, complexity is not earned unless another mandatory primary outcome independently satisfies a preregistered materiality threshold.

### Memory rule

- no material E→F increment: `MEMORY_EXCLUDED` or `SHORT_MEMORY_SUFFICIENT`;
- material, stable E→F increment: memory may be `FULL_MEMORY_SUPPORTED` for the tested scope;
- ambiguous result: memory remains unearned and Q00 cannot use it as required complexity.

### Transfer rule

If assisted performance improves but preregistered unassisted transfer does not, product claims must remain `ASSISTED_ONLY`; the study cannot claim independent reasoning improvement.

### Cheap-substitute rule

If the strongest competent cheap/free substitute is non-inferior on the mandatory primary outcomes within the preregistered margin, the current independent full-product configuration is not promotable without material narrowing/pivot.

### Cognitive-cost rule

A small quality gain can fail when additional time, effort or comprehension burden exceeds the preregistered acceptable cost boundary.

No threshold or primary outcome may be moved after outcome inspection to protect the product thesis.

## 10. Analysis plan

Before `PRE_REGISTERED`, freeze:
- comparison method for repeated/counterbalanced observations;
- uncertainty interval method;
- participant/task dependence treatment;
- multiplicity rule;
- missing-data handling;
- pre-specified sensitivity analyses;
- subgroup policy;
- hidden-rubric scoring version.

Exploratory analyses must be labeled exploratory and cannot alter the registered terminal decision.

## 11. Provenance and anti-gaming

Expected immutable artifacts:
- frozen task/scenario corpus;
- arm materials and semantic version/digests;
- scoring rubric and answer keys kept hidden from participants;
- recruitment/inclusion/exclusion record;
- raw or de-identified observations where permitted;
- analysis artifact and environment/version record;
- adverse/conflicting evidence;
- independent-review note;
- final `EvidenceReceipt`.

Failed variants remain in history. Implementation effort, product enthusiasm, pricing intent or downstream engineering success are not evidence for Q00.

## 12. Safety / research boundary

- no participant is instructed to place a live trade;
- no real-money execution is required;
- no leverage/derivatives/live autonomous execution is part of the study;
- scenarios are historical, synthetic or paper-analysis contexts;
- participant-facing material must not present research outputs as personalized financial advice;
- participant compensation cannot depend on desired product sentiment or a trading outcome.

## 13. Abort conditions

Abort/preserve the run rather than silently repair it when:
- task materials differ materially between intended arms;
- answer keys/rubrics leak before task completion;
- instrumentation cannot compute a mandatory primary outcome;
- cohort eligibility materially deviates from the preregistered population;
- rights/consent constraints invalidate planned evidence retention;
- experiment code/material changes after outcome inspection without a superseding version.

## 14. Terminal decisions

Q00 may end only as:
- `CLOSED_PASS`;
- `CLOSED_CONDITIONAL`;
- `PIVOT_REQUIRED`;
- `STOP_CURRENT_CONFIGURATION`;
- `INCONCLUSIVE`.

Component outcomes such as `MEMORY_EXCLUDED` do not replace the terminal Q00 decision.

## 15. Closure receipt

A promotable Q00 receipt must contain:
- preregistration ref/digest;
- exact executed scope and deviations;
- sample/dependence record;
- primary and secondary results;
- baseline/ablation results;
- uncertainty and sensitivity analysis;
- cognitive-cost result;
- transfer result;
- adverse/conflicting evidence;
- terminal decision and limitations;
- component inclusion/exclusion decisions;
- explicit implications for Q03/Q04/Q05;
- explicit implications for `MK1_BOOTSTRAP_PROFILE`;
- independent reviewer signoff.

Q00 remains `OPEN` until such evidence exists and passes review.
