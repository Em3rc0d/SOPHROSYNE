# System Contracts

## Evidence Contract

Every evidence item contains source/provenance, `as_of` timestamp, observed value/event, epistemic status, freshness, data-rights classification and confidence only when its semantics are formally defined.

## Market State Contract

A market state describes what is observable now, not what must happen next. Dimensions may include trend, momentum, volatility, liquidity, derivatives/positioning, macro context, event context and on-chain context.

## Scenario Contract

A scenario is a plausible future path supported by current evidence. It must expose supporting evidence, contradicting evidence, invalidation conditions, uncertainty and—only when approved/calibrated—a probability.

## Risk Contract

Risk is computed independently from narrative/model conviction. High conviction cannot bypass risk limits.

## Strategy Contract

A strategy is explicit, versioned and testable. An LLM may help translate user intent into a draft rule, but executable semantics must be deterministic and user-visible.

## Decision Record Contract

Every user-visible analysis must be reproducible from its data snapshot, source provenance and feature/ruleset/model versions.

## LLM Contract

LLMs may summarize, translate and explain structured evidence. They may not invent probabilities, mutate risk limits, size positions, create orders or silently change deterministic strategy semantics.
