# Q00 / Q05 External Comparator Freeze Sheet

## Status

`CANDIDATE / NOT_FROZEN / INDEPENDENT_REVIEW_REQUIRED`

## Comparator candidate

```yaml
comparator_id: TV-BASIC-CANDIDATE-2026-09-17
product: TradingView
candidate_plan: Basic
cost_class: free
source_snapshot: mining-site/competitors/2026-09-17-tradingview-comparator-snapshot.md
official_pricing_source: https://www.tradingview.com/pricing/
```

Current official public pricing indicates a Basic/free tier. This establishes a candidate only; it does not freeze the execution state.

## Why this cannot be auto-frozen internally

The current SOPHROSYNE Q00 rehearsal corpus is synthetic. A live TradingView workflow cannot be assumed to display exactly the same synthetic fact set.

Before Q00 `PRE_REGISTERED`, the independent reviewer must choose one of:

### Path G1 — matched historical comparator

- replace/finalize relevant Q00 scenarios as historical true-`as_of` cases;
- use the same underlying market facts in A–F;
- configure TradingView Basic to the same instrument/time boundary;
- freeze screenshots/state and task instructions;
- verify no future/outcome leakage.

### Path G2 — comparator declared inapplicable for a specific scenario

Allowed only when the preregistration explicitly justifies why a credible operational comparator cannot represent the task without changing the information set.

This does not remove G from the overall experiment unless the independent reviewer approves the scoped inapplicability before outcomes.

## Candidate execution state if G1 is selected

```yaml
plan: Basic/free
account: dedicated fresh study account
login_state: logged_in
broker_connection: none
paid_market_data_addons: none
custom_pine_scripts: none
participant_saved_layouts: none
social/community content: hidden_or_not_task_relevant
instrument: frozen per scenario
as_of_boundary: frozen per scenario
chart_interval: frozen per scenario
indicators: frozen and documented
news/fundamentals: only if equally available in the underlying information contract
onboarding_minutes: equalized against SOPHROSYNE comparator task
regional_state: Peru-accessible state verified at freeze
screenshots_digest: pending
feature_state_digest: pending
frozen_at: pending
reviewer: pending
```

## Anti-bias checks

Reviewer must confirm:
- no useful Basic feature is deliberately disabled to weaken G;
- no paid feature is silently added unless price class is reclassified;
- SOPHROSYNE does not receive extra underlying facts;
- TradingView does not receive hidden future data;
- onboarding/help time is comparable;
- task wording does not prime preference;
- outcome remains hidden;
- region/data entitlements are documented.

## Recheck timing

Refresh within 7 days of first participant because external SaaS state can change.

If the plan/features materially change after freeze but before completion:
- record deviation;
- stop affected recruitment if treatment equivalence may change;
- independent reviewer decides whether the run remains valid or is superseded.
