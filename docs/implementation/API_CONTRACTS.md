# MK1 API Contracts

## Principles

- Public API is versioned under `/v1`.
- JSON fields use explicit schemas; no ad-hoc polymorphic blobs for core domain data.
- Timestamps are RFC 3339 UTC.
- Money/price/quantity values are serialized as decimal strings, never JSON binary floats.
- Every response containing derived market interpretation includes `as_of`, `generated_at`, `schema_version` and coverage/degradation metadata.
- All mutations requiring retry safety support `Idempotency-Key`.
- Every request receives or propagates `X-Request-ID`; tracing uses standard trace context.
- Errors use RFC 7807-style Problem Details with stable machine codes.

## Resource model

### Market state

`GET /v1/instruments/{instrument_id}/market-state?as_of=<timestamp>`

Returns:
- instrument identity;
- `as_of`;
- deterministic state dimensions;
- evidence coverage;
- freshness/degradation state;
- algorithm/version bundle;
- provenance links.

The endpoint may return `NO_CONCLUSION` semantics when required evidence is insufficient.

### Scenarios

`GET /v1/instruments/{instrument_id}/scenarios?as_of=<timestamp>`

Each scenario exposes:
- structured scenario type/summary;
- supporting evidence ids;
- contradicting evidence ids;
- invalidation conditions;
- uncertainty;
- probability only if calibration status is approved;
- generator/model version.

### Evidence

`GET /v1/evidence/{evidence_id}`

Returns the user-displayable representation permitted by the active DataRightsRecord. Restricted raw provider content is never leaked through this endpoint.

### Decision ledger

`POST /v1/decision-records`

Creates/finalizes one reproducible record for a requested instrument/context and `as_of` cutoff.

Mutation must be idempotent for the same caller, request body and `Idempotency-Key`.

`GET /v1/decision-records/{id}`

Returns immutable structured content plus replay/version metadata.

`GET /v1/decision-records?instrument_id=&cursor=`

Cursor pagination only; no unstable page-number pagination for append-only records.

### Portfolio snapshots

`POST /v1/portfolio-snapshots`

MK1 accepts manual/read-only data only. Validation rejects unsupported instruments, negative quantities where not explicitly allowed, malformed currency values and ambiguous symbols.

`GET /v1/portfolio-snapshots/{id}/risk`

Returns descriptive risk context, not individualized buy/sell instructions.

### Strategies

`POST /v1/strategies/validate`

Validates a deterministic strategy specification without persisting or executing it.

Returns:
- canonical AST/specification;
- parameter types;
- referenced features;
- validation errors;
- deterministic semantic hash.

`POST /v1/strategies`

Persists a versioned user-approved strategy definition.

`POST /v1/strategies/{id}/versions`

Creates a new immutable version; previous versions remain addressable.

### Backtests

`POST /v1/backtests`

Schedules a reproducible backtest using an immutable strategy version and explicit assumptions.

Required request fields include:
- strategy version;
- instrument universe;
- period;
- benchmark;
- fee/slippage policy;
- data-policy version.

Returns `202 Accepted` + job id.

`GET /v1/backtests/{id}`

Returns status and, once complete, manifest/artifact references and summary metrics.

### Explanation

`POST /v1/explanations`

Accepts only a structured authoritative artifact id (for example a finalized DecisionRecord) plus requested audience level/language. The LLM is not passed unrestricted browsing/tool authority.

The result is explicitly marked `non_authoritative_explanation=true` and links to the authoritative structured source.

## Response envelope

Successful single-resource responses use domain fields directly plus common metadata where relevant; avoid a redundant universal `data` wrapper.

Collections use:

```json
{
  "items": [],
  "next_cursor": null,
  "as_of": "..."
}
```

## Problem Details

Example:

```json
{
  "type": "https://sophrosyne.dev/problems/data-stale",
  "title": "Required market evidence is stale",
  "status": 409,
  "code": "DATA_STALE",
  "detail": "A fresh DecisionRecord cannot be finalized.",
  "request_id": "...",
  "retryable": true
}
```

Stable error families:
- `VALIDATION_FAILED`
- `UNAUTHORIZED`
- `FORBIDDEN`
- `NOT_FOUND`
- `CONFLICT`
- `IDEMPOTENCY_CONFLICT`
- `DATA_STALE`
- `DATA_INSUFFICIENT`
- `RIGHTS_RESTRICTED`
- `PROVIDER_DEGRADED`
- `MODEL_UNAVAILABLE`
- `NOT_EVALUABLE`
- `RATE_LIMITED`
- `INTERNAL_ERROR`

## Idempotency

For supported mutation endpoints:
- key scope = authenticated user/service + route;
- same key + same request hash returns prior semantic result;
- same key + different request hash returns `409 IDEMPOTENCY_CONFLICT`;
- idempotency records have policy-defined retention;
- workers use their own deterministic job idempotency keys.

## Optimistic concurrency

Mutable user-authored resources expose a version/ETag. Updates require `If-Match` or explicit expected version; lost updates fail with `409` rather than silently overwrite.

Immutable resources do not expose update operations.

## Caching

- DecisionRecords: immutable and cacheable by id subject to privacy headers.
- current market state: short-lived, must expose `as_of` and freshness.
- user portfolio data: private/no shared cache.
- rights-restricted evidence: cache policy derived from DataRightsRecord.

A cached response may never omit its original `as_of` timestamp or be relabeled as newly computed.

## Authorization scopes

Logical scopes:
- `market:read`
- `evidence:read`
- `portfolio:read/write`
- `strategy:read/write`
- `research:read/write`
- administrative/research roles are separate from normal user scopes.

Authorization checks occur server-side on every resource access; opaque IDs are not an access-control mechanism.

## Contract compatibility

Breaking changes require `/v2` or an explicitly versioned media/schema boundary. Additive optional fields may ship in `/v1` only when existing semantics are unchanged.

OpenAPI is generated from code and checked into CI as a reviewed artifact. Unexpected schema drift fails CI.