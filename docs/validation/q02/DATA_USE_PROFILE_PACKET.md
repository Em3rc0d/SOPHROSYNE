# Q02 Data Use Profile Packet

## Purpose

Q02 closes only for exact commercial data uses, not for a provider name in the abstract.

Each candidate provider/product/data-family combination receives one versioned `DataUseProfile`. Technical accessibility is insufficient. Every intended storage, transformation, display and commercial use must be supported by authoritative provider evidence.

Unknown or contradictory rights default to `DENY` until resolved.

Canonical policy: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.
Semantic normalization: `docs/validation/CANONICAL_VALIDATION_SPEC.md`.

---

## 1. Profile identity

```yaml
profile_id: Q02-DUP-<provider>-<family>-<version>
status: DRAFT | EVIDENCE_COLLECTING | REVIEW_READY | CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE | SUPERSEDED
provider:
provider_product:
contract_or_plan:
provider_account_class:
user_classification:
geography:
created_at:
evidence_as_of:
reviewed_at:
review_by:
reopen_triggers: []
supersedes:
```

A provider may have multiple profiles because rights can differ by product, data family, latency, user class or geography.

`INCONCLUSIVE` is a valid final result for the profile version but never promotable.

`evidence_as_of`, `review_by` and `reopen_triggers` are mandatory for any promotable profile. If an authoritative source has an effective/expiry date, that date must be represented here or in an authority record.

---

## 2. Technical data scope

```yaml
instrument_family:
asset_universe:
data_families:
  - OHLCV
  - trades
  - quotes
  - order_book
  - corporate_actions
  - fundamentals
  - news
  - macro
  - on_chain
  - other
frequency_or_granularity:
realtime_delayed_eod:
provider_timestamp_semantics:
correction_semantics:
corporate_action_semantics:
session_calendar_semantics:
symbol_identifier_semantics:
currency_semantics:
```

Only include data families actually intended for the profile.

---

## 3. Intended product uses

For every row record `ALLOW | ALLOW_WITH_CONDITIONS | DENY | UNKNOWN`.

| Use | Status | Conditions | Authority ref |
|---|---|---|---|
| API retrieval | UNKNOWN |  |  |
| streaming/WebSocket retrieval | UNKNOWN |  |  |
| raw transient processing | UNKNOWN |  |  |
| raw persistent storage | UNKNOWN |  |  |
| normalized storage | UNKNOWN |  |  |
| historical retention | UNKNOWN |  |  |
| cache | UNKNOWN |  |  |
| internal non-display analytics | UNKNOWN |  |  |
| user-facing raw display | UNKNOWN |  |  |
| user-facing transformed/derived display | UNKNOWN |  |  |
| charts/tables | UNKNOWN |  |  |
| export/download by user | UNKNOWN |  |  |
| alerts/notifications | UNKNOWN |  |  |
| redistribution to another user/service | UNKNOWN |  |  |
| API redistribution/B2B | UNKNOWN |  |  |
| backtesting/research | UNKNOWN |  |  |
| model training | UNKNOWN |  |  |
| model inference features | UNKNOWN |  |  |
| embeddings/vector storage | UNKNOWN |  |  |
| LLM-context use | UNKNOWN |  |  |
| aggregated statistics | UNKNOWN |  |  |
| content screenshots/social examples | UNKNOWN |  |  |
| long-term audit/replay artifact | UNKNOWN |  |  |

A required use with `UNKNOWN` prevents `CLOSED_PASS` and `CLOSED_CONDITIONAL` for any configuration that depends on that use.

---

## 4. Authority hierarchy

For each conclusion, preserve the strongest applicable source:

1. executed contract / order form / data license;
2. incorporated provider terms/product-specific agreement;
3. provider legal/data-licensing written confirmation tied to exact use;
4. authoritative public terms/documentation when contractually applicable;
5. sales/support statement only as supporting context, never to override contradictory legal terms.

```yaml
authority_records:
  - authority_id:
    type:
    title:
    effective_date:
    expiry_or_review_date:
    version_or_digest:
    source_ref:
    relevant_sections:
    scope:
```

If sources conflict, create a contradiction and obtain clarification before promotion.

A provider source that is superseded, expires, changes materially, or ceases to apply to the promoted account/user class makes the dependent profile `STALE_PENDING_REVIEW` for new promotion/release decisions until reconciled.

---

## 5. Storage / retention contract

```yaml
raw_storage_allowed: UNKNOWN
raw_storage_max_duration:
normalized_storage_allowed: UNKNOWN
normalized_retention_limit:
derived_artifact_retention: UNKNOWN
cache_allowed: UNKNOWN
cache_ttl:
backup_copy_rules:
log_or_trace_payload_rules:
right_to_retain_audit_metadata_after_termination:
termination_deletion_requirements:
```

The architecture must distinguish immutable audit metadata from provider content that may be subject to deletion/retention constraints.

---

## 6. Display / entitlement contract

```yaml
display_allowed: UNKNOWN
display_delay:
user_entitlement_required:
entitlement_verification_method:
per_user_or_per_device_constraints:
concurrent_user_constraints:
attribution_required:
attribution_text_or_logo_rules:
derived_display_allowed: UNKNOWN
raw_values_may_be_reconstructed_from_derived_output: UNKNOWN
```

A derived output is not automatically exempt from display/redistribution rules.

---

## 7. Derived-data contract

Describe each derived artifact family intended for MK1:

```yaml
derived_artifacts:
  - artifact_type: MarketState | indicator | risk_metric | scenario_input | strategy_metric | other
    source_fields:
    transformation:
    reversible_to_raw: YES | NO | PARTIAL
    display_intent:
    storage_intent:
    redistribution_intent:
    rights_status: UNKNOWN
    authority_ref:
```

If provider terms use their own definition of “derived data”, preserve that definition and do not substitute SOPHROSYNE terminology.

---

## 8. Model / AI use contract

```yaml
model_training_allowed: UNKNOWN
feature_engineering_allowed: UNKNOWN
embedding_allowed: UNKNOWN
llm_context_allowed: UNKNOWN
provider_content_may_leave_sophrosyne_boundary: UNKNOWN
third_party_model_provider_restrictions:
model_output_ownership_or_redistribution_constraints:
```

If provider data cannot be sent to an external model provider, that is an architecture constraint, not merely procurement metadata.

---

## 9. Cost / quota model

```yaml
currency:
fixed_monthly_cost:
minimum_commitment:
per_request_or_usage_cost:
per_user_or_entitlement_cost:
exchange_or_venue_fees:
redistribution_fees:
realtime_fees:
professional_user_surcharges:
overage_cost:
rate_limits:
concurrency_limits:
commercial_quote_ref:
quote_valid_until:
```

Compute candidate product cost at explicit scales rather than one average:
- research/internal only;
- 10 beta users;
- 100 active users;
- 1,000 active users;
- any provider-specific threshold that causes a step change.

The profile should expose cost discontinuities that can invalidate pricing/unit economics.

A quote past `quote_valid_until` may remain historical evidence but cannot be treated as a current commercial-cost commitment without a refresh or explicit provider confirmation.

---

## 10. Failure / revocation model

```yaml
termination_notice:
provider_suspension_rights:
api_shutdown_or_product_change_terms:
rights_revocation_effect:
required_content_removal_after_termination:
required_user_notification:
kill_switch_scope:
fallback_allowed_during_outage:
```

The system cannot silently continue displaying cached content after rights expire unless explicitly permitted.

---

## 11. Fallback compatibility assessment

Two providers may share a fallback group only when their semantics and rights are compatible enough for the exact product surface.

Evaluate:

```yaml
candidate_fallback_group:
compatibility:
  instrument_identity: PENDING
  event_time: PENDING
  available_at_semantics: PENDING
  granularity: PENDING
  corrections: PENDING
  corporate_actions: PENDING
  sessions: PENDING
  currency: PENDING
  freshness: PENDING
  display_rights: PENDING
  derived_use_rights: PENDING
  attribution: PENDING
  entitlements: PENDING
result: COMPATIBLE | COMPATIBLE_WITH_CONDITIONS | INCOMPATIBLE | PENDING
```

A fallback must never erase source lineage.

---

## 12. Decision rule

### CLOSED_PASS

All mandatory MK1 uses are explicitly allowed under the exact profile, operational constraints are implementable, authoritative evidence is current for the promotion review, and provider economics are compatible with the candidate business model.

### CLOSED_CONDITIONAL

Mandatory uses are allowed only under explicit constraints such as:
- delayed display;
- entitlement verification;
- bounded caching;
- no raw export;
- attribution;
- geography/user restrictions;
- derived-only user surface.

Every condition becomes an executable `DataRightsRecord` requirement.

### PIVOT_REQUIRED

Provider/profile is technically useful but commercially, semantically or contractually incompatible. Select a different provider/data family/surface.

### STOP_CURRENT_CONFIGURATION

No viable provider/profile combination supports a mandatory candidate MK1 surface within acceptable rights/economics.

### INCONCLUSIVE

Required rights remain ambiguous, authoritative material is unavailable/stale, or the exact commercial use cannot be resolved from the evidence. This never promotes.

---

## 13. Frozen outputs

```yaml
approved_profile_id:
provider_set_entry:
asset_universe:
data_families:
freshness_profile:
rights_record_version:
entitlement_model:
retention_limits:
cache_limits:
attribution_requirements:
model_ai_constraints:
fallback_group:
cost_assumptions:
kill_switch_scope:
source_authority_digests:
evidence_as_of:
review_by:
reopen_triggers: []
```

These fields feed the approved `MK1_BOOTSTRAP_PROFILE`.

---

## 14. Mandatory reopen triggers

At minimum, the affected profile must be re-reviewed when any of the following materially changes:
- provider contract/terms/product or plan;
- exchange/venue redistribution policy;
- geography or user classification;
- display/non-display/derived/model use;
- storage/retention/cache semantics;
- asset universe/data family;
- entitlement model;
- provider commercial quote where unit economics depend on it;
- termination/revocation rights;
- fallback-provider compatibility.

Reopening one profile does not automatically invalidate unrelated profiles, but every bootstrap/release that depends on the affected profile becomes pending reconciliation.

---

## Final invariant

> Q02 closes on exact, current, authoritative use rights and economics, never on “the API works.”
