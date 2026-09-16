# MK1 Reference Architecture

## Decision

MK1 is a **modular monolith with isolated worker processes**, not a microservice system.

The objective is to minimize distributed-system failure modes while preserving explicit module boundaries that can later be extracted through ADRs if load, team topology or regulatory isolation requires it.

## Runtime topology

```text
Browser
  |
  v
Web application
  |
  | same-origin /api
  v
Core API ----------------------------------------------------+
  |                                                         |
  | synchronous application services                        |
  v                                                         |
PostgreSQL <---- transactional outbox ---- Worker process    |
  |                                  |                      |
  |                                  +--> provider adapters |
  |                                  +--> market-state jobs  |
  |                                  +--> backtests          |
  |                                  +--> model inference    |
  |                                  +--> LLM explanation    |
  |                                                         |
  +---- immutable records / manifests ----> object storage   |
                                                            |
External providers <-----------------------------------------+
```

## Deployable units

### `web`
Presentation only. Owns no financial truth, model logic or strategy semantics.

Responsibilities:
- authentication UX and session initiation;
- progressive-disclosure rendering;
- user input validation for usability;
- visualization;
- accessibility;
- request correlation propagation.

### `api`
Authoritative synchronous application boundary.

Responsibilities:
- authorization;
- domain invariants;
- transactional writes;
- idempotency;
- query APIs;
- creation/finalization of Decision Records;
- orchestration of background work through durable jobs/outbox.

### `worker`
Executes retryable asynchronous work.

Responsibilities:
- provider ingestion;
- normalization;
- market-state computation;
- reproducible backtests;
- approved model inference;
- explanation generation;
- artifact creation;
- reconciliation.

A worker may produce candidate artifacts but cannot bypass domain validation performed by the application layer.

### `postgres`
System of record for metadata, normalized point-in-time data, domain state, user data, idempotency, jobs and audit references.

### `object storage`
Stores immutable or large artifacts such as experiment manifests, model packages, source receipts, backtest result bundles and optional raw provider payload archives when licensing permits.

## Canonical modules

Each module owns its tables and public application interface. Cross-module writes through another module's tables are forbidden.

1. `identity` — user/account/session references and authorization roles.
2. `catalog` — instruments, venues, symbol mappings and currencies.
3. `rights` — provider capabilities, entitlements and DataRightsRecords.
4. `ingestion` — connectors, cursors, raw receipts, normalization and quality state.
5. `evidence` — Evidence and Claim lifecycle.
6. `market_state` — deterministic/validated state computations.
7. `scenario` — scenario construction, evidence links and invalidators.
8. `risk` — portfolio-independent and portfolio-aware risk calculations.
9. `portfolio` — manual/read-only PortfolioSnapshots in MK1.
10. `strategy` — deterministic strategies, versions and evaluations.
11. `research` — backtests, experiments, ModelArtifacts and validation manifests.
12. `ledger` — immutable DecisionRecords and reproducibility bundles.
13. `explanation` — non-authoritative LLM/plain-language rendering.
14. `audit` — security, administrative and policy-relevant audit events.

## Dependency direction

```text
catalog <- rights <- ingestion -> evidence -> market_state -> scenario
                                  |               |            |
                                  |               v            |
portfolio ----------------------> risk <-----------+            |
strategy ----------------------> research                       |
   |                              |                              |
   +--------------------------> ledger <-------------------------+
                                  |
                                  v
                             explanation
```

`explanation` is downstream only. It never becomes an input to `risk`, `strategy`, `market_state`, `scenario` or execution semantics.

## Transaction model

Within one user-visible mutation, all authoritative state changes commit in one PostgreSQL transaction.

Asynchronous side effects use a **transactional outbox** written in the same transaction as the triggering domain change. Workers claim jobs with row locking and leases. No in-memory queue is authoritative.

## Read model

MK1 uses PostgreSQL queries/materialized projections before introducing a separate search or analytical database. Derived projections may be rebuilt from canonical records.

## Provider abstraction

Provider-specific schemas terminate inside `ingestion/adapters/<provider>`.

Normalized domain code must never import provider SDK types.

All provider adapters implement capabilities for:
- historical fetch;
- incremental fetch/stream where available;
- health/status;
- rate-limit metadata;
- timestamp semantics;
- rights/entitlement reference;
- normalization version.

Fallback is allowed only between semantically compatible and rights-compatible data families.

## No-premature-components rule

MK1 does **not** require Kafka, Kubernetes, a service mesh, a feature store, a vector database, an OLAP cluster or multiple transactional databases.

Any introduction of one requires an ADR containing a measured failure of the simpler architecture.

## Extraction rule

A module may become an independent service only when at least one is demonstrated:
- materially different scaling profile;
- security/regulatory isolation requirement;
- release cadence ownership conflict;
- independently measured resource contention;
- operational blast-radius requirement.

The extraction must preserve API/domain semantics and DecisionRecord reproducibility.