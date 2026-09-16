# Canonical Domain Model

This document defines the vocabulary that implementation must preserve. Names can evolve through ADRs; semantics cannot drift silently.

## Source

An origin of external or internally generated information.

Key properties:
- identity and provider;
- provenance class;
- timestamp/freshness semantics;
- licensing/usage rights;
- trust/quality metadata;
- availability/fallback state.

## Evidence

A point-in-time observation or structured event derived from one or more sources.

Evidence is **not** a conclusion. It carries provenance, freshness and an epistemic status.

Examples: OHLCV observation, funding-rate change, macro release, verified company announcement, exchange inflow measurement.

## Claim

A user-meaningful statement supported by evidence.

A Claim must be labeled as one of:
`OBSERVED`, `ATTRIBUTED`, `INFERRED`, `CORRELATED`, `UNKNOWN`.

## MarketState

A time-bounded representation of current conditions, not a forecast.

Possible dimensions include trend, momentum, volatility, liquidity, positioning/derivatives, macro, events and on-chain state.

## Scenario

A plausible future path conditioned on the current MarketState and supporting evidence.

A Scenario contains supporting evidence, contradicting evidence, invalidators and uncertainty. Probability is optional and forbidden unless calibrated.

## RiskAssessment

An independent evaluation of exposure, downside and constraints.

RiskAssessment must never inherit authority from model conviction. A strong Scenario does not imply acceptable risk.

## Strategy

A versioned, deterministic and testable rule set authored/approved by a user or promoted from a validated research artifact.

A Strategy is distinct from a Scenario: scenarios describe plausible futures; strategies define actions/conditions.

## StrategyState

The evaluation of a Strategy at a point in time:
- `TRIGGERED`
- `NOT_TRIGGERED`
- `NOT_EVALUABLE`
- future execution-specific states only through later ADRs.

## PortfolioSnapshot

A point-in-time representation of positions/exposures used for descriptive portfolio context and risk. In MK1 it must not silently become discretionary portfolio management.

## DecisionRecord

The immutable aggregate that binds MarketState, Scenarios, Evidence, Claims, RiskAssessment, StrategyState, versions and `as_of` timestamps for one user-visible interpretation.

## DataRightsRecord

The contractual metadata that defines allowed use of a data family: display, non-display, derived use, caching, redistribution, geography, entitlements and retention.

## ModelArtifact

A versioned statistical/ML model plus its training data manifest, features, validation results, calibration state, approved regimes and retirement status.

An LLM prompt is not automatically a ModelArtifact with financial authority.

## Experiment

A reproducible test with hypothesis, dataset/sample, methodology, metrics, result and falsification criteria.

## Receipt

The evidence unit promoted from the mining site to support a Claim, Lock closure, Quarry closure or ADR.

## Relationships

```text
Source ──> Evidence ──> Claim ───────────────┐
                 │                            │
                 └────> MarketState ──> Scenario
                           │             │     │
PortfolioSnapshot ──> RiskAssessment <───┘     │
                           │                   │
Strategy ──> StrategyState │                   │
      │                    │                   │
      └────────────────────┴──────────────┬────┘
                                          v
                                   DecisionRecord

DataRightsRecord governs Source/Evidence use.
ModelArtifact may produce MarketState/Scenario features but cannot bypass RiskAssessment.
Experiment validates Strategy/ModelArtifact behavior.
Receipt governs what may be promoted as project truth.
```

## Invariant

No implementation object may collapse Evidence, Claim, Scenario and Strategy into a single generic “signal”. That would destroy provenance, uncertainty and auditability—the core of SOPHROSYNE.
