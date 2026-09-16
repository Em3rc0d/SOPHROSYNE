# Multimodal Market-Intelligence Pipeline

SOPHROSYNE does not reduce market understanding to candles. Its evidence layer is deliberately multimodal and provider-agnostic.

```text
TECHNICAL / OHLCV ─┐
MICROSTRUCTURE ─────┤
DERIVATIVES ────────┤
ON-CHAIN ───────────┼──> normalization/provenance ──> Evidence Store
NEWS / EVENTS ──────┤                                  │
MACRO ──────────────┤                                  v
PORTFOLIO CONTEXT ──┘                            Feature / State Engine
                                                       │
                             ┌─────────────────────────┼────────────────────────┐
                             v                         v                        v
                       Market State              Scenario Engine           Risk Engine
                             │                         │                        │
                             └──────────────┬──────────┴──────────────┬─────────┘
                                            v                         v
                                     Strategy Evaluation       Uncertainty / Quality
                                            │                         │
                                            └──────────────┬──────────┘
                                                           v
                                                   Decision Record
                                                           │
                                                           v
                                                   Explanation Layer
```

## Evidence families

### Technical / OHLCV
Price, volume, returns, trend, momentum, volatility and market-structure features.

Technical indicators are **features**, not the product.

### Microstructure
Spread, depth, trade imbalance, liquidity, order-flow and execution-quality observations where licensed/available.

### Derivatives
Funding, basis, open interest, liquidations and positioning context where meaningful.

### On-chain
Exchange flows, wallet activity and network-state features. A whale transfer is not automatically a sell signal; ambiguity must be preserved.

### News and Events
Verified company announcements, regulatory actions, economic releases, geopolitical/public events and other market-relevant information.

News sentiment is contextual evidence, not an oracle.

### Macro
Rates, inflation, liquidity, FX, volatility and other macro variables. Effects are regime-dependent and must not be encoded as universal causal rules.

### Portfolio Context
Allocation, concentration, overlap, correlation and historical risk context for the user’s portfolio snapshot.

## Separation of engines

### State Engine
Describes current conditions.

### Scenario Engine
Constructs plausible paths and invalidators. It does not have execution authority.

### Risk Engine
Assesses downside/exposure independently of scenario conviction.

### Strategy Engine
Evaluates explicit deterministic user-approved rules.

### Explanation Layer
Translates structured outputs for different expertise levels. It cannot create facts, probabilities or executable authority.

## Failure semantics

Every upstream component must expose freshness, availability and quality. Missing or stale data propagates as uncertainty, not as fabricated certainty.

Allowed degraded outcomes include:
- `INSUFFICIENT_DATA`
- `STALE_DATA`
- `CONFLICTING_EVIDENCE`
- `NO_CONCLUSION`
- `STRATEGY_NOT_EVALUABLE`

## Provider independence

Domain objects must not encode Binance-, Alpaca-, CoinGecko- or other vendor-specific semantics. Provider adapters translate into canonical evidence contracts so sources can be replaced without rewriting the intelligence layer.
