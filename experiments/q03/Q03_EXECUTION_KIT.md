# Q03 Execution Kit — User Value, Repeat Use and WTP

## Status

`READY_FOR_REHEARSAL / BLOCKED_FOR_PROMOTABLE_EXECUTION / NOT_EVIDENCE`

This kit operationalizes `Q03_PREREGISTRATION.md`. It does not manufacture participants, commitment events or paid demand.

Candidate prototype:
- path: `experiments/research-prototype-v1/index.html`;
- semantic version: `research-prototype-v2.3.0`;
- candidate branch: `research/q00-market-scenario-hardening`;
- Git blob identity: `UNFROZEN_UNTIL_FINAL_REVIEW_COMMIT`.

The prototype is suitable for rehearsal and instrumentation review only. Its `prototype_digest` event field intentionally remains `UNFROZEN_REHEARSAL` until the final material set is independently reviewed and frozen before a promotable run.

## 1. Cohort boundary

```yaml
primary_population: adults 18+
promotion_geography: Peru
minimum_primary_discovery_n: 20
minimum_comprehension_n: 30
minimum_repeat_use_n: 20
pricing_stage_1_exposures_per_band: 40
pricing_stage_2_exposures_per_band: 100
```

No participant is asked to place a real trade. Research uses paper/historical/synthetic contexts only.

## 2. E03-A interview script

Before showing SOPHROSYNE, ask the participant to reconstruct one recent investment-research task:
1. What triggered the research?
2. Which sources/tools did you open, and in what order?
3. What took the most time?
4. Where did sources disagree?
5. How did you decide what was trustworthy/current?
6. Could you later reconstruct why you reached the conclusion you did?
7. What workaround did you use?
8. What tools/services do you already pay for or spend meaningful time on?
9. What did you do when evidence was insufficient?
10. What would have made the task materially easier?

Interviewer must not mention evidence graphs, Decision Ledger, “AI”, or desired product features before behavioral reconstruction.

### Coding form

```text
participant_id
eligibility_pass
peru_primary_cohort
R1_recurring_information_synthesis_pain
R2_observable_manual_workaround
R3_conflicting_information_problem
R4_difficulty_reconstructing_prior_reasoning
R5_pays_or_spends_meaningful_time
alternative_problem_framing
source_count
workflow_minutes_estimate
notes_ref
```

`YES` requires a concrete behavior/example, not agreement with a hypothetical statement.

## 3. E03-B matched comprehension test

Use two matched cases with the same underlying facts.

Treatment must expose:
- market state;
- supporting evidence;
- opposing evidence;
- uncertainty/staleness;
- invalidation condition.

Control must contain equivalent facts in a conventional dense format.

Counterbalance order and hide which interface is the candidate product.

### Instrumentation

```text
participant_id
case_id
condition
order_index
started_at
submitted_at
comprehension_score_0_100
confidence_pct
calibration_gap
contradiction_detected
stale_or_missing_detected
observation_vs_inference_correct
technical_interruption_seconds
```

The scoring answer key must be frozen before the first participant result is inspected.

## 4. Prototype instrumentation readiness

The candidate prototype currently emits the following directly in-browser:
- `session_started` / `session_ended`;
- `task_started` / `task_answer_submitted`;
- `evidence_item_opened` and explicit opposing-evidence events;
- uncertainty / invalidation events;
- decision record create/open events;
- cross-session-only `decision_record_revisited`;
- component eligibility/exposure/use events for instrumented surfaces;
- completion time, workload rating and help-requested fields;
- pseudonymous participant id when supplied by the study launcher.

Canonical rehearsal/event-validation artifacts:
- `experiments/q03/q03_event.schema.json`;
- `experiments/q03/validate_event_export.py`;
- `experiments/q03/Q03_14_DAY_RUNBOOK.md`.

Still missing for promotion-grade E03-C:
- approved consent event/version and privacy retention authority;
- server/research-pipeline `received_at_utc`;
- frozen `prototype_digest`;
- neutral reminder delivery/open instrumentation and attribution classification;
- server/analysis-derived `qualifying_activity` / `revisit_classified`;
- test-account/recruitment cohort and Peru eligibility ingestion under the approved protocol;
- 14-day real participant observations.

## 5. E03-C 14-day event contract

Canonical longitudinal semantics: `experiments/q03/Q03_14_DAY_RUNBOOK.md`.

Minimum current prototype events:

```text
session_started
task_started
task_answer_submitted
evidence_item_opened
opposing_evidence_opened
uncertainty_opened
invalidation_opened
decision_record_created
decision_record_opened
decision_record_revisited
component_eligible
component_exposed
component_used
session_ended
```

Future promotion-grade reminder pipeline additionally requires `reminder_delivered` / `reminder_opened` (or a superseding frozen naming contract) before E03-C execution.

Every event records:

```text
participant_id
session_id
event_name
event_at
prototype_version
source: DIRECT | REMINDER | OTHER
record_id_if_applicable
component_id_if_applicable
```

Rules:
- reminders must be neutral;
- revisits directly attributable to a reminder inside the frozen attribution window do not count as unprompted revisits;
- do not award compensation for returning, choosing a paid band, or producing favorable feedback.

## 6. E03-D pricing/commitment execution

Until Q01 clears the exact commercial flow, **no real charge is permitted by this research protocol**.

Allowed research-intent flow:
1. show the exact frozen feature/price proposition;
2. require a deliberate high-friction commitment step;
3. before any transaction would occur, disclose that the study is not processing a charge;
4. record the commitment event and denominator;
5. preserve the exact copy/version shown.

Candidate bands from the preregistration remain hypotheses:
- Free;
- USD 12/month;
- USD 19/month;
- USD 39/month exploratory advanced tier.

Do not change a band after seeing results without creating a new experiment version.

### Pricing event schema

```text
participant_id
price_band
qualified_exposure
commitment_started
commitment_completed
research_disclosure_seen
compensation_cohort
copy_version
exclusion_reason
```

## 7. E03-E historical record diagnostic

Use immutable `as_of` records. Later information is shown separately.

Measure:
- reconstruction of the original reasoning;
- identification of later invalidation/new evidence;
- voluntary use of historical audit trail;
- confusion between historical and hindsight information.

Never rewrite the historical record after later outcomes are known.

## 8. Recruitment integrity

Use at least two recruitment channels where practical. Record channel per participant. Exclude:
- minors;
- duplicate participants;
- participants who saw answer keys;
- participants whose instrumentation is unusable for the primary metric;
- project insiders from the promotable primary cohort.

Do not exclude negative participants post hoc.

## 9. Required immutable outputs

Each sub-experiment must produce:
- frozen manifest/digest;
- recruitment log;
- raw/de-identified measurements where legally permitted;
- exclusion log;
- analysis artifact;
- adverse/conflicting evidence;
- terminal sub-experiment result;
- independent-review note.

## 10. Current execution blockers

```yaml
adult_peru_participants: NOT_RECRUITED
prototype_semantic_version: research-prototype-v2.3.0
prototype_instrumentation: READY_FOR_REHEARSAL
prototype_digest: NOT_FROZEN
reminder_attribution_pipeline: NOT_IMPLEMENTED
fourteen_day_observation: NOT_STARTED
consent_privacy_review: REQUIRES_Q01
paid_charge_flow: PROHIBITED_UNTIL_Q01
independent_reviewer: MISSING
q03_status: OPEN
```

Q03 may not be marked `CLOSED_PASS` or `CLOSED_CONDITIONAL` from interview intentions, demo enthusiasm, synthetic users or assistant-generated responses.