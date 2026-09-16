# MK0 Promotion Packet

## Purpose

This is the single review bundle that determines whether one exact evidence-backed configuration may become production MK1. It summarizes evidence; it does not reinterpret missing evidence or invent bootstrap values.

## Identity

```yaml
promotion_packet_id:
packet_version:
candidate_configuration_id:
created_at:
owner:
independent_reviewer:
status: DRAFT | REVIEW_READY | APPROVED | REJECTED | SUPERSEDED
supersedes:
```

## Required aggregate receipts

```yaml
q01:
  receipt_ref:
  final_decision:
q02:
  aggregate_receipt_ref:
  profile_receipt_refs: []
  final_decision:
q03:
  receipt_ref:
  experiment_receipt_refs: []
  final_decision:
q04:
  receipt_ref:
  baseline_receipt_ref:
  ml_receipt_ref:
  final_decision:
q05:
  receipt_ref:
  final_decision:
```

Every required aggregate decision must be `CLOSED_PASS` or `CLOSED_CONDITIONAL`. `INCONCLUSIVE`, `PIVOT_REQUIRED`, or `STOP_CURRENT_CONFIGURATION` blocks approval.

## Scope compatibility matrix

The packet records and verifies:

```yaml
jurisdiction: Peru
primary_promotion_geography:
primary_study_language:
primary_persona_version:
product_or_prototype_digest:
legal_flow_profile:
data_use_profile_refs: []
provider_semantics_profile_refs: []
asset_universe:
quant_profile_ref:
pricing_surface_version:
```

Evidence from another geography or language may be retained as exploratory evidence but cannot silently close the Peru MK1 scope.

## Conditions matrix

Every `CLOSED_CONDITIONAL` condition is copied verbatim into a structured matrix:

```yaml
conditions:
  - condition_id:
    source_receipt_ref:
    requirement:
    canonical_destination:
    bootstrap_field:
    acceptance_or_regression_check:
```

No condition may remain only in prose.

## Unit-economics synchronization

Required before approval:

```yaml
unit_economics_sync_ref:
unit_economics_version:
q02_provider_cost_refs: []
q03_pricing_evidence_ref:
legal_compliance_recurring_cost_assumptions_ref:
infrastructure_workload_assumptions_ref:
payment_fee_tax_assumptions_ref:
support_burden_ref:
status: PASS | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE
```

Optimistic TAM, conversion, or future scale assumptions cannot substitute for observed/authoritative unit-economics inputs.

## Contradiction review

```yaml
contradiction_log_ref:
items:
  - contradiction_id:
    initial_severity: P0 | P1 | P2 | P3
    current_severity: P0 | P1 | P2 | P3
    status: OPEN | MITIGATING | RESOLVED | ACCEPTED_LIMITATION | SUPERSEDED
    bootstrap_constraint_ref:
```

Approval requires every P0/P1 to be `RESOLVED` or `SUPERSEDED` by a resolved successor. `ACCEPTED_LIMITATION` is allowed only for P2/P3 and must appear in the bootstrap where relevant.

## Architecture-impact review

For every frozen output, record whether it changes an existing internal design invariant.

```yaml
architecture_impacts:
  - source_receipt_ref:
    output_key:
    impact: NONE | CONFIGURATION_ONLY | DESIGN_REOPEN_REQUIRED
    reopened_lock_or_adr_ref:
```

A `DESIGN_REOPEN_REQUIRED` item blocks approval until canonical design is reconciled.

## Bootstrap derivation map

Every non-null bootstrap value has a source:

```yaml
bootstrap_sources:
  - bootstrap_path:
    value_or_ref:
    source_type: EVIDENCE_RECEIPT | CLOSED_DESIGN_CONTRACT | APPROVED_ADR
    source_ref:
```

Manual/unattributed values are forbidden.

At minimum the map covers persona/JTBD/wedge/pricing, legal flow/copy/commercial constraints, portfolio-context scope, provider/data rights/freshness/fallback semantics, quant/ML scope, risk policy, moat status and scale constraints.

## Required attachments

- final aggregate Q01–Q05 receipts;
- experiment/review manifests and digests;
- Q01 external-authority refs;
- Q02 authoritative rights/quote/contract refs;
- Q03 analysis and instrumentation receipts;
- Q04 dataset/reproduction/anti-leakage artifacts;
- Q05 comparator snapshot and linkage analysis;
- contradiction log;
- unit-economics synchronization artifact;
- candidate `MK1_BOOTSTRAP_PROFILE`;
- architecture-impact review;
- build-readiness checklist.

## Approval checklist

The packet may become `APPROVED` only when all are true:
- Q01–Q05 final decisions are promotable and scope-compatible;
- all applicable Q01 legal/commercial domains have authoritative closure or the corresponding commercial capability is explicitly disabled;
- selected Q02 profiles are authoritative and current enough for the proposed activation;
- Q03/Q05 promotion evidence matches the target geography/persona/language;
- Q04 research outputs promoted to MK1 have production-semantics compatibility;
- unit economics are not structurally invalid for the selected configuration;
- no P0/P1 contradiction remains unresolved;
- every conditional restriction has a canonical destination and acceptance/regression check;
- bootstrap derivation contains no manual value;
- any design reopen is resolved before build;
- `docs/implementation/BUILD_READINESS.md` passes.

## Decision

```yaml
final_packet_decision: APPROVED | REJECTED
rationale:
bootstrap_profile_ref:
reviewer_signoff:
final_packet_digest:
```

Approval means only: **this exact configuration has earned the right to be built**.
