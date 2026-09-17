# MK1 Pre-Build Technical Definition of Ready

## Purpose

This is the final technical gate before Phase 0 implementation may begin **after** MK0 evidence promotion authorizes a concrete bootstrap profile.

It answers a narrower question than `BUILD_READINESS.md`:

> If the product/evidence gates were green today, could engineering begin without inventing architecture, repository, persistence, contract, async, testing or delivery semantics during coding?

The answer must be **yes** before build starts.

## Current status

**TECHNICAL DESIGN: CLOSED FOR PRE-BUILD**

**PRODUCTION BUILD: STILL BLOCKED BY MK0 EVIDENCE / PROMOTION**

This document does not override Q00–Q05, Q01/Q02 external authority, the promotion packet or bootstrap-profile requirements.

## Required pre-build contracts

The following must exist and agree:

- `REFERENCE_ARCHITECTURE.md` — deployable/runtime topology;
- `TECH_STACK.md` — technology families/support lines;
- `REPOSITORY_BLUEPRINT.md` — physical monorepo layout;
- `MODULE_BOUNDARIES.md` — dependency/import ownership;
- `DATA_MODEL.md` — logical domain persistence;
- `PERSISTENCE_SCHEMA_BLUEPRINT.md` — PostgreSQL physical conventions;
- `API_CONTRACTS.md` — HTTP semantics;
- `ASYNC_JOB_AND_EVENT_CONTRACTS.md` — outbox/jobs/retries;
- `TOOLCHAIN_AND_CONTRACT_GENERATION.md` — reproducible toolchain/contracts;
- `CONFIGURATION_AND_SECRETS.md` — config/secret boundaries;
- `FAILURE_AND_DEGRADATION.md` — fail-safe semantics;
- `OBSERVABILITY_AND_SLOS.md` — telemetry/SLO contract;
- `SECURITY_CONTROLS.md` — trust/security controls;
- `TEST_STRATEGY.md` — verification layers;
- `CI_CD_AND_ENVIRONMENTS.md` — promotion/rollback environment contract;
- `IMPLEMENTATION_SEQUENCE.md` — build order;
- `FIRST_VERTICAL_SLICE.md` — first end-to-end implementation target.

No contradictory current contract may exist at build start.

## Technical decisions that must be frozen

### Repository

- monorepo layout fixed;
- one Python distribution with API + worker entrypoints;
- Next.js web is presentation only;
- experiments never imported by production code;
- generated TS client is disposable/non-authoritative.

### Module architecture

- module allow-list/dependency graph fixed;
- no cyclic domain dependency;
- table ownership fixed;
- provider SDK boundary fixed to ingestion adapters;
- explanation remains downstream only.

### Persistence

- PostgreSQL schema ownership fixed;
- UUID/decimal/timestamp conventions fixed;
- RLS approach fixed for user-owned data;
- DecisionRecord DB immutability mechanism fixed;
- migration ownership/classification fixed;
- no speculative partitioning.

### API/contracts

- `/v1` contract/versioning semantics fixed;
- decimal strings and UTC timestamp serialization fixed;
- RFC 7807-style errors fixed;
- OpenAPI snapshot generation/review fixed;
- idempotency and optimistic-concurrency rules fixed.

### Async

- PostgreSQL outbox/job model fixed;
- at-least-once + idempotent processing fixed;
- lease/retry/terminal-error semantics fixed;
- initial job type allow-list fixed;
- no order/execution jobs in MK1.

### Toolchain

- supported runtime lines fixed;
- `uv` + locked Python graph fixed;
- `pnpm` + locked JS graph fixed;
- lint/type/test tool families fixed;
- deterministic contract generation fixed;
- SBOM/provenance requirement fixed.

### Verification

- anti-leakage tests mandatory;
- real PostgreSQL integration tests mandatory;
- golden DecisionRecord replay mandatory;
- provider contract fixtures mandatory;
- architecture-import tests mandatory;
- E2E/accessibility/security gates defined;
- failure injection before beta defined.

## Build-time values that remain evidence-derived

The following are intentionally **not** hard-coded by this pre-build contract and must come from the approved `MK1_BOOTSTRAP_PROFILE`:

- initial persona/JTBD/wedge;
- exact first asset/instrument universe;
- exact provider/data product;
- DataUseProfiles and rights constraints;
- selected first data families;
- freshness profiles;
- pricing/entitlement hypothesis;
- exact Q00-surviving component set;
- risk-policy version;
- deterministic feature/state configuration;
- ML scope (`INCLUDE | EXCLUDE | DEFER`);
- legal/claim/disclaimer constraints;
- moat/scale-spend status.

Engineering may not replace a missing bootstrap value with a convenient default.

## Phase 0 authorization checklist

Once MK0 promotion is approved, Phase 0 may open only if all are true:

1. branch protection/review policy for implementation branches is active;
2. exact supported runtime patch versions are selected and recorded;
3. Python/Node package-manager versions are pinned;
4. repository skeleton matches `REPOSITORY_BLUEPRINT.md`;
5. lockfiles can be created without prerelease/unsupported dependencies unless explicitly approved;
6. local PostgreSQL/object storage/telemetry topology is specified;
7. config schema exists with no secret defaults;
8. migration framework initialized;
9. OpenAPI export/client generation path specified;
10. CI pipeline stages mapped to `TEST_STRATEGY.md`;
11. container/SBOM/provenance path specified;
12. staging deployment target/config boundary selected;
13. first vertical slice references the approved bootstrap profile;
14. no production feature code has been written outside the authorized profile.

## Phase 0 exit checklist

Phase 0 is complete only when a clean clone can, without paid/external provider dependencies:

- install from frozen lockfiles;
- run formatting/lint/type checks;
- run unit/property smoke tests;
- migrate an empty PostgreSQL 18 database;
- start API/worker/web health endpoints;
- start S3-compatible local artifact storage;
- generate OpenAPI + web client deterministically;
- execute architecture/import-boundary tests;
- build API/worker/web immutable containers;
- generate SBOM/provenance;
- deploy the same image digests to staging;
- destroy/recreate local state successfully.

No business feature is needed to pass Phase 0.

## Slice-1 entry checklist

The first vertical slice may begin only when:

- Phase 0 passes;
- approved bootstrap profile identifies provider/data/instrument/component scope;
- first provider contract fixture set is legally retainable or synthetic equivalent exists;
- exact DataRightsRecord semantics are known;
- point-in-time timestamp mapping is known for that provider;
- first deterministic MarketState configuration is frozen;
- golden fixture set is preregistered/defined;
- rights/staleness/degradation expectations are testable.

## Technical reopen triggers

This pre-build design reopens when evidence or implementation proves one of the following:

- modular-monolith boundary cannot meet a measured isolation/scale requirement;
- PostgreSQL job/outbox model cannot meet measured backlog/latency/recovery requirements;
- PostgreSQL 18 selected semantics are incompatible with hosting constraints;
- RLS approach cannot be made safe with the connection/session model;
- provider semantics require a data model not representable without breaking point-in-time invariants;
- first vertical slice requires a cyclic module dependency;
- contract generation is non-deterministic or cannot preserve API compatibility;
- required security/legal isolation introduces a new trust boundary.

A reopen is explicit. Coding around it silently is forbidden.

## What does not reopen technical design by itself

- a library implementation preference inside an existing contract;
- code organization refactor that preserves module/API semantics;
- patch-level runtime/security upgrades;
- performance optimizations that preserve observable behavior;
- visual/component implementation choices inside UX contracts.

## Final pre-build invariant

> When build starts, developers choose implementations inside frozen contracts; they do not choose product truth, financial semantics, authority boundaries, data-rights assumptions, module ownership or point-in-time rules.

That is the threshold for SOPHROSYNE to move from design into build.