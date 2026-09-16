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

## ADR policy

Create a new ADR whenever a change modifies product promise, execution authority, risk semantics, regulatory posture, data-rights assumptions, probability semantics, LLM authority or another invariant listed in `GOVERNANCE.md`.
