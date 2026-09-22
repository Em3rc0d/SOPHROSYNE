# Market / Trading Education Synthesis — 2026-09-21

## Status

`OFFICIAL/INSTITUTIONAL EDUCATION SYNTHESIS / DOMAIN FOUNDATION INPUT`

Purpose: build SOPHROSYNE's market-domain baseline from reputable educational and regulatory sources instead of relying on project-owner intuition, social-media trading claims, or a single trading style.

This document is not investment advice and is not evidence that any trading strategy is profitable.

---

## Source hierarchy

Preferred order for domain foundations:

1. regulators / investor-education authorities;
2. professional curricula and university finance courses;
3. exchange / broker educational material for execution mechanics;
4. large broker educational centers for practical analysis;
5. specialist material only when consistent with stronger sources and clearly scoped.

No influencer, Discord/Telegram signal group, anonymous strategy thread, or promotional trading-course claim is used as canonical authority.

---

## Studied curriculum

### Yale — Financial Markets, Robert Shiller

Source:
https://www.coursera.org/learn/financial-markets-global-es

Observed curriculum covers:
- risk and stress;
- CAPM, beta and diversification;
- portfolio frontier;
- behavioral finance and prospect theory;
- stocks, dividends and capital structure;
- discounted present value;
- leverage;
- bubbles/regulation;
- futures/options and hedging.

Key implication:
market decisions exist inside a broader risk/portfolio/behavioral system. A price chart alone is not the complete decision object.

### MIT OpenCourseWare — Investments / Finance Theory

Sources:
https://ocw.mit.edu/courses/15-433-investments-spring-2003/
https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/

Observed curriculum covers:
- portfolio theory;
- CAPM / asset-pricing models;
- empirical equity behavior;
- market efficiency;
- performance evaluation;
- behavioral finance;
- valuation;
- diversification and risky-asset pricing.

Key implication:
SOPHROSYNE should distinguish theoretical model, empirical evidence, estimated value and observed market price.

### CFA Institute — 2026 curriculum/refresher readings

Sources:
https://www.cfainstitute.org/programs/cfa-program/curriculum
https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/overview-equity-securities
https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/equity-valuation-concepts-basic-tools
https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/introduction-financial-statement-analysis
https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/portfolio-risk-return-part-1
https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/introduction-risk-management
https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/the-behavioral-biases-of-individuals

Observed:
- equity represents an ownership claim;
- fundamental analysis uses economy/industry/company information and valuation;
- technical analysis uses market price/volume behavior;
- financial statements and cash generation matter to equity analysis;
- portfolio risk depends on return distributions and correlation;
- diversification is a core risk-control concept;
- behavioral biases alter real decision behavior;
- risk management is part of capital allocation, not a bolt-on after the trade.

Key implication:
a candidate stock decision must be decomposable into value/fundamentals, market behavior, portfolio context, uncertainty and execution.

### SEC Investor.gov — buying/selling and execution

Sources:
https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders
https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14
https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/executing-order
https://www.investor.gov/introduction-investing/getting-started/investing-your-own/online-investing
https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-brokerage-accounts

Observed:
- market orders prioritize execution, not execution price;
- limit orders constrain price but may not execute;
- stop orders become market orders once triggered;
- execution route/liquidity can change realized price;
- online execution speed does not remove research requirements;
- cash and margin accounts have materially different risk semantics.

Key implication:
"price on screen" is not necessarily executable price. Order semantics, spread, depth and account type can be material evidence.

### FINRA — stocks, diversification, day trading

Sources:
https://www.finra.org/investors/investing/investment-products/stocks
https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification
https://www.finra.org/investors/investing/investment-products/stocks/day-trading

Observed:
- stocks are ownership interests and can be held directly or through diversified funds;
- diversification/asset allocation/rebalancing are risk-management tools;
- buying on margin magnifies gains and losses;
- short selling has risks beyond ordinary long ownership;
- FINRA characterizes day trading as extremely risky and unsuitable for limited resources/limited experience/low risk tolerance.

Key implication:
SOPHROSYNE must never collapse a stock-analysis question into a day-trading posture by default.

### IBKR Traders' Academy / CME-contributed education

Sources:
https://www.interactivebrokers.com/campus/trading-course/trading-and-analysis/
https://www.interactivebrokers.com/campus/trading-course/introduction-to-tws-order-types/
https://www.interactivebrokers.com/campus/trading-course/cme-building-a-trade-plan/
https://www.interactivebrokers.com/campus/trading-course/fundamental-analysis-2/
https://www.interactivebrokers.com/campus/trading-course/introduction-to-technical-analysis/
https://www.interactivebrokers.com/campus/trading-course/cme-intermediate-technical-analysis/
https://www.interactivebrokers.com/campus/trading-course/introduction-to-margin/

Observed:
- market maker/taker and liquidity/immediacy are core execution concepts;
- bid/offer spread, liquidity and market hours are relevant before entering a market;
- a trade plan separates objective, methodology, risk rules, entries/exits and trade log;
- fundamental analysis uses balance sheet, income statement and cash flow;
- technical analysis includes chart reading, moving averages, bands/channels, momentum indicators and volatility;
- indicators have limits and must not be treated as deterministic;
- margin can produce losses larger than initial capital.

Key implication:
SOPHROSYNE's Decision Ledger concept is directionally consistent with professional trade-planning/logging practice, but must remain evidence-first rather than becoming a signal journal that rewards hindsight.

### Fidelity Learn — fundamental and technical analysis

Sources:
https://www.fidelity.com/learning-center/trading-investing/stock-analysis
https://www.fidelity.com/learning-center/trading-investing/fundamentals
https://www.fidelity.com/learning-center/trading-investing/technical-analysis/what-is-technical-analysis
https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide

Observed:
- fundamental and technical analysis answer different questions;
- fundamentals include revenue, earnings, balance-sheet strength and cash flow;
- technical analysis uses price, volume, volatility and momentum;
- technical analysis is probability-oriented/reactive rather than predictive certainty;
- indicators can conflict and do not guarantee entries/exits.

Key implication:
technical evidence should be represented as observed market structure + uncertain interpretation, never as a calibrated probability unless separately validated.

---

# Canonical domain lessons

## 1. Investment, trading and execution are separate layers

```text
investment thesis
    ↓
market/trading thesis
    ↓
risk / portfolio compatibility
    ↓
execution plan
    ↓
order / fill / realized cost
```

A valid investment thesis may still have poor timing or execution.
A technically attractive setup may still be fundamentally unattractive for a long-horizon investor.
A good trade process can still lose money.
A profitable outcome can result from poor reasoning.

## 2. Price is not value

Observed market price is a market-clearing/execution fact.

Estimated fundamental value is a model output based on assumptions.

They must never be merged into one field.

## 3. Technical analysis is conditional evidence

Allowed interpretation:
- trend;
- momentum;
- support/resistance;
- volume;
- volatility;
- relative strength;
- market structure.

Not allowed without calibration:
- "RSI says price will rise";
- "breakout = buy";
- "three bullish indicators = 75% probability";
- treating correlated indicators as independent votes.

## 4. Fundamental analysis is not a single ratio

A company-level thesis may require:
- business economics;
- revenue/earnings quality;
- cash flow;
- balance-sheet risk;
- dilution/capital allocation;
- industry position;
- valuation assumptions;
- macro/interest-rate sensitivity;
- catalyst and horizon.

A low P/E alone is not evidence that a stock is cheap.

## 5. Portfolio context matters

The same asset can have different portfolio consequences depending on:
- concentration;
- correlations;
- liquidity needs;
- horizon;
- volatility tolerance;
- existing exposures.

SOPHROSYNE may represent this context only inside the Q01-approved personalization boundary.

## 6. Liquidity and execution are first-class evidence

When relevant, scenarios should include:
- bid/ask spread;
- depth;
- volume/turnover;
- volatility regime;
- market hours/session;
- order type;
- slippage/cost assumptions.

A market order has execution-price uncertainty.
A limit order has non-execution risk.
A stop does not guarantee its trigger price as execution price.

## 7. Leverage changes the problem

Margin, leverage, short selling and derivatives are not ordinary long-only equity semantics.

They require explicit scenario classification and higher risk controls.

No SOPHROSYNE beginner path should silently introduce leverage.

## 8. Risk management precedes outcome

Risk assessment includes:
- maximum acceptable loss;
- exposure sizing;
- liquidity;
- concentration;
- scenario invalidation;
- uncertainty;
- tail behavior;
- costs.

"Stop loss" is not a complete risk-management model.

## 9. A trading plan is a process contract

Professional educational material repeatedly emphasizes:
- objective;
- methodology;
- risk rules;
- entry/exit logic;
- logging/review.

SOPHROSYNE should use this as process structure, not as a mechanism to tell a user what to trade.

## 10. Behavioral bias is part of market decision quality

Review should detect, where the evidence supports it:
- overconfidence;
- confirmation bias;
- loss aversion;
- anchoring;
- recency/hindsight;
- narrative substitution;
- disposition-like behavior.

Do not diagnose a person psychologically from one answer; code observable reasoning patterns only.

---

# Anti-patterns SOPHROSYNE must reject

- signal voting: "3 bullish vs 2 bearish therefore buy";
- TA determinism;
- hindsight scoring;
- outcome = process-quality equivalence;
- P/L as the only success metric;
- price target presented without valuation assumptions;
- stale evidence counted equally with current evidence;
- market order treated as guaranteed displayed price;
- volume treated as liquidity without spread/depth context;
- stop price treated as guaranteed exit price;
- leverage introduced without explicit risk semantics;
- single-stock thesis treated as portfolio advice;
- one indicator or ratio treated as independent confirmation of another derived from the same data;
- certainty percentages without calibration.

---

# What this changes for SOPHROSYNE

The market-domain baseline is now built from external curriculum rather than the project owner.

User feedback remains useful for:
- comprehension;
- UX;
- expectations;
- workflow pain;
- terminology clarity.

User intuition is **not** the authority for:
- market mechanics;
- technical/fundamental correctness;
- execution semantics;
- risk semantics;
- scenario answer keys.

Those require the canonical domain foundation plus independent market-domain review.
