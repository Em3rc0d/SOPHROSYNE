# Governance

SOPHROSYNE follows a docs-first, evidence-gated development model.

## Canonical lifecycle

`brainstorming → research/mining → design → architecture → plan → evidence closure → build → test → certification`

Implementation must not silently resolve open product, legal, data-rights or scientific questions.

## MK policy

- **MK0 — Closure & Validation:** define product, evidence base, contracts, risks and kill criteria; close the method of validation internally; then execute external/empirical validation until one exact MK1 configuration earns promotion.
- **MK1 — Evidence MVP:** build only the approved non-custodial decision-intelligence configuration identified by an immutable `MK1_BOOTSTRAP_PROFILE`.
- **MK2+ — Expansion:** connected data, execution and B2B only after separate gates open.

Each MK has a lock registry. Internal design locks and external/empirical evidence locks use different closure semantics and may not impersonate each other.

---

## Three classes of truth

### 1. Design truth

An internal contract or architecture decision owned by canonical documentation/ADR.

### 2. Evidence truth

An external fact or empirical result that must be observed, contracted, measured or reviewed.

Examples:
- qualified legal opinion;
- provider rights/terms;
- observed user behavior;
- pricing/commitment evidence;
- reproducible quant experiments;
- competitive/retention evidence.

Canonical protocol: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.

### 3. Implementation truth

Proof that built software conforms to closed design and the approved evidence-derived configuration.

Canonical implementation receipt contract: `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

No class may be used as a substitute for another.

---

## Internal design closure

An internal design lock becomes `CLOSED` only when:

- one canonical artifact owns its semantics;
- invariants and allowed/forbidden behavior are explicit;
- failure/degradation semantics are explicit where applicable;
- versioning/change control is explicit;
- implementation verification obligations are named;
- no high-impact choice is intentionally deferred to feature coding.

A closed internal design lock does **not** claim that unbuilt software has already passed tests.

Implementation proof is tracked separately with immutable typed acceptance receipts defined in `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

Examples:
- security control semantics may be `CLOSED` while `SECURITY_READINESS` is still pending;
- SLO targets and measurement semantics may be `CLOSED` while `OBSERVABILITY_SLO` is still pending;
- incident runbooks may be `CLOSED` while `INCIDENT_DRILL` is still pending.

This separation is governed by ADR-0012.

---

## External / empirical evidence closure

The **method** for closing Q01–Q05 is internal design and is frozen. The **outcomes** remain unknown until evidence exists.

Canonical lifecycle:

```text
OPEN
  -> PRE_REGISTERED
  -> EVIDENCE_RUNNING
  -> REVIEW_READY
  -> CLOSED_PASS
     or CLOSED_CONDITIONAL
     or PIVOT_REQUIRED
     or STOP_CURRENT_CONFIGURATION
```

### Pre-registration rule

Any empirical experiment that can materially influence Q03, Q04 or Q05 must freeze its primary measures and decision rule before outcome inspection using `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` or an equivalent versioned artifact satisfying the same contract.

Post-hoc threshold changes require a new experiment version. A failed/inconclusive prior version remains visible.

### External-authority rule

Where closure requires an external authority, internal confidence cannot replace it.

Examples:
- Q01 requires qualified counsel for the exact reviewed flow;
- Q02 requires authoritative provider/contractual evidence for exact intended use.

Silence, ambiguity or an informal assumption is not PASS.

### Evidence receipt rule

A promotable evidence decision requires an immutable `EvidenceReceipt` under `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.

Final receipts preserve:
- scope;
- pre-registration digest where applicable;
- authority/source;
- results;
- limitations;
- adverse/conflicting evidence;
- final decision;
- frozen outputs.

A correction/new result supersedes the receipt; it does not rewrite it in place.

---

## MK0 promotion contract

External evidence does not authorize production implementation directly.

Promotion path:

```text
Q01–Q05 evidence receipts
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
```

Canonical artifacts:
- `docs/validation/MK0_PROMOTION_PACKET.md`;
- `docs/validation/MK1_BOOTSTRAP_PROFILE.md`;
- `docs/implementation/BUILD_READINESS.md`.

### Bootstrap-profile invariant

Production MK1 may build only against one `APPROVED` bootstrap profile.

The profile freezes evidence-derived values including, where applicable:
- persona/JTBD/wedge;
- regulatory flow constraints;
- provider/data-use profiles;
- asset universe;
- fallback/freshness profiles;
- risk-policy version;
- quant baseline and explicit ML scope;
- moat/scale constraint;
- provenance digests.

A materially different configuration requires revalidation/reopening according to the profile's material-change matrix.

### Contradiction rule

A positive result in one Q cannot average away a conflicting fatal result elsewhere.

P0/P1 cross-receipt contradictions block promotion until resolved.

---

## Reopen rule

A closed internal node is reopened only when new evidence demonstrates that its canonical decision is invalid, contradictory or insufficient for the selected scope.

Reopening requires:

1. explicit lock status change;
2. affected canonical artifacts identified;
3. downstream dependency review;
4. an ADR when an invariant changes;
5. new closure evidence before implementation proceeds through the affected boundary.

Implementation inconvenience alone is not authority to silently mutate semantics.

An evidence lock/profile field reopens when its scoped authority no longer covers the intended configuration—for example a new provider, materially changed recommendation semantics or a materially different asset universe.

---

## Evidence classes

Important claims should preserve provenance:

- **OFFICIAL** — regulator, statute, exchange/vendor contract or authoritative specification.
- **ACADEMIC** — peer-reviewed paper or strong methodological source.
- **OBSERVED** — directly measured in our experiments.
- **INFERRED** — reasoned conclusion from evidence.
- **HYPOTHESIS** — intentionally unproven proposition awaiting a test.

Negative/conflicting evidence remains first-class and cannot be deleted because it weakens a preferred thesis.

---

## Change control

Changes to product promise, regulatory posture, data-rights model, execution authority, probability semantics, quant validation, risk limits, LLM authority, runtime topology, point-in-time semantics, design-closure semantics, evidence-closure semantics or critical providers require an ADR or equivalent explicit decision record when they alter an invariant.

Changes to an approved bootstrap configuration are classified by `docs/validation/MK1_BOOTSTRAP_PROFILE.md`:
- evidence-invalidating;
- internal-semantic;
- implementation-conformance;
- editorial/non-semantic.

The classification determines whether evidence, ADRs, receipts and/or a new profile version are required.

---

## Promotion rule

A later MK may not redefine an unresolved earlier lock as closed merely because implementation exists.

Likewise, implementation may not redefine a closed design contract merely because a test is hard to pass. The design is reopened explicitly or the implementation is corrected.

Production implementation may not begin because “most” external evidence is positive. The exact `MK0_PROMOTION_PACKET` and `MK1_BOOTSTRAP_PROFILE` must satisfy `BUILD_READINESS.md`.

> Code is not evidence that the underlying decision was correct.

> A passing implementation receipt is evidence of conformance, not authority to invent new semantics.

> An evidence receipt is authority only for its exact scope, not for a broader unstated product configuration.
