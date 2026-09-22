# Q05 Execution Kit — Competitive Durability

## Status

`READY_FOR_REHEARSAL / BLOCKED_FOR_PROMOTABLE_EXECUTION / NOT_EVIDENCE`

This kit operationalizes `Q05_PREREGISTRATION.md`. It does not assert that SOPHROSYNE has a moat.

The shared candidate artifact at `experiments/research-prototype-v1/` v2.3 emits candidate C01/C02/C04/C05/C07 eligibility, exposure and use events. C01 now distinguishes directional supporting/opposing evidence from non-directional market context. These are **instrumentation readiness**, not adoption/moat evidence. C03/C06/C08 are not represented strongly enough in this throwaway prototype to support promotable component conclusions.

## 1. Entry conditions

```yaml
promotion_geography: Peru
population: adults 18+ matching the promotable Q03 persona
live_trading_required: false
real_money_required: false
comparator_snapshot: mining-site/competitors/2026-09-17-tradingview-comparator-snapshot.md
q03_persona_required: true
q03_repeat_use_data_required_for_e05b: true
```

Q05 must remain scoped to the persona/workflow actually supported by Q03.

## 2. E05-A comparative task run

Use TradingView as the initial frozen representative comparator candidate unless a stronger/more relevant comparator is frozen before participant recruitment.

Before execution freeze:
- exact TradingView plan/tier;
- login state;
- enabled features;
- screenshots/version notes;
- exact SOPHROSYNE prototype version;
- matched task set;
- equal onboarding allocation;
- counterbalancing schedule;
- scoring rubric and preference coding rubric.

Participant sequence:
1. eligibility and adult-age confirmation;
2. neutral onboarding for both workflows;
3. matched task in workflow A;
4. matched task in workflow B;
5. objective comprehension questions;
6. confidence score;
7. blind/neutral workflow preference;
8. open-ended reason: “What specifically made you prefer that workflow for this recurring task?”;
9. only after free-text capture, optional structured follow-up.

Do not tell participants which features are candidate moat components before their open-ended reason is captured.

## 3. Preference reason coding rubric

Two reviewers independently map behavioral/free-text evidence to C01-C08 when possible.

```text
C01 supporting/opposing evidence structure
C02 immutable Decision Ledger
C03 point-in-time provenance/replay
C04 uncertainty/invalidation semantics
C05 progressive explanation depth
C06 reproducible strategy validation
C07 longitudinal personal decision history
C08 rights-aware derived intelligence
OTHER_WORKFLOW_REASON
BRAND_OR_VISUAL_ONLY
NO_CLEAR_REASON
```

A C01-C08 attribution requires a concrete reference to the workflow effect; generic “cleaner”, “better”, “AI”, “looks professional” or brand preference is insufficient.

Disagreements between reviewers are preserved and adjudicated under a frozen rule. Do not post-hoc remap vague praise into a candidate component.

## 4. E05-A event/data schema

```text
participant_id
peru_primary_cohort
q03_persona_match
workflow_order
scenario_pair
sophrosyne_comprehension
comparator_comprehension
sophrosyne_confidence
comparator_confidence
sophrosyne_calibration_gap
comparator_calibration_gap
preferred_workflow
free_text_reason_ref
coded_component_primary
coded_component_secondary
brand_or_visual_only
technical_failure
exclusion_reason
```

All tasks are paper/historical/synthetic. No investment action is requested.

## 5. E05-B repeat-use linkage contract

Primary source is the valid E03-C 14-day experiment.

Canonical component semantics are frozen as a candidate in `experiments/q05/Q05_COMPONENT_EXPOSURE_CONTRACT.md`.

For every C01-C08 component define before analysis:

```yaml
component_id:
eligibility_rule:
exposure_event:
use_event:
return_reason_capture:
minimum_valid_exposure:
```

Recommended event mappings:

| Component | Exposure event | Use/adoption evidence |
|---|---|---|
| C01 | evidence view available/opened | supporting/opposing evidence expanded in >=2 sessions |
| C02 | decision record created | prior decision record revisited |
| C03 | provenance/replay control exposed | provenance or replay opened after initial session |
| C04 | uncertainty/invalidation exposed | uncertainty or invalidation opened in >=2 sessions |
| C05 | deeper disclosure level available | user voluntarily changes depth across sessions |
| C06 | validation surface eligible | historical/paper validation revisited |
| C07 | >=2 prior records exist | longitudinal history used after day 7 |
| C08 | rights-aware source/derived marker exposed | source/derived context inspected when available |

Denominator = eligible exposed repeat users, never all users unless universal exposure is proven.

Required fields:

```text
participant_id
component_id
eligible
exposed
sessions_used
used_after_day_7
independently_cited_as_return_reason
source_event_refs
```

## 6. E05-C defensibility worksheet

For each component, reviewers must complete:

```yaml
component_id:
surface_copyability: HOURS_DAYS | WEEKS | MONTHS_PLUS | UNKNOWN
surface_ui_only: YES | NO
workflow_integration: YES | NO
accumulated_user_history: YES | NO
accumulated_evidence_or_validation_corpus: YES | NO
point_in_time_provenance_history: YES | NO
provider_or_rights_constraint: YES | NO
distribution_or_community_asset: YES | NO
switching_cost_from_longitudinal_state: YES | NO
requires_generic_llm_only: YES | NO
requires_nontrivial_operational_history: YES | NO
observed_repeat_use_linkage: NONE | MODERATE | STRONG | INCONCLUSIVE
competitor_counterexample:
residual_copy_risk:
evidence_refs: []
```

Code complexity is not defensibility evidence. `RIGHTS_OR_DISTRIBUTION_CONSTRAINED` requires actual Q02 evidence; it cannot be inferred from desired licensing difficulty.

## 7. Fair-comparison guardrails

- equal task instructions and onboarding time;
- no deliberately crippled comparator;
- preserve comparator feature/state snapshot;
- no “AI”, “safer”, “smarter” or superiority labels before response;
- randomize/counterbalance order;
- preserve negative reasons and comparator wins;
- no post-hoc change to preference thresholds;
- no moat conclusion from one-session praise alone.

## 8. Required immutable outputs

E05-A:
- comparator snapshot/digest;
- prototype digest;
- participant/recruitment log;
- raw/de-identified measurements where permitted;
- preference reason coding artifact;
- comprehension/calibration analysis;
- independent review.

E05-B:
- linked E03-C receipt;
- exposure-definition version;
- component-level numerators/denominators;
- day-7 longitudinal use;
- return-reason evidence.

E05-C:
- per-component defensibility worksheet;
- competitor counterexamples;
- Q01/Q02 dependency check;
- residual copy-risk statement.

## 9. Current execution blockers

```yaml
q03_promotable_persona: NOT_FROZEN
adult_peru_participants: NOT_RECRUITED
prototype_semantic_version: research-prototype-v2.3.0
instrumented_components: [C01, C02, C04, C05, C07]
non_promotable_or_missing_component_surfaces: [C03, C06, C08]
e03c_14_day_repeat_use_receipt: MISSING
valid_component_exposure_denominators: MISSING
exact_comparator_execution_state: NOT_FROZEN
q01_dependency: OPEN
q02_dependency: OPEN
independent_reviewer: MISSING
moat_status: NOT_EVALUATED
q05_status: OPEN
```

Q05 may not be closed from competitor screenshots, internal enthusiasm, code complexity or assistant-generated users. A `LEARNING_WEDGE` conclusion still requires real comparative/repeat-use evidence under the canonical rules.