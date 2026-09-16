# Evidence Receipt Template

## Purpose

A receipt records what was actually observed, reviewed or contractually confirmed. It never turns missing evidence into a favorable inference. Finalized receipts are immutable; corrections create a superseding receipt.

## Identity

```yaml
receipt_id:
lock_id: Q01 | Q02 | Q03 | Q04 | Q05
lock_version:
receipt_version:
receipt_state: DRAFT | REVIEW_READY | FINAL | SUPERSEDED
final_decision: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE | null
experiment_or_review_id:
created_at:
started_at:
completed_at:
finalized_at:
owner:
independent_reviewer:
supersedes:
superseded_by:
```

Rules:
- `final_decision` is null until `receipt_state: FINAL`;
- `SUPERSEDED` preserves the historical decision and points to its successor;
- only `CLOSED_PASS` or `CLOSED_CONDITIONAL` can contribute promotable frozen outputs.

## Scoped question

```yaml
question:
scope:
  product_or_interaction_version:
  population_or_market:
  primary_promotion_geography:
  study_language:
  provider_or_dataset:
  asset_universe:
  time_window:
  other_constraints:
```

## Preregistration / authority

```yaml
pre_registration_or_review_ref:
pre_registration_or_review_digest:
decision_rule_version:
statistical_contract_ref:
statistical_contract_version:
authority_or_source:
authority_class: OFFICIAL | ACADEMIC | OBSERVED | INFERRED | HYPOTHESIS
source_effective_date:
source_version_or_contract_ref:
```

Q01/Q02 require the external authority defined by the canonical protocol. Q03/Q04/Q05 promotion experiments require preregistration before outcome inspection.

## Sample / dataset / reviewed material

```yaml
sample_or_dataset:
  planned:
  actual:
  inclusion_criteria:
  exclusion_criteria:
  missing_or_removed_observations:
  deviations_from_plan:
  unit_of_analysis:
  denominator_or_exposure_rule:
reviewed_artifacts:
  - ref:
    digest:
    description:
```

## Frozen decision rule

```yaml
primary_measures:
secondary_measures:
pass_rule:
conditional_pass_rule:
pivot_rule:
stop_rule:
inconclusive_rule:
decision_precedence:
```

Regions must cover every valid outcome. Unclassified outcomes are `INCONCLUSIVE`.

## Evidence artifacts

```yaml
raw_artifact_refs:
  - ref:
    digest:
    provenance:
    retention_or_rights_constraint:
analysis_artifact_refs:
  - ref:
    digest:
artifact_digest_manifest_ref:
analysis_code_commit:
environment_lock_digest:
```

## Results / adverse evidence / limitations

```yaml
primary_results:
secondary_results:
sensitivity_or_subgroup_results:
protocol_deviations:
adverse_or_conflicting_evidence:
  - description:
    source_ref:
    severity:
    effect_on_decision:
limitations:
  - limitation:
    likely_direction_of_bias:
    materiality:
```

Do not round or aggregate in a way that hides threshold failure. `none_observed` is valid only when genuinely none was found.

## Frozen outputs

```yaml
frozen_outputs:
  - key:
    value_or_ref:
    source_of_authority:
conditions_if_any:
  - condition:
    canonical_destination:
    bootstrap_field:
    acceptance_or_regression_check:
```

Frozen outputs are the only values the receipt may contribute to a bootstrap candidate.

## Canonical propagation

```yaml
canonical_docs_updated:
  - path:
    commit_or_digest:
reopened_locks:
  - lock_id:
    reason:
new_or_superseding_adrs:
  - adr_id:
contradiction_ids: []
```

## Review / finalization

```yaml
owner_signoff:
independent_reviewer_signoff:
external_authority_ref_if_required:
final_receipt_digest:
```

Finalization requires scope/evidence alignment, traceable raw and analysis artifacts, preserved adverse/failed/inconclusive evidence, exact decision-rule conformance, explicit conditions, and no optimistic interpretation of missing legal/data-rights evidence.

> A receipt is a scoped evidence record, not a narrative permission slip.
