# MK1 Logical Data Model

## Modeling rules

1. All timestamps are UTC and semantically named.
2. External observations preserve both event time and system availability time.
3. Financial values use exact decimal storage where accounting/price precision matters.
4. Provider payloads are immutable receipts; normalized values are versioned transformations.
5. User-visible DecisionRecords are immutable after finalization.
6. Soft mutation of historical truth is forbidden. Corrections create superseding records with lineage.
7. Core entities use UUID/ULID-style opaque identifiers; provider symbols are never primary keys.
8. Every derived artifact records the code/config/model/normalization versions that produced it.

## Time semantics

Every externally sourced observation must distinguish, where available:

- `event_at` — when the market/event occurred;
- `provider_published_at` — provider publication time;
- `available_at` — earliest timestamp the information could legitimately enter a point-in-time simulation;
- `ingested_at` — when SOPHROSYNE received it;
- `as_of` — cutoff used for a derived state/decision.

Backtests and historical reconstructions may use only records whose `available_at <= as_of`.

## Core tables / aggregates

### Catalog

`instrument`
- `id`
- `asset_class`
- `canonical_symbol`
- `name`
- `base_currency`
- `quote_currency`
- `venue_id` nullable
- `active_from`, `active_to`

`instrument_alias`
- `instrument_id`
- `provider_id`
- `provider_symbol`
- validity interval

`venue`
- identity, timezone metadata, calendar reference

### Sources and rights

`source`
- provider identity
- data family
- trust/quality class
- active state

`data_rights_record`
- source/data-family scope
- display/non-display/derived/redistribution permissions
- retention/caching rules
- geography/entitlement constraints
- contract/reference hash
- valid-from/to
- status

`source_capability`
- historical/streaming support
- resolution
- rate limit metadata
- timestamp semantics
- fallback compatibility group

### Ingestion

`raw_receipt`
- source
- provider request/event identity
- payload hash
- object-storage reference or constrained JSONB
- event/published/available/ingested timestamps
- schema version
- rights record id
- quarantine state

`ingestion_cursor`
- adapter + stream/dataset cursor
- last successful boundary
- lease/reconciliation state

`normalized_observation`
- instrument/source
- observation type
- exact values
- all time semantics
- normalization version
- raw receipt lineage
- quality flags

Deduplication key is provider/data-family/instrument/event identity plus payload hash semantics defined by each adapter.

### Evidence and interpretation

`evidence`
- source/observation lineage
- evidence type
- `as_of`
- freshness state
- epistemic status
- quality flags
- rights record

`claim`
- statement key/template + structured parameters
- status: `OBSERVED | ATTRIBUTED | INFERRED | CORRELATED | UNKNOWN`
- valid interval

`claim_evidence`
- supporting/contradicting relation
- evidence id
- contribution metadata where formally defined

`market_state`
- instrument
- `as_of`
- state schema version
- deterministic feature set
- quality/coverage state
- algorithm version

`scenario`
- market-state lineage
- scenario type/schema
- uncertainty state
- optional probability only when `calibration_status=APPROVED`
- invalidation specification
- generator/model version

`scenario_evidence`
- support/contradict relation
- evidence/claim lineage

### Risk

`risk_assessment`
- scope: instrument/portfolio/strategy
- `as_of`
- risk policy version
- metrics
- constraint results
- quality/coverage state

Risk records do not reference narrative conviction as an authority field.

### Portfolio

`portfolio_snapshot`
- user id
- `as_of`
- origin `MANUAL | READ_ONLY_IMPORT`
- currency
- immutable snapshot state

`portfolio_position`
- snapshot
- instrument
- exact quantity/value basis
- optional user-entered cost basis

### Strategy and research

`strategy`
- owner
- identity/status

`strategy_version`
- immutable deterministic specification
- parser/compiler version
- parameter schema
- created/approved timestamps

`strategy_evaluation`
- strategy version
- `as_of`
- result `TRIGGERED | NOT_TRIGGERED | NOT_EVALUABLE`
- evidence/input manifest

`backtest_run`
- strategy/model version
- data manifest hash
- code/config hash
- point-in-time policy version
- cost/slippage assumptions
- status
- artifact reference

`experiment`
- hypothesis
- preregistered metrics/falsification criteria
- sample/data manifest
- result artifact
- status

`model_artifact`
- model family/version
- training-data manifest
- feature schema
- validation/calibration artifact
- approved regimes
- deployment/retirement state

### Decision ledger

`decision_record`
- user/instrument/context scope
- `as_of`
- finalized timestamp
- market-state id
- risk-assessment id
- portfolio snapshot nullable
- strategy evaluation nullable
- schema/version bundle
- coverage/degradation state
- immutable content hash

`decision_record_scenario`
- ordered scenario links

`decision_record_claim`
- rendered/structured claim links

`decision_record_artifact`
- source/evidence/model/manifest references needed for replay

A finalized DecisionRecord is append-only. User annotations are separate child records and never mutate the original analysis.

### Jobs and reliability

`outbox_event`
- aggregate identity/version
- event type
- payload schema version
- idempotency key
- available-after
- claimed/lease/attempt state

`job_run`
- job type
- deterministic input hash
- status
- started/finished timestamps
- attempts
- error taxonomy
- produced artifact ids

`idempotency_record`
- caller scope + key
- request hash
- response/status reference
- expiration

### Audit

`audit_event`
- actor/service
- action
- target
- security/policy category
- timestamp
- trace id
- non-secret metadata

## Constraints that must exist in the database

- unique strategy version number per strategy;
- probabilities constrained to `[0,1]` and nullable unless approved;
- `available_at <= ingested_at` unless an adapter-specific clock-anomaly flag is present and quarantined;
- finalized DecisionRecords cannot be updated/deleted by application roles;
- user-owned entities always carry `user_id` and are protected by authorization/RLS policy tests;
- rights-restricted data cannot be linked to a user-visible display artifact when display permission is false;
- all model/backtest artifacts require a data manifest hash and code/config version.

## Corrections

If a provider corrects historical data:
1. preserve original receipt;
2. ingest correction as a new receipt;
3. mark lineage/supersession;
4. rebuild affected projections;
5. never rewrite a finalized historical DecisionRecord;
6. replay may explicitly choose `knowledge_as_of_then` or `corrected_history_now`, and the distinction must be visible.

## Retention

Retention is policy-driven by DataRightsRecord and privacy requirements. A background compliance job must be able to locate and purge/cache-expire restricted payload classes without deleting immutable metadata proving why an artifact was unavailable.