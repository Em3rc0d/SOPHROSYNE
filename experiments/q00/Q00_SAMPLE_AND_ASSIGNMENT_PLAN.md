# Q00 Sample and Assignment Plan — Candidate Freeze

## Status

`READY_FOR_INDEPENDENT_REVIEW / NOT_PRE_REGISTERED / NOT_EVIDENCE`

This plan closes the internal design of the Q00 assignment mechanism. It does not freeze the experiment until the independent reviewer approves the material set and the final manifest is moved to `PRE_REGISTERED`.

## Population

Primary promotable cohort:
- adults `18+`;
- Peru promotion cohort;
- self-directed market/investment research behavior in the last 90 days;
- no requirement to trade real money;
- no requirement to disclose holdings, balances or brokerage credentials.

Primary-cohort participants who work professionally as investment advisers, portfolio managers, securities brokers or institutional traders are excluded from the promotable retail cohort and may be retained only as a separately labeled exploratory expert cohort.

## Sample plan

```yaml
target_usable_n: 84
minimum_usable_n: 70
williams_sequences: 14
target_per_sequence: 6
minimum_per_sequence: 5
recruitment_target_n: 98
primary_geography: Peru
unit_of_independence: participant
tasks_per_participant:
  arm_tasks: 7
  unassisted_transfer_tasks: 1
max_total_tasks: 8
```

Rationale:
- 84 preserves six complete participants per each of the 14 balanced Williams sequences.
- 70 is the fail-closed minimum: five complete participants per sequence.
- Below 70 usable primary participants, Q00 is `INCONCLUSIVE` regardless of descriptive direction.
- Recruitment target 98 provides headroom for eligibility failures, withdrawal and technical exclusions without changing the minimum after outcome inspection.

This is an early product causal gate, not a population-prevalence estimate and not a profitability study.

## Arm set

```text
A raw information
B stateless structured assistant
C five-question friction
D simple prediction/confidence/outcome feedback
E short-memory SOPHROSYNE
F full SOPHROSYNE
G strongest frozen conventional cheap/free comparator
T unassisted transfer task; not a treatment arm
```

Each participant receives every A–G arm exactly once across seven distinct scenario instances.

## Williams crossover

Seven-arm order uses a first-order carryover-balanced Williams design.

Base sequence:

```text
A B G C F D E
```

Seven cyclic rotations plus their seven reversals produce 14 sequences.

Required properties:
- each arm appears exactly twice in every ordinal task position across the 14 sequences;
- every ordered first-order transition between distinct arms appears exactly twice across the 14 sequences;
- each arm is paired with each of the seven arm-task scenario positions exactly twice across the 14 sequences;
- participant assignment to sequence is deterministic from the frozen assignment seed and recruitment index.

The canonical generator is `experiments/q00/generate_assignment.py`.

## Scenario allocation

Arm-task scenarios:

```text
SYN-01
SYN-02
SYN-03
SYN-04
SYN-06
SYN-07
SYN-08
```

Unassisted transfer scenario:

```text
SYN-05
```

Scenario position is fixed across sequence definitions. Because arms are balanced across positions, every arm-scenario pair occurs equally often over the complete 14-sequence cycle.

SYN-05 is never assigned an A–G treatment surface in the primary transfer analysis.

## Transfer insertion

The transfer task is inserted adjacent to arm F while balancing whether F has already been seen:

- sequences 01–07: transfer immediately **before** F; `prior_F_exposure = false`;
- sequences 08–14: transfer immediately **after** F; `prior_F_exposure = true`.

This yields a 7-sequence vs 7-sequence randomized-order contrast for immediate unassisted transfer while preserving the Williams arm schedule.

The transfer task renders with `?transfer=1`, which removes the candidate assistance surfaces and outcome feedback before submission.

## Primary outcomes and frozen materiality thresholds

### P1 — decision-process score: F vs A

```yaml
metric: decision_process_score_0_100
contrast: F - A
minimum_mean_delta: +8 points
90pct_interval_lower_bound: > +3 points
```

Both conditions are required.

### P2 — incremental complexity: F vs C

```yaml
metric: decision_process_score_0_100
contrast: F - C
minimum_mean_delta: +4 points
90pct_interval_lower_bound: > 0
```

Additionally, the existing simple-friction destruction rule remains authoritative:

```text
benefit_C = mean(C - A)
benefit_F = mean(F - A)

if benefit_F <= 0 -> full-complexity advantage not established
if benefit_C / benefit_F >= 0.80 -> full-complexity advantage not established
```

### P3 — strongest cheap/free comparator: F vs G

Candidate superiority:

```yaml
minimum_mean_delta: +5 points
90pct_interval_lower_bound: > 0
```

Comparator non-inferiority signal:

```yaml
noninferiority_margin: 3 points
rule: upper bound of 90pct interval for (F - G) < +3
```

If G is non-inferior on the primary score and F has no pre-registered cognitive-cost advantage, the independent full-product configuration is not promotable without narrowing/pivot.

If neither superiority nor comparator non-inferiority can be established, the F-vs-G result is `INCONCLUSIVE`; it may not be narrated as a win.

## Memory ablation

Full-memory support requires:

```yaml
contrast: F - E
minimum_mean_delta: +4 points
90pct_interval_lower_bound: > 0
```

Otherwise:
- no material/stable F→E increment: `SHORT_MEMORY_SUFFICIENT`;
- E materially outperforms F: `MEMORY_EXCLUDED` or narrower redesign;
- ambiguous interval: full-memory complexity remains unearned.

## Cognitive-cost guardrail

F cannot earn complexity solely from quality gains if any mandatory burden guardrail fails without a preregistered compensating rule:

```yaml
median_completion_time_ratio_F_over_C: <= 1.50
mean_workload_delta_F_minus_C: <= 0.75  # 1-5 workload scale
help_requested_rate_delta_F_minus_C: <= 0.10
```

A failed burden guardrail triggers `PIVOT_REQUIRED` or `CLOSED_CONDITIONAL` narrowing depending on the complete primary result; it cannot be hidden as a secondary metric.

## Transfer rule

Primary transfer contrast:

```yaml
metric: unassisted_transfer_process_score_0_100
groups:
  exposed: prior_F_exposure == true
  not_yet_exposed: prior_F_exposure == false
minimum_mean_delta: +5 points
90pct_interval_lower_bound: > 0
```

If assisted performance improves but this transfer rule does not pass, claims are limited to `ASSISTED_ONLY`.

## Estimation / uncertainty

Primary arm contrasts use participant-level paired differences.

Because each participant sees every A–G arm once and arm/scenario/order are balanced by design:
1. compute each participant's requested arm contrast;
2. estimate the mean participant contrast;
3. produce a two-sided 90% percentile interval using 10,000 participant bootstrap resamples;
4. bootstrap is stratified by Williams sequence so sequence balance is preserved;
5. use the frozen seed from the final manifest;
6. report raw per-arm means and sequence/scenario diagnostics as secondary checks.

Transfer uses the same 10,000-resample procedure, resampling participants within sequence and comparing the two predeclared transfer groups.

No p-value is required for a PASS. The practical threshold + uncertainty rule is authoritative.

## Missing data

Primary arm contrasts use `COMPLETE_CASE_PRIMARY` for the pair being compared.

Rules:
- participant remains in denominators for behavioral non-actions when the event is valid and non-action is the outcome;
- technical failure may exclude only the affected task under the frozen rule;
- withdrawal never becomes an unfavorable observation unless the metric definition explicitly says so;
- exclusions are coded before analysis and preserved;
- if sequence balance drops below five usable participants in any sequence, Q00 primary result is `INCONCLUSIVE` unless the pre-registered recovery rule explicitly authorizes a full rerun before outcome inspection.

## Anti-peeking

No primary result is inspected until:
- minimum usable sample is reached or recruitment window closes;
- exclusion log is frozen;
- answer-key/scoring pass is complete;
- data-quality checks pass;
- analysis seed and code commit are frozen.

No sequential stopping for a favorable result.

## Freeze dependencies

Before `PRE_REGISTERED`:
- independent methods reviewer approves this design or a superseding version;
- market-domain reviewer approves scenario realism without seeing participant outcomes;
- exact G comparator state is frozen;
- final scenario/rubric private materials are hashed;
- participant notice/consent is cleared by Q01 authority for the intended research flow;
- assignment seed is generated and frozen;
- analysis code commit is frozen;
- recruitment channels and dates are frozen.
