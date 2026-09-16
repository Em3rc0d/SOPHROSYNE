# MK1 Implementation Sequence

This sequence begins only after `BUILD_READINESS.md` Definition of Ready is satisfied.

The ordering is deliberate: authoritative structured truth first, UX/LLM last. Each phase produces a deployable/testable vertical slice rather than a large horizontal code dump.

## Phase 0 — Repository and delivery skeleton

Build only the engineering substrate:
- monorepo/module layout;
- Python/Node lockfiles and toolchains;
- container builds;
- local PostgreSQL + object storage;
- CI checks;
- typed config/secrets boundary;
- migration framework;
- telemetry bootstrap;
- staging deployment path.

Exit gate:
- clean environment can build/test/deploy skeleton;
- production artifact provenance/SBOM works;
- no domain feature yet.

## Phase 1 — Catalog + rights + one provider adapter

Implement:
- instruments/venues/aliases;
- Source/DataRightsRecord;
- one approved provider adapter;
- raw receipts;
- timestamp semantics;
- normalization;
- quarantine;
- ingestion cursor/reconciliation;
- provider health.

Use one narrow instrument/data family first.

Exit gate:
- provider contract fixtures pass;
- duplicate/schema-drift/timestamp-failure tests pass;
- rights-restricted display test passes;
- historical `available_at` lineage demonstrably preserved.

Do not add provider #2 until provider #1 conforms fully to the adapter contract.

## Phase 2 — Evidence + deterministic MarketState

Implement:
- Evidence/Claim lifecycle;
- freshness profiles;
- deterministic baseline features;
- MarketState assembly;
- `READY / DEGRADED / NO_CONCLUSION` semantics.

Exit gate:
- anti-lookahead tests pass;
- contradictory/missing/stale golden cases pass;
- no probability output exists yet unless separately calibrated.

## Phase 3 — Decision Ledger + replay

Implement before sophisticated modeling:
- immutable DecisionRecord;
- version bundle;
- content hashes;
- replay service/command;
- historical browsing;
- golden corpus CI.

Exit gate:
- deterministic golden corpus replay = 100%;
- finalized-record mutation tests fail closed;
- recovery/reconciliation preserves ledger integrity.

This phase makes subsequent model/risk changes auditable.

## Phase 4 — Risk engine

Implement independently from scenarios/models:
- descriptive instrument risk;
- portfolio concentration/exposure;
- volatility/drawdown context;
- policy/version bundle;
- `NOT_EVALUABLE` conditions.

Exit gate:
- hand-computed numerical fixtures match;
- property tests pass;
- scenario/model conviction cannot bypass risk constraints.

## Phase 5 — Market Translator UI

Implement authoritative product experience:
- instrument screen;
- market state;
- supporting/contradicting evidence;
- uncertainty/invalidation;
- freshness/degradation badges;
- progressive disclosure Beginner → Quant;
- Decision Ledger navigation.

Exit gate:
- E2E + accessibility + responsive visual regression green;
- no essential warning hidden by disclosure level;
- comprehension prototype findings incorporated.

## Phase 6 — Manual/read-only Portfolio Context

Implement:
- immutable PortfolioSnapshots;
- manual position entry/import contract;
- descriptive risk only.

Exit gate:
- ownership/IDOR tests green;
- decimal/accounting identities green;
- no personalized buy/sell recommendation surface exists unless Q01 explicitly permits a later scoped feature.

## Phase 7 — Deterministic Strategy DSL

Implement:
- narrow typed grammar/AST;
- validation;
- canonical semantic hash;
- immutable StrategyVersions;
- evaluation outcomes `TRIGGERED / NOT_TRIGGERED / NOT_EVALUABLE`.

Exit gate:
- parser property/round-trip tests;
- deterministic fixtures;
- user-visible exact semantics;
- no LLM is needed for execution semantics.

If an LLM-assisted rule drafting UI is later added, it produces only a draft AST that the deterministic validator/user must approve.

## Phase 8 — Backtesting engine

Implement only after deterministic strategy semantics and point-in-time data are stable:
- immutable dataset manifests;
- cost/slippage policies;
- benchmark comparison;
- accounting engine;
- walk-forward/OOS harness;
- reproducible artifacts.

Exit gate:
- hand-computed mechanics fixtures green;
- intentional leakage fixture rejected;
- dataset manifest present for every completed run;
- Q04 baseline experiment reproducible.

## Phase 9 — Scenario layer / approved quantitative models

Start with deterministic/transparent scenarios.

ML enters only if Q04 evidence supports incremental value. Any promoted model needs ModelArtifact lifecycle, calibration where probability is exposed, drift monitoring and baseline fallback.

Exit gate:
- OOS protocol passed;
- calibration approved for any displayed probability;
- golden replay/version lineage works;
- suspension returns safely to baseline/NO_CONCLUSION.

## Phase 10 — Explanation layer

LLM comes last.

Implement:
- explanation request from finalized authoritative artifact;
- audience/language transform;
- schema/citation validation;
- deterministic fallback template;
- hostile-content tests.

Exit gate:
- LLM outage leaves core product fully usable;
- injected external text cannot gain authority;
- unsupported facts/numbers/probabilities rejected;
- explanation always links to authoritative evidence/record.

## Phase 11 — Staging hardening

Before beta:
- full failure-injection suite;
- provider failover exercises;
- database restore/failover rehearsal;
- credential rotation;
- load/backlog recovery;
- SLO dashboards/alerts;
- security review;
- legal copy/terms verification;
- production rights configuration verification.

## Cross-phase rule

Never advance because the next feature is exciting. Advance only when the previous phase exit gate is green.

## Complexity rule

At every phase, prefer the least complex design satisfying measured requirements:
- one provider before many;
- deterministic baseline before ML;
- PostgreSQL jobs before broker;
- modular monolith before services;
- structured authoritative UI before LLM prose;
- manual/read-only portfolio before broker connection;
- paper/backtest before any future execution work.

## Forbidden shortcuts

- frontend mock semantics becoming production semantics without domain/API contract;
- direct provider calls from browser;
- notebooks promoted as production pipelines;
- LLM text parsed as authoritative strategy/risk/probability state;
- backtest code written before time-availability semantics;
- ML evaluated without simple baselines;
- service extraction without measured need;
- production beta before Q01/Q02 and beta readiness gates.