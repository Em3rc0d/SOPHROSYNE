# Experiment Manifest Template

## Purpose

Every empirical MK0 experiment that may close or materially influence Q00, Q03, Q04 or Q05 must be pre-registered before outcome data are inspected.

This template is designed to prevent post-hoc metric changes, cherry-picking and ambiguous promotion decisions.

Copy this file into a versioned experiment folder or receipt bundle before running the experiment.

Canonical lifecycle/outcome vocabulary is governed by `docs/validation/CANONICAL_VALIDATION_SPEC.md`. This template must use those exact terms rather than aliases.

---

## 1. Identity

```text
experiment_id:
version:
status: DRAFT | PRE_REGISTERED | EVIDENCE_RUNNING | REVIEW_READY | FINAL | SUPERSEDED
lock_ids:
owner:
independent_reviewer:
created_at:
pre_registered_at:
supersedes:
```

A manifest becomes immutable when status moves to `PRE_REGISTERED`.

Any material change after that point requires a new version.

---

## 2. Question

State the exact question in one sentence.

```text
question:
```

Examples of acceptable questions:
- Does the full candidate intervention add material decision-process value beyond competent simple baselines?
- Does Translator View improve objective comprehension while preserving confidence calibration versus the comparison workflow?
- Does the deterministic benchmark harness reproduce point-in-time results under the frozen cost model?
- Does an ML candidate add robust out-of-sample value versus the strongest eligible transparent baseline?

Do not use vague questions such as “Do users like it?” or “Does AI work?”.

---

## 3. Hypothesis and alternatives

```text
primary_hypothesis:
null_or_failure_hypothesis:
plausible_alternative_explanations:
```

A useful experiment must allow the primary hypothesis to fail.

---

## 4. Scope

```text
population_or_market:
asset_universe_if_applicable:
geography:
interaction_or_product_version:
dataset_version:
time_window:
provider_profile:
```

Results may not be generalized beyond this scope without a new evidence argument.

---

## 5. Inclusion / exclusion

```text
inclusion_criteria:
exclusion_criteria:
withdrawal_or_abort_rules:
```

Criteria must be chosen before outcome inspection.

Excluding inconvenient observations after results are known requires explicit adverse-evidence disclosure.

---

## 6. Sample / dataset plan

```text
target_sample_size_or_dataset_size:
minimum_usable_sample:
recruitment_or_sampling_method:
stratification_or_cohorts:
randomization_or_counterbalancing:
missing_data_policy:
```

If sample size is feasibility-driven rather than powered statistically, state that limitation explicitly.

---

## 7. Primary measures

Primary measures determine the experiment result.

```text
primary_measures:
  - name:
    definition:
    unit:
    direction_of_better:
    aggregation:
```

Every measure must be computable from the planned artifacts without subjective reinterpretation after the run.

---

## 8. Secondary / diagnostic measures

```text
secondary_measures:
  - name:
    purpose:
```

Secondary measures may explain a result but cannot rescue a failed primary decision rule unless a new experiment is registered.

---

## 9. Decision rule

Freeze the exact rule before execution.

```text
closed_pass_rule:
closed_conditional_rule:
pivot_required_rule:
stop_current_configuration_rule:
inconclusive_rule:
```

If numeric thresholds are appropriate, put them here now.

If a composite decision is required, define which measures are mandatory and which are supportive.

Do not choose thresholds after seeing results.

---

## 10. Analysis plan

```text
statistical_or_comparison_method:
confidence_interval_or_uncertainty_method:
multiple_testing_control:
subgroup_policy:
sensitivity_analysis:
```

For quant experiments also define:
- untouched test interval;
- walk-forward method;
- purge/embargo where needed;
- transaction-cost assumptions;
- benchmark comparator rule;
- seed policy;
- regime breakdown;
- overfitting-control method.

---

## 11. Data / artifact provenance

```text
raw_artifacts_expected:
normalized_artifacts_expected:
source_provenance:
rights_or_consent_constraints:
retention_constraints:
```

Raw evidence must remain traceable to the final analysis.

---

## 12. Known confounders

```text
known_confounders:
expected_biases:
measurement_limitations:
```

Examples:
- participants recruited from developer communities may not represent broader retail investors;
- repeated briefings may create novelty effects;
- historical market periods may overrepresent a regime;
- provider corrections may change later research truth;
- self-selected pricing-test traffic may inflate purchase intent.

---

## 13. Safety / legal / ethics constraints

```text
constraints:
```

MK0 user research must not depend on real-money trading instructions or pressure participants to transact.

Research prototypes must clearly remain non-production and within the currently permitted product boundary.

---

## 14. Abort conditions

```text
abort_conditions:
```

Examples:
- corrupted dataset;
- rights uncertainty discovered mid-run;
- experimental implementation differs materially from pre-registered version;
- severe instrumentation failure;
- participant cohort no longer matches inclusion criteria.

An aborted experiment is preserved; it is not silently deleted.

---

## 15. Expected outputs

```text
raw_data_ref:
analysis_ref:
plots_or_tables_ref:
experiment_receipt_ref:
canonical_docs_potentially_affected:
```

---

# Final result section

Complete only after the experiment runs.

## 16. Actual execution

```text
started_at:
completed_at:
actual_sample_or_dataset:
protocol_deviations:
missing_data:
```

## 17. Results

```text
primary_results:
secondary_results:
sensitivity_results:
adverse_or_conflicting_evidence:
```

## 18. Decision

```text
result: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE
rationale:
limitations:
```

Only the canonical aggregate outcome vocabulary is valid. `INCONCLUSIVE` is a valid result and cannot be auto-promoted to PASS.

## 19. Freeze outputs

```text
frozen_outputs:
rejected_hypotheses:
follow_up_required:
locks_closed_or_reopened:
```

## 20. Review

```text
owner_signoff:
independent_reviewer_signoff:
reviewed_at:
receipt_digest:
```

---

## Anti-gaming checklist

Before finalizing, confirm:

- primary measures were not changed after seeing outcomes;
- excluded observations follow the pre-registered rule;
- failed variants remain in the experiment history;
- negative evidence is included;
- subgroup analysis was pre-specified or clearly marked exploratory;
- no result is generalized outside its defined scope without qualification;
- a prototype success is not represented as production evidence;
- implementation effort already spent did not lower the gate;
- the final decision follows the registered rule and canonical vocabulary.
