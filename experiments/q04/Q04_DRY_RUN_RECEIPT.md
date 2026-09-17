# Q04 Dry-Run Receipt — Deterministic Harness

## Status

`INCONCLUSIVE / DRY_RUN_ONLY / NOT_PROMOTABLE`

Executed: `2026-09-17`

Harness: `experiments/q04/harness.py`

This receipt records a synthetic-data mechanics dry run. It is evidence that the test harness can detect accounting/ordering defects and reproduce deterministic outputs; it is **not** evidence that a production market-data profile, strategy or ML component is valid.

## Pre-receipt defect found and corrected

The first dry-run implementation failed the golden buy/hold + fee fixture because position timing and cost application were inconsistent with the declared fill semantics. The engine was corrected before this receipt was frozen:
- target exposure is established at time `t`;
- non-negative transaction cost is applied at the rebalance;
- target exposure earns the `t -> t+1` return;
- terminal position is explicitly closed with exit cost.

The failed variant is preserved here as adverse engineering evidence rather than hidden.

## Dry-run profile

```yaml
profile: Q04-SYNTHETIC-MECHANICS-V1
data: deterministic synthetic bars
bar_count: 40
available_at_rule: available_at == t
cost_model: 5 bps base, 50 bps stress
benchmark_subset:
  - cash
  - buy_hold
  - trend
  - momentum
  - mean_reversion
final_test_boundary_declared: observations 30-39
real_money_execution: false
production_provider: none
```

## Observed checks

```yaml
G1_point_in_time_integrity: PASS
G2_golden_buy_hold_fee_fixture: PASS
G3_deterministic_rerun: PASS
G5_cost_monotonicity: PASS
G6_cash_sanity: PASS
G6_buy_hold_sanity: PASS
G7_dataset_integrity: PASS
G8_final_test_boundary_declared: PASS
artifact_hash: d934d4e706a19f975a865893616723112f452dd9e5ac5ff69a56417cc45711ea
```

The artifact hash is the SHA-256 digest of the canonical benchmark-result object from two identical reruns.

## Explicitly unresolved

### G4 — independent reproduction

`NOT_EXECUTED`.

The same assistant/runtime rerunning the same code is not an independent reviewer. Q04 cannot promote until a second independent reviewer/run path reproduces the frozen profile without manually editing results.

### Production point-in-time dataset

`NOT_EXECUTED`.

Synthetic data proves mechanics only. A promotable E04-A run still needs a real provider-backed dataset manifest with timestamp/session/corporate-action/currency semantics as applicable.

### Q02 compatibility

`OPEN`.

A provider profile used for promotion must have the required commercial/data-rights evidence. The current public precheck does not satisfy Q02.

### ML increment

`NOT_STARTED`.

E04-B cannot begin for promotion because E04-A has not reached `CLOSED_PASS`. No `ml_scope: INCLUDE | EXCLUDE | DEFER` decision is authorized by this dry run.

## Terminal interpretation

```yaml
e04a_status: INCONCLUSIVE
q04_status: INCONCLUSIVE
ml_scope: NOT_EVALUATED
mk1_promotion_contribution: NONE
```

## Next valid execution

1. freeze one real research dataset/profile and rights reference;
2. instantiate the full golden-fixture corpus for that profile;
3. run G1-G8;
4. obtain independent reproduction;
5. only after E04-A `CLOSED_PASS`, decide whether E04-B is worth running.

Synthetic strategy returns in this dry run must not be used as profitability, investment, marketing or future-performance evidence.