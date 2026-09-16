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
16. **A closed design decision, a closed evidence result and a passed implementation receipt are different things; none may impersonate another.**
17. **Empirical promotion evidence is pre-registered before outcome inspection.**
18. **Production MK1 builds against one approved immutable bootstrap profile, never an informal “latest” configuration.**

## Program state

**Current phase:** `MK0 — Closure & Validation`

**Internal executable design:** `CLOSED`

**Known internal design nodes remaining:** `0`

**External/empirical validation method:** `CLOSED`

**External/empirical outcomes:** `Q01–Q05 OPEN / PARTIAL`

**MK1 production implementation:** `BLOCKED BY EXTERNAL / EMPIRICAL EVIDENCE`

The project no longer needs to invent either core MK1 architecture or a validation methodology. What remains is to execute the frozen evidence program and determine which exact first production configuration—if any—earns the right to be built.

Canonical internal-closure audit: [`docs/implementation/INTERNAL_CLOSURE_AUDIT.md`](docs/implementation/INTERNAL_CLOSURE_AUDIT.md).

Canonical external-evidence protocol: [`docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`](docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md).

Canonical experiment manifest: [`experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`](experiments/EXPERIMENT_MANIFEST_TEMPLATE.md).

Canonical MK0 promotion packet: [`docs/validation/MK0_PROMOTION_PACKET.md`](docs/validation/MK0_PROMOTION_PACKET.md).

Canonical MK1 bootstrap-profile contract: [`docs/validation/MK1_BOOTSTRAP_PROFILE.md`](docs/validation/MK1_BOOTSTRAP_PROFILE.md).

Canonical implementation-proof schema: [`docs/implementation/ACCEPTANCE_RECEIPTS.md`](docs/implementation/ACCEPTANCE_RECEIPTS.md).

Canonical promotion gate: [`docs/implementation/BUILD_READINESS.md`](docs/implementation/BUILD_READINESS.md).

Until the promotion packet is approved and an `MK1_BOOTSTRAP_PROFILE` reaches `APPROVED`, production feature code must not outrun the evidence.

## External / empirical closure tracks

```text
Q01  Peru regulatory boundary          OPEN — FATAL_IF_FAILED
Q02  Commercial market-data rights     OPEN — FATAL_IF_FAILED
Q03  User value / WTP / repeat use     OPEN / PARTIAL
Q04  Quant baseline / ML increment     OPEN
Q05  Moat / competitive durability     PARTIAL
```

All remaining PARTIAL/OPEN product evidence rows in `MK0_LOCKS.md` map into these tracks; there is no hidden parallel evidence gate.

## Evidence-to-build flow

```text
raw source / external authority / observed behavior
                    |
                    v
           mining / quarry
                    |
                    v
          PRE-REGISTERED plan
                    |
                    v
       experiment / counsel review /
       provider-rights verification
                    |
                    v
           immutable EvidenceReceipt
                    |
                    v
       cross-receipt contradiction review
                    |
                    v
           MK0_PROMOTION_PACKET
                    |
                    v
          MK1_BOOTSTRAP_PROFILE
                    |
                    v
             BUILD_READINESS
                    |
                    v
       production MK1 implementation
                    |
                    v
        typed acceptance receipts
                    |
                    v
          release / certification
```

A successful prototype is not legal clearance. A provider contract is not product demand. A strong backtest is not a moat. Built code is not evidence that the underlying decision was correct.

## Start here

Read the repository in this order:

1. [`GOVERNANCE.md`](GOVERNANCE.md) — the three classes of truth, closure and promotion rules.
2. [`MK0_LOCKS.md`](MK0_LOCKS.md) — canonical lock registry and mapping of all evidence uncertainty to Q01–Q05.
3. [`docs/implementation/INTERNAL_CLOSURE_AUDIT.md`](docs/implementation/INTERNAL_CLOSURE_AUDIT.md) — proof that known MK1 internal design nodes are closed.
4. [`docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`](docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md) — exact lifecycle, authority and PASS/CONDITIONAL/PIVOT/STOP rules for Q01–Q05.
5. [`experiments/FALSIFICATION_PLAN.md`](experiments/FALSIFICATION_PLAN.md) — concrete pre-build evidence workstreams.
6. [`experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`](experiments/EXPERIMENT_MANIFEST_TEMPLATE.md) — pre-registration contract for empirical evidence.
7. [`docs/validation/MK0_PROMOTION_PACKET.md`](docs/validation/MK0_PROMOTION_PACKET.md) — final MK0 review bundle.
8. [`docs/validation/MK1_BOOTSTRAP_PROFILE.md`](docs/validation/MK1_BOOTSTRAP_PROFILE.md) — exact evidence-derived configuration production may build.
9. [`docs/implementation/BUILD_READINESS.md`](docs/implementation/BUILD_READINESS.md) — objective implementation gate.
10. [`docs/product/PRODUCT_THESIS.md`](docs/product/PRODUCT_THESIS.md) — problem, JTBD, category and moat hypothesis.
11. [`docs/architecture/DOMAIN_MODEL.md`](docs/architecture/DOMAIN_MODEL.md) — canonical vocabulary.
12. [`docs/architecture/SYSTEM_CONTRACTS.md`](docs/architecture/SYSTEM_CONTRACTS.md) — evidence, scenario, risk, strategy, record and LLM contracts.
13. [`docs/implementation/ACCEPTANCE_RECEIPTS.md`](docs/implementation/ACCEPTANCE_RECEIPTS.md) — how future implementation proves conformance.
14. [`docs/implementation/REFERENCE_ARCHITECTURE.md`](docs/implementation/REFERENCE_ARCHITECTURE.md) — runtime/deployable/module topology.
15. [`docs/implementation/DATA_MODEL.md`](docs/implementation/DATA_MODEL.md) — point-in-time, lineage and persistence semantics.
16. [`docs/implementation/MARKET_DATA_SEMANTICS.md`](docs/implementation/MARKET_DATA_SEMANTICS.md) — instrument, session, bar, correction, corporate-action and currency semantics.
17. [`docs/quant/VALIDATION_PROTOCOL.md`](docs/quant/VALIDATION_PROTOCOL.md) — scientific gate for strategies and ML.
18. [`docs/implementation/QUANT_ENGINE_CONTRACT.md`](docs/implementation/QUANT_ENGINE_CONTRACT.md) — fills, costs, accounting, returns, drawdown and benchmark mechanics.
19. [`docs/implementation/TEST_STRATEGY.md`](docs/implementation/TEST_STRATEGY.md) — correctness/security/failure gates.
20. [`RISK_REGISTER.md`](RISK_REGISTER.md), [`quarries/README.md`](quarries/README.md) and [`ROADMAP.md`](ROADMAP.md) — active risks, unresolved evidence workstreams and promotion path.

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
│   ├── architecture/
│   ├── implementation/
│   │   ├── INTERNAL_CLOSURE_AUDIT.md
│   │   ├── BUILD_READINESS.md
│   │   ├── ACCEPTANCE_RECEIPTS.md
│   │   └── ...
│   ├── validation/
│   │   ├── EVIDENCE_CLOSURE_PROTOCOL.md
│   │   ├── MK0_PROMOTION_PACKET.md
│   │   └── MK1_BOOTSTRAP_PROFILE.md
│   ├── quant/
│   ├── regulatory/
│   ├── data/
│   ├── security/
│   ├── economics/
│   └── mvp/
├── experiments/
│   ├── FALSIFICATION_PLAN.md
│   └── EXPERIMENT_MANIFEST_TEMPLATE.md
├── mining-site/
├── quarries/
└── sources/
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

The exact provider set, asset universe, interaction constraints, ML scope, pricing hypothesis and other evidence-sensitive values are not guessed here. They are frozen only when the final `MK1_BOOTSTRAP_PROFILE` is approved.

## Motto

> **Evidence over impulse.**

---

SOPHROSYNE is currently a research and engineering project. Nothing in this repository should be interpreted as investment advice or a representation of future performance.
