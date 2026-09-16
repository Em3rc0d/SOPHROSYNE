# Q02 Data Use Profile Packet

## Purpose

Q02 validates one exact commercial data-use configuration. Technical access does not imply commercial permission.

## Profile identity

```yaml
data_use_profile_id:
profile_version:
profile_state: DRAFT | EVIDENCE_RUNNING | REVIEW_READY | FINAL | SUPERSEDED
final_decision: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE | null
provider:
provider_product:
owner:
supersedes:
```

## Intended use

```yaml
instrument_family:
asset_universe:
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
model_embedding_llm_use:
retention:
attribution:
entitlements:
cost_model:
fallback_compatibility:
```

## Authoritative evidence

Every material right/constraint records:

```yaml
right_or_constraint:
status: ALLOWED | ALLOWED_WITH_CONDITIONS | DENIED | UNKNOWN
source_type: CONTRACT | TERMS | QUOTE | WRITTEN_PROVIDER_CONFIRMATION
source_ref:
source_digest:
effective_date:
retrieved_at:
valid_until_if_known:
recheck_trigger_or_date:
conditions: []
conflicts_with_other_provider_statement: []
```

`UNKNOWN` defaults to denied for production.

## Provider semantics profile

Freeze the semantic properties the product/quant engine depends on:

```yaml
provider_semantics_profile_ref:
instrument_identity_rules:
timezone_calendar_session_rules:
price_adjustment_rules:
corporate_action_rules:
missing_data_rules:
currency_fx_rules:
realtime_delay_semantics:
freshness_profile:
revision_backfill_behavior:
rate_limit_or_delivery_constraints:
```

Rights compatibility and semantic compatibility are separate checks.

## Economics

Record fixed/variable fees, user/seat/API/display/non-display charges, entitlement costs, minimums, overages, taxes/FX assumptions where verified, and termination/revocation costs. Feed authoritative values to the unit-economics sync artifact.

## Decision

- `CLOSED_PASS`: every mandatory use explicitly allowed and economically viable.
- `CLOSED_CONDITIONAL`: executable restrictions permit the profile.
- `PIVOT_REQUIRED`: choose another provider/profile or narrower surface.
- `STOP_CURRENT_CONFIGURATION`: no viable profile supports mandatory data needs.
- `INCONCLUSIVE`: necessary authoritative right/cost/semantic evidence is unavailable or materially ambiguous.

## Frozen outputs

```yaml
approved_data_use_profile_ref:
data_rights_record_refs: []
provider_semantics_profile_ref:
freshness_profile:
entitlement_model:
attribution_requirements: []
retention_cache_constraints: []
cost_assumptions_ref:
fallback_group:
rights_recheck_triggers: []
```

Any provider terms/contract/product or material semantics change reopens the affected profile only. Final Q02 promotion uses an aggregate EvidenceReceipt referencing all selected primary/fallback profile receipts.
