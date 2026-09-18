# Q04 Pre-Registration — Deterministic Baseline and Optional ML Increment

## Purpose

Q04 answers two separate questions:

1. Is the quantitative research harness scientifically and mechanically trustworthy enough for MK1 research/backtesting?
2. Does any ML component add robust out-of-sample value beyond the strongest transparent deterministic baseline after realistic costs?

The first can pass even when strategies perform poorly. The second can fail while Q04 still closes successfully with `ml_scope: EXCLUDE` or `DEFER`.

This is a research/paper-validation protocol. It does not authorize real-money deployment or live autonomous execution.

Canonical scientific policy: `docs/quant/VALIDATION_PROTOCOL.md`.
Semantic normalization: `docs/validation/CANONICAL_VALIDATION_SPEC.md`.
Statistical computation contract: `docs/validation/STATISTICAL_DECISION_RULES.md`.

---

# Shared instantiation contract

Before any Q04 run, create a versioned experiment manifest that freezes:

```yaml
experiment_id:
asset_universe:
instrument_ids:
provider_profile_refs:
data_rights_refs:
dataset_manifest_ref:
calendar_session_semantics:
corporate_action_semantics:
currency_semantics:
available_at_semantics:
bar_or_event_granularity:
transaction_cost_model_version:
benchmark_ladder_versions:
train_validation_test_boundaries:
walk_forward_scheme:
primary_metric:
secondary_metrics:
random_seed_policy:
multiple_testing_log_ref:
code_commit:
environment_lock_digest:
```

No asset, interval, fee or benchmark substitution is allowed after outcome inspection without a new experiment version.

Any provider/data-rights profile used for an MK1-promotable result must still be valid/reviewable under Q02; a scientifically valid result using unusable commercial data does not authorize that production profile.

---

# E04-A — Deterministic Baseline Harness Validity

## Question

Can SOPHROSYNE reproduce transparent strategy/accounting results under frozen point-in-time, fill, cost and benchmark semantics?

This experiment validates the **research engine**, not profitability.

## Required benchmark ladder

At minimum instantiate eligible versions of:

```text
B00 cash / no-trade
B01 buy-and-hold
B02 simple trend
B03 simple momentum
B04 simple mean reversion
B05 transparent multifactor
B06 deterministic regime-aware rule
```

If a benchmark is semantically inappropriate for the selected asset/profile, mark it `NOT_APPLICABLE` with reason before outcome inspection.

## Golden fixture corpus

Must include hand-computable cases for:
- single buy/sell fill;
- multiple fills / partial position changes;
- fees;
- slippage/spread model;
- cash accounting;
- realized/unrealized P&L;
- return series;
- drawdown;
- position sizing rule used by the sandbox;
- missing/stale bar behavior;
- no-trade state;
- corporate action case when applicable;
- timezone/session boundary when applicable;
- currency conversion when applicable.

Each fixture declares its own numeric tolerance. Discrete/accounting values that can be represented exactly must match exactly; floating derived metrics use the smallest justified tolerance documented in the fixture.

## Hard PASS gates

All must pass:

### G1 — point-in-time integrity

`0` accepted historical observations may have `available_at > as_of` for the selected replay mode.

Any unexplained leakage is a hard FAIL.

### G2 — golden accounting/fill fixtures

`100%` mandatory fixtures pass their declared tolerance.

### G3 — deterministic rerun

Two reruns using the same manifest/code/environment must produce:
- identical canonical input manifest digests;
- identical discrete fills/orders/state transitions;
- identical canonical artifact hashes where serialization is deterministic;
- otherwise derived numeric series within the frozen tolerance profile.

### G4 — independent reproduction

A second reviewer/run path reproduces the primary benchmark outputs from the frozen manifest without manual result editing.

Canonical handoff: `experiments/q04/Q04_INDEPENDENT_REPRODUCTION_PACKET.md`.

The external reviewer receives the frozen inputs/environment instructions but not the original numeric benchmark output until their independent result artifact is frozen. Same-author/same-runtime reruns do not satisfy G4.

### G5 — cost monotonicity

For a fixed trade path, increasing non-negative transaction costs may not improve net P&L through an accounting bug.

### G6 — benchmark sanity

- cash/no-trade has zero market turnover and only explicitly modeled cash effects;
- buy-and-hold matches independently computed benchmark mechanics;
- all benchmark signals use only information legitimately available at decision time.

### G7 — dataset integrity

No unexplained duplicate timestamps, impossible ordering, unresolved gaps required by the selected profile or silent provider substitutions remain in the final dataset manifest.

### G8 — untouched final test

The final test interval remains untouched by model/rule selection after it is frozen.

## E04-A result

### CLOSED_PASS

All G1–G8 pass.

### PIVOT_REQUIRED

A hard gate fails because dataset/provider/engine semantics require a corrected research profile rather than simply more evidence.

### STOP_CURRENT_CONFIGURATION

The selected profile cannot support a reproducible point-in-time harness or a mandatory assumption is fundamentally incompatible with the intended MK1 quant surface.

### INCONCLUSIVE

Evidence is incomplete because the required data/profile cannot yet be instantiated, independently reproduced, or validly assessed. This never promotes and E04-B may not begin for that profile.

A negative-return strategy does **not** fail E04-A merely because it loses money.

---

# E04-B — Optional ML Incremental Value

## Entry condition

E04-A must already be `CLOSED_PASS` for the exact underlying data/cost/accounting profile used here.

`INCONCLUSIVE`, `PIVOT_REQUIRED` or `STOP_CURRENT_CONFIGURATION` in E04-A blocks ML promotion for that profile.

## Question

Does the ML candidate provide robust incremental out-of-sample value over the strongest eligible transparent deterministic comparator, enough to justify added complexity?

## Comparator selection

The comparator selection rule is frozen before ML test inspection:
- select the strongest deterministic comparator using training/validation data only;
- never choose a deliberately weak comparator to make ML look better;
- final test data cannot choose the comparator.

## Candidate family freeze

Before training, freeze:

```yaml
prediction_or_classification_target:
feature_set_version:
feature_available_at_rules:
model_family:
hyperparameter_search_space:
search_budget:
training_window:
validation_scheme:
final_test_window:
walk_forward_folds:
seed_set:
primary_metric:
calibration_metric_if_probability_output:
complexity_and_latency_budget:
```

Every tried variant counts in the multiple-testing log, including failed variants.

---

## Primary promotion metric

Unless the manifest justifies another metric before inspection:

`primary_metric = delta_net_oos_sharpe_vs_best_deterministic_baseline`

where both strategies use identical:
- evaluation timestamps;
- cost assumptions;
- risk/position-sizing contract where comparison requires it;
- point-in-time dataset semantics.

Sharpe is not treated as sufficient by itself; the guardrails below are mandatory.

---

## ML INCLUDE gate

All applicable conditions must pass:

### M1 — positive distributional evidence

A block-bootstrap (or pre-registered dependence-aware alternative) on the frozen OOS comparison must have the lower bound of a `90%` interval for `Δ net Sharpe` greater than `0`.

### M2 — economically meaningful median improvement

Median walk-forward `Δ net Sharpe >= 0.15`.

### M3 — fold stability

ML beats the comparator on the primary metric in `>= 70%` of valid walk-forward folds.

No single fold may contribute more than 50% of the total measured improvement without being flagged as concentration evidence requiring a regime-specific interpretation.

### M4 — drawdown guardrail

ML maximum drawdown magnitude may not be more than `20%` worse relative to the comparator unless a different risk tradeoff was explicitly pre-registered and justified before inspection.

Example: comparator drawdown 20%; default guardrail permits ML drawdown up to 24%, not 40%.

### M5 — cost-stress robustness

Under `+50%` transaction-cost stress relative to the base cost model:
- ML must retain a positive median primary-metric delta across folds; and
- the claimed incremental advantage may not disappear solely because turnover was ignored.

### M6 — seed/search stability

Result may not depend on one favorable random seed. Report all frozen seeds and aggregate per the pre-registered method.

### M7 — multiple-testing / backtest-overfitting guard

When estimable from the search setup:
- Deflated Sharpe Ratio probability/criterion must meet the pre-registered acceptance rule; and
- Probability of Backtest Overfitting should be `<= 0.20` for the evaluated selection process.

If these methods are not applicable/estimable, the manifest must state why before final review and use another pre-registered multiplicity control. “Not computed because result looked good” is invalid.

### M8 — probability calibration guardrail

If the model exposes probabilities:
- calibration metrics must beat or be non-inferior to the frozen naive/base probability comparator;
- no user-visible probability is promoted unless `CALIBRATION_STATUS = APPROVED` under the system contract.

### M9 — complexity budget

The measured gain must fit the frozen inference/training/operational budget. A tiny statistical improvement that requires an operationally disproportionate dependency may be rejected as `DEFER` even if raw metrics pass.

---

## ML EXCLUDE / DEFER rules

### EXCLUDE

Set `ml_scope: EXCLUDE` for MK1 when:
- E04-A passes; but
- one or more mandatory ML INCLUDE gates fail; and
- there is no distinct pre-registered ML use case that independently passes.

This is a successful Q04 outcome, not project failure.

### DEFER

Set `ml_scope: DEFER` when:
- E04-A passes;
- evidence is promising but sample/regime coverage is insufficient;
- required features/data rights are not yet available for production;
- complexity cost cannot yet be justified; or
- a later MK can revisit the question without changing MK1 core value.

### PIVOT_REQUIRED

Use when the selected target/features/dataset formulation is invalid in a way that requires a new experiment profile rather than simply excluding ML.

### INCONCLUSIVE

Use for E04-B only when the question cannot validly be decided under the frozen manifest because required evidence failed for non-directional reasons such as material instrumentation/data corruption, incomplete prescribed evaluation, or an unresolved methodological contradiction. `INCONCLUSIVE` never becomes `DEFER` merely to permit promotion.

---

# Regime and stress reporting

Every candidate strategy/model report must break out performance where the data permit by pre-defined relevant market conditions such as:
- high vs low volatility;
- trending vs non-trending;
- liquidity/cost regimes;
- selected calendar periods.

Regime labels themselves must be computable point-in-time if used for historical decision logic.

These breakouts diagnose fragility; they do not allow post-hoc selection of “the good regime” as the main result.

---

# Required report metrics

At minimum:
- net cumulative return;
- annualized return where meaningful;
- volatility;
- Sharpe;
- Sortino;
- max drawdown;
- turnover;
- number of trades/events where applicable;
- cost paid;
- cost-stress result;
- comparator delta;
- fold-by-fold results;
- calibration metrics for probability models;
- DSR/PBO or documented alternative where applicable;
- rejected/failed variants count.

No single metric is allowed to stand in for the complete promotion gate.

---

# Q04 aggregate decision

## CLOSED_PASS — ML INCLUDE

E04-A `CLOSED_PASS` plus every applicable ML INCLUDE gate passes.

## CLOSED_PASS — ML EXCLUDE

E04-A `CLOSED_PASS` and ML does not justify added complexity.

## CLOSED_PASS — ML DEFER

E04-A `CLOSED_PASS` and the model question is explicitly postponed with no MK1 dependency.

## PIVOT_REQUIRED

Research profile semantics/data formulation are invalid and must be redesigned.

## STOP_CURRENT_CONFIGURATION

The selected data/profile cannot support reproducible research or the required rights/point-in-time semantics make the candidate quant surface infeasible.

## INCONCLUSIVE

E04-A is inconclusive, or a required aggregate decision cannot be made because evidence is incomplete/invalid without directional support for pass/pivot/stop. This blocks Q04 closure and MK1 promotion until rerun/resolution.

---

## Q04 frozen outputs

```yaml
baseline_harness_receipt:
dataset_manifest_ref:
asset_universe:
provider_profile_refs:
cost_model_version:
benchmark_versions:
walk_forward_scheme:
primary_metrics:
golden_fixture_digest:
anti_leakage_receipt:
independent_reproduction_ref:
ml_scope: INCLUDE | EXCLUDE | DEFER
promoted_model_family_if_any:
model_receipt_if_any:
known_regime_limitations:
research_evidence_as_of:
reopen_triggers:
```

Reopen affected Q04 scope when dataset semantics, provider profile, transaction-cost model, benchmark/accounting rules, label/feature availability, model family (if promoted), or another build-defining research assumption materially changes.

No Q04 receipt authorizes a profitability or future-performance marketing claim.
