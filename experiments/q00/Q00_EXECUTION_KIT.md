# Q00 Execution Kit — Core Causal Value

## Status

`READY_FOR_INDEPENDENT_REVIEW / NOT_EVIDENCE / NOT_PRE_REGISTERED`

This kit operationalizes `Q00_PREREGISTRATION.md`. It does not change Q00's terminal state and does not authorize live trading, personalized recommendations or production implementation.

## 1. Participant boundary

```yaml
population: adults 18+
promotion_geography: Peru
financial_behavior: self-directed investment research
live_trading_required: false
real_money_required: false
personalized_recommendations: prohibited
```

Recruitment must verify age before enrollment. Any participant outside the Peru promotion cohort is exploratory unless separately preregistered.

## 2. Proposed execution design

Primary design: randomized, counterbalanced paper-analysis study using matched synthetic/historical-style scenarios. Each scenario hides future outcome information during the decision-context task.

Required arms remain:
- A raw-information control;
- B stateless structured assistant;
- C five-question friction checklist;
- D simple feedback;
- E short-memory SOPHROSYNE;
- F full candidate SOPHROSYNE;
- G conventional-workflow comparator using the frozen approved comparator snapshot.

Candidate interactive rehearsal material now exists at `experiments/research-prototype-v1/` and exposes A–G with a lockable assignment mode. This closes the **instrumentation shell**, not the empirical gate. G is intentionally non-promotable until the external comparator snapshot/version is frozen before preregistration.

Candidate allocation/minimum/counterbalancing semantics are now instantiated in `Q00_SAMPLE_AND_ASSIGNMENT_PLAN.md` and `generate_assignment.py`. They remain subject to independent-review approval before status may become `PRE_REGISTERED`.

## 3. Scenario corpus contract

Internal market-domain QA before independent R2:
- `docs/quant/MARKET_DOMAIN_FOUNDATION.md`;
- `experiments/q00/Q00_MARKET_SCENARIO_REVIEW_CHECKLIST.md`;
- `mining-site/market/2026-09-21-course-synthesis.md`.

The project owner is not treated as a market-domain authority. User feedback remains UX/comprehension evidence; market correctness is checked against the domain baseline and then independently reviewed.

Every scenario must include the same underlying fact set across arms and contain at minimum:
- 3 supporting observations;
- 2 contradicting observations;
- 1 stale/uncertain item;
- 1 explicit missing-data item;
- 1 scenario invalidator;
- 1 item that is correlated but not evidence of causality;
- a hidden outcome revealed only after the process task.

Current rehearsal corpus contains eight scenario instances across the required families. Seven are assigned to A–G via the Williams schedule; SYN-05 is reserved for the unassisted transfer task.

These are rehearsal materials only until independent market-domain review and final corpus hashing.

All tasks are paper/historical/synthetic. No participant is asked to buy, sell or hold a real asset.

## 4. Five-question friction baseline

Arm C uses only:
1. What is directly observed?
2. What evidence contradicts the leading explanation?
3. What is uncertain, missing or stale?
4. What would invalidate the current scenario?
5. What action is unnecessary until more evidence exists?

This baseline must remain deliberately simple. It cannot secretly receive SOPHROSYNE-only structure.

## 5. Primary scoring rubric

Each response is scored blind to arm where practical.

```yaml
observed_vs_inferred_separation: 0-4
supporting_evidence_identification: 0-4
contradicting_evidence_identification: 0-4
uncertainty_staleness_recognition: 0-4
invalidation_quality: 0-4
process_outcome_separation: 0-4
unnecessary_action_avoidance: 0-4
transfer_quality: 0-4
```

`decision_process_score = sum(D1..D7) / 28 * 100` for normal A–G tasks; transfer uses all eight dimensions: `sum(D1..D8) / 32 * 100`. Canonical anchors live in `Q00_SCORING_RUBRIC.md`.

Confidence is collected separately from correctness/process score for calibration analysis.

## 6. Time/cognitive-cost capture

For every task record:
- task start/end timestamp;
- completion seconds;
- abandoned task flag;
- optional short workload rating;
- help requested;
- arm exposure version.

A quality improvement cannot be called causal-value PASS if the preregistered cognitive/time boundary fails.

## 7. Transfer test

At least one final scenario must:
- use a different regime/context from training/onboarding examples;
- remove in-product assistance before final answer;
- keep rubric hidden;
- measure whether the participant independently carries over contradiction, uncertainty and invalidation reasoning.

If assisted improvement does not transfer, claims remain `ASSISTED_ONLY`.

## 8. Data schema

```text
participant_id
cohort
country
eligibility_pass
scenario_id
arm_id
order_index
started_at
completed_at
process_score
confidence_pct
correctness_pct
calibration_gap
contradiction_detected
stale_or_missing_detected
invalidator_quality
unnecessary_action_avoided
unassisted_transfer
workload_rating
technical_failure
exclusion_reason
```

No real account identifiers, brokerage credentials or live orders are collected.

## 9. Freeze-before-run checklist

Q00 cannot move to `PRE_REGISTERED` until all are frozen:
- independent reviewer;
- exact sample/minimum plan;
- recruitment channels;
- scenario corpus and hashes;
- arm materials and hashes;
- scoring rubric version;
- counterbalancing/randomization plan;
- missing-data/exclusion policy;
- uncertainty interval method;
- multiplicity rule;
- cognitive-cost boundary;
- strongest cheap/free comparator tier/state;
- consent/privacy retention profile.

## 10. Current execution blockers

```yaml
independent_reviewer: MISSING
adult_peru_participants: NOT_RECRUITED
candidate_rehearsal_artifact: experiments/research-prototype-v1/index.html
candidate_branch: research/mk0-handoff-hardening
candidate_index_git_blob: c8d49efb30569f7b3ae3e1b0426e57032f489ff3
seven_arm_instrumentation: READY_FOR_REHEARSAL
eight_scenario_rehearsal_corpus: READY_FOR_REVIEW
external_comparator_g_candidate_sheet: experiments/q00/Q00_G_COMPARATOR_FREEZE_SHEET.md
external_comparator_g_execution_state: NOT_FROZEN
sample_assignment_plan: READY_FOR_REVIEW
scoring_rubric: READY_FOR_REVIEW
reviewer_handoff: READY_TO_SEND
recruitment_moderator_packet: DRAFT_REQUIRES_Q01
scenario_materials_final_digest: MISSING
consent_privacy_clearance: REQUIRES_Q01_REVIEW
status: OPEN
```

No downstream Q03/Q04/Q05 result may compensate for a failed Q00 configuration.