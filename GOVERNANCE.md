# Governance

SOPHROSYNE follows a docs-first, evidence-gated development model governed by a **Closed Validation Graph (CVG)**.

## Canonical lifecycle

The operational sequence remains:

`brainstorming → research/mining → design → architecture → plan → evidence closure → build → test → certification`

But governance authority is **not linear**. Certification, runtime observations, incidents, drift and contradictory evidence feed back into evidence, design and thesis nodes through explicit reverse-validation and reopen edges.

Canonical governance loop:

```text
thesis / invariants
      ↓
evidence / Q00-Q05
      ↓
promotion / bootstrap
      ↓
architecture / contracts
      ↓
implementation
      ↓
test / acceptance receipts
      ↓
certification / release
      ↓
runtime observations / incidents
      ↓
contradiction review / reopen
      └──────────────────────→ thesis / evidence / design
```

Implementation must not silently resolve open product, legal, data-rights or scientific questions.

Canonical CVG specification: `docs/architecture/CLOSED_VALIDATION_GRAPH.md`.

Canonical machine-readable graph: `contracts/validation_graph.yaml`.

Canonical graph-closure audit: `docs/implementation/GRAPH_CLOSURE_AUDIT.md`.

This validation loop is intentionally cyclic. Runtime/module dependency direction remains controlled separately and may remain acyclic where required for maintainability and authority isolation.

## MK policy

- **MK0 — Closure & Validation:** define product, evidence base, contracts, risks and kill criteria; close the method of validation internally; then execute external/empirical validation until one exact MK1 configuration earns promotion.
- **MK1 — Evidence MVP:** build only the approved non-custodial decision-intelligence configuration identified by an immutable `MK1_BOOTSTRAP_PROFILE` and governing CVG snapshot.
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

Under ADR-0016, the CVG links these truth classes without collapsing them. An evidence node may validate a thesis; a design node may constrain an implementation; a receipt may validate implementation conformance; a runtime contradiction may reopen the exact upstream nodes whose closure depended on an invalid edge.

---

## Closed Validation Graph invariants

Every active P0/P1 material node must have:

- one canonical owner;
- explicit bounded scope/version;
- at least one incoming material edge explaining why it is believed/required;
- at least one outgoing material edge explaining what it constrains, produces or how it is later validated;
- explicit reopen/revalidation triggers;
- a reverse-validation path from implementation/verification/runtime evidence back to the governing proposition.

A node without these properties is not closed even if its document appears complete.

Every material edge must define:

- source and destination node ids;
- relation type;
- closure rule;
- required receipts/evidence where applicable;
- revalidation triggers;
- immutable/versioned identity.

P0/P1 orphan nodes, dangling required edges and one-way promotable paths are invalid governance states.

`CLOSED` means **currently supported for the declared scope by all required active incoming validation edges**. It does not mean permanently true.

---

## Internal design closure

An internal design lock becomes `CLOSED` only when:

- one canonical artifact owns its semantics;
- invariants and allowed/forbidden behavior are explicit;
- failure/degradation semantics are explicit where applicable;
- versioning/change control is explicit;
- implementation verification obligations are named;
- no high-impact choice is intentionally deferred to feature coding;
- the node is structurally connected to the governing CVG;
- its forward implementation obligation and reverse-validation/reopen path are declared;
- no unresolved P0/P1 contradiction invalidates its required incoming edges.

A closed internal design lock does **not** claim that unbuilt software has already passed tests.

Implementation proof is tracked separately with immutable typed acceptance receipts defined in `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

Examples:
- security control semantics may be `CLOSED` while `SECURITY_READINESS` is still pending;
- SLO targets and measurement semantics may be `CLOSED` while `OBSERVABILITY_SLO` is still pending;
- incident runbooks may be `CLOSED` while `INCIDENT_DRILL` is still pending;
- graph structure may be `CLOSED_FOR_STRUCTURE` while Phase 0 hashing/`GRAPH_CONFORMANCE` execution remains pending.

This separation is governed by ADR-0012 and ADR-0016.

---

## External / empirical evidence closure

The **method** for closing Q00–Q05 is internal design and is frozen. The **outcomes** remain unknown until evidence exists.

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

Any empirical experiment that can materially influence Q00, Q03, Q04 or Q05 must freeze its primary measures and decision rule before outcome inspection using `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` or an equivalent versioned artifact satisfying the same contract.

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

Evidence receipts bind to the thesis/evidence nodes they validate. Once Phase 0 graph hashing exists, promotable receipts also bind to the relevant `graph_digest`/node digests when applicable.

---

## MK0 promotion contract

External evidence does not authorize production implementation directly.

Promotion path:

```text
Q00–Q05 evidence receipts
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
BUILD_READINESS + CVG closure
        |
        v
production MK1 implementation
```

Canonical artifacts:
- `docs/validation/MK0_PROMOTION_PACKET.md`;
- `docs/validation/MK1_BOOTSTRAP_PROFILE.md`;
- `docs/implementation/BUILD_READINESS.md`;
- `docs/architecture/CLOSED_VALIDATION_GRAPH.md`;
- `contracts/validation_graph.yaml`.

### Bootstrap-profile invariant

Production MK1 may build only against one `APPROVED` bootstrap profile and one compatible governing validation-graph snapshot.

The profile freezes evidence-derived values including, where applicable:
- persona/JTBD/wedge;
- regulatory flow constraints;
- provider/data-use profiles;
- asset universe;
- fallback/freshness profiles;
- risk-policy version;
- quant baseline and explicit ML scope;
- moat/scale constraint;
- provenance digests;
- graph version and, after Phase 0 hashing exists, graph digest.

A materially different configuration requires revalidation/reopening according to the profile's material-change matrix and ADR-0016 graph propagation rules.

### Contradiction rule

A positive result in one Q cannot average away a conflicting fatal result elsewhere.

P0/P1 cross-receipt contradictions block promotion until resolved.

A contradiction is a first-class graph node/condition. It must identify affected nodes/edges and trigger targeted transitive revalidation rather than remain as an informal note.

---

## Reverse-validation rule

Forward traceability is insufficient.

Every material P0/P1 design/product/evidence decision must have a declared return path from downstream verification/runtime evidence to the proposition it is supposed to validate.

Examples:

```text
DATA_TIME_SEMANTICS
  -> ingestion timestamp mapping
  -> market/research implementation
  -> ANTI_LEAKAGE receipt
  -> validates or reopens DATA_TIME_SEMANTICS
```

```text
Q02 rights authority
  -> DataUseProfile
  -> rights enforcement
  -> RIGHTS_CONFIGURATION receipt
  -> provider/contract change detection
  -> Q02 revalidation
```

If no return path exists, the material node is structurally incomplete.

---

## Reopen rule

A closed internal node is reopened when new evidence demonstrates that its canonical decision is invalid, contradictory or insufficient for the selected scope.

Reopening requires:

1. explicit lock/node status change;
2. affected canonical artifacts identified;
3. affected graph edges identified;
4. downstream dependency and reverse-validation review;
5. an ADR when an invariant changes;
6. new closure evidence before implementation proceeds through the affected boundary;
7. stale receipts invalidated according to their `revalidate_on` policy.

Implementation inconvenience alone is not authority to silently mutate semantics.

An evidence lock/profile field reopens when its scoped authority no longer covers the intended configuration—for example a new provider, materially changed recommendation semantics or a materially different asset universe.

Reopening should affect the smallest semantically sufficient cut set; unrelated closed nodes remain valid.

---

## Fixed-point closure rule

A selected scope is considered closed only when repeated validation propagation reaches a stable fixed point:

```text
validate(graph_n) -> graph_n
```

For the relevant gate this means:

- no new unresolved P0/P1 contradiction appears;
- no required edge changes state;
- no closed node depends on a stale/invalid required receipt;
- all required reverse-validation paths exist;
- every active P0/P1 implementation surface is reachable from the approved profile and reaches required verification;
- gate state is stable for the exact graph/profile/build digests.

Any material semantic/evidence/runtime change produces a new graph state requiring recomputation.

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

## Hash-linked governance

SOPHROSYNE uses content-addressed governance rather than a distributed blockchain.

Phase 0 must establish deterministic SHA-256 linkage:

```text
canonical artifact digest
        -> node digest
        -> edge digest
        -> graph digest
        -> promotion/profile digest
        -> build digest
        -> acceptance receipt digest
        -> release/certification digest
```

Changing a material upstream semantic artifact changes the corresponding graph state and invalidates downstream assertions whose revalidation policy depends on that change.

This provides tamper-evident provenance without introducing unnecessary distributed-consensus infrastructure.

---

## Change control

Changes to product promise, regulatory posture, data-rights model, execution authority, probability semantics, quant validation, risk limits, LLM authority, runtime topology, point-in-time semantics, design-closure semantics, evidence-closure semantics, CVG node/edge semantics, graph reachability or critical providers require an ADR or equivalent explicit decision record when they alter an invariant.

Changes to an approved bootstrap configuration are classified by `docs/validation/MK1_BOOTSTRAP_PROFILE.md`:
- evidence-invalidating;
- internal-semantic;
- implementation-conformance;
- editorial/non-semantic.

The classification determines whether evidence, ADRs, graph revalidation, receipts and/or a new profile version are required.

---

## Promotion rule

A later MK may not redefine an unresolved earlier lock as closed merely because implementation exists.

Likewise, implementation may not redefine a closed design contract merely because a test is hard to pass. The design is reopened explicitly or the implementation is corrected.

Production implementation may not begin because “most” external evidence is positive. The exact `MK0_PROMOTION_PACKET`, `MK1_BOOTSTRAP_PROFILE`, Closed Validation Graph and `BUILD_READINESS.md` conditions must all agree.

No downstream green node may rescue a fatal failed incoming edge elsewhere on the active path.

> Code is not evidence that the underlying decision was correct.

> A passing implementation receipt is evidence of conformance, not authority to invent new semantics.

> An evidence receipt is authority only for its exact scope, not for a broader unstated product configuration.

> A closed graph is not a claim of perfect certainty; it is a guarantee that no known material assumption, contradiction or verification obligation is allowed to remain invisible to governance.
