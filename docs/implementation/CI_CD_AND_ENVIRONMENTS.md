# CI/CD and Environment Contract

## Goal

Every deployment must be reproducible, reviewable and reversible without depending on a developer laptop.

## Environments

### `local`
- Docker-based dependencies where practical.
- Synthetic/test credentials only.
- No production provider keys.
- Seeded deterministic fixtures.

### `ci`
- Ephemeral PostgreSQL and object-storage test dependencies.
- Frozen clocks/fixtures where needed.
- No production user data.
- Network access denied by default except explicitly scoped jobs.

### `staging`
- Production-like topology and configuration shape.
- Separate database, storage, auth tenant and provider credentials.
- Used for migrations, failure injection, backup/restore rehearsal and release candidate validation.

### `production`
- No manual schema editing.
- No direct writes from developer machines.
- Changes only through reviewed deployment pipeline and audited emergency procedures.

## Branch and merge policy

- `main` is deployable at all times.
- Feature/design work occurs on branches through pull requests.
- Required checks must pass before merge.
- Force-push to protected `main` is prohibited.
- Release provenance records source commit, container digest, migration version and deployment timestamp.

## Pull-request gates

At minimum:
1. formatting/lint;
2. static typing;
3. unit/domain tests;
4. PostgreSQL integration tests when persistence is touched;
5. anti-leakage/golden replay suite for affected quantitative modules;
6. API/OpenAPI compatibility diff;
7. migration validation;
8. dependency/security scanning;
9. secret scanning;
10. container/SBOM generation for deployable units;
11. critical E2E smoke suite where applicable;
12. docs/link/ADR consistency checks for contract changes.

A change to a documented invariant without corresponding tests/ADR fails review.

## Build artifacts

Deployables are immutable container images identified by digest.

Each build emits:
- source commit SHA;
- dependency lockfile hash;
- SBOM;
- image digest;
- OpenAPI artifact;
- migration head revision;
- test summary;
- build timestamp and builder identity.

The same built artifact is promoted from staging to production; production is not rebuilt from source separately.

## Database migration policy

### General
- Alembic migrations are versioned and reviewed.
- Staging runs against a production-like schema/data-volume sample before production promotion.
- Migration code and application compatibility follow expand/contract where zero-downtime compatibility is needed.
- Destructive migrations require explicit backup/restore verification and retention review.

### Expand/contract sequence
1. expand schema compatibly;
2. deploy code that can use old + new form;
3. backfill/reconcile;
4. verify metrics/invariants;
5. switch reads/writes;
6. remove old structure in a later release.

Rollback does not rely on reverse migrations for destructive data changes. Prefer forward-fix plus restored backup when necessary.

## Deployment sequence

1. CI produces immutable artifacts.
2. Deploy release candidate to staging.
3. Run migrations.
4. Run staging smoke + replay + provider-contract checks.
5. Verify telemetry and error budgets.
6. Promote exact artifact digest to production.
7. Run post-deploy synthetic checks.
8. Observe defined canary window for high-risk changes.
9. Mark release complete only after health gates pass.

## Rollback

Application rollback must support previous compatible container digest.

Before deployment, pipeline records:
- prior application digest;
- prior config version;
- migration compatibility statement;
- feature-flag state.

If schema is forward-compatible, roll back application directly. If not, enter incident procedure; never improvise destructive rollback on production.

## Feature flags / kill switches

High-risk behavior ships behind server-controlled flags where useful:
- provider enablement;
- model version;
- explanation feature;
- new market-state algorithm;
- rights-sensitive display family;
- strategy evaluation class.

Flags are configuration, not a substitute for tests. Flag changes are audited.

## Configuration promotion

Non-secret configuration is versioned. Production config changes follow review and are tied to a release/config revision.

Secrets are never committed and are injected from the deployment secret store.

## Dependency policy

- exact versions locked;
- automated vulnerability/update signals reviewed;
- security patches on supported release lines are prioritized;
- major upgrades run full compatibility/golden suites;
- unmaintained critical dependencies trigger replacement planning.

## Supply-chain controls

Before beta:
- dependency lockfiles committed;
- provenance/SBOM available for deployables;
- base images pinned by digest in production build path;
- repository secret scanning enabled;
- CI credentials least-privilege and short-lived where platform supports it;
- third-party GitHub Actions pinned to immutable revisions where possible.

## Emergency changes

Emergency production changes still require:
- identified incident;
- smallest possible patch;
- peer/reviewer approval when available;
- automated tests appropriate to change;
- audited deployment;
- immediate follow-up PR/postmortem if standard process was shortened.

No emergency path may bypass regulatory/data-rights kill switches or introduce live execution into MK1.

## Production promotion gate

A release is blocked if any of the following is true:
- required CI check red/flaky without resolution;
- unresolved migration incompatibility;
- golden replay mismatch;
- active P0/P1 security defect;
- backup restore not proven within policy window;
- production rights configuration absent/expired;
- required provider health/freshness cannot satisfy product semantics;
- observability for the changed critical path is missing.