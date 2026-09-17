# Q02 Data Rights Review Packet — Initial Production Data Profile

## Status

`OPEN / EXTERNAL_AUTHORITY_REQUIRED / FATAL_IF_FAILED`

This packet defines how SOPHROSYNE proves that a candidate production data profile is commercially usable. It does not assume that API access, a free tier, a developer account or public documentation grants commercial display/non-display/derived-data rights.

Canonical authorities:
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`;
- `docs/data/DATA_RIGHTS.md`;
- `docs/economics/UNIT_ECONOMICS.md`;
- `contracts/validation_graph.yaml`.

---

## 1. Review identity

```yaml
review_id: Q02-MK1-DATA-RIGHTS-V1
status: DRAFT
owner: Em3rc0d
internal_reviewers:
  - data-architecture
  - product
provider_contacts: []
started_at: null
completed_at: null
supersedes: null
```

## 2. Unit of closure

Q02 is never closed “for a provider” in the abstract. The unit of closure is one exact versioned `DataUseProfile`.

```yaml
profile_id:
version:
provider:
provider_product:
instrument_family:
asset_universe: []
historical_or_realtime:
delay_profile:
user_classification:
geography:
raw_storage:
cache_ttl:
display:
non_display:
redistribution:
derived_use:
model_or_embedding_use:
retention:
attribution:
entitlement_requirements: []
cost_model:
fallback_compatibility_group:
```

A field left unknown is treated as **DENIED / NOT AUTHORIZED** for promotion until authoritative evidence resolves it.

## 3. Required evidence per field

For every right or obligation material to the proposed profile, collect the strongest available authority in this order:

1. executed contract / order form / license schedule;
2. provider-specific written confirmation tied to the proposed use;
3. authoritative provider terms/policies with effective date/version;
4. formal quote documenting entitlement/cost assumptions.

Marketing pages, forum answers, third-party summaries or the fact that an endpoint works cannot override contradictory or missing authoritative terms.

Every evidence item records:

```yaml
evidence_id:
provider:
source_type: CONTRACT | WRITTEN_CONFIRMATION | OFFICIAL_TERMS | FORMAL_QUOTE
source_ref:
effective_date:
accessed_at:
exact_claim:
affected_profile_fields: []
constraints: []
conflicts_with: []
provenance: OFFICIAL
```

## 4. Mandatory rights matrix

Each candidate profile must answer explicitly:

| Dimension | Required conclusion |
|---|---|
| Historical access | allowed / constrained / denied / unknown |
| Real-time access | allowed / delayed-only / denied / unknown |
| Raw storage | duration/volume constraints |
| Cache | exact TTL/refresh constraints |
| User display | who may see what and under which entitlement |
| Non-display/internal computation | allowed scope |
| Redistribution | raw/normalized/none and recipient limits |
| Derived data | definition and permitted uses |
| Model/embedding use | training/inference/storage constraints |
| Retention after termination | deletion/export obligations |
| Attribution | exact user-visible requirements |
| Geography | territorial restrictions |
| User classification | subscriber/professional/non-professional or provider-specific classes |
| Entitlements | enforcement requirements |
| Audit/reporting | usage reporting or audit obligations |
| Commercialization | allowed plan/use classes |
| Termination/revocation | effect on stored/derived artifacts |
| Cost | fixed, variable, entitlement/pass-through and scale assumptions |
| Fallback | compatible substitute constraints |

No row may be inferred from technical similarity to another provider/product.

## 5. Provider-question template

When public terms are insufficient, obtain written answers to the exact proposed use rather than asking “can we use your API commercially?”. Questions should cover:

- May SOPHROSYNE persist raw observations, and for how long?
- May normalized values be stored independently of raw payloads?
- May paying end users see raw values, delayed values, normalized values or only derived insights?
- What qualifies as redistribution under this product architecture?
- What qualifies as derived data, and may derived results be retained after source termination?
- Is non-display computation for analytics/backtesting permitted?
- Are model inference, embeddings or model training permitted, and under what restrictions?
- Are per-user entitlements or professional/non-professional classifications required?
- What attribution must be displayed?
- Are there geography restrictions relevant to Peru/LATAM users?
- What reporting/audit obligations apply?
- What fees change with users, symbols, requests, display/non-display status or commercial plan?
- What must be deleted or disabled after termination?

Provider silence is `UNKNOWN`, never permission.

## 6. Cost and unit-economics binding

A rights profile is not promotable merely because it is legally permitted. Record all provider costs capable of changing the unit-economics conclusion:

```yaml
monthly_fixed_cost:
per_user_cost:
per_entitlement_cost:
usage_cost:
exchange_or_venue_fees:
minimum_commitment:
redistribution_fees:
non_display_fees:
derived_data_fees:
professional_user_uplift:
other_pass_through_costs: []
```

These assumptions must be referenced by the applicable unit-economics version.

## 7. Fallback compatibility

A fallback provider belongs to the same compatibility group only when evidence shows compatible enough:
- instrument/venue identity;
- timestamp and `available_at` semantics;
- corrections/revisions;
- sessions/calendars/corporate actions where applicable;
- freshness/delay;
- storage/display/non-display/derived rights;
- attribution/entitlements;
- economically viable cost profile.

“Same symbol” or “same OHLCV shape” is insufficient.

## 8. Decision mapping

### `CLOSED_PASS`
Every mandatory use in the exact initial `DataUseProfile` is explicitly authorized and economically compatible with the candidate MK1 configuration.

### `CLOSED_CONDITIONAL`
The profile may proceed only under explicit restrictions such as delayed display, bounded cache, no raw redistribution, entitlement checks, attribution or user/geography constraints. These become executable product requirements.

### `PIVOT_REQUIRED`
The provider/data family is technically useful but incompatible with intended commercial use or economics. A different provider, narrower universe or derived-only surface is required.

### `STOP_CURRENT_CONFIGURATION`
No viable provider/profile combination supports the mandatory MK1 data surface within acceptable rights/economic constraints.

### `INCONCLUSIVE`
A mandatory right remains ambiguous or authoritative evidence is missing. This state is not promotable.

## 9. Required closure receipt

A Q02 receipt must contain:
- exact `DataUseProfile` ref/digest;
- provider/product identity;
- authoritative evidence refs and effective dates;
- field-by-field rights matrix;
- conflict/ambiguity log;
- commercial quote/cost assumptions;
- entitlement/attribution requirements;
- termination/retention obligations;
- fallback-group conclusion;
- final decision and limitations;
- reviewer signoff;
- canonical docs updated.

## 10. Frozen outputs

A `CLOSED_PASS` or `CLOSED_CONDITIONAL` receipt freezes:

```yaml
initial_provider_set: []
asset_universe: []
data_families: []
data_use_profile_refs: []
data_rights_record_versions: []
fallback_compatibility_groups: []
entitlement_requirements: []
retention_cache_limits: []
attribution_requirements: []
cost_assumption_refs: []
```

These flow into `MK1_BOOTSTRAP_PROFILE` and future rights-configuration acceptance receipts.

## 11. Reopen triggers

Affected Q02 profiles reopen when:
- provider terms/contract/product materially change;
- asset universe or geography changes;
- display/non-display/derived/model use changes;
- retention/cache behavior changes;
- user classification/entitlement model changes;
- pricing/cost structure materially changes;
- fallback semantics change;
- implementation introduces a new use not covered by the approved profile.

## 12. Non-bypass invariant

Accessible data, successful prototypes, a low development-tier price, technical caching capability or a provider salesperson’s ambiguous statement cannot substitute for documented rights.

Q02 remains `OPEN` until every mandatory initial production `DataUseProfile` has authoritative evidence and a promotable receipt.
