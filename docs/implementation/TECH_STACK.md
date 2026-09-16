# MK1 Technology Stack

## Objective

Choose a conservative, supportable stack optimized for correctness, reproducibility and low operational complexity.

## Frozen choices for MK1

### Web
- Next.js 16 Active LTS line.
- Node.js 24 LTS line.
- TypeScript with `strict: true`.
- Server-side session handling; browser receives no provider/API secrets.
- Financial/domain computation is prohibited in the web tier except presentation-only transformations.

### Core API and workers
- Python 3.14 stable line.
- FastAPI for HTTP boundary.
- Pydantic for explicit request/response/domain boundary schemas.
- SQLAlchemy 2-style data access and Alembic migrations.
- Decimal-safe financial calculations; binary floating point is prohibited for money, price, quantity, fees and accounting identities.

### Database
- PostgreSQL 18 stable line.
- UTC timestamps only.
- `numeric` for financial quantities requiring decimal exactness.
- native JSONB only for versioned opaque/provider payloads and manifests, never as a substitute for core relational design.
- declarative partitioning only when measured table size/query behavior justifies it.

### Artifact storage
- S3-compatible object storage behind an internal adapter.
- Content-addressed or immutable keys for research/model/backtest artifacts.
- Local development may use an S3-compatible emulator; provider choice is deployment configuration, not domain logic.

### Queueing and background jobs

MK1 does not require an external message broker.

Durable jobs and the transactional outbox live in PostgreSQL. Workers claim work with `FOR UPDATE SKIP LOCKED`, leases, attempt counters and deterministic idempotency keys.

A broker such as Redis/Kafka may only be introduced after measured throughput/latency evidence through an ADR.

### Authentication
- OIDC/OAuth 2.1 compatible managed identity provider.
- Authorization remains internal to SOPHROSYNE.
- Browser flow uses Authorization Code + PKCE where applicable.
- Server sessions use secure, HTTP-only, same-site cookies.
- No financial provider credentials are stored in browser local storage.

### Observability
- OpenTelemetry-compatible traces/metrics.
- structured JSON logs.
- request/trace IDs propagated web → API → worker.
- vendor-neutral instrumentation; backend vendor is replaceable.

## Version policy

The repository pins exact dependency versions in lockfiles/container digests during implementation. Major/runtime upgrades require CI compatibility checks and an ADR when semantics or support windows materially change.

Security patches within the selected supported line are mandatory.

## Why this stack

- Python keeps quantitative research, validation and production inference in one language.
- PostgreSQL provides transactions, point-in-time relational integrity, durable job coordination and enough analytical capability for MK1's deliberately narrow asset set.
- Next.js provides a mature web delivery model while remaining isolated from financial truth.
- Avoiding a broker and microservices eliminates two major classes of early distributed-system failure.

## Explicit non-choices for MK1

- no MongoDB for canonical financial/domain state;
- no vector database as authoritative evidence storage;
- no Kubernetes requirement;
- no Kafka requirement;
- no serverless-only worker model for long/reproducible research jobs;
- no provider SDK types outside adapters;
- no direct browser access to market-data providers;
- no unpinned production dependencies.

## Portability requirement

Production must run from containers with externally supplied configuration. Managed providers may host the components, but the application must remain portable across compatible PostgreSQL, S3 and OIDC services.