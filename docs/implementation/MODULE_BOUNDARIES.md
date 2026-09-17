# MK1 Module Boundaries

## Purpose

This document makes the modular-monolith dependency graph executable. It defines which modules may depend on which other modules, how they communicate and what imports are forbidden.

A module owns its domain rules, persistence mapping and public contracts. Another module may consume only the published contract surface.

## Canonical modules

- `identity`
- `catalog`
- `rights`
- `ingestion`
- `evidence`
- `market_state`
- `scenario`
- `risk`
- `portfolio`
- `strategy`
- `research`
- `ledger`
- `explanation`
- `audit`

`platform/*` is infrastructure, not a domain module.

## Allowed dependency graph

| Module | May depend on |
|---|---|
| identity | shared only |
| catalog | shared only |
| rights | catalog |
| ingestion | catalog, rights |
| evidence | catalog, rights, ingestion contracts |
| market_state | catalog, evidence |
| scenario | catalog, evidence, market_state, research model-contracts only |
| portfolio | identity, catalog |
| risk | catalog, market_state, portfolio |
| strategy | identity, catalog |
| research | catalog, rights, strategy, ingestion read contracts |
| ledger | identity, catalog, evidence, market_state, scenario, risk, portfolio, strategy, research contracts |
| explanation | ledger, evidence |
| audit | shared only |

Every module may emit audit events through the shared audit port. Emitting an audit event does not grant access to `audit` persistence internals.

## Dependency invariants

1. The graph must remain acyclic.
2. `explanation` is terminal/downstream and cannot be imported by analytical modules.
3. `research` may read approved point-in-time data through an ingestion/query port but never provider adapter types.
4. `risk` never imports `explanation` or model narrative output.
5. `ledger` may aggregate references from many modules but does not gain authority to rewrite their truth.
6. `web` is outside this graph and consumes only HTTP contracts.
7. Provider SDKs terminate inside `ingestion` adapter packages.

## Public contract surface

Each module exports only through `contracts.py` and/or a documented service interface.

A public contract may contain:
- opaque IDs;
- value objects;
- immutable DTOs;
- application commands/queries;
- domain events;
- repository/query ports explicitly intended for another module.

A public contract may not expose:
- SQLAlchemy ORM classes;
- database sessions;
- provider SDK objects;
- FastAPI request objects;
- infrastructure clients;
- module-private enums whose semantics are not versioned.

## Cross-module reads

Preferred order:

1. synchronous public query/service interface for transactional needs;
2. stable read projection for high-volume read-only use;
3. immutable referenced artifact for historical/replay use.

Direct joins across module ORM classes are prohibited in application code.

Database-level SQL joins for operational/reporting projections are allowed only inside an explicitly owned projection/query package and may not mutate source-module tables.

## Cross-module writes

A module never writes another module's tables directly.

Allowed mechanisms:
- invoke the other module's application service in the same transaction when synchronous atomicity is required;
- emit a transactional-outbox event when eventual processing is acceptable.

No caller may construct another module's persistence entity and add it to a shared SQLAlchemy session.

## Transaction ownership

The API application service opens the transaction boundary.

Within a transaction:
- participating module services receive a unit-of-work/repository abstraction;
- domain invariants execute before commit;
- outbox events are persisted atomically;
- no network side effect is executed before commit.

External calls occur before the authoritative transaction only when they are pure reads whose exact returned payload is then captured as a receipt, or after commit through jobs/outbox.

## Typed IDs

Opaque UUIDs are wrapped in module-specific Python types where practical:

```text
InstrumentId
EvidenceId
DecisionRecordId
StrategyVersionId
BacktestRunId
```

Do not use a generic `EntityId` across the domain. Static typing should make accidental cross-entity assignment difficult.

## Shared package rule

`shared/` is intentionally tiny.

Allowed shared concerns:
- opaque ID primitives;
- UTC/time helpers;
- exact-decimal helpers;
- base error/result types;
- correlation/trace context;
- generic immutable contract helpers.

Forbidden in `shared/`:
- financial features;
- market semantics;
- risk calculations;
- strategy logic;
- provider mapping;
- user-specific behavior;
- module repositories.

If a helper needs domain vocabulary, it belongs to the domain module.

## Persistence ownership

Every table has exactly one owner module. Ownership is declared in `PERSISTENCE_SCHEMA_BLUEPRINT.md`.

Cross-module foreign keys may reference stable identifiers, but:
- the referencing module owns the FK column;
- no cross-module `ON DELETE CASCADE` is allowed;
- deletion/purge behavior is explicit and policy-driven;
- an FK does not authorize direct ORM imports.

## Domain events

Events describe facts that already committed.

Naming convention:

```text
<module>.<aggregate>.<past_tense_fact>.v<schema>
```

Examples:
- `ingestion.receipt.normalized.v1`
- `market_state.snapshot.finalized.v1`
- `ledger.decision_record.finalized.v1`
- `rights.data_profile.revoked.v1`

Events are immutable. Consumers must tolerate duplicate delivery.

## Architecture-conformance tests

Phase 0 introduces automated checks that fail CI when:
- a Python module imports another module outside the allow-list;
- ORM models are imported across module persistence packages;
- `apps/web` contains provider SDK dependencies;
- `explanation` is imported upstream;
- production code imports from `experiments/`;
- provider adapter classes escape `ingestion/adapters`.

The first implementation may use a small AST/import-graph test rather than adopting a large architecture framework.

## Change rule

Changing an allowed dependency in a way that introduces new authority or a cycle requires architecture review. A cycle is never accepted as a temporary shortcut.

A new module requires:
1. documented responsibility;
2. owner tables/contracts;
3. place in the dependency graph;
4. failure behavior;
5. test responsibilities;
6. ADR when it changes a frozen invariant or trust boundary.