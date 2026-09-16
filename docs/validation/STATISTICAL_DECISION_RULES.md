# Statistical Decision Rules

## Purpose

This contract defines how preregistered Q03/Q04/Q05 thresholds are computed so identical evidence yields the same numerical decision.

## General rules

1. Compute from full precision; round only for display.
2. Record exact numerators/denominators.
3. Freeze unit of analysis, eligibility/exposure denominator, missing-data method, statistical method and decision precedence before outcomes.
4. Exploratory analyses cannot rescue failed primary gates.
5. Sequential peeking/stopping is prohibited unless preregistered.
6. Validity/instrumentation failure makes the affected result `INCONCLUSIVE` by default; it becomes STOP/PIVOT only if the failure itself demonstrates candidate infeasibility.

## Decision-region exhaustiveness

Each experiment defines mutually exclusive PASS/CONDITIONAL/PIVOT/STOP/INCONCLUSIVE regions or a deterministic precedence. Every valid result must map to exactly one final decision. If no declared region applies, the result is `INCONCLUSIVE`.

## Proportions / Wilson interval

`p_hat = successes / eligible_denominator`.

Where requested, use Wilson score interval without continuity correction. For the current two-sided 80% early-product interval use `z = 1.2815515655446004`. PASS/FAIL uses unrounded bounds. `n=0` is undefined/INCONCLUSIVE.

## Paired means / completion time

Repeated tasks are aggregated at participant level unless another dependence-aware unit is preregistered. Paired mean difference uses `d_i = treatment_i - control_i`. Median time ratio uses `median(treatment_ms)/median(control_ms)` on the same eligible paired set unless the missing-data rule says otherwise.

## Calibration

For confidence/correctness on `[0,100]`:

`participant_gap = abs(confidence_percent - correctness_percent)` and `mean_calibration_gap = mean(participant_gap)`.

Do not use `abs(mean(confidence)-mean(correctness))`.

## Missing data

Allowed preregistered methods: `COMPLETE_CASE_PRIMARY`, `FAILURE_AS_FAILURE`, or an exact `PRE_REGISTERED_IMPUTATION`. Behavioral non-action remains a failure/non-event when the event itself is the outcome and telemetry integrity is valid.

## Threshold boundaries

Inclusive/exclusive operators are literal (`>=`, `>`, `<`, `<=`). Map percentage thresholds from exact ratios, not rounded display values.

## Qualitative coding reliability

When coded qualitative evidence can satisfy a promotion threshold:
- freeze the codebook/rubric before outcomes;
- dual-code at least 25% of eligible primary items chosen under a preregistered sampling rule;
- use Cohen's kappa `>= 0.60` for categorical coding unless a justified alternative reliability statistic/threshold is preregistered;
- disagreements are adjudicated under a frozen rule;
- if the required reliability threshold is not met, coding-derived primary metrics cannot support PASS and are `INCONCLUSIVE` until a new valid study/version is run;
- do not rewrite the codebook after seeing which categories would improve the result.

## Q04 dependence-aware bootstrap

For market-return comparisons, ordinary i.i.d. bootstrap is not default. Freeze bootstrap family, block-length rule and seed before final-test inspection; use at least 10,000 resamples for promotion-grade intervals unless infeasible and justified; resample candidate/comparator in aligned blocks.

## Sharpe

Unless the Q04 manifest freezes a justified alternative:

`Sharpe = mean(net_period_return - matched_risk_free_period_return) / std_sample(...) * sqrt(periods_per_year)` with `ddof=1`.

Use identical conventions for candidate/comparator. Zero variance yields `UNDEFINED`, not infinity.

## Drawdown / cost stress

`drawdown_t = W_t / running_peak_t - 1`; report positive magnitude only when labeled. “20% worse relative drawdown magnitude” means `candidate_mdd <= comparator_mdd * 1.20`.

For +50% cost stress, multiply all frozen variable transaction-cost components by 1.5 without reoptimizing signals unless separately preregistered.

## Multiple testing / seeds

Log every materially influential strategy/model variant, parameter/feature set, evaluation window and selection result. Failed variants do not disappear. Freeze seed set and aggregation before final test; report all frozen seeds.

## Outliers / deviations

Default: keep valid observations. Trimming/winsorization/exclusion requires preregistration, counts and sensitivity analysis where material.

Deviation classes:
`MINOR` (no plausible primary effect), `MATERIAL` (may affect primary result; sensitivity/review), `FATAL` (primary result untrustworthy -> INCONCLUSIVE/re-run). A deviation cannot be downgraded because the desired result passed.

## Reproducibility receipt

Promotion-grade analysis records raw export digest, normalized dataset digest, analysis code commit, environment lock digest, statistical-contract version, experiment-manifest digest and output-table digest. Primary numerators/denominators and decision must reproduce from those inputs.
