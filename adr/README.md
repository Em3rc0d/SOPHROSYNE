# Architecture Decision Records

ADRs capture decisions that must not silently drift as implementation evolves.

## ADR-0001 — Financial Decision Intelligence, not Trading Oracle

**Status:** ACCEPTED

### Context

The project could have remained framed as an ML trading bot. That framing overstates predictability, encourages hype and makes product value depend on persistent alpha.

### Decision

SOPHROSYNE is a **Financial Decision Intelligence** system. It models evidence, market state, scenarios, uncertainty, invalidation and risk. It may support user-defined strategies, but it does not claim to know the future.

### Consequences

- `NO CONCLUSION` and `NO TRADE` are valid states.
- Product value can survive if ML fails to outperform simple rules.
- UX optimizes understanding and calibration, not trading frequency.

---

## ADR-0002 — LLM Outside the Execution Path

**Status:** ACCEPTED

LLMs are restricted to explanation, translation and structured assistance. They cannot directly authorize orders, choose position size, create probabilities, alter risk limits or silently change executable strategy semantics.

Rationale: hallucination, non-determinism, prompt injection and hostile market content make free-form LLM output an unacceptable source of execution authority.

---

## ADR-0003 — Data Rights Are Architecture

**Status:** ACCEPTED

Licensing semantics are first-class domain constraints. Source adapters and derived artifacts must preserve enough provenance and rights metadata to determine allowed storage, display, redistribution and derived use.

Rationale: a prototype built on technically accessible but commercially unusable data is a dead-end architecture.

---

## ADR-0004 — Risk Engine Independent from Model Conviction

**Status:** ACCEPTED

The risk engine is logically independent from prediction, scenario and narrative layers. A model with high conviction cannot bypass portfolio, exposure, freshness or safety limits.

Rationale: confidence in a forecast and tolerance for loss are different dimensions.

---

## ADR-0005 — Decision Records Are Immutable

**Status:** ACCEPTED

A user-visible interpretation is preserved as an immutable Decision Record. Later records may supersede it; past reasoning is never rewritten to improve retrospective accuracy.

Rationale: auditability and trust require visible failure history, not only successful calls.

---

## ADR-0006 — MK1 Uses a Modular Monolith with Isolated Workers

**Status:** ACCEPTED

MK1 uses one authoritative application boundary with explicit internal modules plus separate worker processes for asynchronous/research work. It does not begin as a microservice system.

### Consequences

- domain transactions remain local and easier to reason about;
- distributed failure modes are minimized during the evidence MVP;
- module boundaries are still explicit enough for later extraction;
- a service may be extracted only after measured scaling, security/regulatory isolation, team ownership or blast-radius evidence.

Canonical detail: `docs/implementation/REFERENCE_ARCHITECTURE.md`.

---

## ADR-0007 — PostgreSQL Is the Authoritative Store and Initial Durable Job Queue

**Status:** ACCEPTED

PostgreSQL is the canonical MK1 transactional store and hosts the transactional outbox/durable job coordination using row locking, leases, attempt counts and deterministic idempotency keys.

Kafka/Redis or another broker is not an MK1 prerequisite.

### Consequences

- authoritative state and asynchronous intent can commit atomically;
- operations remain simpler during early product validation;
- a broker requires measured throughput/latency evidence and a new ADR.

Canonical detail: `docs/implementation/REFERENCE_ARCHITECTURE.md`, `docs/implementation/TECH_STACK.md`.

---

## ADR-0008 — Point-in-Time Availability Is a First-Class Time Dimension

**Status:** ACCEPTED

Every external observation distinguishes event time from the earliest time the information could legitimately have been available to SOPHROSYNE (`available_at`). Historical computation may only use data satisfying `available_at <= as_of`.

### Consequences

- look-ahead leakage becomes a schema/testable violation rather than a research convention;
- corrected history and knowledge-as-of-then remain distinct replay modes;
- provider timestamp semantics are part of adapter contracts.

Canonical detail: `docs/implementation/DATA_MODEL.md`, `docs/implementation/REPLAY_AND_REPRODUCIBILITY.md`.

---

## ADR-0009 — Deterministic Baselines Before ML

**Status:** ACCEPTED

Market-state, strategy and quant research begin with deterministic/transparent baselines. ML becomes an optional promoted component only when it demonstrates incremental out-of-sample value under the quantitative validation protocol.

### Consequences

- product value cannot depend on assumed ML alpha;
- ML failure simplifies the system instead of invalidating the entire product;
- every promoted model has a deterministic baseline/fallback or an explicit `NO_CONCLUSION` behavior.

Canonical detail: `docs/quant/VALIDATION_PROTOCOL.md`, `docs/implementation/IMPLEMENTATION_SEQUENCE.md`.

---

## ADR-0010 — Explanation Is a Downstream, Non-Authoritative Layer

**Status:** ACCEPTED

LLM/plain-language explanation consumes structured authoritative artifacts such as finalized DecisionRecords. It is implemented after the authoritative evidence/risk/ledger pipeline and cannot feed back into those semantics.

### Consequences

- LLM outage cannot disable the core product;
- explanation may be regenerated without rewriting historical analytical truth;
- hostile external text cannot acquire system authority through the explanation path.

Canonical detail: `docs/implementation/SECURITY_CONTROLS.md`, `docs/implementation/IMPLEMENTATION_SEQUENCE.md`.

---

## ADR-0011 — Production Artifacts Are Immutable and Promoted, Not Rebuilt

**Status:** ACCEPTED

CI builds immutable deployable artifacts once, records provenance/SBOM/digests, validates the release candidate in staging, and promotes the exact same artifact to production.

### Consequences

- staging and production run identical binaries;
- rollback targets are explicit image/config revisions;
- deployment provenance becomes part of reproducibility and incident analysis.

Canonical detail: `docs/implementation/CI_CD_AND_ENVIRONMENTS.md`.

---

## ADR-0012 — Design Closure Is Separate from Implementation Verification

**Status:** ACCEPTED

### Context

Security, observability and operational nodes were previously marked `CLOSED_FOR_DESIGN` because their actual implementation could only be proven later through tests, drills and measured behavior. That mixed two different states: whether a decision was still architecturally open and whether future code had already proven conformance.

### Decision

MK0 uses `CLOSED` for an internal design node once its semantics, invariants, failure behavior, change control and verification obligations are explicit and no high-impact choice is deferred to coding.

Implementation proof is represented separately through immutable typed acceptance receipts defined in `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

### Consequences

- all known MK1 internal design nodes can be closed without pretending unbuilt software has already passed tests;
- security/SLO/operations targets remain closed contracts while their receipts remain pending until implementation exists;
- a failed receipt blocks promotion but does not silently rewrite the design;
- if implementation reveals a genuine contradiction, the affected lock is explicitly reopened and an ADR is required when an invariant changes;
- `CLOSED_FOR_DESIGN` is retired from the MK1 internal lock table.

Canonical detail: `docs/implementation/INTERNAL_CLOSURE_AUDIT.md`, `docs/implementation/ACCEPTANCE_RECEIPTS.md`, `docs/implementation/BUILD_READINESS.md`.

---

## ADR-0013 — Evidence Authorizes One Exact Bootstrap Configuration, Not a Generic Build

**Status:** ACCEPTED

### Context

Closing Q01–Q05 produces evidence with scope: a legal opinion applies to reviewed flows, provider rights apply to exact data uses, user experiments apply to observed personas/workflows, quant evidence applies to frozen datasets/costs/benchmarks, and moat evidence applies to tested workflow components.

Allowing “mostly positive MK0 evidence” to unlock an unconstrained MK1 build would destroy that scope. Implementation could silently choose a different provider, asset universe, personalization level, ML role or product wedge than the evidence actually validated.

### Decision

External/empirical evidence does not authorize production implementation directly.

MK0 promotion requires:

```text
final Q01–Q05 EvidenceReceipts
        -> contradiction review
        -> approved MK0_PROMOTION_PACKET
        -> approved immutable MK1_BOOTSTRAP_PROFILE
        -> BUILD_READINESS
        -> production implementation
```

Every empirical experiment that materially contributes to Q03/Q04/Q05 promotion must be pre-registered before outcome inspection. Final evidence receipts are immutable and scoped. Production work must identify the approved bootstrap profile it implements.

Material drift from that profile reopens the relevant evidence and/or internal design boundary according to the profile's change-classification rules.

### Consequences

- one positive Q cannot average away a failed fatal Q;
- no provider/asset/interaction/ML substitution is silently treated as equivalent;
- `ML EXCLUDE` or `DEFER` can be successful evidence-derived MK1 outcomes;
- the first production build becomes reproducibly traceable to the exact evidence that justified it;
- implementation sunk cost cannot be used to lower an evidence gate after coding begins;
- future release receipts prove conformance to a known evidence-backed configuration rather than to an informal moving target.

Canonical detail: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`, `docs/validation/MK0_PROMOTION_PACKET.md`, `docs/validation/MK1_BOOTSTRAP_PROFILE.md`, `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`, `docs/implementation/BUILD_READINESS.md`.

---

## ADR-0014 — Layer the Thesis and Require Q00 Causal Value Before Complexity

**Status:** ACCEPTED

SOPHROSYNE separates T0 methodological invariant, T1 problem thesis, T2 causal intervention thesis, T3 product thesis, T4 economic thesis and T5 defensibility thesis. Passing one layer never proves the next.

Q00 is the causal-value gate that must allow competent simple baselines to defeat unnecessary product complexity. Positive willingness-to-pay, sophistication, ML, persistent memory or feature breadth cannot rescue a configuration that fails causal value.

Canonical detail: `adr/ADR-0014-THESIS-STACK-AND-Q00.md`, `docs/product/THESIS_STACK.md`, `docs/validation/Q00_CORE_CAUSAL_VALUE.md`.

---

## ADR-0015 — Pre-Build Physical Architecture Baseline

**Status:** ACCEPTED

MK1 freezes its implementation-shaping physical baseline before product coding: monorepo, one shared Python distribution with API/worker entrypoints, explicit acyclic module boundaries, PostgreSQL ownership/RLS, UUIDv7/exact-decimal/UTC semantics, transactional outbox/jobs, authoritative OpenAPI generation, `uv` + `pnpm`, and one defined first vertical slice.

These decisions constrain implementation but do not authorize build before the evidence-derived bootstrap profile and build-readiness gates pass.

Canonical detail: `adr/ADR-0015-PREBUILD-PHYSICAL-BASELINE.md`, `docs/implementation/PREBUILD_TECHNICAL_DOR.md`.

---

## ADR-0016 — Closed Validation Graph Governance

**Status:** ACCEPTED

SOPHROSYNE is governed by a cyclic validation graph while runtime dependency direction remains acyclic where required. Every material P0/P1 node must be connected, every required edge must carry closure semantics, every promotable path must have reverse validation, contradictions must propagate, and promotion/build/release artifacts must bind to the exact governing graph/profile digests.

The edge contract distinguishes `REQUIRED`, `CONDITIONAL` and `REVERSE_VALIDATION`, allowing structural closure, future verification and reopen behavior to be mechanically separated.

Canonical detail: `adr/ADR-0016-CLOSED-VALIDATION-GRAPH.md`, `docs/architecture/CLOSED_VALIDATION_GRAPH.md`, `contracts/validation_graph.schema.yaml`, `contracts/validation_graph.yaml`.

## ADR policy

Create a new ADR whenever a change modifies product promise, execution authority, risk semantics, regulatory posture, data-rights assumptions, probability semantics, LLM authority, runtime topology, authoritative persistence, point-in-time semantics, design-closure semantics, evidence-closure/promotion semantics, closed-validation-graph semantics or another invariant listed in `GOVERNANCE.md`.

Accepted ADRs may be superseded, but not silently edited into the opposite decision. A reversal requires a new ADR identifying the superseded record and evidence motivating the change.
