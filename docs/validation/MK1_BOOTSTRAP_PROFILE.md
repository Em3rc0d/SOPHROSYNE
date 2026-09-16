# MK1 Bootstrap Profile

## Purpose

The bootstrap profile is the immutable evidence-derived configuration contract for one authorized MK1 build. It is generated only from approved EvidenceReceipts, closed design contracts and approved ADRs.

## Identity

```yaml
bootstrap_profile_id:
profile_version:
created_at:
promotion_packet_ref:
status: DRAFT | APPROVED | SUPERSEDED
supersedes:
```

## Product

```yaml
product:
  primary_persona:
  jtbd_version:
  wedge_version:
  product_thesis_version:
  mk1_spec_version:
  primary_promotion_geography: Peru
  primary_study_language: Spanish
  pricing_hypothesis:
  pricing_surface_version:
  q03_receipt_ref:
```

A different production geography is a material change and reopens the affected evidence/legal scope.

## Legal / commercial activation

```yaml
regulatory:
  jurisdiction: Peru
  regulatory_flow_profile:
  approved_interaction_classes: []
  forbidden_interaction_classes: []
  required_copy_constraints: []
  required_disclaimers: []
  legal_copy_version:
  portfolio_context_scope:
  commercial_activation_constraints: []
  non_securities_applicability_refs: []
  reviewed_prototype_digest:
  legal_receipt_ref:
```

If commercial activation is not yet authorized for an applicable domain, the capability remains disabled; the build may include only the non-commercial surface explicitly allowed by Q01.

## Data

```yaml
data:
  asset_universe: []
  provider_set: []
  data_use_profiles: []
  provider_semantics_profile_refs: []
  fallback_groups: []
  freshness_profiles: []
  entitlement_model:
  attribution_requirements: []
  retention_cache_constraints: []
  rights_recheck_triggers: []
  data_rights_receipt_refs: []
  q02_aggregate_receipt_ref:
```

## Quant

```yaml
quant:
  q04_receipt_ref:
  baseline_receipt_ref:
  dataset_manifest_ref:
  transaction_cost_model_version:
  benchmark_versions: []
  primary_metrics: []
  production_semantics_compatibility_ref:
  ml_scope: INCLUDE | EXCLUDE | DEFER
  ml_receipt_ref: null
  promoted_model_family: null
```

`ml_receipt_ref`/model family may be null when `EXCLUDE` or `DEFER`. Neither state creates an MK1 runtime ML dependency. Later inclusion is a material change and reopens Q04 and any affected Q02 use rights.

## Risk / truth behavior

```yaml
risk:
  risk_policy_version:
  portfolio_context_scope:
  stale_data_behavior:
  no_conclusion_policy:
  causality_label_policy:
  probability_calibration_policy:
```

Where product preference and legal/data constraints conflict, the stricter authoritative constraint wins and affected user evidence is re-evaluated if the experience materially changes.

## Moat / scale posture

```yaml
moat:
  q05_receipt_ref:
  moat_status: SUPPORTED | LEARNING_WEDGE
  supported_components: []
  unsupported_components: []
  scale_spend_constraint:
  claims_allowed: []
  claims_forbidden: []
  next_evidence_horizon:
```

`LEARNING_WEDGE` is a conditional promotion state, not a moat claim.

## Economics

```yaml
economics:
  unit_economics_version:
  unit_economics_sync_ref:
  provider_cost_refs: []
  pricing_evidence_ref:
  infrastructure_assumption_ref:
  payment_tax_assumption_ref:
  support_burden_ref:
```

## Evidence provenance

```yaml
evidence:
  q01_receipt_ref:
  q02_receipt_refs: []
  q03_receipt_ref:
  q04_receipt_ref:
  q05_receipt_ref:
  contradiction_log_ref:
  promotion_packet_ref:
```

Every referenced Q final decision must be `CLOSED_PASS` or `CLOSED_CONDITIONAL`. `INCONCLUSIVE`, `PIVOT_REQUIRED`, or `STOP_CURRENT_CONFIGURATION` cannot appear in an approved profile.

## Build binding

Every production implementation PR must declare:

```yaml
bootstrap_profile_id:
bootstrap_profile_digest:
```

A build may not silently choose another provider, geography, persona, pricing surface, legal interaction class, data use, quant profile, ML scope or moat claim.

## Material-change classes

The following require a new bootstrap version and reopening of affected evidence/ADR scope: jurisdiction/geography; personalization/recommendation semantics; commercial activation; portfolio-context scope; provider/data rights or materially different semantics; asset/data universe beyond approved rights; pricing surface where economics/legal meaning changes; ML include/exclude transition; model probability surface; trust/risk invariant; supported moat/scale claim.

## Approval

```yaml
status: APPROVED
approved_by:
approved_at:
profile_digest:
```

Approval is valid only with an approved `MK0_PROMOTION_PACKET` and passing `BUILD_READINESS`.
