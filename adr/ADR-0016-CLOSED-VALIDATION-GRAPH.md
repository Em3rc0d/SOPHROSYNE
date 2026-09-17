# ADR-0016 — Closed Validation Graph Governance

## Status

ACCEPTED

## Context

SOPHROSYNE already separates design truth, evidence truth and implementation truth, but a linear lifecycle can still hide a subtle failure mode: a downstream artifact may be considered complete without explicitly returning evidence to the upstream proposition it is supposed to validate.

The project requires stronger closure semantics:

- every material node must be connected;
- every material edge must have an explicit closure role and closure rule;
- every forward dependency must have a reverse-validation path;
- every contradiction must propagate to affected nodes;
- every release/build must bind to the exact governing graph/profile digests;
- closure must be recomputed when material evidence or semantics change.

## Decision

Adopt `docs/architecture/CLOSED_VALIDATION_GRAPH.md` as the canonical governance model for material P0/P1 product, evidence, architecture, implementation, verification, certification and runtime assumptions.

The canonical machine-readable contracts are:

- `contracts/validation_graph.schema.yaml` — schema v2;
- `contracts/validation_graph.yaml` — active macro graph, currently `cvg-macro-v2`.

### Runtime architecture remains acyclic where required

This ADR does **not** authorize circular module imports, circular database ownership or circular runtime authority.

The validation graph is cyclic at the governance/evidence layer, while software dependency direction remains controlled by `MODULE_BOUNDARIES.md`.

### Closure meaning

`CLOSED` means currently supported by all active `REQUIRED` incoming validation edges for the declared scope/version.

It does not mean permanently true.

Every material edge declares one closure role:

- `REQUIRED` — blocks target closure/promotion while open;
- `CONDITIONAL` — becomes a gate only when its declared scope/lifecycle condition activates;
- `REVERSE_VALIDATION` — returns evidence/reopen authority upstream and is not itself a current target-closing prerequisite.

This distinction is mandatory and machine-checkable under schema v2.

### No-orphan rule

Every active P0/P1 node must have at least one incoming and one outgoing material edge.

There is no exempt genesis/root node. Even T0 has a declared reverse/reopen path if the methodological invariant itself is contradicted.

### Reverse-validation rule

Every promotable P0/P1 decision must have a path from proposition/design to implementation/verification evidence and back to the governing proposition through `VALIDATES`, `INVALIDATES` or `REOPENS` semantics.

The return path does not create circular authority: downstream evidence does not validate itself; it evaluates a separately owned upstream proposition against predefined criteria.

### Digest binding

Phase 0 must implement deterministic canonical serialization and SHA-256 digests for active graph snapshots.

Applicable promotion packets, bootstrap profiles, builds, acceptance receipts and releases bind to the graph digest they were evaluated against.

Before Phase 0 hashing exists, the graph version is authoritative and digest fields remain explicit pending placeholders; fabricated digests are forbidden.

### Contradiction propagation

P0/P1 contradictions freeze affected promotion/build/release paths, invalidate failed edges and trigger targeted transitive revalidation/reopening.

The contradiction-processing mechanism is a `DESIGN` node; actual discovered contradictions instantiate `CONTRADICTION` nodes.

Historical graph snapshots and receipts remain immutable.

### Fixed-point rule

A scope may be called closed only when validation propagation reaches a stable fixed point with no unresolved P0/P1 contradiction, stale required receipt or active required-edge violation.

A material semantic/evidence/runtime change creates a new graph state that must earn closure again.

## Pre-merge self-red-team consequence

The first draft of the CVG failed its own rules before acceptance:

1. `T0_METHOD` had no incoming/reopen edge and was therefore a P0 orphan;
2. the schema referred to “required incoming edges” without a machine-readable edge role;
3. `CONTRADICTION_REVIEW` was typed as a contradiction event rather than the design mechanism that handles such events.

The design was reopened and corrected before merge:

- `E017` now provides `CONTRADICTION_REVIEW -> T0_METHOD` as `REVERSE_VALIDATION`;
- schema v2 introduces `closure_requirement = REQUIRED | CONDITIONAL | REVERSE_VALIDATION`;
- `CONTRADICTION_REVIEW` is a `DESIGN` node while real contradiction instances use `CONTRADICTION`;
- macro graph advanced to `cvg-macro-v2`.

The failed draft remains in Git history. The project does not rewrite the history of its own contradictions.

## Consequences

### Positive

- no material design claim can become an isolated document;
- downstream verification explicitly returns to upstream authority;
- semantic drift becomes detectable through digest mismatch;
- changes have bounded blast-radius analysis;
- failed evidence cannot be hidden by unrelated successful nodes;
- build/release provenance becomes tamper-evident without adding distributed-ledger infrastructure;
- the governance mechanism itself is falsifiable and reopenable.

### Cost

- more metadata must be maintained;
- graph validation becomes a mandatory CI concern;
- material changes can invalidate several downstream receipts;
- governance becomes stricter than ordinary documentation workflows.

These costs are accepted because SOPHROSYNE prioritizes reproducibility, trust and explicit uncertainty over development convenience.

## Reopen triggers

This ADR reopens if:

- the graph model cannot represent a material lifecycle or authority relationship;
- graph integrity checks create contradictory closure semantics;
- edge-role semantics prove insufficient or ambiguous;
- digest binding cannot be made deterministic;
- evidence/implementation truth cannot be represented without circular authority ambiguity;
- a required reverse-validation path cannot be expressed without violating runtime authority boundaries;
- a simpler governance mechanism provides equivalent traceability and failure propagation with demonstrably lower complexity.

## Implementation obligation

Phase 0 must add a deterministic graph validator implementing at least CVG-001 through CVG-012 from `CLOSED_VALIDATION_GRAPH.md`, including:

- schema/referential-integrity validation;
- required/conditional/reverse edge semantics;
- P0/P1 orphan detection;
- reverse-validation reachability;
- bootstrap -> implementation -> verification -> governing-proposition reachability;
- contradiction propagation support;
- deterministic SHA-256 graph digests;
- `GRAPH_CONFORMANCE` receipt generation.
