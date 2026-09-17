# CI/CD and Environment Contract

## Goal

Every deployment must be reproducible, reviewable and reversible without depending on a developer laptop, and must prove it implements the same approved bootstrap profile and Closed Validation Graph snapshot that authorized the build.

## Environments

### `local`
- Docker-based dependencies where practical.
- Synthetic/test credentials only.
- No production provider keys.
- Seeded deterministic fixtures.
- Graph validation may run with `PENDING_PHASE0_HASH` only before Phase 0 digest tooling is complete.

### `ci`
- Ephemeral PostgreSQL and object-storage test dependencies.
- Frozen clocks/fixtures where needed.
- No production user data.
- Network access denied by default except explicitly scoped jobs.
- Canonical CVG validation runs on every change affecting graph, profile, design contracts, implementation surfaces or acceptance receipts.

### `staging`
- Production-like topology and configuration shape.
- Separate database, storage, auth tenant and provider credentials.
- Used for migrations, failure injection, backup/restore rehearsal and release candidate validation.
- Exact release graph/profile/build digests must be visible in deployment metadata.

### `production`
- No manual schema editing.
- No direct writes from developer machines.
- Changes only through reviewed deployment pipeline and audited emergency procedures.
- Deployed artifact must match the graph/profile/build tuple certified in staging.

## Branch and merge policy

- `main` is deployable at all times.
- Feature/design work occurs on branches through pull requests.
- Required checks must pass before merge.
- Force-push to protected `main` is prohibited.
- Release provenance records source commit, container digest, migration version, bootstrap profile id/digest, graph version/digest and deployment timestamp.
- A PR changing a P0/P1 graph node/edge, authority boundary or reachability must declare whether revalidation and/or an ADR is required.

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
12. docs/link/ADR consistency checks for contract changes;
13. CVG schema + referential-integrity validation;
14. P0/P1 orphan/dangling-edge detection;
15. reverse-validation reachability check for affected material paths;
16. bootstrap-profile -> active implementation reachability check;
17. graph/profile metadata consistency check;
18. graph semantic diff classification for material changes.

A change to a documented invariant without corresponding tests/ADR fails review.

A graph/profile mismatch or P0/P1 graph-integrity failure cannot be overridden by unrelated green tests.

## Graph semantic diff classes

Every graph-impacting change is classified before merge:

### `NON_SEMANTIC`
Formatting/metadata-only change with no node/edge meaning or reachability change.

### `COMPATIBLE_ADDITIVE`
Adds a currently inactive/non-authoritative node/edge without changing existing P0/P1 closure or release paths. Requires graph validation; may require profile update before activation.

### `REVALIDATION_REQUIRED`
Changes active P0/P1 scope, required edge, closure requirement, reverse-validation path, receipt binding or profile reachability. Affected receipts become stale and promotion/release pauses for that scope.

### `BREAKING_GOVERNANCE`
Removes/bypasses required authority, creates an orphan, destroys a return path or changes a fatal gate. Requires ADR, explicit reopen and new closure evidence.

CI must not infer `NON_SEMANTIC` merely from file type or small diff size.

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
- bootstrap profile id/version/digest;
- graph schema version;
- graph version;
- graph digest;
- affected node/edge set for the build change;
- `GRAPH_CONFORMANCE` receipt reference where required;
- build timestamp and builder identity.

The same built artifact is promoted from staging to production; production is not rebuilt from source separately.

After Phase 0 hashing is available, an artifact without graph/profile digests is not promotable.

## Database migration policy

### General
- Alembic migrations are versioned and reviewed.
- Staging runs against a production-like schema/data-volume sample before production promotion.
- Migration code and application compatibility follow expand/contract where zero-downtime compatibility is needed.
- Destructive migrations require explicit backup/restore verification and retention review.
- A migration that changes an authoritative persistence invariant must declare graph/design impact rather than being treated as storage-only work.

### Expand/contract sequence
1. expand schema compatibly;
2. deploy code that can use old + new form;
3. backfill/reconcile;
4. verify metrics/invariants;
5. switch reads/writes;
6. remove old structure in a later release.

Rollback does not rely on reverse migrations for destructive data changes. Prefer forward-fix plus restored backup when necessary.

## Deployment sequence

1. CI validates source, profile and graph integrity.
2. CI produces immutable artifacts with graph/profile/build provenance.
3. Deploy release candidate to staging.
4. Run migrations.
5. Run staging smoke + replay + provider-contract + graph-conformance checks.
6. Verify telemetry and error budgets.
7. Verify release graph/profile digests equal the certified candidate.
8. Promote exact artifact digest to production.
9. Run post-deploy synthetic checks.
10. Observe defined canary window for high-risk changes.
11. Mark release complete only after health gates and graph conformance pass.

## Rollback

Application rollback must support previous compatible container digest.

Before deployment, pipeline records:
- prior application digest;
- prior config version;
- prior bootstrap profile id/digest;
- prior graph version/digest;
- migration compatibility statement;
- feature-flag state.

If schema is forward-compatible, roll back application directly to the exact prior compatible artifact/profile/graph tuple. If not, enter incident procedure; never improvise destructive rollback on production.

A rollback to a build whose graph/profile no longer has valid required authority is prohibited; use incident containment/kill switches and an explicitly valid recovery target instead.

## Feature flags / kill switches

High-risk behavior ships behind server-controlled flags where useful:
- provider enablement;
- model version;
- explanation feature;
- new market-state algorithm;
- rights-sensitive display family;
- strategy evaluation class.

Flags are configuration, not a substitute for tests or graph authority. Flag changes are audited.

A flag cannot activate a node/component excluded by the approved bootstrap profile or unreachable from the active graph.

## Configuration promotion

Non-secret configuration is versioned. Production config changes follow review and are tied to a release/config revision, bootstrap profile and graph snapshot where material.

Secrets are never committed and are injected from the deployment secret store.

A material config change triggering a declared `revalidate_on` condition invalidates the affected receipt until rerun.

## Dependency policy

- exact versions locked;
- automated vulnerability/update signals reviewed;
- security patches on supported release lines are prioritized;
- major upgrades run full compatibility/golden suites;
- unmaintained critical dependencies trigger replacement planning.

A dependency upgrade is not a graph-semantic change by default, but becomes one if it changes an authoritative behavior or trust boundary.

## Supply-chain controls

Before beta:
- dependency lockfiles committed;
- provenance/SBOM available for deployables;
- base images pinned by digest in production build path;
- repository secret scanning enabled;
- CI credentials least-privilege and short-lived where platform supports it;
- third-party GitHub Actions pinned to immutable revisions where possible;
- graph/profile provenance included with release artifacts;
- `GRAPH_CONFORMANCE` receipt is non-waivable for active P0/P1 release paths.

## Emergency changes

Emergency production changes still require:
- identified incident;
- smallest possible patch;
- peer/reviewer approval when available;
- automated tests appropriate to change;
- graph/profile impact classification;
- audited deployment;
- immediate follow-up PR/postmortem if standard process was shortened.

No emergency path may bypass regulatory/data-rights kill switches, fatal CVG edges, graph-conformance integrity or introduce live execution into MK1.

If emergency containment requires temporarily disabling an active surface, the graph/profile state is reconciled immediately after containment; history is not rewritten.

## Production promotion gate

A release is blocked if any of the following is true:
- required CI check red/flaky without resolution;
- graph schema/referential-integrity check fails;
- any active P0/P1 node is orphaned;
- any REQUIRED edge for a closed/promotable target is not closed;
- any active material implementation path lacks a reverse-validation path;
- release build/profile/graph digests disagree;
- required `GRAPH_CONFORMANCE` receipt is absent, stale or FAIL;
- unresolved P0/P1 contradiction/revalidation requirement exists on an active release path;
- unresolved migration incompatibility;
- golden replay mismatch;
- active P0/P1 security defect;
- backup restore not proven within policy window;
- production rights configuration absent/expired;
- required provider health/freshness cannot satisfy product semantics;
- observability for the changed critical path is missing.

A previously certified release is not permanently certified. Runtime incidents, provider/rights changes, drift or other declared triggers can invalidate receipts/edges and force targeted revalidation under ADR-0016.
