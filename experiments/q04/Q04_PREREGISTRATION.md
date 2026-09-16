# Q04 Pre-Registration — Deterministic Harness and Optional ML

## Safety / scope

This is research/backtesting validation. It creates no live-trading authority and no instruction to deploy real money.

# E04-A — Deterministic harness validity

Before execution freeze:

```yaml
research_data_profile_ref:
dataset_manifest_ref:
asset_universe:
bar_or_event_frequency:
availability_semantics:
train_validation_test_windows:
walk_forward_plan:
cost_model_version:
benchmark_ladder_versions:
runtime_version:
dependency_lock_digest:
seed_policy:
analysis_code_commit:
```

## Mandatory gates

1. point-in-time manifest proves intended `available_at <= as_of` semantics;
2. hand-computed accounting/fill fixtures match engine outputs within frozen tolerance;
3. deterministic rerun matches expected outputs/digests;
4. cash/no-trade, buy-and-hold and preregistered transparent baselines execute under identical accounting/cost conventions;
5. untouched temporal test interval is not used for tuning;
6. walk-forward/temporal validation and multiple-testing log are complete;
7. realistic cost model is applied consistently;
8. independent rerun reproduces primary outputs under the environment lock.

A losing baseline may still pass E04-A. Harness validity is not alpha evidence.

Decision: all mandatory validity gates pass -> CLOSED_PASS; data/profile formulation requiring material redesign -> PIVOT_REQUIRED; demonstrated infeasibility -> STOP_CURRENT_CONFIGURATION; missing/ambiguous/reproduction-invalid evidence -> INCONCLUSIVE.

# E04-B — ML incremental value

Run only after E04-A CLOSED_PASS and only if there remains a product reason.

Pre-register target/label, feature availability, train/validation/test segmentation, strongest eligible deterministic comparator selection rule, primary metric, risk/secondary metrics, cost assumptions, complexity budget, seed set, regime breakdown, dependence-aware bootstrap rule, multiple-testing controls and retirement rule.

## INCLUDE gates

ML may be `INCLUDE` only if all preregistered conditions hold, including positive incremental OOS value versus the strongest transparent comparator, dependence-aware interval threshold, stability across required folds/regimes/seeds, drawdown guardrail, transaction-cost stress, and multiple-testing controls where applicable.

Failing to earn inclusion is not project failure:
- `EXCLUDE` when evidence actively fails the inclusion case;
- `DEFER` when evidence is insufficient/nonessential and MK1 has no runtime ML dependency.

# Production-semantics compatibility

Research permission is not production permission. Any quant/model/signal surface promoted to MK1 must have:

```yaml
production_semantics_compatibility_ref:
selected_q02_data_use_profile_refs: []
selected_provider_semantics_profile_refs: []
```

If research and production profiles differ materially in availability, adjustments, sessions, freshness, universe or features, affected validation must be re-run or scoped out. Deployed model/feature use must also be authorized under Q02.

# Aggregate Q04 decision

- `CLOSED_PASS`: E04-A passes and `ml_scope` is frozen as INCLUDE, EXCLUDE or DEFER with no unresolved production-semantics contradiction.
- `CLOSED_CONDITIONAL`: harness is valid but a non-fatal explicit quant/data constraint narrows MK1 and is frozen into bootstrap.
- `PIVOT_REQUIRED`: selected asset/data/label/profile formulation requires material re-scope.
- `STOP_CURRENT_CONFIGURATION`: intended research/production path is demonstrably incompatible with reproducible semantics or mandatory rights/economics.
- `INCONCLUSIVE`: required validity/reproduction/compatibility evidence remains insufficient.

Final output is one aggregate Q04 EvidenceReceipt.

## Frozen outputs

```yaml
q04_receipt_ref:
baseline_receipt_ref:
dataset_manifest_ref:
asset_universe:
transaction_cost_model_version:
benchmark_versions: []
primary_metrics: []
production_semantics_compatibility_ref:
ml_scope: INCLUDE | EXCLUDE | DEFER
ml_receipt_ref:
promoted_model_family:
runtime_version:
dependency_lock_digest:
```

Later movement from EXCLUDE/DEFER to INCLUDE reopens Q04 and any affected Q02 rights/data-use scope.
