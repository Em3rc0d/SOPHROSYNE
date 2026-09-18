# Q02 Provider Data-Rights Inquiry Template

## Status

`READY_TO_SEND / PROVIDER AUTHORITY REQUIRED`

Use one copy per exact provider/product/account class. Do not combine providers in one authority response.

## Opening

We are evaluating a commercial research/decision-support product and need written confirmation of permitted data uses for a specific account/product. We are not asking whether the API is technically accessible; we need rights tied to the intended architecture.

## Identity fields

```yaml
provider:
provider_product:
plan_or_contract_candidate:
account_class:
target_geography: Peru-facing product
asset/data_family:
intended_beta_scale:
intended_commercial_scale:
```

## Required yes/no/conditional questions

Please state `ALLOWED | ALLOWED_WITH_CONDITIONS | NOT_ALLOWED | REQUIRES_CUSTOM_LICENSE` and cite the governing agreement/order form where possible.

1. API/stream retrieval for commercial application.
2. Raw transient processing.
3. Raw persistent storage and maximum duration.
4. Normalized/derived storage and retention.
5. Historical replay/backtesting.
6. Internal non-display analytics.
7. User-facing raw display.
8. User-facing derived/transformed display.
9. Charts/tables.
10. Alerts/notifications.
11. User export/download.
12. Redistribution to end users.
13. B2B/API redistribution.
14. Derived metrics that cannot reconstruct raw values.
15. Model feature engineering.
16. Model training.
17. Embedding/vector storage.
18. Sending provider-derived content to a third-party LLM/model service.
19. Retaining audit metadata after contract termination.
20. Retaining derived decision records that cite provider provenance after termination.
21. Screenshots/examples used in support, documentation or marketing.
22. Attribution/logo requirements.
23. Per-user entitlements or professional/non-professional classification.
24. Geographic restrictions.
25. Fallback/caching behavior during outage.
26. Required deletion/content removal after termination.
27. Any exchange/venue pass-through fees or agreements.
28. Any use that requires an enterprise/custom/redistribution/white-label agreement.

## Derived artifact examples to classify

- MarketState label;
- volatility/liquidity/risk metric;
- supporting/opposing evidence item referencing market data;
- scenario state;
- backtest/strategy metric;
- point-in-time provenance record;
- aggregate statistic;
- LLM plain-language explanation of an already-computed structured result.

Do not assume your provider definition of "derived data" matches ours; please supply the contractual definition that governs.

## Commercial quote

Request:
- fixed monthly cost;
- usage tiers/rate limits;
- per-user/entitlement fees;
- venue/exchange fees;
- redistribution fees;
- overage;
- quote validity date;
- support/SLA;
- termination notice.

Ask for pricing at:
- research/internal;
- 10 beta users;
- 100 active users;
- 1,000 active users.

## Authority requirement

Preferred evidence order:
1. executed contract/order form/data license;
2. incorporated provider terms;
3. written legal/licensing confirmation tied to this use case;
4. current public legal/product terms only where explicitly applicable.

Sales/support statements cannot override contradictory contract terms.

## Final confirmation requested

> Please confirm whether the described use can be performed under the named plan/account class as-is. If not, identify the exact custom license/product and conditions required.

The internal team maps the response into `DATA_USE_PROFILE_PACKET.md`; provider silence is `UNKNOWN`, never approval.
