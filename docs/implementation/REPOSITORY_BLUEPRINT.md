# MK1 Repository Blueprint

## Purpose

This document freezes the physical repository shape used when MK1 implementation is eventually authorized. The goal is to ensure Phase 0 is mechanical: build tooling and code placement should not require new architecture decisions.

This is a pre-build contract only. It does not authorize production implementation while `BUILD_READINESS.md` remains blocked.

## Repository shape

```text
SOPHROSYNE/
├── apps/
│   └── web/
│       ├── src/
│       │   ├── app/
│       │   ├── components/
│       │   ├── features/
│       │   ├── lib/
│       │   └── generated/api/
│       ├── tests/
│       ├── package.json
│       └── tsconfig.json
│
├── backend/
│   ├── src/sophrosyne/
│   │   ├── entrypoints/
│   │   │   ├── api/
│   │   │   └── worker/
│   │   ├── modules/
│   │   │   ├── identity/
│   │   │   ├── catalog/
│   │   │   ├── rights/
│   │   │   ├── ingestion/
│   │   │   ├── evidence/
│   │   │   ├── market_state/
│   │   │   ├── scenario/
│   │   │   ├── risk/
│   │   │   ├── portfolio/
│   │   │   ├── strategy/
│   │   │   ├── research/
│   │   │   ├── ledger/
│   │   │   ├── explanation/
│   │   │   └── audit/
│   │   ├── platform/
│   │   │   ├── db/
│   │   │   ├── jobs/
│   │   │   ├── object_store/
│   │   │   ├── observability/
│   │   │   ├── auth/
│   │   │   └── config/
│   │   └── shared/
│   │       ├── ids.py
│   │       ├── time.py
│   │       ├── decimal.py
│   │       ├── errors.py
│   │       └── contracts.py
│   ├── migrations/
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   ├── contract/
│   │   ├── anti_leakage/
│   │   ├── golden/
│   │   ├── security/
│   │   └── e2e_support/
│   ├── pyproject.toml
│   ├── uv.lock
│   └── alembic.ini
│
├── contracts/
│   ├── openapi/v1.json
│   ├── jsonschema/
│   └── fixtures/
│
├── fixtures/
│   ├── providers/
│   ├── market_time/
│   ├── accounting/
│   ├── leakage/
│   └── golden_decisions/
│
├── infra/
│   ├── containers/
│   ├── compose/
│   └── observability/
│
├── scripts/
│   ├── bootstrap/
│   ├── contracts/
│   ├── ci/
│   └── maintenance/
│
├── experiments/
├── docs/
├── adr/
├── .github/
│   └── workflows/
├── pnpm-workspace.yaml
├── package.json
├── pnpm-lock.yaml
└── README.md
```

## Deployable units

There are exactly three application deployables in MK1:

1. `apps/web` — Next.js presentation layer.
2. `backend` API entrypoint — FastAPI synchronous authoritative boundary.
3. `backend` worker entrypoint — asynchronous/research worker process.

The API and worker are two entrypoints of **one Python distribution**, not duplicated services with separate domain packages. They share the same versioned module code and differ only in startup wiring and permissions.

## Python module shape

Each domain module follows a deliberately small internal shape:

```text
modules/<name>/
├── domain.py          # pure entities/value objects/invariants
├── contracts.py       # public module DTOs/ports/events
├── service.py         # application use cases
├── repository.py      # repository interfaces, not SQLAlchemy models
├── persistence.py     # SQLAlchemy implementation owned by module
├── api.py             # HTTP router only when module exposes HTTP
├── jobs.py            # job handlers owned by module when needed
└── tests/             # optional colocated narrow unit tests
```

A module may split a file only after size/ownership pressure is observed. Creating `domain/`, `application/`, `infrastructure/` directory forests preemptively is prohibited.

## Web shape

The web tier is feature-oriented. It may contain presentation state and formatting, but no independent financial/business truth.

Rules:
- API types are generated into `src/generated/api/` and never hand-edited;
- financial decimal values remain strings until formatting/display conversion;
- domain decisions are never reimplemented in TypeScript;
- browser components may derive presentation-only values such as labels, sorting and local visibility state;
- provider SDKs and provider credentials are forbidden in `apps/web`.

## Contract boundary

The HTTP boundary is OpenAPI-first **from the running Python source of truth**:

```text
Pydantic/FastAPI schemas
        ↓
generated OpenAPI snapshot
        ↓
reviewed contracts/openapi/v1.json
        ↓
generated TypeScript client/types
```

Generated client code is disposable. OpenAPI drift is a CI-visible change.

No handwritten shared Python/TypeScript domain package is allowed because it would create two authoritative semantic implementations.

## Migrations

- Alembic is the only production schema migration mechanism.
- Migration files live only under `backend/migrations`.
- One linear migration head is required for normal merges.
- Merge migrations are allowed only to reconcile concurrent approved branches and must be reviewed explicitly.
- Application startup never auto-runs migrations.
- CI proves both clean-database migration and upgrade from the previous supported schema snapshot.

## Fixtures

Fixtures are first-class reviewed assets.

Provider fixtures must retain only data permitted by the applicable rights contract. When raw payload retention is forbidden, a synthetic contract-equivalent fixture is used instead.

`fixtures/golden_decisions/` contains only deterministic, legally retainable replay material.

## Package/tool ownership

- Python dependency authority: `backend/pyproject.toml` + `backend/uv.lock`.
- JavaScript dependency authority: root/package-level `package.json` + `pnpm-lock.yaml`.
- Container base images are digest-pinned during implementation.
- generated files never become the only source of semantic truth.

## Repository dependency rule

`apps/web` may depend on generated HTTP contracts only.

`backend/modules/*` may depend on other modules only through public contracts allowed by `MODULE_BOUNDARIES.md`.

`backend/platform/*` provides technical capabilities but cannot contain domain decisions.

`experiments/` may import production domain libraries for evaluation only after those libraries exist; production code may not import experiment notebooks/scripts.

## Forbidden repository patterns

- `utils.py` / `helpers.py` dumping grounds across unrelated domains;
- provider-specific models outside `ingestion` adapters;
- SQLAlchemy models imported across module persistence boundaries;
- notebooks as production modules;
- duplicated API and worker domain implementations;
- frontend copies of risk/strategy/market-state algorithms;
- runtime-generated migrations;
- committed secrets or `.env` files containing credentials;
- generated API client edits by hand.

## Phase-0 completion evidence

When build is authorized, the repository skeleton is complete only when a clean environment can:

1. restore exact toolchains;
2. install from lockfiles;
3. start PostgreSQL/object storage locally;
4. run an empty Alembic migration chain;
5. start API, worker and web health endpoints;
6. generate OpenAPI and TypeScript client deterministically;
7. run lint/type/unit/DB smoke checks;
8. build immutable containers;
9. emit SBOM/provenance artifacts;
10. deploy the same built artifacts to staging.

No business feature is required for this Phase-0 gate.