# Q00 Fundamental / Valuation Supplemental Scenario Pack

## Status

CANDIDATE_READY_FOR_R2 / NOT_ASSIGNED_TO_FORMAL_Q00 / NOT_EVIDENCE

Purpose: close the internal knowledge gap identified after market-domain hardening without silently changing the frozen candidate Williams design.

Canonical machine-readable material:
- experiments/q00/fundamental-scenarios/manifest.json

## Why this is supplemental

The current SYN-01…08 corpus is strong on market-state, provenance, execution, causal narratives and uncertainty. It does not adequately test company-level investment reasoning.

This pack adds three candidate investment-horizon scenarios covering:
- good business vs expensive stock;
- EPS vs cash-flow / earnings quality;
- dilution and leverage;
- low multiple vs value trap;
- DCF assumptions;
- management guidance vs observed evidence;
- refinancing / rates.

R2 decides whether these scenarios:
1. replace one or more existing arm-task cases;
2. become a separate preregistered block;
3. remain exploratory;
4. require rework.

No scenario is inserted into the formal Williams assignment before that decision.

## Domain invariants

- price is not value;
- good business is not automatically good stock at any price;
- EPS is not cash flow;
- lower P/E is not automatically cheaper in economic terms;
- DCF output is conditional on assumptions;
- analyst/management forecasts are inference;
- dilution and leverage can change per-share economics;
- macro rates can alter discount rates/refinancing conditions but do not mechanically determine stock direction;
- hidden outcome never determines whether prior reasoning was good.

## Internal QA

All three scenarios require:
- INVESTMENT decision context;
- declared 2–5 year horizon;
- no leverage;
- seven frozen facts;
- at least one valuation item;
- at least three fundamental items;
- provenance/uncertainty;
- falsifiable invalidator classes;
- hidden outcome separate from process scoring.

Internal terminal state: READY_FOR_R2.

## Non-goals

This pack does not:
- produce a fair-value recommendation;
- teach a universal DCF;
- establish alpha;
- set portfolio weights;
- recommend buying or selling a named security;
- claim that these synthetic cases exhaust fundamental analysis.
