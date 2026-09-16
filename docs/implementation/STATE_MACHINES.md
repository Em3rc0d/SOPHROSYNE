# MK1 State Machines

State transitions are explicit domain rules. Direct status assignment outside the owning module is prohibited.

## Evidence

```text
RECEIVED
  -> NORMALIZED
  -> VALIDATED
  -> ACTIVE
  -> STALE
  -> EXPIRED

RECEIVED/NORMALIZED/VALIDATED
  -> QUARANTINED

ACTIVE/STALE
  -> SUPERSEDED
```

Rules:
- `QUARANTINED` evidence is never user-visible as authoritative evidence.
- `STALE` may remain visible only with stale labeling and cannot satisfy freshness-critical gates.
- `SUPERSEDED` remains auditable.

## MarketState

```text
PENDING -> COMPUTING -> READY
                     -> DEGRADED
                     -> NO_CONCLUSION
                     -> FAILED
```

`READY` requires all mandatory dimensions for the selected state profile. `DEGRADED` is allowed only when missing dimensions are non-critical and explicitly surfaced.

## Scenario

```text
DRAFT -> VALIDATED -> ACTIVE -> INVALIDATED
                    -> EXPIRED
                    -> SUPERSEDED
```

A scenario may not become `ACTIVE` without supporting evidence, contradicting-evidence evaluation and at least one invalidation rule or an explicit `NOT_APPLICABLE` rationale approved by schema.

## RiskAssessment

```text
PENDING -> READY
        -> DEGRADED
        -> NOT_EVALUABLE
        -> FAILED
```

Risk cannot be promoted from `NOT_EVALUABLE` by scenario/model confidence.

## Strategy

```text
DRAFT -> VALIDATED -> APPROVED -> ARCHIVED
          |             |
          v             v
       REJECTED       SUSPENDED
```

Each edit after approval creates a new immutable `StrategyVersion`.

## StrategyEvaluation

Terminal outcomes:
- `TRIGGERED`
- `NOT_TRIGGERED`
- `NOT_EVALUABLE`

No implicit “close enough” state exists.

## BacktestRun / Experiment

```text
CREATED -> QUEUED -> RUNNING -> SUCCEEDED
                           -> FAILED_RETRYABLE
                           -> FAILED_TERMINAL
                           -> CANCELLED
```

A `SUCCEEDED` run is not equivalent to `VALIDATED`. Validation is a separate research decision requiring protocol gates.

## ModelArtifact

```text
CANDIDATE -> VALIDATED -> APPROVED -> DEPLOYED -> RETIRED
   |            |           |
   +-> REJECTED +-> REJECTED+-> SUSPENDED
```

Only `APPROVED`/`DEPLOYED` models may influence user-visible derived artifacts, and only within approved regimes. An unavailable/suspended model falls back to an approved baseline or `NO_CONCLUSION`.

## DecisionRecord

```text
REQUESTED -> ASSEMBLING -> FINALIZED
                        -> REJECTED_INCOMPLETE
                        -> FAILED
```

`FINALIZED` is terminal and immutable.

A DecisionRecord must not finalize if any mandatory component is:
- rights-forbidden;
- past its hard freshness threshold;
- semantically inconsistent;
- from an unapproved model where approval is required;
- missing required provenance/version lineage.

## DataRightsRecord

```text
DRAFT -> VERIFIED -> ACTIVE -> SUSPENDED
                       |       -> REVOKED
                       -> EXPIRED
```

`SUSPENDED`, `REVOKED` or `EXPIRED` rights immediately disable new affected user-visible artifacts. Historical records preserve metadata but must respect ongoing display/retention obligations.

## Provider health

```text
UNKNOWN -> HEALTHY -> DEGRADED -> UNAVAILABLE
              ^          |            |
              +----------+------------+
```

Health is measured per capability/data family rather than only per vendor.

## Job lease

```text
AVAILABLE -> CLAIMED -> SUCCEEDED
                    -> RETRY_WAIT -> AVAILABLE
                    -> DEAD_LETTER
```

Workers must support lease expiry/recovery after process death. A claimed job is never considered complete until its authoritative transaction commits.

## Forbidden transitions

Examples that must fail in tests:
- `DRAFT Strategy -> TRIGGERED` without validation/approval;
- `CANDIDATE Model -> DEPLOYED` without validation/approval;
- `QUARANTINED Evidence -> ACTIVE` without re-validation;
- `FAILED Backtest -> VALIDATED`;
- `FINALIZED DecisionRecord -> mutable state`;
- `REVOKED DataRightsRecord -> ACTIVE` without a new verified rights version.