# External Public-Source Refresh — 2026-09-17

## Status

`PUBLIC_PRECHECK_ONLY / NOT_EXTERNAL_AUTHORITY / NOT_PROMOTABLE`

Purpose: preserve current public-source observations that inform Q01/Q02/Q05 outreach. These observations are not legal advice, provider permission or executed commercial rights.

## Provenance rule

```text
OFFICIAL_PUBLIC_SOURCE != COUNSEL_OPINION
OFFICIAL_PUBLIC_SOURCE != EXECUTED_PROVIDER_LICENSE
API_ACCESS != COMMERCIAL_USE_RIGHT
PUBLIC_PRICING != BINDING_COMMERCIAL_QUOTE
```

Every observation below remains subordinate to the canonical Q01/Q02 closure rules.

---

## Q01 — Peru public-law precheck

### SMV — Ley del Mercado de Valores

Source:
https://www.smv.gob.pe/simv/Frm_DetalleSistemaInfoLegal.aspx?CNORMA=DLG0000199600861

Observed from the official SMV legal-information surface:
- Article 6 describes habitual operations carried out for another party as securities-market intermediation.
- The law places securities-market intermediation within an authorized-agent framework.
- Article 194 lists, among operations available to sociedades agentes, advice regarding securities/stock-exchange operations and information/data-processing services.

Interpretation constraint:
- this does **not** determine SOPHROSYNE's legal classification;
- it is a reason to obtain flow-specific Peru counsel review rather than relying on an “information only” label or disclaimer.

### Peru personal-data regulation

Source:
https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus

Observed:
- Decreto Supremo N.° 016-2024-JUS is the Reglamento de la Ley N.° 29733, Ley de Protección de Datos Personales, published 2024-11-30.

Related 2025 sanction-methodology source:
https://www.gob.pe/institucion/anpd/normas-legales/7575999-476-2025-jus-sg

Observed:
- Resolución Ministerial N.° 476-2025-JUS/SG approves a methodology for calculating personal-data fines under the updated regulatory framework.

Interpretation constraint:
- the project does not self-classify lawful basis, consent, retention, cross-border-transfer or research-telemetry obligations;
- Q01 counsel/privacy authority remains required before collecting promotable human telemetry.

---

## Q02 — CoinGecko public licensing precheck

Official pricing / licensing:
https://www.coingecko.com/en/api/pricing
https://www.coingecko.com/en/api/enterprise/data-license

Official API terms:
https://www.coingecko.com/en/api_terms

Official support article:
https://support.coingecko.com/hc/en-us/articles/16760512207257-What-Are-the-Differences-Between-Commercial-and-Custom-Licenses

Observed from current public materials:
- standard commercial plans may be used in monetized applications subject to the applicable terms;
- attribution is required under the standard commercial posture described on the pricing/support surfaces;
- standard terms restrict resale/redistribution/sublicensing of API access/raw data;
- custom/enterprise licensing is presented for uses such as redistribution and white-label arrangements.

Unresolved for SOPHROSYNE:
- exact raw/normalized/derived retention;
- audit/replay retention;
- model training/embedding/third-party LLM context;
- reconstructability of derived outputs;
- exact redistribution boundary;
- termination deletion requirements;
- exact commercial quote at intended scale.

Therefore:
`Q02 CoinGecko profile = UNKNOWN/PENDING_PROVIDER_AUTHORITY`.

---

## Q02 — Alpaca public precheck

Official disclosures:
https://alpaca.markets/disclosures

Official Market Data API overview:
https://docs.alpaca.markets/us/docs/about-market-data-api

Official Connect API overview:
https://docs.alpaca.markets/us/docs/about-connect-api

Official Market Data FAQ:
https://docs.alpaca.markets/us/docs/market-data-faq

Observed:
- Alpaca distinguishes Trading API access for individual users/developers from Broker API access for partners building multi-user platforms.
- Broker API market-data documentation lists multi-user subscription tiers and states custom pricing/tailored solutions are available.
- Connect API documentation states commercial applications that make money must disclose that commercial use in registration and receive written approval.
- Alpaca disclosure materials incorporate exchange/subscriber agreements and other market-data terms.
- Historical/current market-data access differs by subscription/feed.

Legacy/current-applicability caution:
- some public agreement PDFs include restrictions on reproducing/distributing/selling/commercially exploiting market data without written consent;
- the exact agreement hierarchy applicable to SOPHROSYNE's intended account/product must be confirmed by Alpaca in writing rather than inferred from an old/public PDF.

Unresolved:
- exact commercial account class;
- display/non-display rights;
- derived-data rights;
- end-user entitlement mechanics;
- storage/retention;
- redistribution;
- model/LLM use;
- partner pricing and venue pass-through obligations.

Therefore:
`Q02 Alpaca profile = UNKNOWN/PENDING_PROVIDER_AUTHORITY`.

---

## Q05 / Q00 comparator candidate — TradingView

Official pricing/features:
https://www.tradingview.com/pricing/
https://es.tradingview.com/pricing/

Observed from current public pricing:
- TradingView offers a Basic/free tier and paid tiers;
- the public feature matrix includes charting, market/fundamental/economic data surfaces, alerts, paper trading and other research/trading workflow features depending on tier.

Interpretation:
- TradingView remains a strong real-world conventional-workflow comparator candidate;
- the formal experiment must still freeze exact tier, login state, data entitlements, enabled features, region and task instructions before recruitment;
- the current SOPHROSYNE arm G proxy is not a promotable substitute for that exact external state.

---

## Refresh / staleness rule

Re-check this receipt before any external packet is frozen if:
- more than 30 days pass before provider/counsel outreach;
- provider pricing/terms pages change;
- target product/data use changes;
- TradingView plan/features change materially;
- applicable Peru law/regulation changes.

A refreshed public source can narrow questions; it still cannot close Q01/Q02.
