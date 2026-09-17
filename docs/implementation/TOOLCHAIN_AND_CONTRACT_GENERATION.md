# MK1 Toolchain and Contract Generation

## Purpose

This document freezes the development toolchain and the generated-contract workflow so Phase 0 can be reproduced from a clean machine without implementation-time choices.

It complements `TECH_STACK.md`; that file chooses technology families, while this file chooses the concrete developer workflow and sources of truth.

## Runtime baseline

At build start, use the latest security-patched release inside the already approved supported lines:

- Node.js 24 LTS line;
- Next.js 16 Active LTS line;
- Python 3.14 stable line;
- PostgreSQL 18 supported line.

The exact patch versions used by a release are pinned in toolchain/container metadata and lockfiles. Patch upgrades inside these lines do not require an ADR unless they change semantics or compatibility.

Do not move to Node Current, Python 3.15+, PostgreSQL 19+, or Next.js 17 merely because they exist; a line change requires compatibility review.

## Package managers

### Python

Use `uv` as the canonical Python environment/dependency/lock workflow.

Authority:
- `backend/pyproject.toml` — declared dependencies/tool config;
- `backend/uv.lock` — exact resolved dependency graph.

Rules:
- CI uses `uv sync --frozen` or equivalent frozen-lock behavior;
- production images install from the lockfile;
- ad-hoc `pip install` is not part of the build;
- notebooks/experiments use an explicit optional dependency group when they need additional tooling.

### JavaScript / TypeScript

Use `pnpm` workspaces.

Authority:
- `package.json` with exact `packageManager` field;
- `pnpm-workspace.yaml`;
- `pnpm-lock.yaml`.

Rules:
- CI uses frozen lockfile mode;
- package-manager version is pinned through Corepack/package metadata;
- no npm/yarn lockfiles are committed.

## Python engineering tools

Canonical tool families:
- Ruff — formatting/linting/import hygiene;
- Pyright — static type checking;
- pytest — test runner;
- Hypothesis — property-based tests for numerical/time/state invariants;
- SQLAlchemy 2 style — persistence;
- Alembic — migrations;
- FastAPI/Pydantic — HTTP/schema boundary.

Required CI commands are wrapped in repository scripts but must remain runnable directly from the locked environment.

## Web engineering tools

Canonical tool families:
- TypeScript `strict: true`;
- ESLint executed directly, using Next.js-compatible rules;
- Prettier for formatting unless a later single-tool formatting ADR replaces it;
- Vitest for pure component/utility tests where appropriate;
- Playwright for E2E/browser/accessibility flows;
- generated OpenAPI client/types for API access.

Next.js financial semantics are not tested by duplicating backend calculations in TypeScript.

## Contract source-of-truth hierarchy

### HTTP API

Source of truth:

```text
Python application contracts
  -> Pydantic/FastAPI schema
  -> generated OpenAPI document
  -> committed reviewed snapshot
  -> generated TypeScript client/types
```

Canonical file:

```text
contracts/openapi/v1.json
```

CI fails when generated OpenAPI differs from the committed snapshot without the PR containing the reviewed contract change.

The TypeScript generated client is not authoritative and may be regenerated at any time.

### JSON Schema

JSON Schema snapshots are generated only for contracts that benefit from language-neutral artifact validation, such as:
- strategy DSL/specification;
- experiment/manifest artifacts;
- selected immutable artifact envelopes.

Canonical snapshots live under:

```text
contracts/jsonschema/
```

A JSON Schema does not supersede the domain invariant implementation; it is an interchange/validation contract.

### Events

Internal outbox events use explicitly versioned Python contracts. Representative event fixture schemas are checked into `contracts/fixtures/` for compatibility tests.

No external schema registry is required in MK1.

## Generated-code policy

Generated code must carry a header indicating its source and generation command.

Generated directories:
- may be deleted/regenerated;
- are not edited manually;
- are reviewed for semantic diff, not style;
- never contain secrets.

CI runs generation twice or compares clean-tree output so non-deterministic generators are caught.

## Contract-generation commands

Phase 0 creates stable scripts conceptually equivalent to:

```text
scripts/contracts/export-openapi
scripts/contracts/generate-web-client
scripts/contracts/export-jsonschema
scripts/contracts/check-clean
```

The exact shell/Python wrapper is implementation detail, but the commands must:
1. run from a clean checkout;
2. use frozen dependencies;
3. produce deterministic output;
4. fail non-zero on incompatible or dirty drift.

## Versioning rules

- API breaking changes require `/v2` or an explicitly versioned media/schema contract.
- additive optional fields may remain `/v1` when old meaning is unchanged.
- event payload breaking changes increment event schema version.
- immutable artifact schemas carry explicit schema versions.
- strategy DSL semantic changes create a new parser/compiler semantic version and never reinterpret prior hashes.

## CI gate order

The default PR pipeline is ordered to fail cheaply:

1. repository/lockfile sanity;
2. formatting/lint/import-boundary checks;
3. static type checks;
4. pure unit/property tests;
5. contract generation + clean diff;
6. PostgreSQL migration/integration tests;
7. provider contract fixtures for affected adapters;
8. anti-leakage/golden/accounting suites for affected modules;
9. web unit/build checks;
10. browser E2E/accessibility on required paths;
11. security/static supply-chain scans;
12. container build + SBOM/provenance;
13. staging-only gates where applicable.

Path filtering may skip expensive unaffected suites only when dependency mapping proves they are not impacted.

## Dependency and container security

Phase 0 must establish:
- dependency vulnerability scanning for Python/Node lockfiles;
- container/image scanning;
- SBOM generation for deployable images;
- digest-pinned production base images;
- provenance tying image digest to source commit, lockfiles and build workflow.

Scanner warnings are triaged by severity/reachability rather than ignored or blindly suppressing the tool.

Suppressions require:
- vulnerability/advisory id;
- reason;
- owner;
- expiry/review date.

## Reproducibility

A build record contains:
- git commit;
- bootstrap-profile id once MK1 build is authorized;
- Node/Python/PostgreSQL/Next supported-line snapshot;
- exact lockfile digests;
- container base-image digests;
- generated contract digests;
- build timestamp/environment identity;
- produced image/artifact digests;
- SBOM reference.

## Test-network policy

Unit/contract/golden CI has no uncontrolled internet dependency.

Live provider/model smoke tests are separate jobs/environments with:
- explicit credentials;
- rate limits;
- no promotion authority by themselves;
- recorded provider/version/time;
- graceful skip/fail classification when external availability is the only failure.

A live smoke test never replaces deterministic fixtures.

## Local development

Canonical local prerequisites:
- supported Node/Python toolchains;
- `uv`;
- `pnpm`/Corepack;
- Docker-compatible container runtime with Compose;
- Git.

Local services start through repository-owned Compose definitions:
- PostgreSQL;
- S3-compatible object-store emulator;
- optional local telemetry collector.

No developer needs Kafka, Kubernetes, Redis or cloud credentials for normal local development.

## Environment parity

Local/dev/staging/production share:
- the same application container images where feasible;
- the same migrations;
- the same contract artifacts;
- the same configuration schema.

They differ by externally supplied configuration/credentials, not by code branches.

## Toolchain acceptance gate

Phase 0 is not complete until a clean checkout can deterministically:
- restore exact package-manager versions;
- install both lockfiles in frozen mode;
- format/lint/type-check successfully;
- generate contracts with no uncommitted drift;
- run PostgreSQL integration tests;
- build web/API/worker containers;
- produce SBOM + image/source provenance;
- start the stack locally without external paid services.