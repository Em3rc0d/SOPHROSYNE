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

## ADR policy

Create a new ADR whenever a change modifies product promise, execution authority, risk semantics, regulatory posture, data-rights assumptions, probability semantics, LLM authority, runtime topology, authoritative persistence, point-in-time semantics or another invariant listed in `GOVERNANCE.md`.

Accepted ADRs may be superseded, but not silently edited into the opposite decision. A reversal requires a new ADR identifying the superseded record and evidence motivating the change.