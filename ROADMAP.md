# Roadmap

## MK0 — Closure & Validation — ACTIVE

### Internal design state

**Executable architecture design: CLOSED for known MK1 decisions.**

The repository now freezes:
- domain vocabulary and system contracts;
- modular-monolith + isolated-worker topology;
- production runtime lines and portability rules;
- point-in-time data/time semantics;
- API/error/idempotency contracts;
- state machines;
- failure/degradation/fallback behavior;
- replay/reproducibility;
- security controls and LLM isolation;
- configuration/secrets;
- observability/SLO targets;
- test strategy;
- CI/CD, migration and rollback rules;
- operational incident runbooks;
- build-readiness and implementation sequence.

Canonical index: `docs/implementation/BUILD_READINESS.md`.

### MK0 remaining goals

- close legal/data/scientific/commercial unknowns;
- validate target user and willingness-to-pay;
- prove deterministic quant baseline before ML scope;
- validate moat/wedge enough to justify MK1 engineering;
- name the exact initial provider/data/instrument profile after rights review.

### MK0 exit criteria

- Peru legal flow reviewed and product/copy aligned;
- commercial data-rights matrix approved for exact MVP sources/use;
- user tests demonstrate recurring value/comprehension advantage and sufficient willingness-to-pay evidence;
- quant baseline harness reproduces simple benchmarks/costs and establishes whether ML belongs in MK1 at all;
- moat/wedge evidence is sufficient or the thesis is explicitly pivoted;
- initial asset universe, provider/fallback set, freshness profile and risk policy are frozen;
- `MK0_LOCKS.md` has no OPEN/PARTIAL item whose outcome would materially change MK1 architecture or core scope.

Research/prototype work may continue only under the allowances in `docs/implementation/BUILD_READINESS.md`. Production product-feature implementation remains blocked until the Definition of Ready is satisfied.

## MK1 — Evidence MVP — BLOCKED UNTIL MK0 GATE

Scope:
- Market Translator;
- progressive Evidence View;
- immutable Decision Records;
- read-only/manual Portfolio Context;
- deterministic Strategy Sandbox;
- backtest + paper validation;
- optional validated scenario/model layer;
- downstream learning/explanation layer.

Implementation order is fixed by `docs/implementation/IMPLEMENTATION_SEQUENCE.md`:

```text
platform skeleton
  -> catalog / rights / one provider
  -> evidence / deterministic MarketState
  -> Decision Ledger / replay
  -> risk
  -> Market Translator UI
  -> portfolio context
  -> deterministic strategy DSL
  -> backtesting
  -> validated scenarios / optional ML
  -> LLM explanation LAST
  -> staging hardening
```

No live auto-trading.

### MK1 beta gate

Beta requires all implementation/test/security/restore/observability gates in `docs/implementation/BUILD_READINESS.md` and `docs/implementation/TEST_STRATEGY.md`.

## MK2 — Connected Intelligence — FUTURE

Possible scope, subject to new locks:
- licensed real-time feeds;
- broker/exchange read-only connectors;
- richer on-chain and event intelligence;
- B2B/API experiments;
- advanced regime/risk models.

Nothing in MK2 is automatically promoted from a successful MK1. New legal, rights, threat, economics and architecture locks must be opened first.

## MK3 — Deterministic Execution — FUTURE / NOT COMMITTED

Only if legal, security, broker and quant gates justify it.

Requirements would include deterministic execution, explicit user-approved strategy contracts, no LLM in order path, circuit breakers, reconciliation, idempotency, kill switches and jurisdiction-specific compliance.

MK3 must be designed as a new trust boundary; MK1/MK2 architecture does not silently acquire execution authority.