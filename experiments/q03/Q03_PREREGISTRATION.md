# Q03 Pre-Registration — User Value, Repeat Use and Willingness to Pay

## Purpose

Q03 asks whether the candidate SOPHROSYNE workflow solves a repeated problem strongly enough to justify an MK1 build and whether some target users show credible willingness to commit at a commercially plausible price.

This document freezes **product decision gates**, not population-level scientific claims. Small early-stage samples are used to decide whether to continue, narrow, pivot or stop. If the minimum usable sample is not reached, the result is `INCONCLUSIVE`.

No participant is asked to place a real trade or make an investment decision because of the study.

Primary target participants are adults (18+) who independently research or manage their own investments.

Canonical experiment template: `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`.
Semantic normalization: `docs/validation/CANONICAL_VALIDATION_SPEC.md`.

Initial promotable MK1 geography is **Peru**. Evidence from other LATAM/global participants may be exploratory or supportive, but it cannot silently substitute for Peru evidence in the final promotion decision.

---

# Shared qualification contract

## Primary candidate cohort

A participant qualifies for the primary cohort when all are true:
- age 18+;
- self-directed or materially involved in their own investment research;
- has evaluated or managed at least one investment position in the previous 90 days;
- uses at least two information sources/tools when researching decisions;
- is not participating solely because they work on SOPHROSYNE or already know the intended hypothesis.

For promotion to the initial Peru MK1, the primary promotable cohort must be Peru-based/Peru-market-eligible under the frozen Q01 eligibility profile, or the manifest must pre-register a separate Peru confirmation gate before aggregate Q03 can close promotably.

## Secondary exploratory cohort

May include more experienced systematic/technical users and/or non-Peru LATAM/global users. Their evidence is reported separately unless the manifest explicitly pre-registers pooled exploratory analysis.

Exploratory participants do not count toward Peru primary minimums merely because their behavior appears favorable.

## Compensation integrity

Participant compensation:
- may compensate time/participation;
- must not depend on desired behavior, preference, return frequency, willingness-to-pay, commitment outcome or “correct” product sentiment;
- must be frozen/disclosed by cohort before outcome inspection;
- must be analyzed separately when its structure could plausibly distort economic-intent metrics.

A pricing/commitment cohort whose incentive structure materially contaminates willingness-to-pay cannot be the sole basis for a promotable paid-band result.

## Exclusions

- professional users whose workflow is institutionally mandated and not comparable to the target retail workflow, unless enrolled as a separate exploratory cohort;
- participant cannot complete the study language/materials;
- instrumentation failure prevents primary measures;
- duplicate participant;
- participant saw answer keys or internal scoring criteria before task completion.

Post-hoc exclusion for inconvenient outcomes is prohibited.

---

# E03-A — Behavioral Discovery

## Question

Does the candidate target cohort show a repeated, behaviorally observable problem around turning fragmented market information into an understandable, reviewable decision context?

## Sample

```yaml
target_n: 28-32
minimum_usable_primary_n: 20
primary_cohort_target: 20-24
secondary_exploratory_target: 4-8
promotion_geography: Peru
```

Recruit across more than one source/channel where practical to reduce single-community bias.

Exploratory/non-Peru participants are not used to fill the 20-participant primary minimum unless a different pooling rule was pre-registered before any outcome inspection and remains compatible with the promotion geography.

## Interview rule

Observe the participant's current workflow before showing SOPHROSYNE.

Do not lead with features such as “Would evidence graphs help you?”. Ask them to reconstruct a recent research task:
- what triggered it;
- sources/tools used;
- sequence of actions;
- time/effort;
- what they found confusing;
- how they reconciled conflicting information;
- how they later remembered why they made a decision;
- what they pay for now.

## Primary measures

For each participant code, using a pre-defined rubric:

```text
R1 recurring_information_synthesis_pain       YES/NO
R2 observable_manual_workaround               YES/NO
R3 conflicting_information_problem            YES/NO
R4 difficulty_reconstructing_prior_reasoning   YES/NO
R5 pays_or_spends_meaningful_time_on_workflow  YES/NO
```

A “YES” requires concrete behavioral evidence/examples, not agreement with a hypothetical question.

## PASS rule

`CLOSED_PASS` evidence contribution when, among at least 20 usable primary-cohort participants:
- `R1 YES >= 60%`; and
- `R2 YES >= 40%`; and
- at least two of `R3/R4/R5` are `YES >= 35%`; and
- no single alternative problem framing explains the observed pain more coherently in `> 50%` of usable primary participants.

These are continuation thresholds, not claims that 60% of all retail investors share the problem.

## CONDITIONAL rule

Use `CLOSED_CONDITIONAL`/narrowing evidence when the PASS pattern is strong in one identifiable promotable cohort but not across the originally proposed cohort.

Required output: a narrower persona definition and new cohort-specific follow-up plan.

## STOP rule

Current persona/wedge receives stop evidence if:
- `R1 YES < 35%`; and
- `R2 YES < 25%`;

with at least 20 usable primary-cohort participants and no major recruitment/instrumentation failure.

## INCONCLUSIVE

Anything between defined bands, below minimum primary sample, or materially contaminated by recruitment/compensation/instrumentation issues.

---

# E03-B — Translator Comprehension Test

## Question

Does the SOPHROSYNE Translator/Evidence representation improve decision-context comprehension or materially reduce workflow friction without increasing unjustified confidence?

## Design

Within-participant, counterbalanced comparison using the same underlying evidence represented in two formats:
- `TREATMENT`: candidate SOPHROSYNE Translator/Evidence View;
- `CONTROL`: conventional dense market-information presentation containing equivalent underlying facts.

Use at least two matched cases with different evidence patterns so one scenario does not determine the result.

Do not label one interface as “AI” or “improved”.

## Sample

```yaml
target_usable_n: 36
minimum_usable_n: 30
allocation: counterbalanced order
promotion_geography: Peru primary or explicit Peru-confirmation stratum
```

## Primary measures

### M1 — objective comprehension

Score 0–100 using a frozen answer key covering:
- observable market state;
- supporting evidence;
- contradicting evidence;
- uncertainty/staleness;
- what would invalidate the represented scenario.

### M2 — task completion time

Time from task start to final submitted answer, excluding documented technical interruption.

### M3 — confidence calibration gap

`abs(self_reported_confidence_percent - correctness_percent)`.

Lower is better.

## Secondary measures

- detects at least one contradicting item;
- detects stale/missing evidence;
- correctly distinguishes observation from inference;
- NASA-TLX-style workload subset or another pre-registered cognitive-effort measure if used;
- qualitative failure reason.

## PASS rule

Pass if either path A or B is satisfied **and** the calibration guardrail passes.

### Path A — comprehension gain

- treatment mean comprehension is at least `+8 percentage points` versus control; and
- treatment median completion time is no more than `110%` of control median.

### Path B — efficiency gain with non-inferior comprehension

- treatment mean comprehension difference is not worse than `-5 percentage points`; and
- treatment median completion time is `<= 80%` of control median.

### Calibration guardrail

Treatment mean calibration gap may not worsen by more than `5 percentage points` versus control.

## STOP rule

Stop/rework the representation if either:
- treatment mean comprehension is worse by `>= 10 percentage points`; or
- mean confidence increases by `>= 10 percentage points` while mean correctness falls by `>= 5 percentage points`.

## CONDITIONAL

If only one major case type or one participant cohort passes, narrow the wedge/use case and re-register a targeted follow-up.

## INCONCLUSIVE

Minimum sample not reached, instrumentation invalid, Peru confirmation absent for promotion, or results fall between the declared decision regions.

---

# E03-C — 14-Day Repeat-Use Proxy

## Question

After initial novelty, do qualified users voluntarily return to the decision-intelligence workflow and use evidence/history features over multiple days?

## Sample

```yaml
target_enrolled_n: 28
minimum_instrumented_n: 20
observation_window_days: 14
promotion_geography: Peru primary or explicit Peru-confirmation stratum
```

Participants may receive onboarding and neutral availability reminders. A session entered directly from a reminder within the pre-registered attribution window is **not** counted as an unprompted revisit.

## Prototype boundary

The prototype provides research/decision-context tasks and paper/historical material only. It does not instruct participants to make real-money trades.

## Primary measures

```text
M1 multi_day_active_rate
  = participants active on >=3 distinct days / instrumented participants

M2 unprompted_revisit_rate
  = participants with >=1 qualifying unprompted revisit after day 3 / instrumented participants

M3 evidence_history_revisit_rate
  = participants who revisit a prior Decision Record/evidence trail at least once / instrumented participants
```

## PASS rule

All must hold:
- `M1 >= 50%`;
- `M2 >= 35%`;
- `M3 >= 30%`.

Additionally, no instrumentation defect may explain more than 10% of missing primary events.

## CONDITIONAL rule

Conditional/narrowing evidence when:
- `M1 >= 40%`; and
- at least one of M2/M3 meets its PASS threshold;

but full PASS is not reached.

Freeze which cohort/use-case generated the repeat use and do not generalize beyond it.

## STOP rule

Stop/rework the current repeat-use hypothesis if either:
- `M1 < 25%`; or
- `M2 < 15%`;

with at least 20 valid instrumented participants.

## Secondary measures

- median active days;
- evidence expansion actions;
- uncertainty/invalidation interactions;
- number of prior-record revisits;
- self-reported replacement vs complement of existing workflow;
- abandonment reason.

These diagnose behavior; they do not override failed primary gates.

---

# E03-D — Pricing / Commitment Test

## Question

After users understand the product, does at least one plausible paid price produce non-trivial high-friction commitment evidence?

## Safety/legal boundary

Until Q01 permits the actual commercial charging flow, this experiment **must not execute a real charge**. A high-friction checkout simulation/fake-door may be used only if non-deceptive and appropriately disclosed at the point no transaction occurs, consistent with the Q01-reviewed research posture.

A real paid pilot is stronger evidence only after the exact paid/subscription/payment flow is legally and operationally authorized.

Do not imply investment returns or personalized financial outcomes.

## Price bands

Initial hypotheses:
- Free;
- USD 12/month;
- USD 19/month;
- USD 39/month exploratory advanced tier.

The exact currency/localized presentation used in an experiment must be frozen in its manifest.

## Two-stage design

### Stage 1 — signal screen

Purpose: eliminate obviously weak price bands, not close Q03.

```yaml
minimum_qualified_exposures_per_paid_band: 40
```

Primary action = deliberate high-friction commitment event such as checkout initiation after viewing exact feature/price details.

A simple pricing-page view or button curiosity click is insufficient.

### Stage 2 — closure test

Run only for one or two candidate paid bands selected by the Stage-1 rule defined before inspection.

```yaml
minimum_qualified_exposures_per_tested_band: 100
```

## Primary metric

`qualified_commitment_rate = high_friction_commitments / qualified_price_exposures`.

Report exact numerator/denominator and a Wilson confidence interval; do not report only percentages.

## Compensation/economic-intent rule

The participant must not receive compensation contingent on:
- selecting a paid band;
- initiating commitment;
- saying they would pay;
- completing a checkout-like action;
- returning to the product.

If general participation compensation could plausibly affect economic intent, report the cohort separately and do not use it as the sole promotable pricing evidence without an uncontaminated confirmation cohort.

## PASS contribution

A paid band supplies promotable pricing evidence when:
- observed qualified commitment rate is `>= 8%`; and
- the lower bound of the two-sided 80% Wilson interval is `> 3%`;
- the cohort matches the Q03 candidate persona and promotion geography;
- no misleading investment-performance claim was used to obtain commitment;
- the economic-intent evidence is not solely derived from a materially contaminated incentive structure.

The 80% interval is a pragmatic early-product uncertainty check, not a claim of population certainty.

## CONDITIONAL

Observed rate `>= 5%` but fails the PASS uncertainty rule: retain price as a hypothesis, not a validated paid band.

## STOP for a tested band

Observed commitment rate `< 3%` with at least 100 qualified exposures: reject that band/offer configuration for the tested cohort unless a new materially different offer is pre-registered.

## INCONCLUSIVE

Anything else, insufficient qualified exposures, unresolved legal/research-flow ambiguity or materially contaminated economic-intent evidence.

---

# E03-E — Historical Decision Record Diagnostic

## Purpose

This is supportive evidence for Q03/Q05, not an independent Q03 closure gate.

## Sample

At least 15 participants drawn from E03-C when possible.

## Task

Participants inspect a historical `as_of` Decision Record and later information without allowing the historical record to be rewritten.

Measure:
- correct reconstruction of why the original record said what it said;
- recognition of later invalidation/new evidence;
- whether immutable history helps audit/review;
- whether the participant voluntarily revisits the history.

## Support threshold

Strong supportive evidence if:
- `>= 70%` correctly reconstruct the original reasoning from the record; and
- `>= 50%` report and behaviorally demonstrate at least one useful historical-review action.

Failure here may weaken the Decision Ledger/moat hypothesis but cannot be hidden by passing other Q03 experiments.

---

# Q03 aggregate decision

Q03 is reviewed only after E03-A, E03-B, E03-C and E03-D have final receipts. E03-E is diagnostic/supportive.

For initial MK1 promotion, the aggregate evidence must satisfy the Peru geography rule; non-Peru evidence may remain supportive but cannot close the Peru demand lock alone.

## CLOSED_PASS

All of:
- E03-A `CLOSED_PASS` contribution;
- E03-B PASS under its pre-registered rule;
- E03-C PASS under its pre-registered rule;
- at least one paid band in E03-D contributes PASS evidence;
- required Peru promotion evidence exists;
- no unresolved P0/P1 contradiction with Q01/Q02;
- no severe trust/calibration failure contradicts the product thesis.

## CLOSED_CONDITIONAL

May be used when evidence consistently supports a **narrower** persona/use case or a learning-wedge MK1, provided:
- E03-A is at least conditional;
- E03-B is not STOP;
- E03-C is at least conditional;
- E03-D provides at least non-trivial conditional commitment evidence;
- Peru promotion scope remains supported;
- the narrowing is explicitly frozen in the bootstrap profile.

## PIVOT_REQUIRED

Use when observed users repeatedly value a materially different workflow/persona than the candidate thesis.

## STOP_CURRENT_CONFIGURATION

Use when repeated behavior shows weak problem intensity, poor comprehension/trust outcome, poor repeat use and weak commitment under plausible tested variants.

## INCONCLUSIVE

Insufficient primary samples, missing Peru confirmation, contaminated/invalid measurement, unresolved material contradictions, or mixed results that do not satisfy the declared aggregate rules.

---

## Q03 frozen outputs

A promotable Q03 receipt must freeze:

```yaml
primary_persona_version:
qualified_cohort_definition:
promotion_geography: Peru
jtbd_version:
wedge_version:
required_trust_features:
translator_representation_version:
repeat_use_profile:
initial_pricing_hypothesis:
pricing_evidence_type: RESEARCH_INTENT | AUTHORIZED_PAID_PILOT
rejected_price_bands_or_offers:
validated_failure_modes:
experiment_receipt_refs:
```

These values feed `MK1_BOOTSTRAP_PROFILE`.
