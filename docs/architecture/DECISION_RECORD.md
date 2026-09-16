# Decision Record

The Decision Record is the canonical audit object for a user-visible market interpretation.

```yaml
record_id: dr_...
asset: BTCUSDT
as_of: 2026-09-16T12:00:00-05:00
market_state:
  trend: bullish
  momentum: weakening
  volatility: elevated
scenarios:
  - id: continuation
    status: plausible
    supporting_evidence: []
    contradicting_evidence: []
    invalidators: []
  - id: consolidation
    status: plausible
risk:
  level: elevated
uncertainty:
  level: high
evidence:
  - claim: price remains above selected trend baselines
    epistemic_status: OBSERVED
    source_id: source_...
  - claim: exchange inflow may increase sell-side availability
    epistemic_status: INFERRED
    source_id: source_...
strategy_state:
  user_rule_id: null
  status: NOT_EVALUATED
versions:
  data_snapshot: ...
  feature_pipeline: ...
  model: ...
  ruleset: ...
```

## Epistemic statuses

- `OBSERVED` — directly measured.
- `ATTRIBUTED` — an identified source explicitly makes the causal/event attribution.
- `INFERRED` — our model/rule interpretation.
- `CORRELATED` — association only.
- `UNKNOWN` — evidence is insufficient.

`CORRELATED` must never be surfaced as causal language.

## Immutability

A record may be superseded by a later record but must not be rewritten to make past reasoning look better.
