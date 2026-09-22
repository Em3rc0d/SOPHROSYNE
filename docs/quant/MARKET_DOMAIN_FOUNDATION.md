# SOPHROSYNE Market Domain Foundation

## Status

`CANONICAL INTERNAL DOMAIN BASELINE / NOT INVESTMENT ADVICE / NOT EMPIRICAL ALPHA EVIDENCE`

Evidence source:
`mining-site/market-education/2026-09-21-market-course-synthesis.md`.

Purpose: define the minimum market/investment knowledge that SOPHROSYNE design, scenarios, UI labels and reasoning logic must respect before any market-domain reviewer evaluates higher-order correctness.

---

## 1. Domain model

SOPHROSYNE must distinguish six layers:

```text
L1 instrument / ownership semantics
L2 fundamental / valuation context
L3 market state / technical evidence
L4 portfolio / risk context
L5 execution / microstructure
L6 decision process / review
```

No layer substitutes for another.

### L1 — instrument

For equities:
- common/preferred stock;
- ownership/capital structure;
- dividends/buybacks/dilution;
- corporate actions;
- exchange/listing/session;
- long/short/leverage state.

### L2 — fundamentals / valuation

Possible evidence families:
- revenue;
- margins;
- EPS/earnings quality;
- operating/free cash flow;
- assets/liabilities/debt;
- capital allocation;
- industry economics;
- macro sensitivity;
- valuation model/relative valuation.

Every valuation statement must identify assumptions/horizon or be labeled incomplete.

### L3 — market / technical

Possible observations:
- price;
- returns;
- trend;
- momentum;
- volatility;
- volume;
- breadth;
- support/resistance;
- relative strength;
- gap/regime;
- cross-asset context.

Technical evidence is descriptive/probabilistic unless a calibrated predictive model exists.

### L4 — portfolio / risk

Possible context:
- horizon;
- concentration;
- correlation;
- risk budget;
- liquidity need;
- drawdown sensitivity;
- diversification;
- existing exposure.

Portfolio context is not collected or used for individualized output until Q01 permits the exact interaction.

### L5 — execution

Possible fields:
- bid;
- ask;
- spread;
- depth;
- venue/session;
- order type;
- order size;
- partial-fill risk;
- slippage;
- fees;
- market impact;
- settlement/account type.

Displayed price is not guaranteed execution price.

### L6 — decision process

Required reasoning primitives:
- observed;
- inferred;
- supporting;
- opposing;
- missing;
- stale;
- uncertain;
- invalidator;
- time horizon;
- process action;
- later outcome separated from prior reasoning.

---

## 2. Investment vs trading classification

Every scenario declares:

```yaml
decision_context:
  mode: INVESTMENT | SWING_TRADE | INTRADAY | EXECUTION_ONLY | RESEARCH_ONLY
  horizon:
  instrument:
  leverage: NONE | MARGIN | DERIVATIVE | SHORT | OTHER
  portfolio_context_used: false
```

If not declared, default is `RESEARCH_ONLY`.

SOPHROSYNE must never infer a user should day-trade merely because short-term market data are present.

---

## 3. Evidence classes

Each evidence item receives:

```yaml
evidence_class:
  FUNDAMENTAL
  VALUATION
  PRICE
  MOMENTUM
  VOLUME
  VOLATILITY
  LIQUIDITY
  BREADTH
  MACRO
  EVENT
  POSITIONING
  PORTFOLIO
  EXECUTION
  PROVENANCE

observability:
  OBSERVED
  DERIVED
  INFERRED

freshness:
  CURRENT
  STALE
  MISSING
  UNKNOWN

independence_group:
source_ref:
as_of:
available_at:
```

Evidence in the same `independence_group` cannot be counted as independent confirmation merely because it appears in multiple indicators.

Example:
RSI, momentum oscillator and rate-of-change derived from the same price history are related technical transformations, not three independent sources.

---

## 4. Market-state interpretation

### Trend

Trend is an observed/derived property of price behavior over a declared window.

It does not imply continuation.

### Momentum

Momentum measures persistence/strength of price movement under a defined calculation.

It does not imply fair value.

### Volume

Volume is activity, not automatically liquidity or conviction.

Interpret alongside:
- spread;
- depth;
- session;
- typical volume;
- venue/context.

### Volatility

Volatility is variability/risk-state information.

Higher volatility is not inherently bullish or bearish.

### Support / resistance

Treat as market-behavior/reference levels, not guaranteed barriers.

### Indicator disagreement

Conflicting indicators are evidence of ambiguity, not a reason to average them into false precision.

---

## 5. Fundamental interpretation

A fundamental thesis separates:

```text
business quality
financial condition
growth
cash generation
capital structure
valuation
catalyst
horizon
risk / invalidator
```

Rules:
- growth does not automatically imply undervaluation;
- good company does not automatically imply good stock at any price;
- low valuation multiple does not automatically imply bargain;
- earnings without cash-flow/balance-sheet context may be incomplete;
- forecast is inference, not observation.

---

## 6. Portfolio / risk rules

SOPHROSYNE recognizes:
- asset-specific risk;
- systematic risk;
- concentration;
- correlation;
- diversification;
- volatility;
- drawdown;
- liquidity;
- leverage.

Process-quality outputs may discuss these concepts generically.

Individualized sizing/allocation/recommendation requires the approved Q01 posture.

No default percentage position size, stop distance or target return is canonically assumed.

---

## 7. Execution rules

### Market order

```text
execution priority: high
price certainty: low
non-execution risk: low when market is available/liquid
```

### Limit order

```text
price constraint: explicit
execution guarantee: none
```

### Stop order

Trigger changes order state; trigger price is not guaranteed execution price.

### Stop-limit

Adds execution-price control while increasing non-execution risk.

### Liquidity

Execution quality depends on more than volume.

Relevant evidence can include:
- spread;
- depth;
- order size;
- volatility;
- venue/session.

---

## 8. Leverage / short / derivative boundary

When `leverage != NONE`:
- scenario must flag elevated loss mechanics;
- margin/collateral semantics must be explicit;
- potential loss beyond initial amount must be represented where applicable;
- beginner simplification cannot hide these mechanics.

No leverage is introduced merely to increase scenario difficulty.

---

## 9. Technical-analysis epistemic contract

Allowed:
- "momentum is positive under this definition";
- "price broke the prior range";
- "volume did/did not confirm relative to this baseline";
- "volatility is elevated";
- "this setup resembles a historical pattern."

Not allowed without separate calibration:
- "there is a 73% chance price rises";
- "RSI confirms a buy";
- "MACD crossover predicts the next move";
- "support will hold";
- "three indicators make the thesis three times stronger."

Technical analysis may contribute evidence. It is not an oracle.

---

## 10. Fundamental-analysis epistemic contract

Allowed:
- report observed financial metrics;
- derive transparent ratios;
- state assumptions;
- compare valuation under explicit models;
- identify uncertainty.

Not allowed:
- convert analyst consensus into fact;
- hide model sensitivity;
- call a company undervalued without showing valuation basis;
- treat past growth as guaranteed future growth.

---

## 11. Behavioral reasoning contract

The system may flag reasoning patterns such as:
- evidence selection skew;
- excessive confidence relative to evidence;
- recency/hindsight use;
- narrative without causal support;
- reluctance to update after invalidation.

It must not diagnose personality or psychological disorders.

---

## 12. Decision Ledger fields

A strong record should be able to preserve:

```yaml
as_of:
context_mode:
horizon:
instrument:
observations: []
inferences: []
supporting_evidence: []
opposing_evidence: []
missing_or_stale: []
liquidity_execution_notes: []
fundamental_notes: []
technical_notes: []
risk_notes: []
invalidation_conditions: []
confidence_in_interpretation:
process_posture:
later_outcome_ref:
hindsight_review:
```

The later outcome cannot rewrite the original record.

---

## 13. Beginner UX rule

Beginner mode explains:
- what is known;
- what is uncertain;
- why a signal is not a guarantee;
- what market term means;
- what additional evidence matters.

It does not simplify by inventing certainty.

Examples:
- "El precio está subiendo" is acceptable.
- "La acción seguirá subiendo" is not supported merely by trend.
- "El volumen aumentó" is acceptable.
- "Los compradores tienen el control" is inference and must be labeled as such.

---

## 14. Scenario realism requirements

Every promotable market scenario must declare:
- instrument/context;
- horizon/mode;
- as_of;
- information availability;
- evidence classes;
- technical/fundamental coverage where relevant;
- liquidity/execution relevance;
- invalidator;
- uncertainty;
- hidden later outcome;
- why the scenario is not asking for a live trade.

A market-domain reviewer evaluates realism against this foundation, not against the project owner's trading intuition.

---

## 15. Alpha / prediction boundary

This domain foundation teaches market mechanics and disciplined reasoning.

It does **not** establish:
- predictive alpha;
- profitable indicators;
- valid price targets;
- profitable strategy;
- optimal trade sizing;
- suitability for a person.

Those require Q04 empirical validation and, where personalized, the Q01-approved product posture.

---

## Final invariant

> SOPHROSYNE is allowed to understand markets deeply without pretending that market knowledge creates certainty.

The system's job is to structure evidence, uncertainty, risk and decision process; prediction claims require separate empirical proof.
