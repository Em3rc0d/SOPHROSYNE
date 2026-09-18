# Q03 14-Day Repeat-Use Runbook

## Status

`READY_FOR_Q01_AND_INDEPENDENT_REVIEW / DO_NOT_START YET`

This runbook freezes the internal semantics of E03-C. It does not authorize collection until the consent/privacy flow is approved and the prototype digest is frozen.

## Study clock

```yaml
study_timezone: America/Lima
day_boundary: local calendar day in America/Lima
window_length: 14 local calendar days
day_0: enrollment + first qualifying session
primary_observation_days: 0-13 inclusive
```

UTC timestamps remain stored in the event envelope, but active-day classification uses the frozen study timezone.

## Primary behavioral definitions

### Qualifying activity

A session counts as meaningful only when at least one of the following valid events occurs after `session_started`:
- `task_answer_submitted`;
- `evidence_item_opened`;
- `uncertainty_opened`;
- `invalidation_opened`;
- `decision_record_created`;
- `decision_record_opened` for a historical record.

Passive page load alone never qualifies.

### Active day

One local study day with at least one qualifying activity.

### Multi-day active participant

`>= 3` active days during the 14-day window.

### Historical revisit

`decision_record_revisited` may be emitted only when:
- the record was created in an earlier session;
- the record identity is stable;
- the opening occurs in a later qualifying session.

Opening the same record twice in one session is not a revisit.

## Reminder policy

Primary organic-use measurement is protected from reminder inflation.

```yaml
days_0_to_6:
  reminders: none
day_8:
  neutral_reminder: one
day_12:
  neutral_reminder: optional_secondary_only
```

The day-12 reminder is disabled by default and may be activated only before preregistration.

Candidate neutral reminder:

> Tienes disponible tu historial de investigación del estudio. Si deseas, puedes revisarlo o continuar con un nuevo caso. No es necesario hacerlo para recibir compensación ni para completar el estudio.

Final wording requires Q01/consent approval.

## Reminder attribution

For each delivered reminder:

```text
0h <= session_start - reminder_delivered_at < 24h   => PROMPTED
24h <= delta < 48h                                  => AMBIGUOUS
delta >= 48h                                        => eligible UNPROMPTED
session before first reminder                       => eligible UNPROMPTED
```

A session cannot be both prompted and unprompted.

Primary unprompted-return metric:
- qualifying session after local study day 3;
- classification `UNPROMPTED`;
- valid telemetry;
- participant still eligible.

`AMBIGUOUS` remains reported and is excluded from the primary unprompted numerator.

## Primary repeat-use metrics

```yaml
M1_multi_day_active_rate:
  numerator: participants with >=3 active days
  denominator: eligible enrolled participants with valid primary telemetry

M2_unprompted_revisit_rate:
  numerator: participants with >=1 UNPROMPTED qualifying session after day 3
  denominator: eligible enrolled participants with valid primary telemetry

M3_historical_record_revisit_rate:
  numerator: participants with >=1 valid cross-session decision_record_revisited
  denominator: eligible participants with at least one prior record available for revisit
```

Non-returners remain in the denominator where telemetry integrity establishes that absence of activity is observable.

## Compensation isolation

Compensation may not depend on:
- number of return sessions;
- reminder opening;
- willingness to pay;
- favorable feedback;
- choosing SOPHROSYNE;
- simulated market outcomes.

If completion compensation requires a final debrief, the base participation amount and completion conditions must be frozen before recruitment so repeated use is not implicitly purchased.

## Pricing isolation

E03-D pricing/commitment exposure occurs:
- after day 14; or
- in a separately randomized cohort.

It is never inserted into the primary organic repeat-use window if doing so can materially change return behavior.

## Telemetry data quality

Promotion-grade E03-C requires:
- frozen prototype digest;
- approved consent digest;
- pseudonymous participant ID;
- event-schema version;
- server/research-pipeline receive timestamp or equivalent independently retained receipt;
- no known >10% loss for events required by a primary metric;
- explicit test-account exclusion;
- deduplication by event ID;
- clock-order validation;
- recruitment/cohort classification.

The current browser-only prototype is rehearsal-ready but not promotion-grade collection.

## Loss / corruption rules

### Local/browser data loss

If browser-local events are the only copy and a participant clears storage:
- do not reconstruct activity from memory/interview;
- mark the affected telemetry interval `UNRECOVERABLE`;
- apply the frozen denominator rule;
- if >10% of primary participants have unrecoverable intervals, affected metric is `INCONCLUSIVE`.

### Collector outage

If a future approved research collector is used:
- client retains an idempotent local queue until acknowledged;
- event IDs remain stable across retries;
- duplicate acknowledgements are harmless;
- outage/recovery is logged;
- no silently invented receive timestamps.

### Clock anomaly

Events with impossible order, time travel across session bounds or material client clock skew are quarantined. They are not silently reordered.

## 14-day operational checklist

Before enrollment:
- Q01 research consent/privacy clearance;
- independent reviewer;
- prototype digest frozen;
- event schema frozen;
- reminder copy/schedule frozen;
- participant inclusion manifest frozen;
- recruitment channels frozen;
- collector/export retention path tested with synthetic IDs;
- deletion/withdrawal procedure rehearsed.

During run:
- no aggregate outcome dashboard for investigators involved in recruitment;
- monitor only operational integrity, not directional primary results;
- record outages/deviations;
- do not change reminder schedule.

After window:
- close recruitment;
- freeze exclusion/deviation log;
- freeze event export digest;
- execute DQ1-DQ9;
- only then calculate primary metrics.

## Abort / rerun

Abort or mark affected result `INCONCLUSIVE` if:
- reminders are sent outside the frozen schedule to >10% of primary cohort;
- primary telemetry loss exceeds the frozen tolerance;
- participant IDs cannot be deterministically deduplicated;
- compensation is changed based on observed return behavior;
- prototype semantics materially change during the cohort without a preregistered versioning rule;
- consent/privacy authority is invalidated.
