# Provider Rights Precheck — 2026-09-17

## Status

`PUBLIC_TERMS_PRECHECK / NOT_CONTRACTUAL_CLEARANCE`

This file narrows Q02 using current official provider materials. It does **not** authorize production use. Public docs and retail/API terms remain subordinate to executed commercial agreements and written provider confirmation for the exact `DataUseProfile`.

## Receipt R-Q02-001 — CoinGecko commercial/API terms

```yaml
receipt_id: receipt_q02_coingecko_commercial_20260917
title: CoinGecko commercial API licensing and API terms
sources:
  - https://support.coingecko.com/hc/en-us/articles/16760512207257-What-Are-the-Differences-Between-Commercial-and-Custom-Licenses
  - https://www.coingecko.com/en/api/enterprise/data-license
  - https://www.coingecko.com/en/api_terms
accessed_at: 2026-09-17
provenance_class: OFFICIAL
confidence: high
related_locks: [Q02]
related_quarries: [Q02]
```

### Public-source facts

Current CoinGecko materials state that the standard Commercial License for qualifying paid plans allows monetizing proprietary applications that integrate CoinGecko data, requires attribution, and does not permit raw-data/API redistribution or syndication without a custom agreement. CoinGecko also publishes separate enterprise/custom licensing for redistribution and white-label use.

The API Terms additionally impose storage/caching and termination obligations and contain restrictions around storing/deriving from data except as expressly permitted by the applicable license/agreement.

### SOPHROSYNE implication

A candidate crypto `DataUseProfile` can remain under evaluation for **derived intelligence with attribution and no raw redistribution**, but long-lived Decision Ledger/evidence retention, transformed-data persistence, embeddings/model use, fallback behavior and post-termination retention require provider-specific written confirmation before Q02 promotion.

```yaml
candidate_profile: CRYPTO_CG_DERIVED_V0
provider: CoinGecko
commercial_app: PUBLIC_TERMS_SUPPORT_CANDIDATE
raw_redistribution: DENIED_WITHOUT_CUSTOM_LICENSE
attribution: REQUIRED
raw_storage: CONSTRAINED
cache: CONSTRAINED
long_lived_derived_retention: UNKNOWN_NEEDS_WRITTEN_CONFIRMATION
model_or_embedding_use: UNKNOWN_NEEDS_WRITTEN_CONFIRMATION
termination_retention: CONSTRAINED
q02_status: OPEN
```

## Receipt R-Q02-002 — Alpaca market data / partner boundary

```yaml
receipt_id: receipt_q02_alpaca_market_data_20260917
title: Alpaca market-data customer and Broker API terms boundary
sources:
  - https://docs.alpaca.markets/us/docs/about-market-data-api
  - https://files.alpaca.markets/disclosures/library/AcctAppMarginAndCustAgmt.pdf
accessed_at: 2026-09-17
provenance_class: OFFICIAL
confidence: high
related_locks: [Q02]
related_quarries: [Q02]
```

### Public-source facts

Alpaca's current Market Data API documentation distinguishes regular/trading access from Broker API partner access and advertises custom pricing/tailored market-data solutions for partners. Its current securities customer agreement states that market data may not be reproduced, distributed, sold or commercially exploited without written Alpaca consent.

### SOPHROSYNE implication

Retail/developer API access is not evidence that a paid SOPHROSYNE application may display, persist or derive US-equity data commercially. A production profile must be tied to the appropriate partner/commercial agreement and downstream exchange entitlements.

```yaml
candidate_profile: US_EQUITIES_ALPACA_PARTNER_V0
provider: Alpaca
technical_access: SUPPORTED
commercial_display: WRITTEN_AGREEMENT_REQUIRED
non_display_computation: WRITTEN_AGREEMENT_REQUIRED
redistribution: WRITTEN_AGREEMENT_REQUIRED
long_lived_storage: WRITTEN_AGREEMENT_REQUIRED
derived_data: WRITTEN_AGREEMENT_REQUIRED
user_entitlements: PROVIDER_EXCHANGE_PROFILE_REQUIRED
cost_model: PARTNER_QUOTE_REQUIRED
q02_status: OPEN
```

## Initial fail-closed provider matrix

| Data family | Candidate | Current public evidence | Promotion posture |
|---|---|---|---|
| Crypto market data | CoinGecko commercial API | Commercial app use appears supportable under qualifying license; attribution required; raw redistribution restricted | `OPEN — written use-profile confirmation required` |
| US equities / ETFs | Alpaca partner market data | Technical/partner products exist; retail agreement does not grant commercial exploitation | `OPEN — executed partner/data agreement required` |
| News/events | No provider frozen | No rights profile yet | `OPEN` |
| Macro | No provider frozen | No rights profile yet | `OPEN` |
| On-chain | No provider frozen | No rights profile yet | `OPEN` |

## Q02 pre-provider conclusion

```yaml
q02_public_precheck: COMPLETE
production_profile_authorized: false
initial_candidate_provider_set:
  - CoinGecko
  - Alpaca
mandatory_next_external_actions:
  - obtain written CoinGecko confirmation for exact derived/storage/model/termination profile
  - obtain Alpaca partner/commercial market-data quote and written rights matrix
  - capture exchange/user-entitlement obligations for US equities
  - freeze provider-backed fallback compatibility groups
promotion_status: OPEN
```

No paid public beta may expose either candidate data family until `quarries/q02/Q02_DATA_RIGHTS_REVIEW_PACKET.md` has authoritative provider evidence for every mandatory field.