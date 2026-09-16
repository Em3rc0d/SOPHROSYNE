# MK1 Quant / Backtest Engine Contract

## Purpose

The engine must make trading/research mechanics explicit so a strategy result cannot depend on hidden fill, timing, accounting or metric assumptions.

This contract defines mechanics. It does not declare any strategy profitable or suitable.

## Event timing

A signal computed with inputs available at timestamp `t` cannot receive an execution fill before the first execution point allowed by the strategy/data profile after `t`.

Examples:
- a strategy computed from a completed daily close cannot fill at that same close unless a separately modeled pre-close decision process proves the information was available in time;
- a signal from a completed 1-minute bar cannot fill inside that already completed bar.

The engine records both signal time and fill time.

## Bar-based fill policies

MK1 uses explicit named fill policies. No implicit fill exists.

Initial supported research policies may include:
- `NEXT_BAR_OPEN`;
- `NEXT_BAR_VWAP_APPROX` only when the required data/method exists;
- `NEXT_BAR_CLOSE` for intentionally delayed strategies.

Each policy defines:
- eligible next interval/session;
- price source;
- spread/slippage model;
- behavior when next bar is missing;
- behavior around market close/holiday;
- partial-fill assumption if supported.

A strategy/backtest manifest records the exact fill policy version.

## Transaction costs

Costs are explicit components, never one opaque haircut:
- commission/fee;
- bid-ask spread assumption;
- slippage/market-impact approximation where applicable;
- taxes/levies when the research scope requires them;
- funding/borrow costs only if a future instrument profile introduces those features.

MK1's initial long-only/simple profiles must not model unsupported short/leverage mechanics accidentally.

## Position and cash accounting

Canonical accounting identity:

`equity = cash + sum(marked_position_values) + explicitly modeled accrued items`

Rules:
- quantities/prices/cash use exact-decimal accounting where practical;
- fees reduce cash exactly once;
- no negative cash unless the strategy/profile explicitly permits financing;
- no short position unless explicitly enabled by a future profile;
- rejected/unfilled orders do not mutate position state;
- position transitions are event-sourced or reproducibly derivable from fills.

## Mark-to-market

Portfolio/backtest valuation declares:
- mark price type;
- timestamp/session;
- currency conversion source/policy if needed;
- stale-price behavior.

A stale mark cannot be presented as fresh without a quality flag.

## Returns

The result schema distinguishes at minimum:
- arithmetic period return;
- compounded cumulative return;
- price return;
- total return when dividends/reinvestment are explicitly modeled;
- benchmark-relative/excess return where applicable.

No report labels a price-only calculation as total return.

## Annualization

Annualization conventions are profile/config versioned.

For daily listed-market research, the chosen trading-day convention must be explicit (for example 252 when appropriate to the methodology).

For 24/7 crypto, calendar-day/hour conventions are explicit and not inherited from equities.

Sharpe/Sortino calculations record:
- return frequency;
- annualization factor;
- risk-free-rate assumption (including zero if deliberately used);
- treatment of missing periods.

## Drawdown

Drawdown is computed from the running high-water mark of the chosen equity/return series.

Report:
- maximum drawdown magnitude;
- peak date/time;
- trough date/time;
- recovery date/time when recovered;
- unrecovered state at sample end.

No absolute-dollar and percentage drawdowns are mixed without labels.

## Trade statistics

Trade aggregation semantics are explicit. Entry/exit pairs, scale-in/out behavior and partial positions cannot be counted differently across runs without a metric-version change.

Minimum definitions cover:
- number of fills;
- number of round trips/trades under the chosen aggregation rule;
- win/loss/breakeven classification;
- gross/net P&L;
- expectancy;
- profit factor where denominator semantics are defined;
- turnover.

## Benchmark

Every performance claim has a relevant benchmark or explicitly states why none is used.

Benchmark series follows the same:
- point-in-time data rules;
- return convention;
- corporate-action/total-return convention;
- sample boundaries.

A model is not compared against a benchmark using cleaner information or more favorable cost treatment than the strategy.

## Warm-up and feature availability

Indicators/features that require history declare a warm-up window. The engine may not emit a valid signal before all mandatory features are valid.

Missing input yields `NOT_EVALUABLE` rather than implicit zero/default unless the feature specification explicitly defines a value.

## Universe membership

Historical instrument membership is evaluated point-in-time. Current constituents/symbols cannot be retroactively projected backward.

A universe specification records:
- eligibility rule;
- rebalance/evaluation schedule;
- membership availability time;
- delisting handling;
- liquidity/data-quality constraints.

## Corporate actions

Fill/position/accounting behavior follows the active market-data profile:
- splits adjust units/economic value consistently;
- dividends affect cash/total-return only when the selected methodology models them;
- delisting/merger handling is explicit;
- no future corporate-action knowledge leaks into earlier decisions.

## Missing market data

The engine never invents a fill because a bar is missing.

Possible policy outcomes:
- defer to next eligible observation;
- reject/not-fill;
- mark run segment not evaluable;
- terminate a position/run according to an explicit delisting policy.

The chosen policy is versioned and reported.

## Multiple testing

Every candidate configuration tested in a research campaign is logged. Selecting the best result after many trials without accounting for selection bias is prohibited.

Promotion evidence follows `docs/quant/VALIDATION_PROTOCOL.md` and records:
- search space;
- trial count;
- untouched test period;
- correction/robustness method.

## Probability and classification metrics

If a model emits probabilities, evaluation includes calibration, not just discrimination/accuracy.

Candidate metrics may include Brier score/log loss/calibration error plus task-appropriate discrimination metrics. The exact metric set is fixed per experiment before reading the final test result.

## Numerical tolerances

Financial accounting fixtures should match exactly where decimal arithmetic is used.

Statistical floating-point outputs declare tolerances in tests. A tolerance cannot be widened merely to make a regression pass without explanation/review.

## Backtest result status

A technically completed run may be:
- `SUCCEEDED` — engine completed;
- `INVALID_DATA`;
- `INVALID_CONFIGURATION`;
- `NOT_EVALUABLE`;
- `FAILED`.

`SUCCEEDED` does not mean scientifically validated or profitable.

Separate research promotion status applies after validation protocol review.

## Minimum manifest

Every run persists:
- strategy/model version;
- code/build version;
- dataset manifest;
- universe definition;
- `as_of`/sample period;
- fill policy;
- fees/spread/slippage assumptions;
- accounting/return metric version;
- benchmark definition;
- seeds where applicable;
- output artifact hash.

## Hand-computed reference fixtures

Before beta, create tiny datasets where expected values are calculated manually for:
- one buy/hold trade with fee;
- multiple trades and drawdown;
- split event;
- dividend/price-vs-total-return case if ETF profile uses it;
- missing next bar;
- stale price;
- currency conversion if cross-currency is enabled;
- strategy signal timing proving no same-bar look-ahead.

The implementation cannot be promoted until these fixtures match.

## Non-goals for MK1

Unless opened by a future ADR/profile, the engine does not need:
- options Greeks/exercise/assignment;
- futures margin/roll mechanics;
- short borrow availability;
- leverage/liquidation;
- market microstructure/order-book simulation;
- sophisticated market impact.

Unsupported mechanics are rejected rather than approximated invisibly.