# Q03 Instrumentation Contract

## Purpose

Q03 decisions depend on behavior, not only interviews. This contract defines the minimum event model needed to reproduce E03-B, E03-C, E03-D and supportive E03-E measurements without collecting unnecessary financial data.

Analytics events are experiment evidence. They must be versioned, attributable to the exact prototype variant and protected from post-hoc semantic changes.

---

## Event envelope

Every event contains:

```yaml
event_id:
event_name:
event_schema_version:
occurred_at_utc:
received_at_utc:
experiment_id:
experiment_version:
participant_id:        # pseudonymous
session_id:
task_id:
variant_id:
prototype_digest:
source: UI | MODERATOR | SYSTEM
recruitment_cohort:
```

Never use email/name/account credentials as `participant_id`.

---

## Common optional context

```yaml
context:
  case_id:
  scenario_as_of:
  reminder_id:
  reminder_attribution_window_active:
  comparator_id:
  price_band_id:
  component_id:
  client_event_sequence:
```

Do not place raw portfolio positions, account identifiers or credentials in generic context.

---

# Required events

## Study/session lifecycle

### `study_consent_recorded`

Fields:
```yaml
consent_version:
consent_digest:
```

### `session_started`

### `session_ended`

Fields:
```yaml
end_reason: COMPLETED | USER_LEFT | TECHNICAL_FAILURE | MODERATOR_STOP | OTHER
```

---

## Task lifecycle

### `task_started`

Fields:
```yaml
task_type:
case_id:
```

### `task_answer_submitted`

Fields:
```yaml
answer_ref:
confidence_percent:
completion_ms:
```

Answers themselves may live in a separate research artifact rather than analytics payloads.

### `task_scored`

Server/research-pipeline event only.

```yaml
score_percent:
scoring_rubric_version:
contradiction_detected_correctly:
staleness_detected_correctly:
observation_inference_distinction_correct:
```

The scoring rubric is frozen before outcomes are inspected.

---

## Evidence workflow

### `evidence_item_opened`

```yaml
evidence_role: SUPPORTING | OPPOSING | NEUTRAL | UNKNOWN
```

### `opposing_evidence_opened`

Explicit event for Q03/Q05 diagnostics.

### `uncertainty_opened`

### `invalidation_opened`

### `provenance_opened`

### `decision_record_opened`

```yaml
record_age_class: CURRENT | HISTORICAL
```

### `decision_record_revisited`

Emitted only when the participant has previously opened the same logical record in an earlier qualifying session.

---

## Repeat-use events

### `qualifying_activity`

Derived/server-side event identifying activity that counts toward an active day.

Rules:
- passive page load alone does not qualify;
- at least one meaningful research action is required;
- exact qualifying action set is frozen before E03-C starts.

### `reminder_delivered`

```yaml
reminder_id:
channel:
```

### `reminder_opened`

```yaml
reminder_id:
```

### `revisit_classified`

Server/analysis event.

```yaml
classification: PROMPTED | UNPROMPTED | AMBIGUOUS
attribution_rule_version:
```

`AMBIGUOUS` is excluded from the primary unprompted-revisit numerator but remains reported.

---

## Pricing events

### `pricing_exposure_started`

```yaml
price_band_id:
price_displayed:
currency:
feature_matrix_version:
pricing_copy_digest:
```

One participant may not silently count as multiple independent exposures to different paid bands unless the experiment explicitly uses and models repeated exposure.

### `pricing_details_viewed`

Diagnostic only.

### `pricing_commitment_started`

Primary high-friction intent event.

Must represent a deliberate action beyond a curiosity click.

### `pricing_commitment_completed`

Use only when a legally/operationally appropriate real transaction or equivalent validated commitment exists.

### `pricing_fake_door_disclosed`

Records the point where the participant is told no charge/transaction will occur in a non-deceptive fake-door design.

---

## Competitive/moat events

### `workflow_preference_submitted`

```yaml
selected_workflow:
reason_text_ref:
```

### `component_reason_coded`

Research-pipeline event.

```yaml
component_id:
coding_rubric_version:
reviewer_id:
```

Free-text preference reasons are stored separately with appropriate privacy controls.

---

# Derived metric definitions

Metric definitions are versioned analysis code/contracts, never ad-hoc dashboard calculations.

## Active day

A UTC/local-study day containing at least one `qualifying_activity` event under the frozen experiment rule.

The study manifest must freeze timezone/day-boundary semantics before start.

## Multi-day active participant

Participant with active days `>= 3` during the E03-C 14-day observation window.

## Unprompted revisit

A qualifying new session after day 3 classified `UNPROMPTED` by the frozen reminder-attribution rule.

The default rule should conservatively classify sessions near reminder delivery as prompted rather than inflating organic return.

## Evidence/history revisit

Participant emits `decision_record_revisited` at least once during the observation window.

## Qualified pricing exposure

A `pricing_exposure_started` event where:
- participant meets the pre-registered Q03 cohort definition;
- page/offer rendered successfully;
- price/feature matrix matches the assigned band digest;
- participant had not already been invalidated by experiment exclusion criteria.

## Qualified commitment

A valid `pricing_commitment_started` event satisfying the pre-registered friction requirement and not generated by automation/test accounts.

---

# Data quality gates

Before a receipt uses telemetry:

### DQ1 — event schema validity

`>= 99.5%` of events required for primary metrics must pass schema validation.

### DQ2 — prototype integrity

No primary-metric event may come from an unregistered `prototype_digest` unless explicitly treated as a protocol deviation.

### DQ3 — duplicate control

Duplicate/retry events must be deduplicated by `event_id` or documented idempotency logic.

### DQ4 — clock sanity

Events with impossible ordering or material clock skew are quarantined and reported.

### DQ5 — participant denominator integrity

Every participant included/excluded from a primary denominator has one explicit reason traceable to the pre-registered rules.

### DQ6 — reminder attribution integrity

A participant/session cannot be counted as both prompted and unprompted.

### DQ7 — test-account exclusion

Synthetic/test events are marked and excluded through pre-registered identifiers, never by eyeballing results later.

If an instrumentation defect affects more than 10% of observations needed by an E03-C primary metric, that metric cannot PASS without a new experiment version or a pre-registered recovery rule.

---

# Privacy / logging rules

Analytics payloads must not contain:
- passwords/tokens/secrets;
- raw auth headers;
- broker/exchange account numbers;
- exact portfolio holdings unless a dedicated approved study field requires them;
- free-text notes copied into generic logs;
- payment-card data.

Experiment logs use participant IDs and event metadata only.

---

# Event-versioning rule

Changing the meaning of an event requires a new `event_schema_version`.

Examples requiring a new version:
- what counts as `qualifying_activity`;
- reminder attribution window;
- commitment friction definition;
- component coding rubric;
- scoring rubric semantics.

Historical events are interpreted under the version that generated them, not silently reclassified under new semantics.

---

# Analysis reproducibility

Every Q03/Q05 receipt relying on telemetry references:

```yaml
event_export_digest:
event_schema_versions:
analysis_code_commit:
metric_contract_version:
participant_inclusion_manifest_digest:
```

Given the same exported event corpus and analysis code, primary metric numerators/denominators must reproduce exactly.

---

## Final invariant

> If we cannot reconstruct exactly why a participant counted in a numerator or denominator, the metric is not promotion-grade evidence.
