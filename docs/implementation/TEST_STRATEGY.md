# MK1 Test Strategy

## Principle

Tests must prove domain invariants, point-in-time correctness, authorization and failure behavior—not only happy-path HTTP responses.

A release is blocked by any failing test in a mandatory gate. Flaky tests are treated as defects, not retried until green without investigation.

## Test pyramid

### 1. Domain unit tests — mandatory on every PR

Cover pure logic without network or database when possible:
- Evidence/Claim/Scenario semantic separation;
- state-machine transitions and forbidden transitions;
- freshness classification;
- risk independence from scenario/model conviction;
- deterministic strategy semantics;
- exact decimal arithmetic;
- idempotency decision logic;
- rights-policy decisions;
- probability/calibration guards;
- `NO_CONCLUSION` and `NOT_EVALUABLE` behavior.

Property-based tests are required for high-risk numerical/time invariants such as:
- position/risk arithmetic;
- timestamp ordering;
- strategy parser/compiler round trips;
- idempotency keys;
- probability ranges;
- aggregation identities.

### 2. Database integration tests — mandatory on every PR affecting persistence

Run against real PostgreSQL, not SQLite emulation.

Verify:
- migrations from clean database;
- constraints/indexes;
- transaction rollback;
- finalized DecisionRecord immutability;
- concurrent idempotent requests;
- worker claiming via `SKIP LOCKED`/leases;
- row/user isolation policies;
- outbox atomicity;
- optimistic concurrency;
- retention/rights queries.

### 3. Provider contract tests

Every adapter ships with immutable captured/synthetic fixtures representing:
- normal payload;
- missing fields;
- duplicate event;
- correction/update;
- rate limit response;
- timeout;
- schema drift/unknown enum;
- malformed timestamp;
- unavailable market/holiday where relevant.

Live-provider smoke tests run separately with low rate and never become the only validation source.

Adapter tests assert provider types never leak into normalized domain interfaces.

### 4. Point-in-time / anti-leakage tests

Mandatory for research and market-state code.

Tests must fail if:
- data with `available_at > as_of` enters a historical computation;
- revised data is silently substituted into `KNOWLEDGE_AS_OF_THEN`;
- future corporate-action knowledge leaks backward;
- train/validation/test windows overlap incorrectly;
- normalization uses future global statistics;
- labels/features are misaligned by timestamp.

At least one synthetic dataset intentionally containing future leakage is required to prove the guard detects it.

### 5. Golden DecisionRecord replay tests

For the golden corpus, CI replays deterministic records and asserts:
- content hash/semantic equality;
- lineage completeness;
- stable error/degradation states;
- no newly displayed probability without calibration;
- expected rights filtering.

Any intentional semantic change requires reviewed fixture/version migration plus ADR/changelog note.

### 6. Backtest validation tests

Verify engine mechanics independently of strategy quality:
- transaction costs/slippage applied once and correctly;
- no fill before signal availability;
- benchmark calculation correctness;
- position accounting and cash conservation;
- drawdown/return metrics against hand-computed fixtures;
- missing/stale data handling;
- deterministic seed behavior;
- survivorship/universe policy where applicable.

A profitable fixture is never used as proof of strategy value; tests prove mechanics only.

### 7. API contract tests

Verify OpenAPI-compatible requests/responses for:
- auth/authorization;
- decimal serialization;
- timestamps;
- Problem Details codes;
- cursor pagination;
- idempotency conflict behavior;
- ETag/optimistic concurrency;
- cache/privacy headers;
- version compatibility.

OpenAPI diff is a PR gate for breaking changes.

### 8. Security tests

Mandatory cases:
- IDOR/resource ownership;
- CSRF/session handling where applicable;
- XSS through provider/news/user text;
- SQL injection and unsafe dynamic queries;
- SSRF from configurable provider URLs;
- secret leakage in logs/errors;
- prompt injection / hostile external content reaching explanation layer;
- authorization bypass on admin/research endpoints;
- rights kill switches;
- rate limiting/abuse controls.

### 9. LLM explanation tests

The LLM layer is tested as non-authoritative transformation:
- structured authoritative facts cannot be changed silently;
- unsupported numbers/probabilities are rejected;
- prompt-injected provider text cannot grant tool/action authority;
- citations/evidence ids referenced by prose must exist in the supplied artifact;
- deterministic fallback template works when model is unavailable;
- unsafe/unparseable output is discarded, never partially trusted.

Use mocked/frozen model outputs in CI; live-model evaluation is separate because provider nondeterminism must not make CI flaky.

### 10. End-to-end tests

Critical journeys:
1. authenticate;
2. open instrument;
3. inspect Market State and evidence;
4. expand contradictory evidence/invalidation;
5. finalize and revisit a DecisionRecord;
6. enter manual portfolio snapshot and view descriptive risk;
7. validate/save strategy version;
8. launch backtest and inspect completed artifact;
9. simulate stale provider -> visible degradation;
10. explanation unavailable -> structured product remains usable.

### 11. Visual/accessibility regression

For the progressive-disclosure UI:
- desktop/mobile screenshots for critical surfaces;
- no hidden essential warnings at smaller breakpoints;
- keyboard navigation;
- semantic headings/landmarks;
- contrast and focus states;
- screen-reader labels for charts where feasible;
- reduced-motion behavior.

### 12. Performance/load tests

Before beta:
- representative API read load;
- concurrent DecisionRecord assembly requests;
- worker backlog recovery after outage;
- database lock/contention test;
- representative backtest memory/time budget;
- large Decision Ledger pagination.

Performance tests use realistic cardinality estimates and fail if resource growth is unbounded.

### 13. Failure-injection tests

Staging/CI scenarios:
- kill worker during job;
- database connection interruption;
- object storage failure;
- provider timeout/rate limit;
- corrupt provider payload;
- revoked rights record;
- model suspension;
- LLM outage;
- clock-skew fixture.

Expected outputs must match `FAILURE_AND_DEGRADATION.md`.

## Coverage policy

Line coverage is diagnostic, not the goal. Mandatory coverage targets focus on critical modules, but promotion depends on invariant/golden/failure tests rather than gaming a single percentage.

No critical domain branch may be intentionally untested without a documented exception.

## Test data policy

- no production user data in CI;
- synthetic portfolio/user data;
- provider fixtures only when contract/rights permit retention;
- secrets supplied only to isolated live-provider smoke environments;
- deterministic timezone/clock controls.

## Release gate

Production promotion requires:
- unit/domain green;
- DB integration green;
- provider contracts green for active providers;
- anti-leakage green;
- golden replay green;
- API contract green;
- security gate green;
- E2E critical paths green;
- migration dry-run green;
- backup/restore check within policy window;
- no unresolved P0/P1 known defect.

A manual override, if ever allowed, requires an audited incident/risk acceptance record and cannot bypass legal/data-rights hard locks.