# ADR-0016 — Closed Validation Graph Governance

## Status

ACCEPTED

## Context

SOPHROSYNE already separates design truth, evidence truth and implementation truth, but a linear lifecycle can still hide a subtle failure mode: a downstream artifact may be considered complete without explicitly returning evidence to the upstream proposition it is supposed to validate.

The project requires stronger closure semantics:

- every material node must be connected;
- every material edge must have a closure rule;
- every forward dependency must have a reverse-validation path;
- every contradiction must propagate to affected nodes;
- every release/build must bind to the exact governing graph/profile digests;
- closure must be recomputed when material evidence or semantics change.

## Decision

Adopt `docs/architecture/CLOSED_VALIDATION_GRAPH.md` as the canonical governance model for material P0/P1 product, evidence, architecture, implementation, verification, certification and runtime assumptions.

The canonical machine-readable contracts are:

- `contracts/validation_graph.schema.yaml`;
- `contracts/validation_graph.yaml`.

### Runtime architecture remains acyclic where required

This ADR does **not** authorize circular module imports, circular database ownership or circular runtime authority.

The validation graph is cyclic at the governance/evidence layer, while software dependency direction remains controlled by `MODULE_BOUNDARIES.md`.

### Closure meaning

`CLOSED` means currently supported by all required active incoming validation edges for the declared scope/version.

It does not mean permanently true.

### No-orphan rule

Every active P0/P1 node must have at least one incoming and one outgoing material edge.

### Reverse-validation rule

Every promotable P0/P1 decision must have a path from proposition/design to implementation/verification evidence and back to the governing proposition through `VALIDATES`, `INVALIDATES` or `REOPENS` semantics.

### Digest binding

Phase 0 must implement deterministic canonical serialization and SHA-256 digests for active graph snapshots.

Applicable promotion packets, bootstrap profiles, builds and acceptance receipts bind to the graph digest they were evaluated against.

### Contradiction propagation

P0/P1 contradictions freeze affected promotion/build/release paths, invalidate failed edges and trigger targeted transitive revalidation/reopening.

Historical graph snapshots and receipts remain immutable.

### Fixed-point rule

A scope may be called closed only when validation propagation reaches a stable fixed point with no unresolved P0/P1 contradiction, stale required receipt or required edge state transition.

## Consequences

### Positive

- no material design claim can become an isolated document;
- downstream verification explicitly returns to upstream authority;
- semantic drift becomes detectable through digest mismatch;
- changes have bounded blast-radius analysis;
- failed evidence cannot be hidden by unrelated successful nodes;
- build/release provenance becomes tamper-evident without adding distributed-ledger infrastructure.

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
- digest binding cannot be made deterministic;
- evidence/implementation truth cannot be represented without circular authority ambiguity;
- a simpler governance mechanism provides equivalent traceability and failure propagation with demonstrably lower complexity.

## Implementation obligation

Phase 0 must add a deterministic graph validator implementing at least CVG-001 through CVG-012 from `CLOSED_VALIDATION_GRAPH.md`.
