# MK0 Lock Registry

## Product / evidence locks

All non-closed product/evidence rows map to the canonical Q00–Q05 closure system. Q00 is the core causal-value gate; Q01–Q05 cover legal/compliance, data rights, user/commercial evidence, quantitative components and defensibility. There is no hidden parallel evidence system.

### Status vocabulary

`Status` is deliberately small:
- `CLOSED` — the scoped claim/constraint is decided for MK0;
- `PARTIAL` — some evidence exists but the scoped claim is not promotable yet;
- `OPEN` — required evidence has not closed the scoped claim.

Blocking/fatality semantics live in `Promotion role`; they are not encoded by inventing extra status names.

| Lock | Status | Promotion role | Canonical track | Decision / Evidence | Closure evidence |
|---|---|---|---|---|---|
| Problem exists | CLOSED | FOUNDATION / REOPEN_ON_Q00 | T1 + Q00 | Market complexity/information overload are plausible problems, but product-value interpretation is subordinate to causal testing. | Reopen if Q00 shows no material decision-process problem or trivial baseline suffices. |
| Product thesis | PARTIAL | FATAL_IF_Q00_FAILS | T2/T3 + Q00 | Financial Decision Intelligence is the candidate category; current intervention must beat strong simple baselines. | Q00 causal-value receipt + Q03 product-use evidence. |
| Core causal value | OPEN | FATAL_FOR_CURRENT_CONFIGURATION | Q00 | Complexity is not value unless the candidate intervention materially outperforms simple/cheap baselines under robust controls. | Q00 preregistered causal/ablation bundle. |
| Initial persona | PARTIAL | BLOCKING_IF_SCOPE_CHANGES | Q03 constrained by Q00 | Spanish-first capable beginner / intermediate self-directed investor remains the candidate. | Behavioral discovery + repeat-use + Q00 subgroup evidence. |
| Wedge | PARTIAL | BLOCKING | Q00 + Q03 | Progressive disclosure + evidence + auditability + risk-first UX are candidate mechanisms, not assumed causal drivers. | Q00 component/ablation evidence + Q03 repeat-use evidence. |
| Competition | CLOSED | INPUT_TO_Q00/Q05 | Q00 + Q05 | AI/NL/backtesting/automation/memory already exist; those capabilities alone are not moat. | Competitive refresh remains recurring evidence. |
| Moat | PARTIAL | BLOCKING_OR_CONDITIONAL | Q05 after Q00 | No single feature is moat. Defensibility must emerge from a validated compound system/accumulated asset. | Q05 comparative/retention/replicability evidence after causal value survives. |
| Peru regulatory boundary | OPEN | FATAL_IF_FAILED | Q01 | Personalized recommendations/execution and commercial/legal flows may cross regulated boundaries. | Written competent-authority review of exact frozen flows/copy. Issue #2. |
| Custody | CLOSED | HARD_MK1_CONSTRAINT | Q01 constraint | Excluded from MK1. | Keep excluded unless a future MK explicitly reopens the trust/regulatory boundary. |
| Live auto-trading | CLOSED | HARD_MK1_CONSTRAINT | Q01 constraint | Excluded from MK1. | Re-open only in a future MK with a new execution/regulatory trust boundary. |
| Market-data technical access | CLOSED | INPUT_TO_Q02 | Q02 | Sufficient technical sources exist for research. | Does not substitute for commercial rights. |
| Market-data commercial rights | OPEN | FATAL_IF_FAILED | Q02 | Access does not imply display/redistribution/derived-data rights. | Final receipts for exact production `DataUseProfile`s. Issue #3. |
| XTB automation | CLOSED | SCOPE_CONSTRAINT | Scope | Public API discontinued; no MK1 execution dependency. | Monitor only. |
| Quant feasibility | CLOSED | LIMIT / INPUT_TO_Q04 | Q04 | Signals may exist; durable alpha is not assumed. | Baseline experiment decides what the harness can demonstrate. |
| ML incremental value | OPEN | BLOCKING_FOR_ML_ONLY | Q04 subordinate to Q00 | ML must earn its place versus transparent baselines OOS after costs. | Pre-registered benchmark experiment. |
| Explainability/auditability | CLOSED | INTERNAL_CONTRACT | Internal design | Decision Record is mandatory. | Implementation acceptance receipts. |
| Causality claims | CLOSED | INTERNAL_CONTRACT | Internal design | OBSERVED / ATTRIBUTED / INFERRED / CORRELATED / UNKNOWN. | Enforce output schema. |
| LLM authority | CLOSED | HARD_MK1_CONSTRAINT | Internal design | LLM cannot invent probabilities or authorize trades. | Enforce architecture + acceptance receipts. |
| Security posture | CLOSED | INTERNAL_CONTRACT | Internal design | Least privilege, isolated LLM, no withdrawals/execution creds, kill/revoke paths. | Implementation proof via typed security receipt before real credentials/beta. |
| Unit economics | PARTIAL | BLOCKING_IF_NONVIABLE | Q02 + Q03 after Q00 | Viability depends on actual provider/compliance costs, pricing intent and retention; willingness to pay cannot rescue failed causal value. | Synchronize Q02 cost receipts + Q03 pricing/repeat-use evidence after Q00. |
| TAM/SAM/SOM | OPEN | NON_BLOCKING_UNLESS_SCOPE_CHANGES | Q03 commercial analysis | Bottom-up market sizing is not allowed to fabricate demand. | Observed funnel/account/user evidence. Reopens scope only if it materially changes MK1 boundaries. |
| MVP scope | PARTIAL | REOPEN_ON_Q00/Q01/Q03/Q04 | Q00 + Q01 + Q03 + Q04 | Translator/evidence/ledger/portfolio context/strategy sandbox are candidate components, not all guaranteed to survive ablation. | Q00 may remove unnecessary complexity; other Qs can re-scope. |
| GTM | PARTIAL | NON_BLOCKING_FOR_CORE_BUILD | Q03 + Q05 | Trust/content/community/partnerships remain channel hypotheses. | Channel/commitment evidence; not a standalone architecture gate. |
| Willingness-to-pay / retention | OPEN | BLOCKING | Q03 constrained by Q00 | Recurring value is not yet proven. Positive WTP is insufficient if incremental causal/product value fails. | Behavioral/comprehension/repeat-use/pricing bundle + Q00 compatibility. Issue #4. |
| Liability/reputation | PARTIAL | BLOCKING_AT_LEGAL/BETA_BOUNDARIES | Q01 + MK1 beta receipts | Incident semantics are closed; terms/claim policy depend on legal flow and implemented controls. | Authority-aligned terms/claim policy + beta incident/security receipts. |

### Evidence-status rule

The statuses above describe **outcomes not yet observed**, not missing internal design.

The method for closing them is frozen by:
- `docs/product/THESIS_STACK.md`;
- `docs/validation/Q00_CORE_CAUSAL_VALUE.md`;
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`;
- `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`;
- `docs/validation/MK0_PROMOTION_PACKET.md`;
- `docs/validation/MK1_BOOTSTRAP_PROFILE.md`.

No row may be marked closed merely because implementation exists or because a nearby Q passed. Closure scope must match its final `EvidenceReceipt`.

A positive Q03/Q04/Q05 result may not rescue a failed Q00 current configuration.

## Internal executable-design locks

| Lock | Status | Canonical artifact |
|---|---|---|
| Product promise / thesis layering | CLOSED | `docs/product/PRODUCT_THESIS.md`, `docs/product/THESIS_STACK.md`, `docs/mvp/MK1_SPEC.md` |
| Core causal-value falsification method | CLOSED | `docs/validation/Q00_CORE_CAUSAL_VALUE.md` |
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
| External-evidence closure protocol | CLOSED | `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md` |
| Experiment pre-registration contract | CLOSED | `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` |
| MK0 promotion packet contract | CLOSED | `docs/validation/MK0_PROMOTION_PACKET.md` |
| MK1 bootstrap-profile contract | CLOSED | `docs/validation/MK1_BOOTSTRAP_PROFILE.md` |
| Build-readiness gate | CLOSED | `docs/implementation/BUILD_READINESS.md` |
| Implementation order | CLOSED | `docs/implementation/IMPLEMENTATION_SEQUENCE.md` |

**Every known internal executable-design row is `CLOSED`.**

Pending implementation tests, drills, measured SLOs, security verification and restore/rotation exercises are not open MK0 design decisions. They are typed MK1/beta acceptance receipts defined by `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

## Current promotion state

**Internal design graph:** `CLOSED`.

**Known internal design nodes remaining:** `0`.

**External/empirical validation method:** `CLOSED`.

**External/empirical outcomes Q00–Q05:** `OPEN / PARTIAL AS LISTED ABOVE`.

**MK1 production implementation:** `BLOCKED` until Q00–Q05 applicable evidence satisfies `docs/implementation/BUILD_READINESS.md` and one evidence-derived `MK1_BOOTSTRAP_PROFILE` is approved.

The remaining uncertainty is intentionally empirical/external: core causal value, regulation, commercial data rights, user value/WTP/retention, quant baseline/ML increment and moat durability. Provider-specific production selection is evidence-gated rather than an internal architectural ambiguity.

## Hard MK1 invariants

- no custody;
- no personalized investment recommendation until Q01 clears the exact flow;
- no live autonomous execution;
- no unlicensed data redistribution;
- no LLM-generated trading authority;
- no performance claim without reproducible evidence;
- no historical research using information with `available_at > as_of`;
- no displayed probability without approved empirical calibration;
- no finalized DecisionRecord mutation;
- no empirical experiment used for promotion without a pre-registered manifest;
- no `OPEN` evidence ambiguity is interpreted optimistically; unknown legal/rights authority remains unapproved;
- no production feature implementation that bypasses the MK0 build-readiness gate;
- no production implementation against an unspecified or unapproved bootstrap profile;
- no implementation-complete claim without the applicable typed acceptance receipt;
- no internal design semantic may be changed silently during coding: reopen the lock and issue an ADR when an invariant changes;
- no evidence receipt may be silently edited after finalization: supersede it explicitly;
- no complexity may be credited as product value unless Q00 shows material incremental value over competent simpler baselines;
- no feature, language, memory mechanism, LLM capability, backtest engine or Decision Record may be called a moat without Q05 evidence;
- no willingness-to-pay signal may rescue a current configuration that fails Q00 causal value.
