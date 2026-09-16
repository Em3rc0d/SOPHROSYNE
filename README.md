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

## Program state

**Current phase:** `MK0 — Closure & Validation`

**Decision:** `GO-MVP-CONDITIONAL`

Four hard external-evidence locks remain before a commercial beta can be treated as cleared:

1. Peru regulatory opinion on exact product flows and copy.
2. Commercial data-rights confirmation for production sources.
3. Real willingness-to-pay evidence from target users.
4. Quant baseline study proving reproducibility and preventing inflated backtest claims.

Until those close, product code must not outrun the documentation.

## Start here

Read the repository in this order:

1. [`GOVERNANCE.md`](GOVERNANCE.md) — how decisions and MK promotion work.
2. [`MK0_LOCKS.md`](MK0_LOCKS.md) — current truth about what is closed and what is not.
3. [`docs/product/PRODUCT_THESIS.md`](docs/product/PRODUCT_THESIS.md) — problem, JTBD, category and moat hypothesis.
4. [`docs/architecture/DOMAIN_MODEL.md`](docs/architecture/DOMAIN_MODEL.md) — canonical vocabulary.
5. [`docs/architecture/SYSTEM_CONTRACTS.md`](docs/architecture/SYSTEM_CONTRACTS.md) — evidence, scenario, risk, strategy, record and LLM contracts.
6. [`docs/architecture/MULTIMODAL_PIPELINE.md`](docs/architecture/MULTIMODAL_PIPELINE.md) — end-to-end intelligence architecture.
7. [`docs/quant/VALIDATION_PROTOCOL.md`](docs/quant/VALIDATION_PROTOCOL.md) — scientific gate for strategies and ML.
8. [`RISK_REGISTER.md`](RISK_REGISTER.md) and [`quarries/README.md`](quarries/README.md) — active risks and unresolved workstreams.
9. [`docs/mvp/MK1_SPEC.md`](docs/mvp/MK1_SPEC.md) — what the first product may and may not contain.
10. [`ROADMAP.md`](ROADMAP.md) — promotion path beyond MK0.

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
    └── SOURCE_REGISTER.md
```

## Planned MK1

The minimal product is intentionally narrow:

- Market Translator.
- Progressive Evidence View.
- Decision Record ledger.
- Read-only/manual Portfolio Context.
- Strategy Sandbox with backtesting and paper-only validation.
- Learning/explanation layer.

Explicitly out of scope for MK1: custody, copy trading, strategy marketplace, autonomous execution, personalized investment recommendations, leverage/options/futures workflows and claims that AI predicts future prices.

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
implementation
```

Implementation never promotes itself to evidence.

## Motto

> **Evidence over impulse.**

---

SOPHROSYNE is currently a research and engineering project. Nothing in this repository should be interpreted as investment advice or a representation of future performance.
