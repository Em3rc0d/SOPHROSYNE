# MK1 First Vertical Slice

## Purpose

This document defines the first production-quality vertical slice to build **after** MK0 promotion and `BUILD_READINESS` approval.

It is deliberately smaller than the full Market Translator. Its goal is to prove the complete authoritative path from approved source data to an immutable user-visible DecisionRecord before portfolio, strategy, backtesting, ML or LLM layers are added.

## Entry conditions

The slice cannot begin until:
- Q00 final receipt is promotable and the surviving component set is frozen;
- Q01–Q05 promotion requirements applicable to the slice are promotable;
- one `MK1_BOOTSTRAP_PROFILE` is approved;
- provider/data profile used by the slice is explicitly approved by Q02;
- `BUILD_READINESS.md` passes;
- Phase 0 repository/toolchain skeleton is green.

## Slice scope

Exactly one narrow approved instrument/data family is used first.

Canonical flow:

```text
approved provider fixture/live-read
        ↓
raw receipt + rights lineage
        ↓
normalization
        ↓
normalized observation
        ↓
evidence
        ↓
deterministic MarketState
        ↓
DecisionRecord
        ↓
GET /v1/decision-records/{id}
        ↓
minimal web evidence view
```

The first slice demonstrates authoritative truth, not feature breadth.

## Included modules

- `identity` — minimal authenticated user/session context.
- `catalog` — one venue/instrument and aliases.
- `rights` — exact active `DataRightsRecord`/profile.
- `ingestion` — one approved adapter + raw receipt + normalization.
- `evidence` — one or more structured evidence objects/claims.
- `market_state` — deterministic state only.
- `ledger` — immutable finalized DecisionRecord.
- `audit` — security/policy-relevant audit events.
- `apps/web` — read-only presentation of the record/evidence state.

## Explicitly excluded from Slice 1

- portfolio-aware behavior;
- strategy DSL;
- backtesting;
- ML prediction;
- displayed probabilities;
- LLM explanation;
- news/social/on-chain expansion unless the bootstrap profile selected that exact data family for the first slice;
- broker/exchange account connection;
- live trading/order execution;
- personalized buy/sell recommendations.

A component excluded by Q00 cannot be reintroduced into this slice merely because implementation is convenient.

## Required endpoints

Minimal HTTP surface:

```text
GET  /v1/instruments/{instrument_id}/market-state?as_of=
POST /v1/decision-records
GET  /v1/decision-records/{id}
GET  /v1/evidence/{evidence_id}
GET  /health/live
GET  /health/ready
```

No generic admin CRUD API is created for internal tables.

## DecisionRecord creation contract

`POST /v1/decision-records` accepts:
- instrument/context reference;
- `as_of`;
- idempotency key through header;
- optional bootstrap-supported display/context parameters only.

The API either:
- finalizes one immutable record;
- returns an explicit degradation/no-conclusion result;
- or fails with stable Problem Details.

It never silently substitutes fresher/future data for the requested `as_of`.

## First source adapter contract

The first adapter must prove all adapter obligations, not only the happy payload:
- historical/incremental read supported by the approved profile;
- provider timestamps mapped to event/published/available/ingested semantics;
- rights profile attached;
- duplicate detection;
- correction lineage;
- malformed/unknown schema quarantine;
- 429/timeout handling;
- health/status signal;
- deterministic normalization version.

Do not add provider #2 until this adapter is green.

## Deterministic MarketState

The first MarketState uses only transparent features that survived Q00/product validation and require no ML authority.

Requirements:
- deterministic function of point-in-time inputs + versioned configuration;
- exact input manifest/hash available;
- `READY | DEGRADED | NO_CONCLUSION` state;
- no inferred probability unless separately approved/calibrated;
- missing/stale evidence remains visible.

The exact feature set comes from the approved bootstrap profile; this document does not invent it.

## Minimal web surface

One instrument/DecisionRecord surface shows:
- instrument identity;
- `as_of` and generated time;
- MarketState dimensions that survived Q00;
- supporting evidence;
- contradicting evidence when present;
- freshness/degradation state;
- provenance/source class allowed for display;
- immutable DecisionRecord id/version/hash metadata in an expandable technical view.

The UI must not imply action authority or profitability.

## Database acceptance for this slice

Must prove:
- migrations clean;
- RLS isolates two synthetic users;
- rights-disabled evidence cannot appear in user-display joins;
- `available_at > as_of` observation cannot enter the record;
- finalized record update/delete is rejected;
- duplicate ingest/POST retries create one semantic result;
- correction receipt does not rewrite finalized historical record.

## Golden fixtures

The first slice ships with a small golden corpus including:
1. normal fresh observation;
2. stale input -> degraded/no-conclusion;
3. contradictory evidence;
4. duplicate provider event;
5. corrected provider observation;
6. rights record revoked;
7. future-leak fixture intentionally rejected;
8. provider timeout/rate limit;
9. malformed timestamp/schema drift;
10. worker crash/retry around an idempotent job.

## Required tests

### Unit/property
- timestamp ordering;
- freshness classification;
- rights decision;
- MarketState determinism;
- content-hash determinism;
- state-machine transitions.

### Database/integration
- migrations;
- constraints;
- RLS;
- outbox atomicity;
- job lease recovery;
- immutable ledger trigger/policy.

### Contract
- OpenAPI snapshot;
- provider fixtures;
- Problem Details codes;
- decimal/timestamp serialization.

### Anti-leakage
- synthetic future observation must cause test failure if selected.

### E2E

```text
login
  -> instrument view
  -> ingest/fixture available
  -> market state visible
  -> finalize record
  -> reload/revisit same immutable record
  -> provider stale/revoked fixture shows explicit degradation
```

## Observability acceptance

The slice emits trace correlation through:

```text
web -> api -> db/outbox -> worker -> db -> api
```

Required metrics/log dimensions:
- request latency/error family;
- ingestion freshness;
- worker queue age/attempts;
- DecisionRecord assembly success/degradation;
- rights-policy denials;
- replay/hash mismatch = zero tolerance alert in staging.

No raw secrets/provider payloads are logged.

## Security acceptance

At minimum:
- ownership/IDOR tests;
- CSRF/session policy where applicable;
- input/XSS encoding for provider/user strings;
- no arbitrary provider URL SSRF;
- secret redaction;
- RLS isolation;
- rate-limit/abuse guard for record creation;
- no web access to provider credentials.

## Failure acceptance

The slice must remain semantically safe when:
- provider is unavailable;
- worker is killed mid-job;
- object storage is unavailable;
- rights are revoked;
- required data becomes stale;
- database transaction rolls back.

Safe behavior is visible degradation/failure, never fabricated fresh state.

## Exit gate

Slice 1 is complete only when:
- all mandatory tests are green;
- golden replay of its deterministic corpus is 100%;
- OpenAPI/client generation is clean;
- provider contract tests are green;
- anti-leakage suite is green;
- rights kill-switch behavior is green;
- DecisionRecord immutability is green;
- staging failure-injection for provider/worker/object-store has expected results;
- mobile/desktop accessibility for the minimal view is green;
- acceptance receipt set required by `BUILD_READINESS` is produced for this scope.

Only after this gate may Phase 4+ functionality build on the slice.

## Success criterion

The first slice succeeds if SOPHROSYNE can prove:

> For one approved data profile and one narrow product path, the same point-in-time evidence produces a reproducible, rights-aware, immutable DecisionRecord that remains understandable and safe under retries, stale data and provider failure.

It does not need to prove alpha, ML value, product-market fit or future execution.