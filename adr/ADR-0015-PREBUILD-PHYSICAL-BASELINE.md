# ADR-0015 — Pre-Build Physical Architecture Baseline

**Status:** ACCEPTED

## Context

SOPHROSYNE already has a closed logical architecture, but implementation could still drift if engineers independently choose repository layout, module import rules, database organization, async semantics, package managers, generated-contract flow or first-slice boundaries.

Those decisions are implementation-shaping and high leverage. Leaving them implicit would move architecture back into coding.

## Decision

MK1 freezes the following physical baseline before product implementation:

1. **Monorepo** with `apps/web`, one Python `backend` distribution, contracts, fixtures, infra, scripts, experiments and docs.
2. **One Python distribution, two entrypoints**: API and worker share the same module/domain code.
3. **Module boundaries are explicit and acyclic**; cross-module writes go through application services or outbox events, never direct foreign persistence mutation.
4. **PostgreSQL schemas expose table ownership** and user-owned data receives RLS defense-in-depth.
5. **UUIDv7 + exact-decimal + explicit UTC/time semantics** are the default physical representation choices.
6. **PostgreSQL transactional outbox/jobs** use at-least-once delivery, leases and idempotent handlers; no external broker is an MK1 prerequisite.
7. **OpenAPI is generated from the authoritative Python boundary**, committed as a reviewed snapshot, and used to generate disposable TypeScript API types/client code.
8. **`uv` and `pnpm`** are the package/lock workflows for Python and JavaScript respectively.
9. **The first production-quality vertical slice** is provider -> receipt -> normalization -> evidence -> deterministic MarketState -> immutable DecisionRecord -> API -> minimal web view.
10. **No Q00-excluded component may re-enter during build by convenience.**
11. These decisions do not authorize build until the evidence-derived `MK1_BOOTSTRAP_PROFILE` and `BUILD_READINESS` gates pass.

Canonical detail:
- `docs/implementation/REPOSITORY_BLUEPRINT.md`
- `docs/implementation/MODULE_BOUNDARIES.md`
- `docs/implementation/PERSISTENCE_SCHEMA_BLUEPRINT.md`
- `docs/implementation/ASYNC_JOB_AND_EVENT_CONTRACTS.md`
- `docs/implementation/TOOLCHAIN_AND_CONTRACT_GENERATION.md`
- `docs/implementation/FIRST_VERTICAL_SLICE.md`
- `docs/implementation/PREBUILD_TECHNICAL_DOR.md`

## Consequences

- Phase 0 becomes a reproducible substrate build rather than an architecture-design session.
- API and worker cannot silently diverge into separate domain implementations.
- frontend code cannot become a second financial/business authority.
- persistence and async behavior become testable before product features expand.
- provider #2, broker infrastructure, microservices, Kafka/Redis, speculative partitioning and other complexity require measured need rather than anticipation.
- the exact provider, asset/data profile, feature set and ML scope remain evidence-derived and are **not** hard-coded by this ADR.

## Reopen conditions

This ADR must be superseded when measured evidence shows that one of its physical assumptions cannot satisfy an approved MK1 profile without violating an invariant. Examples include:
- required security/regulatory isolation incompatible with one Python deployable codebase;
- measured PostgreSQL job/backlog failure requiring a broker;
- hosting requirements incompatible with the chosen persistence/runtime line;
- RLS/session model cannot be made safe;
- a provider/data profile cannot be represented without breaking point-in-time or rights semantics;
- module graph becomes cyclic under a legitimately approved feature.

A preference for another framework/tool is not sufficient evidence to supersede this ADR.

## Non-goals

This ADR does not choose:
- the production cloud/vendor;
- the first market-data provider;
- the first exact asset universe;
- pricing;
- ML inclusion;
- live execution;
- a second provider;
- a future service-extraction topology.

Those remain evidence/profile dependent.