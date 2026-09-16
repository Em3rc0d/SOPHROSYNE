# MK1 Market Data Semantics

## Purpose

Market-data bugs are often semantic rather than syntactic. SOPHROSYNE therefore defines how instruments, sessions, bars, corrections and corporate actions are interpreted before implementation.

## Instrument identity

A ticker/symbol is an alias, never the identity of an instrument.

Canonical instrument identity is stable across:
- provider symbol changes;
- venue-specific aliases;
- corporate renames;
- temporary provider mapping changes.

`instrument_alias` records provider + venue + validity interval. Ambiguous aliases are rejected rather than guessed.

## Asset-scope rule

MK1 begins with the smallest rights-cleared universe. Different asset classes do not silently share semantics.

Profiles are explicit, for example:
- `CRYPTO_SPOT_24_7`;
- `US_LISTED_ETF_REGULAR_SESSION`.

A profile owns its calendar, pricing, corporate-action and missing-data rules.

## Time and sessions

All stored timestamps are UTC. Venue/session interpretation uses a versioned exchange/calendar definition.

For session-based assets:
- holidays and early closes are calendar data, not missing bars;
- pre/post-market data is excluded unless the profile explicitly includes it;
- daylight-saving changes are resolved through the venue timezone/calendar, never manual fixed offsets.

For 24/7 assets:
- bars still have a deterministic UTC boundary convention;
- provider-specific daily cutoffs are normalized or kept distinct with lineage if they are not semantically equivalent.

## Bar contract

A normalized OHLCV bar records:
- canonical instrument;
- source;
- interval;
- interval start/end convention;
- open/high/low/close;
- volume and volume unit/meaning;
- event/available/ingested timestamps;
- adjustment state;
- quality flags;
- normalization version.

Invariants:
- `low <= open, close <= high` where source semantics are standard OHLC;
- high >= low;
- interval boundaries cannot overlap within one canonical series/version;
- duplicate source bars are reconciled deterministically;
- zero volume and missing volume are distinct states.

## Missing bars

Missing does not automatically mean zero activity.

Each profile defines whether a missing interval is:
- expected closed session;
- no-trade interval supported by provider semantics;
- provider/data gap;
- quarantined anomaly.

Forward-filling OHLC/returns for backtesting is prohibited unless a specific methodology explicitly justifies it. Features requiring unavailable input become unavailable or use a documented method with a distinct version.

## Provider corrections

A corrected bar/event never overwrites the raw receipt silently.

The normalization layer records supersession lineage. Historical replay distinguishes:
- what was known then;
- corrected history now.

## Corporate actions for listed instruments

Where applicable, preserve raw corporate-action events separately:
- splits/reverse splits;
- cash dividends;
- stock distributions;
- symbol changes;
- mergers/spinoffs where the initial asset profile supports them;
- delisting/termination.

Price-series adjustment is a derived view with an explicit policy/version, not destruction of raw prices.

At minimum distinguish:
- raw/unadjusted prices;
- split-adjusted prices;
- total-return series when dividends/reinvestment assumptions are intentionally modeled.

A backtest manifest must state which series/policy it uses.

## Dividends and total return

Price return and total return are different metrics.

If a benchmark/strategy claims total return, dividends and reinvestment convention must be modeled explicitly. If not available, report price-return semantics rather than imply total return.

## Delistings and survivorship

Historical universes must preserve instruments that later disappear when they were eligible at the historical `as_of` time.

A current-symbol list cannot be retroactively used as a historical investable universe without a documented survivorship limitation.

## Currency

Every price/valuation records its quote/base currency. Cross-currency portfolio/risk calculations require an explicit FX source, `as_of`, availability semantics and conversion policy.

No numeric values from different currencies are aggregated without conversion.

## Crypto-specific semantics

For crypto spot:
- venue is material; BTC/USD on venue A is not assumed identical to venue B;
- quote currency/stablecoin identity is explicit;
- fiat USD and USD-pegged tokens are not interchangeable without a policy;
- exchange outages/gaps remain source-specific;
- aggregate/reference prices require a separately versioned methodology.

## ETF/equity-specific semantics

For listed ETFs/equities:
- venue/calendar is explicit;
- adjustment policy is explicit;
- split/dividend data availability is point-in-time aware;
- delisting/symbol-change lineage is preserved;
- regular vs extended session is never inferred from timestamp alone.

## Order book / tick data

Not required for MK1 baseline. If introduced later, it opens new contracts for sequence ordering, snapshot/delta recovery, crossed books, venue clocks and retention rights. Existing bar semantics must not be reused as if equivalent.

## Data-quality flags

Normalized observations may carry flags such as:
- `LATE`;
- `DUPLICATE_SOURCE_EVENT`;
- `CORRECTED`;
- `TIMESTAMP_ANOMALY`;
- `OUTLIER_UNVERIFIED`;
- `PARTIAL_INTERVAL`;
- `PROVIDER_GAP`;
- `RIGHTS_LIMITED`.

Flags are provenance/quality information. They do not authorize silent repair.

## Outlier handling

Outliers are not deleted merely because they are inconvenient.

Process:
1. preserve raw receipt;
2. detect/flag;
3. cross-check against an approved compatible source where rights permit;
4. quarantine only according to a versioned rule;
5. record repair/supersession lineage.

Quant research must disclose whether flagged observations were included or excluded.

## Resampling

Higher timeframe bars derived from lower timeframe data use deterministic UTC/session boundaries defined by profile. Provider-supplied bars and locally resampled bars have distinct lineage and are not assumed identical without tests.

## Market-data promotion gate

An initial data family is production-ready only when:
- instrument mapping is unambiguous;
- timestamp/availability semantics are documented;
- session/calendar behavior is tested;
- correction behavior is tested;
- missing data is distinguishable from market closure/no-trade;
- corporate-action policy is defined where applicable;
- currency semantics are explicit;
- rights permit the exact storage/display/derived use;
- provider fixtures include pathological cases;
- a fallback, if declared, has semantic-equivalence tests.

The provider's API documentation is necessary but does not override SOPHROSYNE's canonical semantics.