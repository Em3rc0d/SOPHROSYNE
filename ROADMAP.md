# Roadmap

## MK0 — Closure & Validation — ACTIVE

### Internal design state

**Executable architecture design: CLOSED.**

**Known internal design nodes remaining: 0.**

**External/empirical validation method: CLOSED.**

The repository now freezes:
- product promise and MK1 boundaries;
- domain vocabulary and system contracts;
- modular-monolith + isolated-worker topology;
- production runtime lines and portability rules;
- point-in-time data/time semantics;
- market-data identity/session/correction/corporate-action/currency semantics;
- API/error/idempotency contracts;
- state machines;
- failure/degradation/fallback behavior;
- replay/reproducibility;
- deterministic quant/backtest mechanics;
- security controls and LLM isolation;
- configuration/secrets;
- observability/SLO targets and measurement contract;
- test strategy;
- CI/CD, migration and rollback rules;
- operational incident runbooks;
- typed implementation acceptance receipts;
- Q01–Q05 evidence lifecycle and authority model;
- empirical pre-registration contract;
- MK0 promotion-packet contract;
- immutable MK1 bootstrap-profile contract;
- build-readiness and implementation sequence.

Canonical closure artifacts:
- `docs/implementation/INTERNAL_CLOSURE_AUDIT.md`;
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`;
- `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`;
- `docs/validation/MK0_PROMOTION_PACKET.md`;
- `docs/validation/MK1_BOOTSTRAP_PROFILE.md`;
- `docs/implementation/ACCEPTANCE_RECEIPTS.md`;
- `docs/implementation/BUILD_READINESS.md`.

A pending legal opinion, provider right, user experiment or operational drill does not mean the validation/design method is open. The method is closed; the evidence outcome remains pending until observed.

### MK0 remaining goals

MK0 is now execution of evidence, not invention of more internal architecture.

Remaining tracks:

```text
Q01  Peru regulatory boundary          OPEN — FATAL_IF_FAILED
Q02  Commercial market-data rights     OPEN — FATAL_IF_FAILED
Q03  User value / WTP / repeat use     OPEN / PARTIAL
Q04  Quant baseline / ML increment     OPEN
Q05  Moat / competitive durability     PARTIAL
```

All other open/partial product-evidence rows map into these tracks in `MK0_LOCKS.md`.

### MK0 evidence execution order

Work may run in parallel where independence permits, but dependencies are fixed:

```text
Q03 behavioral discovery / prototype evidence ----+
                                                   +--> validated interaction/wedge
Q04 deterministic baseline research ---------------+

validated interaction/wedge --> Q01 counsel review

candidate data/asset profile --> Q02 rights/cost review

Q03 repeat-use evidence --> Q05 moat/replicability review

Q01 + Q02 + Q03 + Q04 + Q05
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
```

Q04 research can precede commercial Q02 closure only when the data used are permitted for the research purpose. Q01 must review the actual interaction model intended for MK1, not a materially different mock.

### MK0 exit criteria

MK0 exits only when:
- Q01 has a promotable final legal evidence receipt for exact frozen flows/copy;
- Q02 has promotable final receipts for every initial production `DataUseProfile`;
- Q03 supports the selected persona/JTBD/wedge/repeat-use/pricing hypothesis or those product docs are explicitly pivoted;
- Q04 has a reproducible deterministic baseline and explicit ML `INCLUDE`, `EXCLUDE` or `DEFER` decision;
- Q05 is supported or explicitly closed conditionally as a learning wedge with scale-spend constraints;
- all empirical promotion experiments were pre-registered and failed/inconclusive versions remain preserved;
- unit economics are synchronized with Q02 costs and Q03 pricing/retention evidence;
- initial asset universe, provider/fallback set, freshness profile and risk-policy version are frozen;
- no unresolved P0/P1 cross-receipt contradiction remains;
- no evidence-driven selection has reopened an unresolved P0/P1 internal architecture node;
- one `MK0_PROMOTION_PACKET` is `APPROVED`;
- one exact `MK1_BOOTSTRAP_PROFILE` is `APPROVED`;
- `docs/implementation/BUILD_READINESS.md` passes.

Research/prototype work may continue only under the allowances in `BUILD_READINESS.md`. Production product-feature implementation remains blocked until these criteria are satisfied.

The successful MK0 statement is deliberately narrow:

> **One exact first-production configuration has earned the right to be built.**

It is not a claim of profitability, permanent regulatory safety, product-market fit or production reliability.

---

## MK1 — Evidence MVP — BLOCKED UNTIL MK0 EVIDENCE GATE

Scope remains intentionally narrow:
- Market Translator;
- progressive Evidence View;
- immutable Decision Records;
- read-only/manual Portfolio Context;
- deterministic Strategy Sandbox;
- backtest + paper validation;
- optional validated scenario/model layer;
- downstream learning/explanation layer.

The final concrete values for provider set, asset universe, legal interaction profile, pricing hypothesis, ML scope and related evidence-sensitive choices come from the approved `MK1_BOOTSTRAP_PROFILE`; they are not guessed in advance.

Implementation order remains fixed by `docs/implementation/IMPLEMENTATION_SEQUENCE.md`:

```text
platform skeleton
  -> catalog / rights / one approved provider profile
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

### MK1 build binding

Every production feature PR must identify its governing `bootstrap_profile_id`, affected profile sections and whether the change requires evidence revalidation, ADR work or implementation acceptance receipts.

A material provider/asset/interaction/ML/authority change cannot silently drift away from the approved profile.

### MK1 implementation proof

Completion claims use typed immutable receipts defined in `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

Design semantics are not silently changed to make a receipt pass. If implementation reveals a real design contradiction, the affected lock is explicitly reopened and an ADR is created when an invariant changes.

### MK1 beta gate

Beta requires all implementation/test/security/restore/observability/incident receipts in `docs/implementation/BUILD_READINESS.md`, `docs/implementation/ACCEPTANCE_RECEIPTS.md` and `docs/implementation/TEST_STRATEGY.md`, plus proof that released semantics still match the approved bootstrap profile.

---

## MK2 — Connected Intelligence — FUTURE

Possible scope, subject to new locks:
- licensed real-time feeds beyond the approved MK1 profile;
- broker/exchange read-only connectors;
- richer on-chain and event intelligence;
- B2B/API experiments;
- advanced regime/risk models.

Nothing in MK2 is automatically promoted from a successful MK1. New legal, rights, threat, economics, evidence and architecture locks must be opened first.

---

## MK3 — Deterministic Execution — FUTURE / NOT COMMITTED

Only if legal, security, broker and quant gates justify it.

Requirements would include deterministic execution, explicit user-approved strategy contracts, no LLM in order path, circuit breakers, reconciliation, idempotency, kill switches and jurisdiction-specific compliance.

MK3 must be designed as a new trust boundary; MK1/MK2 architecture does not silently acquire execution authority.
