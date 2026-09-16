# Evidence Receipt Template

## Purpose

This template instantiates the `EvidenceReceipt` contract defined in `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.

A receipt records what was actually observed, reviewed or contractually confirmed. It must not convert missing evidence into a favorable inference.

A finalized receipt is immutable. Corrections or new evidence create a superseding receipt.

---

## 1. Identity

```yaml
receipt_id:
lock_id: Q01 | Q02 | Q03 | Q04 | Q05
lock_version:
receipt_version:
status: DRAFT | REVIEW_READY | CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE | SUPERSEDED
experiment_or_review_id:
created_at:
started_at:
completed_at:
finalized_at:
owner:
independent_reviewer:
supersedes:
```

---

## 2. Scoped question

```yaml
question:
scope:
  product_or_interaction_version:
  population_or_market:
  geography:
  provider_or_dataset:
  asset_universe:
  time_window:
  other_constraints:
```

The final decision applies only to this scope.

---

## 3. Pre-registration / authority

```yaml
pre_registration_ref:
pre_registration_digest:
authority_or_source:
authority_class: OFFICIAL | ACADEMIC | OBSERVED | INFERRED | HYPOTHESIS
source_effective_date:
source_version_or_contract_ref:
```

For Q01/Q02, external authority fields are mandatory where the closure protocol requires them.

For Q03/Q04/Q05 empirical experiments, pre-registration is mandatory before outcome inspection.

---

## 4. Sample / dataset / reviewed material

```yaml
sample_or_dataset:
  planned:
  actual:
  inclusion_criteria:
  exclusion_criteria:
  missing_or_removed_observations:
  deviations_from_plan:

reviewed_artifacts:
  - ref:
    digest:
    description:
```

Any post-registration exclusion must be explained explicitly.

---

## 5. Decision rule frozen before outcome inspection

```yaml
primary_measures:
secondary_measures:
pass_rule:
conditional_pass_rule:
pivot_rule:
stop_rule:
inconclusive_rule:
```

For Q01/Q02, replace quantitative measures where inappropriate with the exact authority/rights questions whose answers determine the outcome.

---

## 6. Raw evidence

```yaml
raw_artifact_refs:
  - ref:
    digest:
    provenance:
    retention_or_rights_constraint:
```

Raw evidence must remain traceable to analysis unless external legal/provider constraints prohibit retention; in that case preserve the minimum lawful audit metadata.

---

## 7. Results

```yaml
primary_results:
secondary_results:
sensitivity_or_subgroup_results:
protocol_deviations:
```

Do not round or selectively aggregate results in a way that hides threshold failures.

---

## 8. Adverse / conflicting evidence

```yaml
adverse_or_conflicting_evidence:
  - description:
    source_ref:
    severity:
    effect_on_decision:
```

This section is mandatory. Use `none_observed` only when genuinely none was found.

---

## 9. Limitations

```yaml
limitations:
  - limitation:
    likely_direction_of_bias:
    materiality:
```

Unknown direction is valid. Do not invent precision.

---

## 10. Final decision

```yaml
final_decision: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE
rationale:
```

### CLOSED_PASS

The exact scoped claim is sufficiently supported for promotion.

### CLOSED_CONDITIONAL

The scoped configuration may proceed only with the listed constraints.

### PIVOT_REQUIRED

The current configuration is unsupported but a materially different candidate is plausible.

### STOP_CURRENT_CONFIGURATION

The exact configuration must not proceed.

### INCONCLUSIVE

Evidence is insufficient to decide. This state never auto-promotes to PASS.

---

## 11. Frozen outputs

```yaml
frozen_outputs:
  - key:
    value_or_ref:
    source_of_authority:

conditions_if_any:
  - condition:
    canonical_destination:
```

Frozen outputs are the only values this receipt is allowed to promote into a candidate `MK1_BOOTSTRAP_PROFILE`.

---

## 12. Canonical updates

```yaml
canonical_docs_updated:
  - path:
    commit_or_digest:

reopened_locks:
  - lock_id:
    reason:

new_or_superseding_adrs:
  - adr_id:
```

A receipt that materially changes product or architecture semantics is incomplete until the corresponding canonical documentation is synchronized.

---

## 13. Contradiction references

```yaml
contradiction_ids:
  -
```

A receipt may be individually positive while still being blocked from promotion by an unresolved cross-receipt P0/P1 contradiction.

---

## 14. Review and finalization

```yaml
owner_signoff:
independent_reviewer_signoff:
external_authority_ref_if_required:
final_receipt_digest:
```

Before finalization confirm:

- scope matches the actual evidence;
- pre-registration/authority existed before the final decision;
- raw evidence remains traceable;
- failed/inconclusive variants were not deleted;
- adverse evidence is preserved;
- the final decision follows the frozen rule;
- conditions are explicit and actionable;
- no claim exceeds the receipt scope;
- no missing legal/data-rights answer is interpreted optimistically;
- no implementation effort or sunk cost influenced the decision threshold.

---

## Finalization invariant

> A receipt is a scoped record of evidence, not a narrative permission slip.

If new evidence changes the conclusion, create a new receipt with `supersedes` rather than editing the finalized record.
