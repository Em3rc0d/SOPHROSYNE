# ADR-0014 — Layer the Thesis and Require Q00 Causal Value Before Complexity

**Status:** ACCEPTED

## Context

Repeated red-team passes weakened several candidate claims:
- translation is a feature, not a moat;
- Spanish is distribution/localization, not a moat by itself;
- LLM capability is commodity-level;
- persistent memory is increasingly reproducible by broker-native systems;
- multi-source ingestion and backtesting are capabilities;
- Decision Records are trust primitives, not automatically defensibility;
- a calibration/decision-memory system may still fail because simple friction captures the benefit, because learning does not transfer, because outcome bias remains, or because users will not pay enough to support the cost structure.

A single broad thesis would let the project rescue failed claims by moving definitions after results are observed.

## Decision

SOPHROSYNE adopts a layered thesis defined in `docs/product/THESIS_STACK.md`:

- T0 methodological invariant;
- T1 problem thesis;
- T2 causal intervention thesis;
- T3 product thesis;
- T4 economic thesis;
- T5 defensibility thesis.

Passing one layer never proves the next. Failure is scoped to the claim actually contradicted.

SOPHROSYNE also adopts `docs/validation/Q00_CORE_CAUSAL_VALUE.md` as the causal-value gate preceding strong interpretation of Q03/Q04/Q05 evidence.

The full candidate product must be capable of losing to deliberately competent simple baselines.

## Required destructive baselines

Q00 includes, at minimum:
- raw-information control;
- stateless structured assistance;
- five-question friction checklist;
- simple prediction/confidence/outcome feedback;
- short-memory configuration;
- full candidate configuration.

Relevant cheap/free external substitutes may be included where operationally appropriate.

## Consequences

- product complexity is not credited as value merely because it is sophisticated;
- persistent memory may be excluded while the causal intervention survives;
- ML may be excluded while the product thesis survives;
- a B2C economic failure does not retroactively falsify causal utility, but it kills the B2C business thesis;
- moat claims require separate Q05 evidence after core value survives;
- positive willingness-to-pay cannot rescue a configuration that fails Q00 core causal value;
- simple friction capturing most of the measured effect forces simplification or pivot;
- assisted performance is distinguished from independent skill transfer;
- process quality is not equated with realized return;
- no universal gamified “decision intelligence score” is required.

## Supersession / drift

This ADR does not supersede ADR-0001. It narrows how Financial Decision Intelligence must earn its product claims.

Any future attempt to:
- remove Q00;
- treat WTP as evidence of causal value;
- label a commodity feature as moat without Q05;
- collapse T1–T5 into one success metric;
- protect complexity from competent simple baselines;

requires a new ADR that explicitly supersedes this record.

## Canonical artifacts

- `docs/product/PRODUCT_THESIS.md`
- `docs/product/THESIS_STACK.md`
- `docs/validation/Q00_CORE_CAUSAL_VALUE.md`
- `MK0_LOCKS.md`

## Final invariant

> **SOPHROSYNE earns complexity one validated layer at a time, and its strongest baseline must be allowed to defeat it.**
