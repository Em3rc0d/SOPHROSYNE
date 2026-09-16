# MK1 Bootstrap Profile Contract

## Purpose

`MK1_BOOTSTRAP_PROFILE` is the immutable, evidence-derived configuration that production MK1 implementation is authorized to build.

It exists to prevent a common failure mode: closing validation on one product/data/quant configuration and then quietly implementing a different one.

The profile contains no aspirational values. Every field must trace to a final evidence receipt, accepted ADR or already-closed internal design contract.

---

## Canonical schema

```yaml
profile_id:
version:
status: DRAFT | CANDIDATE | APPROVED | SUPERSEDED
created_at:
approved_at:
canonical_commit:
supersedes:

product:
  primary_persona:
  jtbd_version:
  wedge_version:
  product_thesis_version:
  mk1_spec_version:
  pricing_hypothesis:

regulatory:
  jurisdiction: Peru
  regulatory_flow_profile:
  approved_interaction_classes: []
  forbidden_interaction_classes: []
  required_copy_constraints: []
  required_disclaimers: []
  legal_receipt_ref:

data:
  asset_universe:
  provider_set: []
  data_use_profiles: []
  fallback_groups: []
  freshness_profiles: []
  entitlement_model:
  attribution_requirements: []
  data_rights_receipt_refs: []

quant:
  baseline_receipt_ref:
  dataset_manifest_ref:
  transaction_cost_model_version:
  benchmark_versions: []
  primary_metrics: []
  ml_scope: INCLUDE | EXCLUDE | DEFER
  ml_receipt_ref:

risk:
  risk_policy_version:
  portfolio_context_scope:
  stale_data_behavior:
  no_conclusion_policy:

moat:
  moat_receipt_ref:
  status: SUPPORTED | CONDITIONAL | LEARNING_WEDGE
  supported_components: []
  unsupported_components: []
  scale_spend_constraint:

operations:
  implementation_sequence_version:
  acceptance_receipt_contract_version:
  initial_environment_profile:

provenance:
  mk0_promotion_packet_ref:
  source_digests: []
  adr_set_digest:
  canonical_doc_digests: []
```

---

## Profile states

### DRAFT

Fields are still being populated from evidence. Production implementation is not authorized.

### CANDIDATE

All required fields are populated and the profile can enter promotion review.

### APPROVED

The `MK0_PROMOTION_PACKET` has passed and this exact profile is authorized for implementation.

### SUPERSEDED

A later approved profile replaces this version. Historical implementation/release artifacts continue to reference the profile version they were built against.

---

## Evidence ownership

| Profile section | Primary authority |
|---|---|
| product | Q03 + closed product contracts |
| regulatory | Q01 |
| data | Q02 |
| quant | Q04 |
| moat | Q05 |
| risk | closed internal contracts + evidence-driven selected profile |
| operations | closed internal implementation contracts |
| provenance | promotion packet / repository history |

A field cannot be filled merely because it is convenient for implementation.

---

## Material-change matrix

After approval, changes are classified by impact.

### Class A — evidence-invalidating

Examples:
- new personalization/recommendation semantics;
- different jurisdiction;
- provider/data family with materially different rights;
- new asset universe requiring different market/session/corporate-action semantics;
- ML added after profile approved with `EXCLUDE`;
- new pricing/entitlement model that changes legal or data-rights classification;
- change to product wedge/persona based on new evidence.

Required action:
1. affected evidence lock reopens;
2. new evidence plan/receipt where required;
3. architecture impact review;
4. new bootstrap-profile version;
5. production implementation pauses for affected scope.

### Class B — internal-semantic

Examples:
- changing authoritative persistence semantics;
- changing point-in-time rules;
- changing LLM authority;
- changing risk authority;
- changing DecisionRecord immutability;
- changing runtime topology in a way covered by ADR policy.

Required action:
1. affected internal design node reopens;
2. new/superseding ADR;
3. internal closure audit repeated for impacted dependencies;
4. new bootstrap-profile version if implementation configuration changes.

### Class C — implementation-conformance

Examples:
- library upgrade with no semantic effect;
- implementation detail within frozen interface/behavior contracts;
- performance optimization preserving semantics;
- refactor preserving external/internal contracts.

Required action:
- normal implementation/test/acceptance receipts;
- no evidence lock reopened unless behavior actually changes.

### Class D — editorial/non-semantic

Examples:
- typo fixes;
- non-substantive documentation formatting;
- wording changes that do not alter legal/product meaning.

Required action:
- ordinary review;
- no profile version required unless a canonical digest policy intentionally tracks such changes.

---

## Build authorization rule

Production MK1 work must identify the bootstrap profile it implements.

Every production feature PR should be able to answer:

```text
bootstrap_profile_id:
affected_profile_sections:
semantic_change: YES | NO
requires_revalidation: YES | NO
requires_adr: YES | NO
acceptance_receipts_required: []
```

If a feature cannot identify its governing profile/contract, the work is not ready for production implementation.

---

## Provider substitution rule

A provider is not interchangeable merely because it exposes the same symbol or OHLCV shape.

A substitution is permitted without reopening Q02 only if the replacement belongs to an already-approved fallback compatibility group whose receipt proves compatible:
- time semantics;
- instrument identity;
- rights profile;
- freshness profile;
- corrections behavior;
- corporate actions/session behavior where applicable;
- attribution/entitlement requirements.

Otherwise, create a new `DataUseProfile` receipt and a new bootstrap profile version.

---

## Asset-universe rule

The asset universe is part of the validated configuration.

Adding assets may affect:
- provider rights/cost;
- exchange/session calendars;
- corporate actions;
- liquidity/cost model;
- benchmark selection;
- risk policy;
- legal/product presentation.

Therefore “add one more asset” is not automatically a trivial implementation change.

---

## ML-scope rule

`ml_scope` is explicit:

### INCLUDE

Only when Q04 produced a promoted model/model family and the authoritative role of that model is specified.

### EXCLUDE

MK1 intentionally proceeds without ML as an alpha component. No implementation PR may silently add predictive authority.

### DEFER

The product proceeds with deterministic intelligence while a later MK/experiment may re-open the ML question.

All three are valid evidence-derived outcomes.

---

## Pricing-hypothesis rule

The profile may carry an initial pricing hypothesis, but this is not permanent commercial truth.

Changing price alone may be Class C/D if nothing else changes. It becomes Class A when the price or entitlement design changes:
- user classification;
- provider entitlements;
- data redistribution rights;
- legal posture;
- feature authority boundaries;
- target persona/wedge.

---

## Risk-policy binding

The bootstrap profile references an exact `risk_policy_version`.

Risk policy remains independent from model conviction. No evidence receipt or model promotion may grant a model authority to bypass:
- exposure limits;
- freshness gates;
- portfolio constraints;
- `NO CONCLUSION` / `NO TRADE` behavior;
- rights restrictions.

---

## Reproducibility binding

Every quant/research result used by MK1 must be reconstructible from the profile references:
- dataset manifest;
- cost model;
- benchmark versions;
- model/strategy versions where applicable;
- source/provider profile;
- point-in-time semantics;
- code/build identity once implementation exists.

---

## Relationship to release artifacts

The profile is pre-build configuration truth. Later implementation/release artifacts add implementation proof.

```text
Evidence receipts
      |
      v
MK1_BOOTSTRAP_PROFILE
      |
      v
Production implementation
      |
      v
Acceptance receipts
      |
      v
Release candidate
      |
      v
Production release
```

A release must never claim a different bootstrap profile than the one its implemented semantics actually follow.

---

## Approval invariant

An approved profile means:

> **This exact MK1 configuration has passed the evidence gates required to justify implementation.**

It does not mean:
- profitable;
- regulation-proof in every jurisdiction;
- product-market fit proven;
- moat proven forever;
- production reliability proven;
- security proven before implementation receipts exist.

Those claims require their own evidence.
