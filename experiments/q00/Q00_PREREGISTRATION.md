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

Canonical candidate plan: `experiments/q00/Q00_SAMPLE_AND_ASSIGNMENT_PLAN.md`.

Candidate values to be reviewed and frozen before `PRE_REGISTERED`:

```yaml
target_sample_size: 84 usable primary participants
minimum_usable_sample: 70
primary_peru_minimum: 70
williams_sequences: 14
target_per_sequence: 6
minimum_per_sequence: 5
recruitment_target: 98
randomization_or_counterbalancing: seven-arm first-order carryover-balanced Williams crossover
arm_tasks_per_participant: 7
unassisted_transfer_tasks_per_participant: 1
unit_of_independence: participant
missing_data_policy: pairwise COMPLETE_CASE_PRIMARY for arm contrasts; behavioral non-action remains denominator where observable
withdrawal_policy: preserve withdrawal/exclusion reason; never reclassify for directional convenience
```

The canonical generator is `experiments/q00/generate_assignment.py`.

If fewer than 70 usable primary participants remain, or any Williams sequence has fewer than five usable participants, the primary Q00 result is `INCONCLUSIVE` unless an independently reviewed recovery rule was frozen before outcome inspection.

## 8. Primary outcomes

The generic scoring semantics are frozen as a candidate in `experiments/q00/Q00_SCORING_RUBRIC.md`. Scenario-specific answer keys remain private and are bound by digest before the formal run.

Mandatory primary decision surfaces:

```yaml
P1_full_vs_raw:
  metric: decision_process_score_0_100
  contrast: F - A
  minimum_mean_delta: +8
  90pct_interval_lower_bound: "> +3"

P2_full_vs_friction:
  metric: decision_process_score_0_100
  contrast: F - C
  minimum_mean_delta: +4
  90pct_interval_lower_bound: "> 0"
  simple_friction_capture_limit: "< 80% of F benefit over A"

P3_full_vs_strong_substitute:
  metric: decision_process_score_0_100
  contrast: F - G
  superiority_candidate:
    minimum_mean_delta: +5
    90pct_interval_lower_bound: "> 0"
  comparator_noninferiority_margin: 3 points

memory_ablation:
  contrast: F - E
  full_memory_support_minimum_mean_delta: +4
  90pct_interval_lower_bound: "> 0"

unassisted_transfer:
  metric: transfer_process_score_0_100
  contrast: prior_F_exposure - not_yet_F_exposed
  minimum_mean_delta: +5
  90pct_interval_lower_bound: "> 0"

cognitive_cost_guardrails:
  median_completion_time_ratio_F_over_C: "<= 1.50"
  mean_workload_delta_F_minus_C: "<= 0.75"
  help_requested_rate_delta_F_minus_C: "<= 0.10"
```

Contradiction detection, uncertainty/staleness recognition, process/outcome separation and unnecessary-action avoidance remain rubric dimensions and diagnostic outcomes. They may explain a primary result but cannot rescue a failed mandatory gate.

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

Candidate analysis method, subject only to independent pre-outcome review:

- requested A–G contrasts are computed as participant-level paired differences;
- uncertainty uses 10,000 two-sided 90% percentile bootstrap resamples;
- bootstrap resampling is stratified by Williams sequence;
- participant is the independence unit; repeated tasks are never counted as independent participants;
- transfer analysis compares the predeclared `prior_F_exposure` groups created by the transfer insertion rule;
- exact bootstrap seed is frozen in the final manifest;
- primary missing-data handling follows the candidate sample plan;
- no sequential peeking/stopping;
- subgroup analyses are exploratory unless separately preregistered;
- generic scoring rubric version and private scenario answer-key digest are frozen before first outcome inspection.

The final analysis code/seed/answer-key digest become immutable at `PRE_REGISTERED`.

Exploratory analyses cannot alter the registered terminal decision.

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
