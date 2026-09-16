# Experiment Manifest Template

## Purpose

Every empirical experiment capable of changing MK1 scope is pre-registered before outcome inspection. The manifest freezes the question, evidence scope, analysis and decision regions so results cannot move the goalposts.

## Identity and scope

```yaml
experiment_id:
experiment_version:
lock_id: Q03 | Q04 | Q05
status: DRAFT | PRE_REGISTERED | RUNNING | REVIEW_READY | FINAL | SUPERSEDED
owner:
independent_reviewer:
created_at:
pre_registered_at:
supersedes:

question:
hypothesis:
failure_hypothesis:
product_or_prototype_digest:
primary_promotion_geography:
study_language:
population_or_market:
asset_or_dataset_scope:
time_window:
```

For current MK1 human promotion studies, default `primary_promotion_geography: Peru` and `study_language: Spanish`. Other cohorts require explicit exploratory labels or a separately revalidated promotion scope.

## Population / dataset plan

```yaml
planned_sample_or_dataset:
minimum_usable_sample:
recruitment_or_source:
inclusion_criteria:
exclusion_criteria:
withdrawal_or_missing_data_rule:
compensation_or_incentive_rule:
unit_of_analysis:
eligible_denominator_rule:
exposure_eligibility_rule:
```

Repeated observations from one participant are not independent unless the analysis explicitly models that dependence.

## Treatment / comparator / execution

```yaml
variants_or_candidates:
comparator_selection_rule:
assignment_or_counterbalancing:
task_or_scenario_refs:
moderator_or_execution_script_ref:
reminder_or_contact_policy_ref:
randomization_seed_policy:
```

## Measures and analysis

```yaml
primary_measures:
secondary_measures:
qualitative_coding_rubric_ref:
qualitative_reliability_rule:
statistical_contract_ref: docs/validation/STATISTICAL_DECISION_RULES.md
statistical_contract_version:
analysis_plan:
missing_data_method:
outlier_rule:
multiple_testing_rule:
```

Any qualitative coding that can satisfy a promotion threshold must use a frozen codebook and pre-registered reliability rule.

## Decision regions

```yaml
pass_rule:
conditional_pass_rule:
pivot_rule:
stop_rule:
inconclusive_rule:
decision_precedence:
```

Regions must be mutually exclusive or have deterministic precedence frozen here. Every possible valid outcome must map to one final decision. Unclassified valid outcomes default to `INCONCLUSIVE`, never PASS.

## Known confounders / validity threats

```yaml
known_confounders:
protocol_deviation_policy:
instrumentation_quality_gates:
external_authority_or_rights_constraints:
```

A data/instrumentation validity failure normally makes the affected metric/experiment `INCONCLUSIVE`; it becomes STOP/PIVOT only if the failure itself proves the candidate configuration infeasible.

## Expected artifacts

```yaml
raw_artifact_refs_expected:
normalized_dataset_ref_expected:
analysis_code_commit_expected:
environment_lock_digest_expected:
output_table_ref_expected:
receipt_template_ref: docs/validation/EVIDENCE_RECEIPT_TEMPLATE.md
```

## Anti-gaming lock

After `PRE_REGISTERED`, do not change primary measures, thresholds, denominator/exposure eligibility, sample minimum, comparator, final-test interval, coding rubric, statistical method or precedence because observed outcomes are inconvenient. A material correction creates a new experiment version; the old version remains in history.

## Final result

```yaml
final_decision: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE
receipt_ref:
```

The manifest is not itself evidence; its paired EvidenceReceipt records what happened.
