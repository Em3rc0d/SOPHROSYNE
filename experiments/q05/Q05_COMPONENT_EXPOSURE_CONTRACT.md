# Q05 Component Eligibility / Exposure / Use Contract

## Status

`CANDIDATE_V1 / READY_FOR_INDEPENDENT_REVIEW / NOT_EVIDENCE`

This contract prevents Q05 from treating "feature existed in the build" as exposure or adoption.

## General denominator invariant

For component Cxx:

```text
eligible_exposed_repeat_user =
  primary cohort eligible
  AND Q03 repeat-user condition true
  AND valid component_eligible event
  AND valid component_exposed event
  AND exposure rule version matches frozen contract
```

Missing exposure data never means "exposed but did not use".

## C01 — supporting/opposing evidence structure

```yaml
eligibility:
  arm: [E, F]
  condition: scenario contains both supporting and opposing evidence
exposure:
  event: component_exposed
  component_id: C01
  rule: evidence structure rendered in a qualifying session
use:
  event: component_used
  qualifying_use_type: EVIDENCE_EXPANDED
adoption_candidate:
  requirement: valid use in >=2 distinct qualifying sessions
```

## C02 — Decision Ledger / historical record

```yaml
eligibility:
  condition: participant has >=1 saved record from an earlier task/session
exposure:
  component_id: C02
  rule: history control rendered while a prior record is available
use:
  qualifying_use_type: DECISION_RECORD_OPENED
repeat_use:
  stronger_event: decision_record_revisited
```

Same-session duplicate opening is not revisit.

## C03 — point-in-time provenance/replay

```yaml
current_prototype_status: NOT_SUFFICIENTLY_INSTRUMENTED
promotion_use: PROHIBITED_FROM_V2_2
required_future_exposure:
  provenance/replay control rendered with valid as_of semantics
required_future_use:
  provenance or replay opened after initial exposure
```

Q05 cannot infer C03 adoption from generic evidence expansion.

## C04 — uncertainty/invalidation

```yaml
eligibility:
  arm: [E, F]
  condition: uncertainty/invalidation surfaces exist for scenario
exposure:
  component_id: C04
  rule: uncertainty and invalidation controls are rendered
use:
  qualifying_use_types: [UNCERTAINTY_OPENED, INVALIDATION_OPENED]
adoption_candidate:
  requirement: qualifying use in >=2 distinct sessions
```

## C05 — progressive explanation depth

```yaml
eligibility:
  arm: [F]
  condition: >=2 depth levels available
exposure:
  component_id: C05
  rule: depth selector rendered
use:
  qualifying_use_type: DEPTH_CHANGED
adoption_candidate:
  requirement: voluntary depth change in >=2 distinct sessions
```

Programmatic/default depth changes do not count.

## C06 — reproducible strategy validation

```yaml
current_prototype_status: NOT_IMPLEMENTED
promotion_use: PROHIBITED_FROM_V2_2
```

No Q05 claim for C06 is allowed from this prototype.

## C07 — longitudinal decision history

```yaml
eligibility:
  condition: >=2 prior valid records exist
exposure:
  component_id: C07
  rule: longitudinal history is rendered after eligibility
use:
  qualifying_use_type: HISTORICAL_RECORD_REVISITED
adoption_candidate:
  requirement: use occurs after local study day 7
```

## C08 — rights-aware derived intelligence

```yaml
current_prototype_status: NOT_IMPLEMENTED_AS_PROMOTABLE_SURFACE
promotion_use: PROHIBITED_FROM_V2_2
dependency: Q02
```

Generic labels such as OBSERVED or STALE are not evidence of C08.

## Event integrity

Every component event must include:
- participant/session/task identity;
- prototype version/digest;
- component ID;
- eligibility/exposure rule version;
- stable exposure instance ID;
- source;
- timestamp.

Duplicate retries are deduplicated by event ID/exposure instance ID.

## Q05 v2.2 allowed interpretation

Instrumented enough for rehearsal:
`C01, C02, C04, C05, C07`.

Not eligible for promotable component-level conclusion from this artifact:
`C03, C06, C08`.

A Q05 aggregate moat conclusion cannot be manufactured by averaging only the instrumented components.

## Reopen triggers

Re-freeze this contract when:
- component UI/eligibility materially changes;
- event meaning changes;
- Q03 persona/repeat-use definition changes;
- Q02 changes C08 rights semantics;
- a new prototype exposes C03/C06/C08;
- reminder/assignment logic changes exposure opportunities.
