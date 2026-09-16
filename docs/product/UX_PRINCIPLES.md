# UX Principles

SOPHROSYNE exists to reduce cognitive load without hiding uncertainty. The interface must make complex market evidence understandable while preserving the user’s agency.

## Progressive disclosure

The same underlying evidence should be explorable at increasing depth:

1. **Beginner** — plain-language market state, risk and uncertainty.
2. **Investor** — main drivers, portfolio context and invalidators.
3. **Trader** — indicators, market structure and strategy conditions.
4. **Quant** — raw metrics, calibration, validation and provenance.
5. **Developer** — structured contracts and APIs in later phases.

Users should not need to learn the entire vocabulary before receiving value, but every simplified statement must remain traceable to deeper evidence.

## Evidence before action

Do not lead with a giant BUY/SELL button.

Preferred hierarchy:

`What is happening? → Why? → What contradicts it? → What could invalidate it? → What is the risk? → What does my rule say?`

## Uncertainty is visible

Unknown, conflicting, stale or incomplete evidence must be represented as product state—not buried in a disclaimer.

Examples:
- data freshness badge;
- conflicting-evidence state;
- uncertainty explanation;
- scenario invalidators;
- `NO CONCLUSION`.

## Confidence must not become persuasion

A numerical probability or confidence score may only appear when its semantics and calibration are defensible. Visual emphasis must not make weak evidence feel certain.

## No dark patterns for trading activity

Never optimize UX for:
- trade frequency;
- urgency;
- FOMO;
- streaks or casino-like reinforcement;
- hiding losses;
- frictionless escalation into leverage.

The product’s success metric is better understanding and disciplined behavior, not order count.

## User agency

The system distinguishes:
- what the market evidence says;
- what SOPHROSYNE infers;
- what the user’s explicit strategy says;
- what action, if any, the user chooses.

Those layers must never be visually collapsed into a single imperative.

## Learn in context

Education should appear at the moment it helps answer a real question. Example: instead of a generic RSI lesson, explain why overextension matters in the current MarketState and show the underlying metric on demand.

## Accessibility and localization

Financial meaning must survive translation. Localization is semantic, not word-for-word. Numeric formats, time zones, currencies, color dependence and financial terminology require explicit tests.

## Responsive/mobile-first constraint

The initial wedge is mobile-first, but evidence must remain inspectable. Compact screens may hide detail behind progressive disclosure; they may not hide contradictions, uncertainty, stale-data warnings or risk.

## UX validation gate

Before freezing MK1 UX, compare SOPHROSYNE against chart-first presentation using:
- comprehension accuracy;
- time-to-understanding;
- confidence calibration;
- ability to identify uncertainty;
- ability to explain why a scenario is plausible;
- user return behavior.

A prettier interface is not sufficient evidence of a better decision system.
