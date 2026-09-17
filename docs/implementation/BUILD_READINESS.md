# MK1 Build Readiness Gate

## Current verdict

**INTERNAL DESIGN: CLOSED**

**KNOWN INTERNAL DESIGN NODES REMAINING: 0**

**MK1 IMPLEMENTATION: BLOCKED BY EXTERNAL / EMPIRICAL LOCKS**

The architecture is specific enough to implement without choosing major system semantics during coding. Remaining implementation tests, drills and measured operational properties are acceptance evidence, not unresolved MK0 design decisions.

Canonical internal-closure audit: `docs/implementation/INTERNAL_CLOSURE_AUDIT.md`.

Canonical implementation-verification schema: `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

Canonical thesis layering: `docs/product/THESIS_STACK.md`.

Canonical core causal-value gate: `docs/validation/Q00_CORE_CAUSAL_VALUE.md`.

Canonical external/empirical closure protocol: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.

Canonical pre-build experiment template: `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`.

Canonical MK0 promotion packet: `docs/validation/MK0_PROMOTION_PACKET.md`.

Canonical evidence-derived implementation profile: `docs/validation/MK1_BOOTSTRAP_PROFILE.md`.

---

## Internal design locks

| Lock | Status | Canonical artifact |
|---|---|---|
| Product thesis / layered claims | CLOSED | `docs/product/PRODUCT_THESIS.md`, `docs/product/THESIS_STACK.md`, `docs/mvp/MK1_SPEC.md` |
| Core causal-value falsification method | CLOSED | `docs/validation/Q00_CORE_CAUSAL_VALUE.md` |
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
| Security controls | CLOSED | `docs/implementation/SECURITY_CONTROLS.md` |
| Config/secrets | CLOSED | `docs/implementation/CONFIGURATION_AND_SECRETS.md` |
| Observability/SLO contract | CLOSED | `docs/implementation/OBSERVABILITY_AND_SLOS.md` |
| Test strategy | CLOSED | `docs/implementation/TEST_STRATEGY.md` |
| CI/CD / migration / rollback | CLOSED | `docs/implementation/CI_CD_AND_ENVIRONMENTS.md` |
| Operational incident model | CLOSED | `docs/implementation/OPERATIONS_RUNBOOK.md` |
| Quant validation method | CLOSED | `docs/quant/VALIDATION_PROTOCOL.md` |
| Data-rights architecture | CLOSED | `docs/data/DATA_RIGHTS.md` |
| Acceptance-receipt schema | CLOSED | `docs/implementation/ACCEPTANCE_RECEIPTS.md` |
| Internal closure audit | CLOSED | `docs/implementation/INTERNAL_CLOSURE_AUDIT.md` |
| External-evidence closure protocol | CLOSED | `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md` |
| Experiment pre-registration contract | CLOSED | `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` |
| MK0 promotion packet contract | CLOSED | `docs/validation/MK0_PROMOTION_PACKET.md` |
| MK1 bootstrap-profile contract | CLOSED | `docs/validation/MK1_BOOTSTRAP_PROFILE.md` |
| Build-readiness gate | CLOSED | this document |
| Risk-minimizing implementation order | CLOSED | `docs/implementation/IMPLEMENTATION_SEQUENCE.md` |

Every known MK1 internal design node remains closed.

A future `SECURITY_READINESS`, `OBSERVABILITY_SLO`, `INCIDENT_DRILL`, `BACKUP_RESTORE`, `GOLDEN_REPLAY` or other implementation receipt may still be pending because the implementation does not yet exist. That status belongs to MK1/beta verification, not to the MK0 design graph.

---

## External / empirical locks that still block MK1

### Q00 — Core causal value — FATAL_FOR_CURRENT_CONFIGURATION

Requires preregistered evidence that the candidate intervention produces material incremental decision-process value over competent simple baselines and realistic cheap/free substitutes.

A valid `CLOSED_CONDITIONAL` may narrow the intervention by excluding persistent memory, ML, multimodal complexity or other components.

A failed current configuration cannot be rescued by willingness-to-pay, model sophistication or moat narrative.

### Q01 — Peru regulatory boundary — FATAL_IF_FAILED

Issue #2.

Requires written qualified external review of the exact frozen product/commercial flows within the applicable Peru legal surfaces.

Closure authority is external. Self-certification is not allowed.

### Q02 — Commercial market-data rights — FATAL_IF_FAILED

Issue #3.

Requires authoritative evidence for every initial production `DataUseProfile` covering the intended commercial use.

Unknown or stale rights default to denied/pending review.

### Q03 — Willingness to pay / repeat use

Issue #4.

Requires pre-registered behavioral, comprehension, repeat-use and pricing/commitment evidence compatible with the intervention scope that survives Q00.

Statements of enthusiasm alone do not close the lock.

### Q04 — Quant baseline / ML incremental value

Requires a reproducible deterministic baseline harness before any ML promotion decision.

A valid closure may explicitly exclude ML from MK1. Q04 complexity cannot substitute for Q00 product-value evidence.

### Q05 — Moat / competitive durability

Issue #6.

Requires preference/repeat-use evidence and a replicability assessment after core value survives.

A valid conditional closure may authorize MK1 only as a learning wedge while scale architecture/large GTM spend remain blocked.

---

## Evidence lifecycle requirement

Each external / empirical lock must follow the canonical validation lifecycle and terminal vocabulary defined by the validation system.

No Q may move directly from `OPEN` to a promotable state without the required immutable `EvidenceReceipt`.

Empirical Q00/Q03/Q04/Q05 experiments use `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` before outcome inspection.

---

## Allowed work before all locks close

To preserve docs-first discipline, **production feature implementation remains blocked**.

Allowed activities:
- research scripts used strictly to close Q00/Q03/Q04/Q05;
- throwaway/prototype UX used for causal/behavioral/legal review, clearly outside production architecture;
- provider/legal discovery;
- infrastructure spikes whose output is evidence/measurement, not production code;
- test fixture/schema prototyping needed to validate a design assumption;
- generation of evidence receipts, contradiction logs and candidate bootstrap profiles.

These artifacts do not become MK1 production code merely because they are useful.

---

## Definition of Ready — start production MK1 implementation

All must be true:

1. Q00 has a final `CLOSED_PASS` or `CLOSED_CONDITIONAL` receipt defining the exact intervention scope and excluded/deferred complexity.
2. Q01 has a final `CLOSED_PASS` or `CLOSED_CONDITIONAL` evidence receipt from the required external authority.
3. Q02 has a final promotable evidence receipt for every initial production `DataUseProfile`.
4. Q03 has final promotable evidence supporting the selected persona/JTBD/wedge and is compatible with Q00 conclusions.
5. Q04 baseline-harness validity is reproducibly closed; ML is explicitly `INCLUDE`, `EXCLUDE` or `DEFER`.
6. Q05 is `CLOSED_PASS` or an explicit `CLOSED_CONDITIONAL` learning-wedge state whose scale constraints are frozen.
7. Every empirical experiment used for closure was pre-registered before outcome inspection.
8. Failed/inconclusive evidence remains preserved in the experiment/evidence history.
9. Initial production provider set and fallback compatibility groups are frozen by Q02 evidence.
10. Initial exact asset universe and corresponding market-data profile(s) are frozen.
11. Initial freshness profiles and risk policy version are frozen.
12. Corporate-action/session/currency semantics for every selected profile are confirmed against actual provider capabilities/fixtures.
13. Unit-economics assumptions are synchronized with observed pricing evidence and actual provider/compliance cost assumptions.
14. No unit-economics or WTP result is being used to rescue failed Q00 causal value.
15. Cross-receipt contradiction log has no unresolved P0/P1 item.
16. Architecture impact review finds no unresolved P0/P1 internal contradiction introduced by evidence-driven selections.
17. `MK0_LOCKS.md` contains no OPEN/PARTIAL evidence item whose outcome would materially change MK1 system boundaries.
18. One `MK1_BOOTSTRAP_PROFILE` is `APPROVED` and identifies the exact configuration to build, including Q00-driven exclusions/constraints.
19. `docs/validation/MK0_PROMOTION_PACKET.md` is instantiated for the candidate and receives final `APPROVED` status.

The internal design graph itself is not a remaining condition: it is already closed. If new evidence materially invalidates an internal decision, that node is explicitly reopened under governance rather than silently changed in code.

---

## Build authorization rule

Every production implementation PR after MK0 promotion must identify:

```text
bootstrap_profile_id:
affected_profile_sections:
semantic_change: YES | NO
requires_revalidation: YES | NO
requires_adr: YES | NO
acceptance_receipts_required: []
```

Production work that cannot identify its governing bootstrap profile is not ready.

---

## Definition of Ready — beta

In addition to implementation completion:

- mandatory CI gates green;
- all required current acceptance receipts defined by `ACCEPTANCE_RECEIPTS.md` are `PASS`;
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
- user-facing legal copy/terms match the Q01-approved flow profile;
- production data use matches Q02-approved `DataUseProfile`s;
- product surface matches the Q00-approved intervention scope;
- no excluded Q00 component is silently reintroduced;
- no uncalibrated probability or unsupported performance claim exposed;
- released semantics still match the approved `MK1_BOOTSTRAP_PROFILE`.

---

## Definition of Done — one vertical slice

A slice is done only when it has:
- bootstrap-profile traceability;
- domain/API contract;
- persistence migration where required;
- authorization;
- telemetry;
- unit/integration/contract tests;
- failure/degradation behavior;
- user-visible stale/error semantics;
- applicable acceptance receipt evidence;
- documentation/ADR updates for semantic changes;
- staging verification.

A UI screen backed by mock data is not a completed vertical slice.

---

## Stop rule

If new evidence invalidates causal value, product, legal, data-rights, quant or an internal architectural assumption, **stop and update the graph before coding around the contradiction**.

The purpose of this gate is not to eliminate all uncertainty—impossible in a real system—but to ensure no known high-impact decision is deferred accidentally into implementation and no validated configuration is silently replaced during build.
