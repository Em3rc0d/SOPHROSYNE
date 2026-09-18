# TradingView Comparator Snapshot — 2026-09-17

## Status

`OFFICIAL_PUBLIC_SNAPSHOT / COMPARATOR_CANDIDATE`

This snapshot exists to prevent Q00/Q05 from selecting a deliberately weak comparator after seeing outcomes.

## Receipt R-Q05-001

```yaml
receipt_id: receipt_q05_tradingview_features_20260917
title: TradingView official feature snapshot
source: https://www.tradingview.com/features/
accessed_at: 2026-09-17
provenance_class: OFFICIAL
confidence: high
related_locks: [Q00, Q05]
related_quarries: [Q00, Q05]
supersedes: null
superseded_by: null
```

## Observed official capabilities

TradingView's current official feature material describes a broad market-research workflow including:
- multi-chart market visualization;
- alerts and watchlist alerts;
- fundamental/financial data;
- stock/ETF/crypto/bond screeners;
- macroeconomic data and calendars;
- News Flow;
- strategy testing / historical simulation;
- portfolio tracking;
- Pine Script customization;
- multi-device use.

Supporting official pages:
- https://www.tradingview.com/support/solutions/43000746464-getting-started-with-supercharts/
- https://www.tradingview.com/support/solutions/43000739708-watchlist-alerts-your-trading-edge/
- https://www.tradingview.com/pricing/

The official pricing surface observed on 2026-09-17 exposes a Basic/free tier plus paid tiers. Basic is therefore the current initial cheap/free comparator candidate, not a frozen execution state.

## Why this is a fair comparator candidate

TradingView overlaps materially with the user's existing research workflow problem: market state inspection, screening, alerts, fundamentals, news, strategy testing and portfolio context. It is therefore unsuitable to treat a toy dashboard or a plain chart as the main competitive baseline.

This snapshot does **not** claim TradingView is globally the “best” competitor. It only establishes that it is a strong, real, current workflow comparator for the candidate SOPHROSYNE tasks.

## Frozen Q00/Q05 comparator posture

```yaml
comparator_id: TV-WORKFLOW-2026-09-17
product: TradingView
snapshot_date: 2026-09-17
role:
  - Q00 strongest realistic conventional-workflow comparator candidate
  - Q05 E05-A representative competing workflow
candidate_plan: Basic/free
freeze_sheet: experiments/q00/Q00_G_COMPARATOR_FREEZE_SHEET.md
required_run_freeze:
  - exact plan/tier visible to participants
  - exact logged-in/logged-out state
  - exact features used in task
  - task instructions
  - onboarding time
  - any regional availability differences
```

## Anti-bias rule

At execution time:
- do not disable relevant TradingView features merely to improve SOPHROSYNE's result;
- do not give SOPHROSYNE more onboarding time;
- do not describe either workflow as “safer”, “AI-powered”, “professional” or “better”;
- use matched tasks and equivalent underlying information where possible;
- preserve screenshots/version notes for the exact comparator state.

## Candidate moat gap to test, not assume

The comparative hypothesis is not that SOPHROSYNE has more charts, alerts or screeners. The candidate differentiators that must be behaviorally tested remain:
- explicit supporting/opposing evidence;
- immutable point-in-time Decision Ledger;
- provenance/replay;
- uncertainty/invalidation semantics;
- progressive explanation depth;
- reproducible validation workflow;
- longitudinal decision context;
- rights-aware derived intelligence.

If users do not prefer or repeatedly use these deeper workflow semantics, Q05 must not manufacture a moat claim.