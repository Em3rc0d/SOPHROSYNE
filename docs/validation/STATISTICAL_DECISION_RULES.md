# Statistical Decision Rules

## Purpose

This document removes implementation ambiguity from quantitative decision gates used by MK0 evidence experiments.

It does not choose experiment-specific thresholds; those live in the pre-registered Q03/Q04/Q05 manifests. This document defines how those thresholds are computed and compared so two reviewers using the same evidence reach the same numerical result.

---

## General principles

1. Compute from full-precision source values; round only for display.
2. Record exact numerators and denominators for all rates/proportions.
3. Never change the statistical method after observing outcomes unless the original method is invalid; if so, mark the original experiment inconclusive and create a new version.
4. Do not use significance testing as a substitute for the pre-registered product decision rule.
5. Missing data, exclusions and protocol deviations follow the pre-registered manifest, not analyst preference.
6. Exploratory analyses remain labeled exploratory and cannot rescue a failed primary gate.
7. Sequential peeking/stopping is prohibited unless the manifest pre-registers a sequential design.

---

# Proportions

## Point estimate

For a binary event:

```text
p_hat = successes / eligible_denominator
```

The denominator is determined by the pre-registered eligibility rule.

Do not remove participants from the denominator because they did not perform the desired behavior.

## Wilson score interval

Where a pre-registered gate requests a Wilson interval, use the standard score interval without continuity correction.

Given:

```text
n = denominator
x = successes
p = x / n
z = standard-normal quantile for requested two-sided coverage
```

Center:

```text
center = (p + z²/(2n)) / (1 + z²/n)
```

Half-width:

```text
half = z/(1 + z²/n) * sqrt(p(1-p)/n + z²/(4n²))
```

Bounds:

```text
lower = center - half
upper = center + half
```

For the two-sided 80% interval used in current Q03/Q05 early-product gates:

```text
z = 1.2815515655446004
```

Evaluate PASS/FAIL using unrounded `lower`/`upper`; display rounding does not change the decision.

If `n = 0`, the metric is undefined and the result is `INCONCLUSIVE`.

---

# Means / medians / paired comparisons

## Participant-level aggregation first

When a participant completes multiple tasks/cases, the manifest must state whether the unit of analysis is:
- participant-level average;
- participant-case observation;
- another explicitly justified unit.

Do not treat repeated observations from the same participant as independent merely to inflate sample size.

## Mean difference

For paired treatment/control studies, default mean-difference reporting uses participant-level paired differences:

```text
d_i = treatment_i - control_i
mean_delta = mean(d_i)
```

The sign convention must be documented because “higher is better” differs by metric.

## Median time ratio

For decision rules using median completion time:

```text
ratio = median(treatment_completion_ms) / median(control_completion_ms)
```

The same eligible participant set should be used on both sides unless the pre-registered missing-data rule says otherwise.

---

# Confidence calibration gap

When confidence and correctness are both expressed on `[0,100]`:

```text
participant_gap = abs(confidence_percent - correctness_percent)
mean_calibration_gap = mean(participant_gap)
```

Q03/Q05 compare treatment and control mean participant gaps.

Do not compute `abs(mean(confidence) - mean(correctness))`; that can hide individual miscalibration.

---

# Missing data

Before execution, each experiment declares one of:

### COMPLETE_CASE_PRIMARY

Primary metric uses only participants with all fields needed for that paired metric. The number/reason of removed participants is reported.

### FAILURE_AS_FAILURE

For behavioral events where non-action is itself the meaningful outcome, absence of the event remains in the denominator rather than being treated as missing.

Example: a participant who does not return during E03-C is a non-returner, not missing data, assuming telemetry integrity is valid.

### PRE_REGISTERED_IMPUTATION

Allowed only when the exact imputation method is specified before outcomes are observed and is appropriate for the measure.

Post-hoc imputation chosen to improve results is prohibited.

---

# Threshold boundaries

Use exact inclusive/exclusive semantics as written.

Examples:

```text
>= 50%  includes exactly 0.50
> 50%   excludes exactly 0.50
< 25%   excludes exactly 0.25
<= 25%  includes exactly 0.25
```

When a percentage threshold maps to participant counts, calculate from the exact ratio rather than rounding the percentage first.

---

# Q04 time-series dependence

Ordinary i.i.d. bootstrap is not the default for market-return comparisons because serial dependence may exist.

For gates requiring a dependence-aware bootstrap:
- block/bootstrap family is frozen before final-test inspection;
- block-length rule is frozen in the experiment manifest;
- number of resamples is at least `10,000` for promotion-grade intervals unless computationally infeasible and explicitly justified;
- random seed(s) are recorded;
- both strategy/comparator series are resampled in aligned blocks so their paired relationship is preserved.

The final-test interval may not be repeatedly re-used to tune block length for a favorable result.

---

# Sharpe computation contract

Unless an instantiated Q04 manifest freezes a justified alternative:

```text
period_return = net strategy return after modeled costs
excess_period_return = period_return - matched risk_free_period_return
Sharpe = mean(excess_period_return) / std_sample(excess_period_return) * sqrt(periods_per_year)
```

Rules:
- sample standard deviation uses `ddof = 1`;
- annualization factor matches the actual period/calendar semantics;
- zero-variance series yields `UNDEFINED`, not infinite Sharpe;
- comparator and candidate use identical risk-free/annualization conventions;
- results with too few independent effective observations to interpret are flagged as a limitation.

If the product research profile elects zero risk-free rate for a specific study, that assumption must be frozen before inspection and applied equally.

---

# Drawdown contract

From an equity/wealth index `W_t`:

```text
peak_t = max(W_0 ... W_t)
drawdown_t = W_t / peak_t - 1
max_drawdown = min(drawdown_t)
```

Report magnitude as a positive percentage only when explicitly labeled `max_drawdown_magnitude`.

When a guardrail says “20% worse relative drawdown magnitude”:

```text
candidate_mdd_magnitude <= comparator_mdd_magnitude * 1.20
```

Do not interpret this as +20 percentage points.

---

# Transaction-cost stress

Cost-stress variants keep the same underlying trades/signals whenever the purpose is cost sensitivity.

For `+50%` cost stress:

```text
stressed_cost_component = base_cost_component * 1.5
```

Apply to all variable transaction-cost components named in the frozen cost model unless the manifest explicitly excludes a component for a documented semantic reason.

Do not re-optimize the model/strategy under stressed costs unless that is a separately pre-registered robustness experiment.

---

# Multiple testing

Every strategy/model variant that materially influenced selection is logged.

The multiple-testing log includes:
- candidate ID;
- hypothesis/model family;
- parameters/features tried;
- evaluation windows used;
- primary metrics observed during selection;
- reason rejected/promoted.

A failed variant does not disappear because its code was deleted.

Where DSR/PBO are used, record the exact implementation/reference and all inputs needed to reproduce them.

---

# Randomness and seeds

For randomized experiments/models:
- seed set is frozen before final-test inspection;
- report every frozen seed, not only the best;
- aggregation rule across seeds is pre-registered;
- if a library/hardware path is non-deterministic, record that limitation and use repeated-run stability checks.

---

# Outlier handling

Default: keep valid observations.

Any trimming/winsorization/outlier exclusion requires:
- a pre-registered rule based on data validity or an explicit robust-analysis design;
- reporting both raw count and excluded count;
- sensitivity analysis where material.

“Looks extreme” is not an exclusion rule.

---

# Protocol deviations

A deviation is classified before seeing whether it helps/hurts the hypothesis where possible:

```text
MINOR       no plausible effect on primary result
MATERIAL    may affect primary result; sensitivity/review required
FATAL       primary result cannot be trusted; experiment INCONCLUSIVE/re-run
```

A deviation cannot be downgraded because the desired result passed.

---

# Reproducible analysis receipt

Promotion-grade empirical analysis references:

```yaml
raw_export_digest:
normalized_dataset_digest:
analysis_code_commit:
environment_lock_digest:
statistical_contract_version:
experiment_manifest_digest:
output_table_digest:
```

Primary numerators/denominators and decision status must reproduce from those inputs.

---

## Final invariant

> The decision rule is part of the experiment before the result is known, not an interpretation layer added afterward.
