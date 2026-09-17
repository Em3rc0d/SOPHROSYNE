# MK1 Async Job and Event Contracts

## Purpose

This document freezes the semantics of PostgreSQL-backed jobs and the transactional outbox before implementation begins.

MK1 guarantees **at-least-once delivery and idempotent processing**. It does not claim exactly-once execution.

## Core rule

Any authoritative state change and its corresponding outbox event are committed in the same PostgreSQL transaction.

Network side effects, provider calls, object-store writes and expensive research work happen in worker jobs after commit unless the operation is an explicitly captured read whose exact response becomes an immutable receipt.

## Outbox event envelope

Every outbox event contains:

```text
event_id              uuidv7
aggregate_type        text
aggregate_id          uuid
aggregate_version     bigint
event_type            text
schema_version        integer
occurred_at           timestamptz
available_after       timestamptz
idempotency_key       text
trace_id              text
payload               jsonb
created_at             timestamptz
published_at          timestamptz null
attempt_count         integer
last_error_code       text null
```

`payload` contains only the minimum immutable data required to identify/process the event. Large artifacts are referenced by immutable ID/hash, not embedded.

## Event naming

Canonical name:

```text
<module>.<aggregate>.<past_tense_fact>.v<schema>
```

Examples:
- `ingestion.receipt.captured.v1`
- `ingestion.observation.normalized.v1`
- `market_state.snapshot.finalized.v1`
- `ledger.decision_record.finalized.v1`
- `rights.data_profile.revoked.v1`

The version suffix describes event payload semantics, not application release version.

## Event compatibility

Consumers must:
- reject unknown major/schema semantics explicitly;
- ignore additive optional fields they do not need;
- never reinterpret a historical event by current business rules;
- persist the consumer code/schema version in produced authoritative artifacts where replay matters.

Breaking payload semantics create a new event schema version.

## Job record

A job contains:

```text
job_id
job_type
schema_version
input_ref_or_payload
input_hash
idempotency_key
priority
state
available_after
lease_owner
lease_expires_at
attempt_count
max_attempts
started_at
finished_at
last_error_code
last_error_detail_redacted
result_refs
trace_id
created_at
```

## Job state machine

```text
READY
  -> LEASED
      -> SUCCEEDED
      -> READY            # retryable failure, delayed
      -> FAILED_TERMINAL
      -> CANCELLED

LEASED --lease expiry--> READY
```

No second hidden `RUNNING` truth is required. `LEASED` means one worker currently owns the right to execute until lease expiry.

## Claiming

Workers claim ready jobs using one transaction with row locking (`FOR UPDATE SKIP LOCKED`) and set:
- `lease_owner`;
- `lease_expires_at`;
- incremented attempt state where appropriate.

A worker must verify ownership before final status transition.

Lease duration is job-type specific and longer jobs renew leases periodically.

## Retry taxonomy

### Retryable transient

Examples:
- provider timeout;
- HTTP 429/temporary provider unavailable;
- temporary object-store/network failure;
- transient database deadlock/serialization failure outside the claiming transaction.

Action:
- exponential backoff with jitter;
- capped delay;
- respect provider `Retry-After` where authoritative;
- preserve attempt/error metadata.

### Policy blocked

Examples:
- data-rights record revoked;
- required entitlement missing;
- calibration/model approval suspended;
- required source stale beyond policy.

Action:
- do not blind-retry rapidly;
- move to terminal/policy-blocked semantic error or reschedule only when a governing policy-change event explicitly makes it eligible.

### Permanent invalid input

Examples:
- schema invalid;
- unsupported instrument;
- invariant violation;
- unknown event schema.

Action:
- `FAILED_TERMINAL`;
- no automatic retry.

## Retry budget

Every job type declares:
- `max_attempts`;
- initial delay;
- maximum delay;
- lease duration;
- deadline/maximum wall-clock age when applicable.

Retries are not infinite. Exhausted jobs remain queryable and auditable.

## Idempotency

Every handler has a deterministic idempotency scope.

Examples:

```text
capture provider window:
  provider + dataset + window_start + window_end + request_semantics_version

normalize receipt:
  raw_receipt_id + normalization_version

market state:
  instrument_id + as_of + state_algorithm_version + input_manifest_hash

backtest:
  strategy_version + dataset_manifest + cost_policy + code/config digest

explanation:
  authoritative_artifact_id + audience + language + explanation_policy_version
```

A duplicate delivery must return/attach the existing semantic result rather than create a second authoritative artifact.

## Initial job types

The allowed MK1 set is narrow:

- `INGEST_SOURCE_WINDOW`
- `NORMALIZE_RAW_RECEIPT`
- `RECONCILE_SOURCE`
- `ASSEMBLE_MARKET_STATE`
- `ASSEMBLE_DECISION_RECORD`
- `RUN_BACKTEST`
- `RUN_APPROVED_MODEL_INFERENCE`
- `GENERATE_EXPLANATION`
- `APPLY_RETENTION_POLICY`
- `REBUILD_DERIVED_PROJECTION`
- `VERIFY_ARTIFACT_INTEGRITY`

There is **no live order/execution job type in MK1**.

Adding a job type that changes financial authority requires governance review and may require an ADR/evidence revalidation.

## Concurrency keys

Job types declare optional serialization keys.

Examples:
- provider ingestion cursor: one active job per provider/dataset partition;
- retention: one active job per rights/profile scope;
- DecisionRecord assembly: idempotency key naturally collapses duplicates.

Do not use one global worker lock.

## Cancellation

Cancellation is cooperative.

A cancellable handler checks state at safe boundaries and exits without publishing authoritative success.

Completed immutable artifacts are not deleted merely because the initiating job was later cancelled.

## Outbox publication

For MK1, the outbox is consumed by internal workers directly from PostgreSQL; no external broker is required.

`published_at` means the event has been acknowledged by the internal dispatch/consumer workflow, not that every downstream effect succeeded.

If a future broker is introduced, the authoritative event identity remains the outbox `event_id` and downstream consumers remain idempotent.

## Failure handling

Job failure must never silently mutate product truth.

Examples:
- failed explanation -> authoritative DecisionRecord stays usable;
- failed model inference -> baseline/NO_CONCLUSION path according to policy;
- failed provider ingestion -> freshness/degradation state becomes visible;
- failed backtest -> no partial result presented as completed.

## Observability

Every execution records:
- queue wait time;
- attempts;
- handler duration;
- outcome class;
- lease renewals;
- provider/error code category;
- trace correlation;
- backlog age by job type.

Alerts key on age/SLO and terminal error rate, not only queue depth.

## Security

- payloads contain no secrets;
- provider credentials are resolved at execution time from secret/config boundary;
- error detail is redacted before persistence;
- user-scoped jobs carry opaque user/resource IDs but not unnecessary personal data;
- worker authorization is least privilege.

## Acceptance tests

Before asynchronous domain features are accepted:
- duplicate event delivery produces one semantic result;
- worker crash after side effect but before ack is safe on retry;
- lease expiry enables recovery without concurrent double-commit;
- terminal validation failures do not loop;
- 429/timeout retry respects policy;
- revoked rights prevent relevant jobs;
- cancellation never emits false success;
- backlog recovery after worker outage meets the approved staging SLO;
- no live execution/order job exists in MK1.