# MK0 Lock Registry

## Product / evidence locks

| Lock | Status | Decision / Evidence | Closure evidence |
|---|---|---|---|
| Problem exists | CLOSED | Market complexity and information overload are real; product targets translation + discipline. | Ongoing validation only. |
| Product thesis | CLOSED | Financial Decision Intelligence, not prediction/guru product. | Frozen for MK1. |
| Initial persona | PARTIAL | Spanish-first beginner/intermediate self-directed investor. | 15–25 behavioral interviews. |
| Wedge | PARTIAL | Progressive disclosure + evidence + auditability + risk-first UX. | Prototype comparison test. |
| Competition | CLOSED | AI/NL/backtesting/automation already exist; those are not the moat. | Quarterly refresh. |
| Moat | PARTIAL | Trust/evidence graph + beginner-to-quant UX + decision ledger. | Retention and preference evidence. |
| Peru regulatory boundary | OPEN — FATAL_IF_FAILED | Personalized recommendations/execution may cross regulated boundaries. | Written counsel review of exact flows/copy. Issue #2. |
| Custody | CLOSED | Excluded from MK1. | Keep excluded. |
| Live auto-trading | CLOSED_FOR_MK1 | Excluded from MK1. | Re-open in future MK only. |
| Market-data technical access | CLOSED | Sufficient technical sources exist for research. | None. |
| Market-data commercial rights | OPEN — FATAL_IF_FAILED | Access does not imply display/redistribution/derived-data rights. | Provider-by-provider written rights matrix. Issue #3. |
| XTB automation | CLOSED | Public API discontinued; no MK1 execution dependency. | Monitor only. |
| Quant feasibility | CLOSED_WITH_LIMIT | Signals may exist; durable alpha is not assumed. | Baseline empirical study before claims. |
| ML incremental value | OPEN | ML must beat simple baselines OOS after costs. | Benchmark experiment. Issue #5. |
| Explainability/auditability | CLOSED | Decision Record is mandatory. | Implement contract. |
| Causality claims | CLOSED | OBSERVED / ATTRIBUTED / INFERRED / CORRELATED / UNKNOWN. | Enforce output schema. |
| LLM authority | CLOSED | LLM cannot invent probabilities or authorize trades. | Enforce architecture. |
| Security posture | CLOSED | Least privilege, isolated LLM, no withdrawals/execution creds, kill/revoke paths. | Implementation proof via typed security receipt before real credentials/beta. |
| Unit economics | PARTIAL | Potentially viable if retention and data rights work. | Real CAC/churn/WTP/vendor quotes. |
| TAM/SAM/SOM | OPEN | Bottom-up model required. | Account/user data + observed funnel. |
| MVP scope | CLOSED | Translator + evidence + ledger + portfolio context + strategy sandbox. | Freeze after first user-test round unless evidence forces pivot. |
| GTM | PARTIAL | Trust/content/community/partnerships are hypotheses. | Channel experiments. |
| Willingness-to-pay / retention | OPEN | Recurring value is not yet proven. | Behavioral/pricing/retention experiments. Issue #4. |
| Liability/reputation | PARTIAL | Incident semantics are closed; terms/claim policy still depend on legal/product evidence. | Counsel-aligned terms + claim policy + beta incident drill. |

## Internal executable-design locks

| Lock | Status | Canonical artifact |
|---|---|---|
| Product promise / MK1 boundaries | CLOSED | `docs/product/PRODUCT_THESIS.md`, `docs/mvp/MK1_SPEC.md` |
| Domain vocabulary | CLOSED | `docs/architecture/DOMAIN_MODEL.md` |
| System contracts | CLOSED | `docs/architecture/SYSTEM_CONTRACTS.md` |
| Runtime topology | CLOSED | `docs/implementation/REFERENCE_ARCHITECTURE.md` |
| Technology stack / portability | CLOSED | `docs/implementation/TECH_STACK.md` |
| Data model / point-in-time semantics | CLOSED | `docs/implementation/DATA_MODEL.md` |
| Market-data semantics | CLOSED | `docs/implementation/MARKET_DATA_SEMANTICS.md` |
| API / error / idempotency contracts | CLOSED | `docs/implementation/API_CONTRACTS.md` |
| State machines | CLOSED | `docs/implementation/STATE_MACHINES.md` |
| Failure / degradation / fallback | CLOSED | `docs/implementation/FAILURE_AND_DEGRADATION.md` |
| Replay / reproducibility | CLOSED | `docs/implementation/REPLAY_AND_REPRODUCIBILITY.md` |
| Quant / backtest engine mechanics | CLOSED | `docs/implementation/QUANT_ENGINE_CONTRACT.md` |
| Observability / beta SLO contract | CLOSED | `docs/implementation/OBSERVABILITY_AND_SLOS.md` |
| Test strategy / release gates | CLOSED | `docs/implementation/TEST_STRATEGY.md` |
| CI/CD / migrations / rollback | CLOSED | `docs/implementation/CI_CD_AND_ENVIRONMENTS.md` |
| Implementation security controls | CLOSED | `docs/implementation/SECURITY_CONTROLS.md` |
| Configuration / secrets | CLOSED | `docs/implementation/CONFIGURATION_AND_SECRETS.md` |
| Incident / operations model | CLOSED | `docs/implementation/OPERATIONS_RUNBOOK.md` |
| Acceptance-receipt schema | CLOSED | `docs/implementation/ACCEPTANCE_RECEIPTS.md` |
| Internal closure audit | CLOSED | `docs/implementation/INTERNAL_CLOSURE_AUDIT.md` |
| Build-readiness gate | CLOSED | `docs/implementation/BUILD_READINESS.md` |
| Implementation order | CLOSED | `docs/implementation/IMPLEMENTATION_SEQUENCE.md` |

**Every internal executable-design row is now `CLOSED`.**

Pending implementation tests, drills, measured SLOs, security verification and restore/rotation exercises are not open MK0 design decisions. They are typed MK1/beta acceptance receipts defined by `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

## Current promotion state

**Internal design graph:** `CLOSED`.

**Known internal design nodes remaining:** `0`.

**MK1 production implementation:** `BLOCKED` until the external/empirical Definition of Ready in `docs/implementation/BUILD_READINESS.md` is satisfied.

The remaining unknowns are external or empirical: regulation, commercial data rights, user willingness-to-pay/retention, quant baseline/ML increment and moat durability. Provider-specific production selection is likewise evidence-gated rather than an internal architectural ambiguity.

## Hard MK1 invariants

- no custody;
- no personalized investment recommendation until counsel clears exact flow;
- no live autonomous execution;
- no unlicensed data redistribution;
- no LLM-generated trading authority;
- no performance claim without reproducible evidence;
- no historical research using information with `available_at > as_of`;
- no displayed probability without approved empirical calibration;
- no finalized DecisionRecord mutation;
- no production feature implementation that bypasses the MK0 build-readiness gate;
- no implementation-complete claim without the applicable typed acceptance receipt;
- no internal design semantic may be changed silently during coding: reopen the lock and issue an ADR when an invariant changes.
