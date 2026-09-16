# MK1 Build Readiness Gate

## Current verdict

**INTERNAL DESIGN: READY**

**MK1 IMPLEMENTATION: BLOCKED BY EXTERNAL / EMPIRICAL LOCKS**

The architecture is now specific enough to implement without choosing major system semantics during coding. That does **not** mean the product is guaranteed to work on the first implementation attempt; it means remaining uncertainty is intentionally exposed as evidence work rather than hidden design ambiguity.

## Internal design locks

| Lock | Status | Canonical artifact |
|---|---|---|
| Product thesis / boundaries | CLOSED | `docs/product/PRODUCT_THESIS.md`, `docs/mvp/MK1_SPEC.md` |
| Domain vocabulary | CLOSED | `docs/architecture/DOMAIN_MODEL.md` |
| System contracts | CLOSED | `docs/architecture/SYSTEM_CONTRACTS.md` |
| Runtime topology | CLOSED | `docs/implementation/REFERENCE_ARCHITECTURE.md` |
| Technology stack | CLOSED | `docs/implementation/TECH_STACK.md` |
| Data/time semantics | CLOSED | `docs/implementation/DATA_MODEL.md` |
| Market-data semantics | CLOSED | `docs/implementation/MARKET_DATA_SEMANTICS.md` |
| API/error/idempotency semantics | CLOSED | `docs/implementation/API_CONTRACTS.md` |
| Domain state machines | CLOSED | `docs/implementation/STATE_MACHINES.md` |
| Failure/degradation/fallback | CLOSED | `docs/implementation/FAILURE_AND_DEGRADATION.md` |
| Replay/reproducibility | CLOSED | `docs/implementation/REPLAY_AND_REPRODUCIBILITY.md` |
| Quant/backtest mechanics | CLOSED | `docs/implementation/QUANT_ENGINE_CONTRACT.md` |
| Security controls | CLOSED_FOR_DESIGN | `docs/implementation/SECURITY_CONTROLS.md` |
| Config/secrets | CLOSED | `docs/implementation/CONFIGURATION_AND_SECRETS.md` |
| Observability/SLO model | CLOSED_FOR_BETA_TARGETS | `docs/implementation/OBSERVABILITY_AND_SLOS.md` |
| Test strategy | CLOSED | `docs/implementation/TEST_STRATEGY.md` |
| CI/CD / migration / rollback | CLOSED | `docs/implementation/CI_CD_AND_ENVIRONMENTS.md` |
| Operational incident model | CLOSED_FOR_DESIGN | `docs/implementation/OPERATIONS_RUNBOOK.md` |
| Quant validation method | CLOSED | `docs/quant/VALIDATION_PROTOCOL.md` |
| Data-rights architecture | CLOSED | `docs/data/DATA_RIGHTS.md` |
| Build-readiness gate | CLOSED | this document |
| Risk-minimizing implementation order | CLOSED | `docs/implementation/IMPLEMENTATION_SEQUENCE.md` |

`CLOSED_FOR_DESIGN` means implementation must still produce the operational receipt/tests before beta.

## External / empirical locks that still block MK1

### Q01 — Peru regulatory boundary — FATAL_IF_FAILED
Issue #2.

Requires written qualified Peruvian securities counsel review of concrete product flows/copy.

Why it blocks build promotion:
- exact UX/copy and some API behavior may change depending on whether a flow is considered generalized information, personalized recommendation, intermediation or another regulated activity;
- building around an unverified interpretation creates expensive rework and liability.

### Q02 — Commercial market-data rights — FATAL_IF_FAILED
Issue #3.

Requires provider-by-provider written rights matrix.

Why it blocks build promotion:
- a technically valid API source can still be unusable for display, derived data, retention or redistribution;
- the production data model already supports rights, but production provider selection cannot be frozen without this receipt.

### Q03 — Willingness to pay / retention
Issue #4.

Requires behavioral interviews, comprehension comparison, pricing/fake-door and retention evidence.

Why it blocks full product build:
- prevents engineering a technically elegant product users do not repeatedly value.

### Q04 — Quant baseline / ML incremental value
Issue #5.

Requires reproducible benchmark experiment.

Why it blocks predictive/ML scope:
- deterministic baseline must exist before ML complexity;
- no ML/alpha claim enters implementation requirements until evidence exists.

### Q05 — Moat / competitive durability
Issue #6.

Requires preference/retention/trust evidence and competitive refresh.

Why it blocks scale architecture, not the research prototype itself:
- prevents optimizing for a moat that may be only localization or thin LLM wrapping.

## Allowed work before all locks close

To preserve the docs-first discipline, **product feature implementation remains blocked**.

Allowed activities:
- research scripts used strictly to close Q03/Q04/Q05;
- throwaway/prototype UX used for behavioral tests, clearly outside the production architecture;
- provider/legal discovery;
- infrastructure spikes whose output is evidence/measurement, not production code;
- test fixture/schema prototyping needed to validate a design assumption.

These artifacts do not become MK1 production code unless promoted through the normal gate.

## Definition of Ready — start production MK1 implementation

All must be true:

1. Q01 closed with written legal receipt or product scope explicitly redesigned to satisfy counsel.
2. Q02 closed for the exact initial instrument/data families chosen for MK1.
3. Q03 has enough evidence to justify the chosen wedge and repeat-use hypothesis, or the product thesis has been explicitly pivoted and docs updated.
4. Q04 has a reproducible deterministic baseline; ML scope is either justified or explicitly removed.
5. Q05 is either supported sufficiently for MK1 or explicitly downgraded to a hypothesis that does not alter the core build.
6. Initial production provider set and fallback compatibility groups are named.
7. Initial exact asset universe and corresponding market-data profile(s) are frozen.
8. Initial freshness profiles and risk policy versions are frozen.
9. Corporate-action/session/currency semantics for every selected profile are confirmed against provider capabilities and fixtures.
10. Architecture/ADR review finds no unresolved P0/P1 design contradiction.
11. `MK0_LOCKS.md` contains no OPEN/PARTIAL item whose outcome would materially change MK1 system boundaries.

If any item would materially change the architecture, implementation remains blocked.

## Definition of Ready — beta

In addition to implementation completion:

- mandatory CI gates green;
- golden replay 100% for deterministic corpus;
- anti-leakage suite green;
- provider contracts and market-data pathological fixtures green;
- hand-computed quant/accounting/fill fixtures green;
- rights configuration active/verified;
- security readiness receipt complete;
- backup restore and credential rotation drills passed;
- measured DB/service recovery meets approved beta RPO/RTO targets;
- production synthetic checks and dashboards live;
- no unresolved P0/P1 defects;
- user-facing legal copy/terms match counsel-approved flow;
- no uncalibrated probability or unsupported performance claim exposed.

## Definition of Done — one vertical slice

A slice is done only when it has:
- domain/API contract;
- persistence migration where required;
- authorization;
- telemetry;
- unit/integration/contract tests;
- failure/degradation behavior;
- user-visible stale/error semantics;
- documentation/ADR updates for semantic changes;
- staging verification.

A UI screen backed by mock data is not a completed vertical slice.

## Stop rule

If new evidence invalidates product, legal, data-rights or quant assumptions, **stop and update the graph before coding around the contradiction**.

The purpose of this gate is not to eliminate all uncertainty—impossible in a real system—but to ensure no known high-impact decision is deferred accidentally into implementation.