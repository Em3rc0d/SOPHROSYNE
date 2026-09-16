# Q03 / Q05 Instrumentation Contract

## Purpose

Behavioral evidence must be reproducible from versioned events without unnecessary financial data.

## Event envelope

```yaml
event_id:
event_name:
event_schema_version:
occurred_at_utc:
received_at_utc:
experiment_id:
experiment_version:
participant_id:
session_id:
task_id:
variant_id:
prototype_digest:
source: UI | MODERATOR | SYSTEM
recruitment_cohort:
primary_promotion_geography:
study_language:
study_timezone:
```

Never use name/email/account credentials as participant ID.

## Core events

Study/session: `study_consent_recorded`, `session_started`, `session_ended`.

Task/scoring: `task_started`, `task_answer_submitted`, `task_scored` with scoring-rubric version, confidence, completion time and objective comprehension flags.

Evidence/history: `evidence_item_opened`, `opposing_evidence_opened`, `uncertainty_opened`, `invalidation_opened`, `provenance_opened`, `decision_record_opened`, `decision_record_revisited`.

Repeat use: `qualifying_activity`, `reminder_delivered`, `reminder_opened`, `revisit_classified` with `PROMPTED | UNPROMPTED | AMBIGUOUS` and attribution-rule version.

Pricing: `pricing_exposure_started` with price, currency, billing period, tax/fee presentation, entitlement matrix/copy digest; `pricing_commitment_started`; optional `pricing_commitment_completed`; `pricing_fake_door_disclosed`. Commitment events carry `commitment_friction_rule_version`.

Moat/exposure: `component_exposure_recorded` with `component_id` and `exposure_rule_version`; `workflow_preference_submitted`; `component_reason_coded` with coding-rubric version/reviewer.

## Derived metrics

### Active day
A frozen study-timezone day with at least one meaningful `qualifying_activity`; passive page load does not qualify.

### Multi-day active
Active on at least 3 distinct days in the 14-day E03-C window.

### Unprompted revisit
A qualifying new session on study days 4–14 classified `UNPROMPTED` under the frozen reminder rule.

### Historical revisit
At least one valid `decision_record_revisited` during the observation window.

### Qualified pricing exposure
Participant meets cohort criteria, offer rendered successfully, assigned pricing/entitlement digest is correct, and no preregistered exclusion applied.

### Qualified commitment
A deliberate event beyond a curiosity click satisfying the frozen friction rule; automation/test accounts excluded by preregistered identifiers.

### Component exposure denominator
For each Q05 component, denominator is `eligible_exposed_repeat_users`: eligible repeat users who received a valid `component_exposure_recorded` before the behavior being measured. Participants never exposed because of progressive disclosure are not failures for that component; exposure exclusions remain traceable and reported.

## Data-quality gates

- DQ1: >=99.5% of events required for primary metrics pass schema validation.
- DQ2: primary events use registered prototype digests or are documented deviations.
- DQ3: retries/duplicates are deduplicated by event ID/idempotency rule.
- DQ4: impossible ordering/material clock skew is quarantined.
- DQ5: every primary denominator inclusion/exclusion has one traceable reason.
- DQ6: no session is both prompted and unprompted.
- DQ7: synthetic/test accounts are excluded under frozen identifiers.
- DQ8: component exposure occurs before component-linked outcome for denominator eligibility.

If an instrumentation defect affects >10% of observations required by a primary metric, that metric is `INCONCLUSIVE` unless a preregistered recovery rule resolves validity. It cannot PASS through post-hoc repair.

## Privacy / versioning

Do not log secrets, raw auth headers, full account identifiers, payment-card data, generic free text, or exact holdings without approved necessity. Changing event meaning requires a new schema version. Historical events are interpreted under their generating version.

## Reproducibility

Receipts using telemetry reference event-export digest, schema versions, analysis-code commit, metric-contract version and participant-inclusion/exposure manifest digest.
