# MK1 Persistence Schema Blueprint

## Purpose

This document maps the logical data model to PostgreSQL implementation conventions. It does not replace Alembic migrations; it constrains what those migrations are allowed to invent.

## Database principles

- PostgreSQL 18 supported line.
- UTC `timestamptz` for all instants.
- exact decimal storage for financial values.
- UUIDv7 opaque identifiers for new aggregate identities.
- JSONB only for versioned opaque payload/manifests, never core relational state.
- append-only history where provenance matters.
- user-owned rows protected by application authorization plus database RLS defense-in-depth.
- no application role may mutate finalized ledger history.

## PostgreSQL schemas

Use explicit PostgreSQL schemas to make table ownership visible:

```text
identity
catalog
rights
ingestion
evidence
market
portfolio
strategy
research
ledger
jobs
audit
```

`public` contains only extensions and migration metadata unless a later ADR says otherwise.

Mapping:
- `market_state` and `scenario` tables live in `market`;
- `explanation` artifacts live as derived references under `ledger`/object storage because explanation is non-authoritative;
- cross-cutting asynchronous state lives in `jobs`.

## Database roles

Production roles are separated:

- `sophrosyne_migrator` — DDL only; not used by application runtime.
- `sophrosyne_api` — normal synchronous application access.
- `sophrosyne_worker` — background-job access, restricted from identity/session mutation unless explicitly required.
- `sophrosyne_readonly` — operational/reporting reads.

Secrets for these roles are distinct.

The API/worker roles receive only the grants required by their active modules. They never own schemas.

## Identifier policy

Primary aggregate IDs use PostgreSQL `uuid` values generated as UUIDv7 either through the supported runtime helper or PostgreSQL 18 `uuidv7()` where appropriate.

Rules:
- provider symbols are never primary keys;
- natural keys receive unique constraints when required but remain mutable only through versioned semantics;
- APIs serialize IDs as canonical UUID strings;
- foreign-key IDs are named `<aggregate>_id`.

## Decimal policy

Canonical normalized financial values default to `numeric(38,18)` unless a narrower domain contract is justified.

This covers:
- prices;
- quantities;
- fees;
- cash balances;
- portfolio values;
- cost basis.

Percentages/probabilities use explicit numeric scale appropriate to the metric. IEEE binary floats are forbidden for authoritative money/price/quantity/accounting fields.

Analytical arrays/artifacts may use floating-point formats outside authoritative accounting state when the exact representation is captured in a versioned research artifact.

## Common columns

Mutable metadata tables normally include:

```text
id uuid primary key
created_at timestamptz not null
updated_at timestamptz not null
version bigint not null default 1
```

Immutable event/history rows normally include:

```text
id uuid primary key
created_at timestamptz not null
content_hash text not null
schema_version integer not null
supersedes_id uuid null
```

Do not add `updated_at` to immutable records.

## Core physical ownership

### `identity`

- `identity.user_account`
- `identity.external_identity`
- `identity.session_audit_ref` only when needed; session authority may remain in the managed IdP/server-session store.

No financial profile inference belongs here.

### `catalog`

- `catalog.venue`
- `catalog.instrument`
- `catalog.instrument_alias`
- `catalog.calendar_profile`
- `catalog.currency`

Key indexes:
- unique provider alias by provider + symbol + validity boundary;
- active instrument lookup by canonical symbol/venue;
- validity-range indexes for historical symbol resolution.

### `rights`

- `rights.source`
- `rights.source_capability`
- `rights.data_rights_record`
- `rights.entitlement_profile`

Every rights record contains validity/effective timestamps and an authority/reference digest.

Indexes prioritize active rights by source/data family/geography/user class.

### `ingestion`

- `ingestion.raw_receipt`
- `ingestion.normalized_observation`
- `ingestion.ingestion_cursor`
- `ingestion.quality_incident`

`raw_receipt` payload bytes should live in object storage when permitted; the table stores hash, URI/reference, metadata and rights lineage.

Required indexes:
- `(source_id, available_at)`;
- `(instrument_id, observation_type, available_at)`;
- provider event identity/dedup key;
- quarantine state;
- cursor ownership/lease fields.

### `evidence`

- `evidence.evidence`
- `evidence.claim`
- `evidence.claim_evidence`

Supporting/contradicting relation is an enum/check-constrained value.

Claims never store narrative text as the sole semantic representation; structured key + parameters remain authoritative.

### `market`

- `market.market_state`
- `market.market_state_evidence`
- `market.scenario`
- `market.scenario_evidence`
- `market.risk_assessment`

`scenario.probability` is nullable and DB-constrained to `[0,1]`.

A non-null displayed probability additionally requires `calibration_status='APPROVED'` at application-validation time and through a DB check where representable.

### `portfolio`

- `portfolio.snapshot`
- `portfolio.position`

Snapshots are immutable after finalization.

Positions use exact quantities and carry the parent `user_id` redundantly where useful for RLS/ownership checks.

### `strategy`

- `strategy.strategy`
- `strategy.strategy_version`
- `strategy.strategy_evaluation`

Unique constraint: `(strategy_id, version_number)`.

Strategy versions are immutable after creation.

### `research`

- `research.backtest_run`
- `research.experiment`
- `research.model_artifact`
- `research.dataset_manifest`
- `research.calibration_artifact`

Large result payloads remain in object storage; relational tables store immutable manifest/artifact digests and summary metadata.

Every completed backtest requires:
- dataset manifest reference;
- code/build identity;
- cost-policy version;
- point-in-time policy version;
- benchmark version.

### `ledger`

- `ledger.decision_record`
- `ledger.decision_record_scenario`
- `ledger.decision_record_claim`
- `ledger.decision_record_artifact`
- `ledger.decision_annotation`

Finalized `decision_record` rows are append-only.

Immutability is enforced by both:
1. application state machine;
2. database trigger/policy that rejects `UPDATE`/`DELETE` on finalized rows for runtime roles.

Annotations are separate rows and may supersede prior annotations without changing the record.

### `jobs`

- `jobs.outbox_event`
- `jobs.job_run`
- `jobs.idempotency_record`

Detailed state semantics are defined in `ASYNC_JOB_AND_EVENT_CONTRACTS.md`.

### `audit`

- `audit.audit_event`
- `audit.policy_change_event`

Audit events are append-only and may contain only non-secret metadata.

## Foreign-key policy

Cross-module foreign keys are allowed only to stable identifiers and never imply ownership.

Rules:
- no cross-module `ON DELETE CASCADE`;
- default delete behavior is `RESTRICT`;
- policy-driven purge/anonymization is explicit;
- provenance/history references may intentionally retain pseudonymous IDs after user-data deletion where law/rights permit and the privacy contract requires it.

## RLS policy

RLS is enabled on user-owned tables including at minimum:
- portfolio snapshots/positions;
- user-owned strategies/versions;
- user-visible DecisionRecords/annotations;
- user-scoped research runs when persisted as private artifacts.

The API transaction sets a transaction-local user context, for example:

```text
SET LOCAL app.user_id = '<uuid>'
```

Policies compare ownership against that value.

Requirements:
- transaction-local only; never session-global state in a pooled connection;
- missing user context denies user-scoped rows;
- admin/research bypass uses separate audited roles, not a magic user id;
- CI contains RLS leakage tests across two synthetic users.

RLS complements application authorization; it does not replace it.

## Time/point-in-time constraints

Where applicable:
- `available_at <= ingested_at` unless quarantined for documented clock anomaly;
- validity intervals use half-open `[from,to)` semantics;
- `as_of` queries filter `available_at <= as_of`;
- provider corrections create new rows/lineage rather than update historical receipts.

Range/temporal constraints introduced in PostgreSQL 18 may be used where they make interval validity safer, but adoption must remain understandable in migrations/tests.

## Index policy

Indexes are justified by canonical access paths, not added speculatively.

Initial required families:
- point-in-time observation lookup;
- Decision Ledger cursor pagination by user + finalized timestamp + id;
- active rights lookup;
- job ready/lease lookup;
- idempotency lookup;
- instrument alias validity lookup;
- strategy version lookup.

Partial indexes are preferred for hot states such as ready jobs or active rights when they materially reduce working set.

## Partitioning rule

No table is partitioned in the first schema merely because it may become large.

Partitioning requires measured cardinality/query/vacuum pressure and an ADR if it changes operational semantics. Likely future candidates are observations/raw receipts/audit events, but none are pre-partitioned by default.

## Migration safety

Every migration must classify itself:

```text
EXPAND
BACKFILL
CONTRACT
DATA_REPAIR
```

Rules:
- destructive `CONTRACT` changes require evidence the old application version no longer needs the field/table;
- large backfills are resumable and run separately from latency-sensitive deploy startup;
- DDL locks/timeouts are tested in staging for non-trivial tables;
- migration rollback means restoring compatible application/schema state, not pretending all DDL can always be reversed safely.

## Retention and purge

Retention jobs evaluate both:
- privacy/user deletion policy;
- `DataRightsRecord` retention/cache policy.

Raw content may be deleted while preserving non-content metadata/hash proving why a past artifact is no longer fully replayable.

Replay capability is labeled explicitly when retention changes it:
- `FULL_REPLAYABLE`;
- `PARTIAL_REPLAYABLE`;
- `PROVENANCE_VERIFIABLE`;
- `NON_REPLAYABLE`.

No product copy promises perpetual full replay independent of licensing/privacy constraints.

## Schema acceptance gate

Before domain implementation begins, CI must prove:
- clean migration from empty PostgreSQL 18;
- no multiple Alembic heads;
- expected schemas/roles/grants;
- UUID/decimal/time check fixtures;
- RLS isolation;
- finalized DecisionRecord mutation denied;
- cross-module cascade absent;
- point-in-time indexes support representative query plans;
- downgrade/recovery procedure documented for the current migration set.