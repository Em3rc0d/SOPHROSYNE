# MK1 Bootstrap Provenance Matrix

## Purpose

This matrix prevents `MK1_BOOTSTRAP_PROFILE` from acquiring values through implementation-time judgement. Every required field family has an evidence producer, compatibility rule and fail-closed behavior.

## Provenance matrix

| Bootstrap field | Producer | Compatibility rule | Missing/conflict behavior |
|---|---|---|---|
| `q00_receipt_ref` | Q00 | must be final promotable receipt | BLOCKED |
| `intervention_scope` | Q00 | exact causal-value scope that survived baseline/ablation tests | BLOCKED |
| `required_components` | Q00 | only components needed by promotable intervention | empty unless supported |
| `excluded_components` | Q00 + Q01–Q05 | union of all prohibited/unproven components | fail closed |
| `deferred_components` | Q00/Q04/Q05 | may not be implemented as required/core until revalidated | fail closed |
| `memory_scope` | Q00 | EXCLUDED / SHORT / FULL / NOT_APPLICABLE only | BLOCKED |
| `transfer_claim_scope` | Q00 | claims cannot exceed measured assisted/transfer evidence | BLOCKED |
| `cognitive_cost_constraints` | Q00 | product UX must stay inside accepted burden envelope | BLOCKED if material |
| `jurisdiction` | Q01 | must equal reviewed jurisdiction | BLOCKED |
| `eligible_user_geography` | Q01 + Q03 | legal eligibility must contain empirically validated promotion cohort | BLOCKED |
| `primary_persona_version` | Q03 + Q00 | must match promotable Q03 cohort within Q00-supported intervention | BLOCKED |
| `jtbd_version` | Q03 + Q00 | must reference tested workflow and causal mechanism | BLOCKED |
| `wedge_version` | Q03 + Q00 | conditional narrowing must be preserved | BLOCKED |
| `translator_representation_version` | Q03 | must be tested version or reviewed successor with no material semantic drift | BLOCKED |
| `pricing_hypothesis` | Q03 | research price evidence only; cannot rescue failed Q00 | BLOCKED if paid tier required |
| `paid_flow_status` | Q01 + Q03 | paid activation requires legal allowance + demand evidence | CHARGE_DISABLED until both |
| `provider_profiles` | Q02 | exact provider/product/profile rights only | BLOCKED |
| `asset_universe` | Q02 + Q04 | intersection only | BLOCKED if empty |
| `data_families` | Q02 + Q00 | every family has authorized use profile and remains necessary for supported intervention | BLOCKED / simplify if unnecessary |
| `rights_policy_versions` | Q02 | no UNKNOWN right | BLOCKED |
| `entitlement_policy` | Q02 | compatible with user class/geography | BLOCKED |
| `retention_cache_policy` | Q02 | cannot exceed provider allowance | BLOCKED |
| `attribution_requirements` | Q02 | promoted into UI/API requirements | BLOCKED if unresolved |
| `freshness_profiles` | Q02 + internal market-data contract | must be <= rights/technical limits and explicit by data family | BLOCKED |
| `portfolio_context_scope` | Q01 + product scope + Q00 | no broader personalization than legal or causal-value scope permits | BLOCKED |
| `legal_copy_version` | Q01 | exact reviewed copy or semantically non-material revision | BLOCKED |
| `claim_lexicon_version` | Q01 + Q00 | no claim broader than legal or measured causal/transfer evidence | BLOCKED |
| `required_disclaimers` | Q01 | exact applicable set | BLOCKED |
| `consent_recordkeeping_profile` | Q01 | privacy/consumer/securities requirements reconciled | BLOCKED |
| `baseline_harness_receipt` | Q04-A | must be CLOSED_PASS | BLOCKED |
| `dataset_manifest_ref` | Q04 + Q02 | dataset source rights compatible with research/product use | BLOCKED |
| `cost_model_version` | Q04 | frozen in passing baseline receipt | BLOCKED |
| `benchmark_versions` | Q04 | passing benchmark ladder only | BLOCKED |
| `ml_scope` | Q04-B + Q00 | INCLUDE / EXCLUDE / DEFER only after Q04-A; cannot be required if Q00 excludes it | default EXCLUDE until authorized |
| `promoted_model_family` | Q04-B | only when `ml_scope=INCLUDE` and receipt passes | NULL otherwise |
| `moat_status` | Q05 + Q00 | Q05 cannot treat Q00-excluded commodity component as moat | BLOCKED |
| `supported_components` | Q05 + Q00 | exposure-aware evidence only, intersection with Q00-allowed scope | empty unless supported |
| `scale_spend_constraint` | Q05 | LEARNING_WEDGE keeps scale spend gated | BLOCKED if absent |
| `risk_policy_version` | internal closed risk contract + promotion packet | cannot be weakened by external evidence | BLOCKED |
| `feature_flags` | Q00–Q05 + promotion packet | most restrictive compatible state wins | fail closed |
| `excluded_features` | Q00–Q05 | any prohibited/unproven/excluded feature remains excluded | fail closed |

## Conflict resolution

When multiple producers constrain the same field:

1. compute the intersection of permitted scope;
2. if an unambiguous safe intersection exists, promotion may freeze that narrower scope;
3. if scope meaning changes materially, create a P1 contradiction and update the affected canonical specification;
4. if no safe intersection exists, promotion is blocked;
5. implementation may never choose one producer over another ad hoc;
6. positive downstream evidence may not broaden an upstream Q00 exclusion without reopening Q00.

## Provenance record

Every instantiated bootstrap field records:

```yaml
field_name:
value:
producer_receipts: []
source_artifact_digests: []
constraint_refs: []
derivation_rule:
frozen_at:
reviewer:
```

Derived values such as an asset-universe intersection or an allowed-component intersection must record the derivation, not merely the resulting list.

## Re-opening

If a producer receipt is superseded or reopened, dependent bootstrap fields become `STALE_PENDING_REVIEW` and cannot authorize a new deployment/release until reconciled.

If a feature in `excluded_components` is proposed for reintroduction, Q00 and any other producer that excluded it must be reopened as applicable.

## Final invariant

> Every build-defining value is evidence-derived or contract-derived; no complexity is introduced because implementation wanted it, and no downstream commercial signal can override an upstream causal-value exclusion.
