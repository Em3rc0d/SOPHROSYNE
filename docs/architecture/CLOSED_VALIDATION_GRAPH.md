# Closed Validation Graph (CVG)

## Purpose

SOPHROSYNE is governed as a **closed validation graph**, not as a one-way document pipeline.

The objective is not to claim impossible certainty about markets, users, regulators or future production behavior. The objective is stronger and more operationally useful:

> No material uncertainty may remain unmodeled; no material claim may exist without an owner; no owner may declare closure without explicit validators; no validator may be accepted without immutable evidence; and no contradiction may remain local when it invalidates upstream or downstream assumptions.

A node is therefore not considered trustworthy because it was written earlier. It remains trustworthy only while its incoming validation edges remain valid.

## Two graphs, one system

SOPHROSYNE intentionally distinguishes:

1. **Runtime dependency graph** — remains mostly acyclic where required for software maintainability. Circular imports, circular table ownership and circular authority are forbidden.
2. **Validation graph** — intentionally cyclic. Design creates implementation obligations; implementation creates test evidence; tests create acceptance receipts; receipts validate design assumptions; runtime observations can invalidate receipts and reopen design.

The validation graph is cyclic by construction even when implementation dependencies are not.

```text
THESIS / INVARIANTS
        |
        v
EVIDENCE / Q00-Q05
        |
        v
PROMOTION / BOOTSTRAP
        |
        v
ARCHITECTURE / CONTRACTS
        |
        v
IMPLEMENTATION
        |
        v
TEST / ACCEPTANCE RECEIPTS
        |
        v
CERTIFICATION / RELEASE
        |
        v
RUNTIME OBSERVATION / INCIDENTS
        |
        +--------------------------+
                                   |
                                   v
                     CONTRADICTION / REOPEN
                                   |
                                   +----> THESIS / EVIDENCE / DESIGN
```

There is no terminal semantic state. `CLOSED` means **currently supported by the complete set of required incoming edges**, not permanently true.

---

## Graph primitives

### Node

A node represents one material proposition, decision, invariant, evidence conclusion, implementation surface, verification obligation or runtime observation.

Minimum fields:

```yaml
node_id: stable-string
node_type: THESIS | EVIDENCE | DESIGN | PROFILE | IMPLEMENTATION | VERIFICATION | CERTIFICATION | RUNTIME | CONTRADICTION
owner: canonical-artifact-or-authority
state: OPEN | CLOSED | CLOSED_CONDITIONAL | PENDING_EVIDENCE | FAILED | REOPENED | RETIRED
scope: explicit bounded scope
version: immutable semantic version or digest
content_digest: sha256 canonical content digest
materiality: P0 | P1 | P2 | P3
reopen_triggers: []
```

A node without explicit scope is invalid because its closure cannot be bounded.

### Edge

An edge is a typed assertion about the relationship between two nodes.

Minimum fields:

```yaml
edge_id: stable-string
from: node_id
to: node_id
relation: REQUIRES | VALIDATES | CONSTRAINS | PRODUCES | IMPLEMENTS | TESTS | CERTIFIES | OBSERVES | INVALIDATES | REOPENS
state: OPEN | CLOSED | FAILED | SUPERSEDED
closure_rule: machine-readable-or-canonical-reference
required_receipts: []
revalidate_on: []
edge_digest: sha256 canonical edge digest
```

An edge is not decorative documentation. If it is required for a promotable path and remains `OPEN`, the destination cannot be promoted.

### Receipt

A receipt is immutable evidence that an edge or set of edges was actually evaluated.

Receipts bind to:
- graph digest;
- node ids and node digests;
- edge ids and edge digests;
- build/config/provider/profile digests where applicable;
- executed checks and evidence artifacts;
- pass/fail/waiver semantics.

A receipt produced against a stale graph digest cannot silently validate a newer graph.

### Graph snapshot

A graph snapshot is an immutable canonical serialization of all active nodes and edges used for a promotion/build/release decision.

```yaml
graph_version: string
generated_at_utc: timestamp
nodes_digest: sha256
edges_digest: sha256
graph_digest: sha256
bootstrap_profile_digest: sha256 | null
supersedes_graph_digest: sha256 | null
```

The `graph_digest` is recorded in promotion packets, build metadata and applicable acceptance receipts.

---

## Closure semantics

### Structural closure

A node is structurally closed only if:

1. it has one canonical owner;
2. all required incoming edges are present;
3. every required incoming edge has a closure rule;
4. all outgoing material dependencies are declared;
5. verification/reopen obligations are declared;
6. no P0/P1 contradiction is unresolved;
7. its scope and version are immutable for the closure decision;
8. it is not an orphan in the authoritative graph.

### Evidentiary closure

An evidence-dependent node additionally requires valid EvidenceReceipts from the authority/experiment defined by its incoming edges.

### Implementation closure

An implementation node additionally requires acceptance receipts proving conformance to the exact governing design/profile digests.

### Operational closure

Operational/certification nodes remain valid only while runtime observations have not triggered an explicit invalidation/revalidation condition.

---

## No-orphan invariant

Every P0/P1 active node must have:

- at least one incoming edge that explains why it is believed/required; and
- at least one outgoing edge that explains what it affects or how it is later validated.

Exceptions are prohibited for P0/P1 nodes.

Lower-materiality leaf artifacts may be explicitly marked `NON_AUTHORITATIVE_LEAF`, but such artifacts cannot authorize product behavior.

---

## Strong-cycle invariant

Every promotable P0/P1 decision must participate in at least one complete validation cycle:

```text
proposition
  -> evidence/design constraint
  -> implementation obligation
  -> verification obligation
  -> receipt/runtime observation
  -> validates or reopens proposition
```

Before implementation exists, the cycle may be **structurally closed but evidentially pending**: verification nodes and reverse edges must already be declared even though receipts do not exist yet.

This is how MK0 can close architecture without pretending MK1 tests have already passed.

---

## Reverse-validation invariant

Forward traceability is insufficient.

Every material design edge must have a declared reverse-validation path.

Example:

```text
DATA_TIME_SEMANTICS
    --IMPLEMENTS--> INGESTION_TIMESTAMP_MAPPING
    --TESTS-------> ANTI_LEAKAGE_VERIFICATION
    --PRODUCES----> ANTI_LEAKAGE_RECEIPT
    --VALIDATES---> DATA_TIME_SEMANTICS
```

If the anti-leakage receipt fails, the system may initially suspect implementation. If repeated conforming implementations fail because the design assumption itself is invalid, the reverse path reopens the design node through the contradiction protocol.

---

## Contradiction propagation

A contradiction is a first-class node, never an informal comment.

```yaml
node_type: CONTRADICTION
severity: P0 | P1 | P2 | P3
conflicts_with: [node_id...]
evidence: [immutable-ref...]
resolution_state: OPEN | RESOLVED_IMPLEMENTATION | RESOLVED_DESIGN | RESOLVED_EVIDENCE | ACCEPTED_LIMITATION
```

For P0/P1 contradictions:

1. promotion/build/release through affected paths freezes;
2. all directly invalidated edges become `FAILED`;
3. affected descendants are marked `REVALIDATION_REQUIRED`;
4. reverse-validation paths identify candidate upstream nodes;
5. the smallest semantically sufficient cut set is reopened;
6. new evidence/ADR/version closes the cut set;
7. descendants are revalidated transitively.

The system must prefer targeted reopening over globally discarding unrelated closed nodes.

---

## Reopen algorithm

Given invalidated node/edge `x`:

1. locate all active incoming/outgoing edges of `x`;
2. classify whether failure is implementation, evidence, scope, design or external-authority failure;
3. compute affected transitive dependents until reaching independently validated boundaries;
4. reopen every node whose closure depended on a failed edge;
5. preserve unaffected nodes and all historical receipts;
6. issue a new graph version after repair;
7. invalidate any receipt bound to obsolete node/edge/graph digests where `revalidate_on` applies.

Historical graph snapshots are immutable.

---

## Hash-linked governance

SOPHROSYNE does **not** need a distributed blockchain to obtain tamper-evident governance properties.

It uses content-addressed linkage:

```text
canonical artifact digest
        ↓
node digest
        ↓
edge digest
        ↓
graph digest
        ↓
promotion/profile digest
        ↓
build digest
        ↓
acceptance receipt digest
        ↓
release/certification digest
```

Changing an upstream semantic artifact changes its digest and therefore invalidates every downstream assertion whose revalidation policy includes that dependency.

This provides blockchain-like auditability without introducing consensus/network complexity that the product does not need.

---

## Canonical macro-cycle

The authoritative lifecycle is a loop:

```text
T0-T5 / Product Thesis
        ↓
Q00-Q05 Validation
        ↓
MK0 Promotion Packet
        ↓
MK1 Bootstrap Profile
        ↓
Architecture + Technical Contracts
        ↓
Build Phase / Vertical Slice
        ↓
Acceptance Receipts
        ↓
Certification / Release
        ↓
Runtime Outcomes + Incidents + Drift
        ↓
Contradiction Review
        ↓
Revalidate / Narrow / Reopen / Retire
        └──────────────────────────────> T0-T5 / Q / Design
```

No phase can use later success to retroactively erase earlier failure.

---

## Required subcycles

### Product-value cycle

```text
THESIS -> Q00 -> approved intervention -> built surface -> observed use/outcomes -> Q00/Q03 revalidation -> THESIS
```

### Regulatory cycle

```text
Q01 authority -> approved flow constraints -> product/API/UI -> legal conformance review -> changed flow detection -> Q01 revalidation
```

### Data-rights cycle

```text
Q02 rights -> DataUseProfile -> ingestion/storage/display enforcement -> RIGHTS_CONFIGURATION receipt -> provider/contract change -> Q02 revalidation
```

### Point-in-time cycle

```text
DATA_TIME_SEMANTICS -> ingestion mapping -> research/market state -> ANTI_LEAKAGE receipt -> provider correction/new semantics -> DATA_TIME_SEMANTICS revalidation
```

### Replay cycle

```text
REPLAY_CONTRACT -> DecisionRecord implementation -> GOLDEN_REPLAY receipt -> semantic change detection -> REPLAY_CONTRACT revalidation
```

### Security cycle

```text
SECURITY_CONTROLS -> implementation -> SECURITY_READINESS -> incidents/threat changes -> control review -> SECURITY_CONTROLS
```

### Reliability cycle

```text
FAILURE_DEGRADATION -> jobs/runtime -> failure injection + SLO receipts -> incidents -> runbook/design review -> FAILURE_DEGRADATION
```

### Quant cycle

```text
Q04/VALIDATION_PROTOCOL -> research engine -> reproducible experiment -> observed OOS result/drift -> Q04/model lifecycle -> VALIDATION_PROTOCOL
```

---

## Graph validity rules

A candidate graph is invalid if any of the following is true:

- duplicate node or edge id;
- dangling edge endpoint;
- P0/P1 orphan node;
- closed node with open required incoming edge;
- closed edge without closure rule;
- receipt references stale/missing node or edge digest;
- promotable node lacks a reverse-validation path;
- contradiction exists without affected-node/edge links;
- material semantic change does not produce a new node/artifact version;
- a build/release references a graph digest other than the approved one;
- an implementation component is not reachable from the approved bootstrap profile;
- an active runtime surface has no test/receipt path;
- an active test/receipt has no governing design/evidence node;
- a P0/P1 cycle cannot return from implementation/runtime evidence to the proposition it is supposed to validate.

---

## Fixed-point closure

For a selected scope, closure is reached when repeated validation propagation reaches a fixed point:

```text
validate(graph_n) -> graph_n
```

Meaning:
- no new unresolved contradiction appears;
- no required edge changes state;
- no closed node depends on an invalid/stale receipt;
- all P0/P1 nodes satisfy structural and applicable evidence/implementation closure;
- all required reverse-validation paths exist;
- promotion/build/release gate state is stable.

Any semantic/evidence/runtime change produces `graph_n+1` and closure must be recomputed.

---

## CI enforcement target

Phase 0 must introduce a deterministic graph validator that fails CI when graph integrity rules are violated.

Minimum checks:

```text
CVG-001 schema valid
CVG-002 ids unique
CVG-003 edge referential integrity
CVG-004 no P0/P1 orphan nodes
CVG-005 closed-node incoming-edge closure
CVG-006 reverse-validation path exists
CVG-007 contradiction propagation links complete
CVG-008 receipt digests match active graph
CVG-009 bootstrap -> implementation reachability
CVG-010 implementation -> verification reachability
CVG-011 verification -> governing proposition return path
CVG-012 graph digest deterministic
```

The validator proves graph integrity, not truth of external evidence. Truth still comes from the authority/experiment represented by the receipt.

---

## Epistemic invariant

The strongest valid claim SOPHROSYNE may make about itself is not:

> "There is no uncertainty."

It is:

> **There is no material uncertainty, assumption, contradiction or verification obligation that is allowed to remain invisible to the governing graph.**

That is the project-level definition of solidity.