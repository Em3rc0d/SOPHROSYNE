# MK1 Implementation Sequence

This sequence begins only after `BUILD_READINESS.md` Definition of Ready is satisfied for one approved `MK1_BOOTSTRAP_PROFILE` and one compatible Closed Validation Graph snapshot.

The ordering is deliberate: authoritative structured truth first, UX/LLM last. Each phase produces a deployable/testable vertical slice rather than a large horizontal code dump.

Every phase participates in the governance cycle:

```text
approved proposition/profile
      -> implementation obligation
      -> phase verification/receipt
      -> validates or reopens governing node/edge
```

Advancing a phase never severs its reverse-validation path.

## Phase 0 — Repository, graph validator and delivery skeleton

Build only the engineering substrate:
- monorepo/module layout;
- Python/Node lockfiles and toolchains;
- container builds;
- local PostgreSQL + object storage;
- CI checks;
- typed config/secrets boundary;
- migration framework;
- telemetry bootstrap;
- staging deployment path;
- deterministic parser/validator for `contracts/validation_graph.yaml`;
- canonical serialization + SHA-256 node/edge/graph digests;
- CVG-001 through CVG-012 checks;
- graph diff / affected-node reachability primitives;
- `GRAPH_CONFORMANCE` receipt emission.

Exit gate:
- clean environment can build/test/deploy skeleton;
- production artifact provenance/SBOM works;
- graph canonical serialization is deterministic;
- no P0/P1 orphan or dangling endpoint in active graph;
- bootstrap -> implementation -> verification -> governing-proposition reachability is mechanically checkable;
- Phase 0 `GRAPH_CONFORMANCE` receipt is PASS for exact graph/profile/build metadata;
- no domain feature yet.

Phase 0 tooling validates graph integrity. It does not fabricate truth for Q00–Q05 or external authorities.

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

Graph obligation:
- declare exact profile/node/edge set instantiated by the provider/data path;
- verify Q02/DataUseProfile reachability;
- ensure provider contract/rights verification returns to governing data-rights/data-semantics nodes.

Exit gate:
- provider contract fixtures pass;
- duplicate/schema-drift/timestamp-failure tests pass;
- rights-restricted display test passes;
- historical `available_at` lineage demonstrably preserved;
- current `GRAPH_CONFORMANCE` remains PASS for affected path.

Do not add provider #2 until provider #1 conforms fully to the adapter contract.

## Phase 2 — Evidence + deterministic MarketState

Implement:
- Evidence/Claim lifecycle;
- freshness profiles;
- deterministic baseline features;
- MarketState assembly;
- `READY / DEGRADED / NO_CONCLUSION` semantics.

Graph obligation:
- MarketState path remains downstream of approved provider/evidence nodes;
- anti-leakage/freshness verification returns to data/time and evidence contracts.

Exit gate:
- anti-lookahead tests pass;
- contradictory/missing/stale golden cases pass;
- no probability output exists yet unless separately calibrated;
- graph/profile/build references agree.

## Phase 3 — Decision Ledger + replay

Implement before sophisticated modeling:
- immutable DecisionRecord;
- version bundle;
- content hashes;
- graph/profile/build references in reproducibility metadata where applicable;
- replay service/command;
- historical browsing;
- golden corpus CI.

Graph obligation:
- replay receipt returns to ledger/reproducibility contracts;
- semantic graph/profile mismatch is visible, never normalized away.

Exit gate:
- deterministic golden corpus replay = 100%;
- finalized-record mutation tests fail closed;
- recovery/reconciliation preserves ledger integrity;
- current graph conformance passes.

This phase makes subsequent model/risk changes auditable.

## Phase 4 — Risk engine

Implement independently from scenarios/models:
- descriptive instrument risk;
- portfolio concentration/exposure;
- volatility/drawdown context;
- policy/version bundle;
- `NOT_EVALUABLE` conditions.

Graph obligation:
- risk node remains independent from model/scenario conviction;
- property/numerical verification returns to the governing risk contract.

Exit gate:
- hand-computed numerical fixtures match;
- property tests pass;
- scenario/model conviction cannot bypass risk constraints;
- no graph edge grants narrative/model authority over risk.

## Phase 5 — Market Translator UI

Implement authoritative product experience:
- instrument screen;
- market state;
- supporting/contradicting evidence;
- uncertainty/invalidation;
- freshness/degradation badges;
- progressive disclosure Beginner → Quant;
- Decision Ledger navigation.

Graph obligation:
- every displayed authoritative statement is reachable from structured source/evidence nodes;
- comprehension/use evidence has a return path to Q00/Q03 rather than being treated as permanent UX truth.

Exit gate:
- E2E + accessibility + responsive visual regression green;
- no essential warning hidden by disclosure level;
- comprehension prototype findings incorporated;
- product surface remains within Q00/Q01 approved scope.

## Phase 6 — Manual/read-only Portfolio Context

Implement:
- immutable PortfolioSnapshots;
- manual position entry/import contract;
- descriptive risk only.

Graph obligation:
- ownership/security/risk verification returns to governing contracts;
- no new recommendation authority edge is introduced implicitly.

Exit gate:
- ownership/IDOR tests green;
- decimal/accounting identities green;
- no personalized buy/sell recommendation surface exists unless Q01 explicitly permits a later scoped feature and the graph/profile are revalidated accordingly.

## Phase 7 — Deterministic Strategy DSL

Implement:
- narrow typed grammar/AST;
- validation;
- canonical semantic hash;
- immutable StrategyVersions;
- evaluation outcomes `TRIGGERED / NOT_TRIGGERED / NOT_EVALUABLE`.

Graph obligation:
- strategy execution semantics remain deterministic/non-LLM;
- parser/property verification returns to strategy contract.

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

Graph obligation:
- every research result binds to data/config/code/profile/graph provenance;
- anti-leakage and quant-accounting receipts return to data/time/quant contracts and Q04.

Exit gate:
- hand-computed mechanics fixtures green;
- intentional leakage fixture rejected;
- dataset manifest present for every completed run;
- Q04 baseline experiment reproducible.

## Phase 9 — Scenario layer / approved quantitative models

Start with deterministic/transparent scenarios.

ML enters only if Q04 evidence supports incremental value and the approved profile/graph activates it. Any promoted model needs ModelArtifact lifecycle, calibration where probability is exposed, drift monitoring and baseline fallback.

Graph obligation:
- model authority is an explicit node/edge, never an implicit code path;
- OOS/calibration/drift evidence returns to Q04/model lifecycle;
- suspension can reopen/disable affected edges without breaking deterministic baseline paths.

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

Graph obligation:
- explanation remains downstream only;
- no edge from explanation grants authority into market state, risk, strategy or execution semantics;
- hostile-output verification returns to LLM/security authority contracts.

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
- production rights configuration verification;
- full `GRAPH_CONFORMANCE` for exact release graph/profile/build digests;
- contradiction/reopen drill for at least one synthetic material graph invalidation.

Exit gate:
- all beta-required receipts PASS;
- graph/profile/build/release digests agree;
- no unresolved P0/P1 contradiction/revalidation requirement;
- runtime observation/reopen path is operational, not merely documented.

## Cross-phase rule

Never advance because the next feature is exciting. Advance only when the previous phase exit gate is green **and** the active graph/profile remains valid for the next phase.

Each production PR declares:

```text
bootstrap_profile_id:
graph_version:
graph_digest:
affected_node_ids: []
affected_edge_ids: []
semantic_change: YES | NO
graph_revalidation_required: YES | NO
acceptance_receipts_required: []
```

A newly introduced P0/P1 implementation surface without a governing node, required edge and verification-return path fails the phase gate.

## Complexity rule

At every phase, prefer the least complex design satisfying measured requirements:
- one provider before many;
- deterministic baseline before ML;
- PostgreSQL jobs before broker;
- modular monolith before services;
- structured authoritative UI before LLM prose;
- manual/read-only portfolio before broker connection;
- paper/backtest before any future execution work.

Complexity must be reachable from validated nodes and must survive its own reverse-validation loop.

## Forbidden shortcuts

- frontend mock semantics becoming production semantics without domain/API/graph contract;
- direct provider calls from browser;
- notebooks promoted as production pipelines;
- LLM text parsed as authoritative strategy/risk/probability state;
- backtest code written before time-availability semantics;
- ML evaluated without simple baselines;
- service extraction without measured need;
- implementation surface added outside approved profile/graph reachability;
- verification receipt with no governing proposition/design path;
- graph/profile digest mismatch ignored because feature tests pass;
- fatal upstream failed edge averaged away by downstream green checks;
- production beta before Q01/Q02 and beta readiness gates.
