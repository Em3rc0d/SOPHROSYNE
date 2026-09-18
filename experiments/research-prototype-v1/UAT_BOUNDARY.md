# Research Prototype UAT Boundary

## Purpose

This document separates what can be validated by different reviewer profiles before MK0 promotion.

## Novice / non-specialist reviewer

A novice reviewer is **not** asked to validate market-model correctness.

They may validly evaluate:

- whether the scenario can be understood without prior trading expertise;
- whether favorable and contradicting evidence are distinguishable;
- whether uncertainty and missing information are visible;
- whether deeper detail feels like additional context rather than additional certainty;
- whether the decision-record flow feels understandable rather than bureaucratic;
- whether terminology creates unnecessary cognitive load.

A novice reviewer must never be treated as authority for:

- validity of technical indicators;
- market microstructure interpretation;
- quantitative thresholds;
- point-in-time data correctness;
- model calibration;
- trading or investment suitability.

## Market-domain reviewer

A market-domain reviewer evaluates:

- whether scenario framing is realistic;
- whether evidence categories are economically coherent;
- whether contradictions and invalidators are meaningful;
- whether the workflow helps disciplined analysis versus common alternatives;
- whether any wording accidentally implies causal certainty or trading advice.

This is still research review, not promotable evidence unless executed under the frozen protocol.

## Quant / engineering reviewer

Quant/engineering review owns:

- deterministic calculations;
- timestamps / point-in-time semantics;
- stale/missing data behavior;
- leakage prevention;
- reproducibility;
- metric definitions;
- fixture correctness;
- event schema and export integrity.

## Governance rule

No reviewer class may impersonate another.

A positive novice UX review cannot validate quantitative correctness.
A positive expert review cannot prove novice comprehensibility.
Automated smoke tests prove implementation properties only; they do not prove product value.

Q00 remains the authority for incremental causal value.
