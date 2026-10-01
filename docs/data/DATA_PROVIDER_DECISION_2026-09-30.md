# Data Provider Decision — Public-Research Strategy — 2026-09-30

## Status

PUBLIC_PREVIEW_PROVIDER_DEPENDENCY: NONE

Q04_REAL_DATA_PROVIDER: DEFERRED_UNTIL_INTERNAL_RESEARCH_USE_IS_JUSTIFIED

This is an engineering/product decision based only on current public provider terms.

## Decision matrix

### CoinGecko

Public materials indicate:
- standard commercial plans may be used inside monetized products with required attribution;
- raw API/data resale, redistribution or syndication is prohibited without an executed/custom agreement;
- custom redistribution/white-label rights are associated with Enterprise/custom licensing.

Decision:
- acceptable future candidate for crypto-derived surfaces where standard commercial terms clearly fit;
- do not redistribute raw CoinGecko data;
- do not make CoinGecko a dependency of the current public research preview;
- any future public raw-data/display behavior must be re-evaluated against the exact then-current terms.

### Alpaca

Public documentation indicates:
- commercial Connect applications that make money must disclose commercial use and receive written approval;
- Broker API partner market-data plans and custom pricing exist;
- end-user/broker integrations introduce entitlement and approval complexity.

Decision:
- do not make Alpaca a bootstrap dependency;
- do not implement brokerage OAuth, live trading or user-account connectivity in MK0 research preview;
- retain Alpaca only as a future integration candidate after MK0 and explicit commercial-rights review.

### Tiingo

Current public pricing/documentation states:
- commercial internal-use plans exist at a published flat rate;
- internal-use data may not be displayed/shared with another person or organization;
- display redistribution is a separate commercial product, with public startup pricing for EOD + IEX redistribution.

Decision:
- strongest currently observed candidate for Q04 internal stock-data research because the internal-use boundary and public price are unusually explicit;
- if purchased later, use internal-use data only for Q04 calculations/fixtures;
- do not publish raw Tiingo data under an internal-use license;
- any public display requires the appropriate redistribution license.

### Twelve Data

Current public support materials state:
- business plans support commercial display/internal use subject to exchange licensing;
- individual plans permit development/testing/educational use but not commercial display or redistribution;
- redistribution requires a separate agreement.

Decision:
- viable future public-display candidate only if business/exchange licensing is justified;
- not needed for current preview.

### Alpha Vantage

Public terms/documentation route commercial usage to separate written/commercial arrangements.

Decision:
- not selected for bootstrap because the public path is less self-contained for our exact commercial use.

### Nasdaq Data Link / Nasdaq data

Public data-license terms rely on an executed order form for the licensed data/use.

Decision:
- not selected for bootstrap.

## Product architecture consequence

Research preview:

~~~text
synthetic fixtures
      ↓
browser-only reasoning
      ↓
no external provider
      ↓
no raw-data licensing dependency
~~~

Q04:

~~~text
rights-compatible internal dataset
      ↓
point-in-time normalization
      ↓
internal deterministic benchmark
      ↓
derived benchmark receipts
      ↓
no raw provider publication
~~~

Future production:

~~~text
provider selected only after
rights + economics + scale + display model
are explicit
~~~

## Cost posture

No provider purchase is required for the public research preview.

Do not incur data-provider spend until:
- Q00/Q03 justify continuing;
- the Q04 real-data run is ready;
- the chosen provider license clearly covers the exact use.

## Final decision

> Decouple evidence-engineering from market-data procurement.

SOPHROSYNE can validate its reasoning UX and research methodology without carrying live-data licensing risk into the public prototype.
