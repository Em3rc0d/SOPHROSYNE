# SOPHROSYNE

> **Financial Decision Intelligence** — transform market uncertainty into understandable evidence, scenarios, risk and disciplined decisions.

SOPHROSYNE is a docs-first research and product program for building a financial decision-intelligence system for self-directed retail investors. It is designed to reduce the learning curve around market data without pretending that markets are deterministic or that AI can know the future.

The name comes from the Greek concept **sophrosyne**: self-control, prudence, moderation and soundness of mind. That is also the product philosophy: **evidence over impulse**.

## Product thesis

Retail investors can access more market data than ever—candles, indicators, order books, derivatives, macro releases, news, on-chain activity and portfolio data—but access is not the same as understanding. SOPHROSYNE aims to translate heterogeneous market evidence into a structured view of:

- **Market State** — what is observable now.
- **Scenarios** — plausible paths supported by current evidence.
- **Evidence** — supporting and contradicting facts, with provenance.
- **Uncertainty** — what is unknown, stale or weakly supported.
- **Invalidation** — what would make a scenario cease to be credible.
- **Risk** — downside, concentration and regime-aware exposure.
- **Strategy State** — whether a user-defined rule is triggered, not triggered or not evaluable.

The system must be able to say **NO CONCLUSION** or **NO TRADE**. Activity is not a success metric.

## What SOPHROSYNE is not

- Not a trading oracle.
- Not a guaranteed-return system.
- Not a “guru” or signal-selling product.
- Not an autonomous LLM trader.
- Not a broker or custodian in MK1.
- Not a TradingView clone.
- Not a promise that ML creates alpha.

## Engineering invariants

1. **Evidence before recommendation.**
2. **Risk engine independent from prediction/model engine.**
3. **LLMs never control funds or order execution.**
4. **Probabilities must be empirically calibrated before being displayed.**
5. **Every user-visible interpretation has provenance and an `as_of` timestamp.**
6. **Correlation is never presented as causality without explicit attribution.**
7. **Data rights are part of architecture, not procurement paperwork.**
8. **NO CONCLUSION and NO TRADE are valid outputs.**
9. **No hidden backtest cherry-picking.**
10. **Every model and strategy must be versioned, auditable and retireable.**
11. **No critical provider may become an unbounded single point of business failure.**
12. **Live trading is not an MK1 requirement.**
13. **Historical computation cannot use evidence that was not yet available at its `as_of` cutoff.**
14. **A finalized Decision Record is immutable.**
15. **Product code does not begin while a known open lock can materially change MK1 architecture or scope.**

## Program state

**Current phase:** `MK0 — Closure & Validation`

**Internal executable design:** `READY`

**MK1 production implementation:** `BLOCKED BY EXTERNAL / EMPIRICAL LOCKS`

The architecture is now specific enough that implementation should not need to invent major semantics while coding. Remaining blockers are intentionally external or empirical rather than hidden design ambiguity:

1. Peru regulatory opinion on exact product flows and copy — issue #2.
2. Commercial data-rights confirmation for exact production sources/use — issue #3.
3. Real willingness-to-pay and retention evidence — issue #4.
4. Reproducible deterministic quant baseline and evidence for/against ML increment — issue #5.
5. Moat/competitive durability evidence — issue #6.

Canonical gate: [`docs/implementation/BUILD_READINESS.md`](docs/implementation/BUILD_READINESS.md).

Until that gate is satisfied, production feature code must not outrun the evidence.

## Start here

Read the repository in this order:

1. [`GOVERNANCE.md`](GOVERNANCE.md) — how decisions and MK promotion work.
2. [`MK0_LOCKS.md`](MK0_LOCKS.md) — current truth about what is closed and what is not.
3. [`docs/product/PRODUCT_THESIS.md`](docs/product/PRODUCT_THESIS.md) — problem, JTBD, category and moat hypothesis.
4. [`docs/architecture/DOMAIN_MODEL.md`](docs/architecture/DOMAIN_MODEL.md) — canonical vocabulary.
5. [`docs/architecture/SYSTEM_CONTRACTS.md`](docs/architecture/SYSTEM_CONTRACTS.md) — evidence, scenario, risk, strategy, record and LLM contracts.
6. [`docs/implementation/BUILD_READINESS.md`](docs/implementation/BUILD_READINESS.md) — objective implementation gate.
7. [`docs/implementation/REFERENCE_ARCHITECTURE.md`](docs/implementation/REFERENCE_ARCHITECTURE.md) — runtime/deployable/module topology.
8. [`docs/implementation/DATA_MODEL.md`](docs/implementation/DATA_MODEL.md) — point-in-time, lineage and persistence semantics.
9. [`docs/implementation/MARKET_DATA_SEMANTICS.md`](docs/implementation/MARKET_DATA_SEMANTICS.md) — instrument, session, bar, correction, corporate-action and currency semantics.
10. [`docs/implementation/API_CONTRACTS.md`](docs/implementation/API_CONTRACTS.md) — API/error/idempotency contract.
11. [`docs/implementation/FAILURE_AND_DEGRADATION.md`](docs/implementation/FAILURE_AND_DEGRADATION.md) — how the system fails safely.
12. [`docs/implementation/REPLAY_AND_REPRODUCIBILITY.md`](docs/implementation/REPLAY_AND_REPRODUCIBILITY.md) — historical truth and replay contract.
13. [`docs/quant/VALIDATION_PROTOCOL.md`](docs/quant/VALIDATION_PROTOCOL.md) — scientific gate for strategies and ML.
14. [`docs/implementation/QUANT_ENGINE_CONTRACT.md`](docs/implementation/QUANT_ENGINE_CONTRACT.md) — fills, costs, accounting, returns, drawdown and benchmark mechanics.
15. [`docs/implementation/TEST_STRATEGY.md`](docs/implementation/TEST_STRATEGY.md) — correctness/security/failure gates.
16. [`RISK_REGISTER.md`](RISK_REGISTER.md) and [`quarries/README.md`](quarries/README.md) — active risks and unresolved workstreams.
17. [`docs/mvp/MK1_SPEC.md`](docs/mvp/MK1_SPEC.md) and [`docs/implementation/IMPLEMENTATION_SEQUENCE.md`](docs/implementation/IMPLEMENTATION_SEQUENCE.md) — what MK1 contains and the only intended build order.
18. [`ROADMAP.md`](ROADMAP.md) — promotion path beyond MK0.

## MK1 implementation architecture

```text
Browser
  ↓
Web presentation tier
  ↓
Core API / modular monolith
  ↓
PostgreSQL authoritative state
  ├── transactional outbox / durable jobs
  └── immutable metadata / lineage
        ↓
   isolated workers
      ├── provider ingestion
      ├── deterministic market-state computation
      ├── risk / strategy / backtest
      ├── approved model inference
      └── LLM explanation LAST

Large/reproducible artifacts → S3-compatible object storage
```

The LLM/explanation layer is downstream-only. It cannot feed authoritative market state, risk, strategy or probability semantics.

## Repository map

```text
SOPHROSYNE/
├── README.md
├── GOVERNANCE.md
├── MK0_LOCKS.md
├── RISK_REGISTER.md
├── ROADMAP.md
├── adr/
│   └── README.md
├── docs/
│   ├── product/
│   │   ├── PRODUCT_THESIS.md
│   │   ├── USER_TRUST_AND_GTM.md
│   │   └── UX_PRINCIPLES.md
│   ├── architecture/
│   │   ├── DOMAIN_MODEL.md
│   │   ├── SYSTEM_CONTRACTS.md
│   │   ├── DECISION_RECORD.md
│   │   └── MULTIMODAL_PIPELINE.md
│   ├── implementation/
│   │   ├── BUILD_READINESS.md
│   │   ├── REFERENCE_ARCHITECTURE.md
│   │   ├── TECH_STACK.md
│   │   ├── DATA_MODEL.md
│   │   ├── MARKET_DATA_SEMANTICS.md
│   │   ├── API_CONTRACTS.md
│   │   ├── STATE_MACHINES.md
│   │   ├── FAILURE_AND_DEGRADATION.md
│   │   ├── REPLAY_AND_REPRODUCIBILITY.md
│   │   ├── QUANT_ENGINE_CONTRACT.md
│   │   ├── SECURITY_CONTROLS.md
│   │   ├── CONFIGURATION_AND_SECRETS.md
│   │   ├── OBSERVABILITY_AND_SLOS.md
│   │   ├── TEST_STRATEGY.md
│   │   ├── CI_CD_AND_ENVIRONMENTS.md
│   │   ├── OPERATIONS_RUNBOOK.md
│   │   └── IMPLEMENTATION_SEQUENCE.md
│   ├── quant/
│   │   └── VALIDATION_PROTOCOL.md
│   ├── regulatory/
│   │   └── REGULATORY_BOUNDARY.md
│   ├── data/
│   │   └── DATA_RIGHTS.md
│   ├── security/
│   │   └── SECURITY_AND_AI_RISK.md
│   ├── economics/
│   │   └── UNIT_ECONOMICS.md
│   └── mvp/
│       └── MK1_SPEC.md
├── experiments/
│   └── FALSIFICATION_PLAN.md
├── mining-site/
│   └── README.md
├── quarries/
│   └── README.md
└── sources/
    ├── SOURCE_REGISTER.md
    └── IMPLEMENTATION_STACK_RECEIPTS.md
```

## Planned MK1

The minimal product is intentionally narrow:

- Market Translator.
- Progressive Evidence View.
- Decision Record ledger.
- Read-only/manual Portfolio Context.
- Deterministic Strategy Sandbox with backtesting and paper-only validation.
- Optional scenario/model layer only when validated.
- Learning/explanation layer implemented after authoritative structured intelligence.

Explicitly out of scope for MK1: custody, copy trading, strategy marketplace, autonomous execution, unreviewed personalized investment recommendations, leverage/options/futures workflows and claims that AI predicts future prices.

## Research-to-truth flow

```text
raw source
    ↓
mining-site receipt
    ↓
quarry / experiment
    ↓
canonical document
    ↓
ADR when the decision changes an invariant
    ↓
build-readiness gate
    ↓
implementation
    ↓
tests / operational receipts
```

Implementation never promotes itself to evidence.

## Motto

> **Evidence over impulse.**

---

SOPHROSYNE is currently a research and engineering project. Nothing in this repository should be interpreted as investment advice or a representation of future performance.
