# MK1 Bootstrap Profile Contract

## Purpose

`MK1_BOOTSTRAP_PROFILE` is the immutable, evidence-derived configuration that production MK1 implementation is authorized to build.

It exists to prevent a common failure mode: closing validation on one product/data/quant configuration and then quietly implementing a different one.

The profile contains no aspirational values. Every field must trace to a final evidence receipt, accepted ADR, already-closed internal design contract or active Closed Validation Graph node/edge.

An approved profile is inseparable from one governing graph snapshot. Profile semantics and graph reachability are two views of the same authorized configuration.

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

graph:
  graph_version:
  graph_digest: PENDING_UNTIL_PHASE0_HASHING_AVAILABLE
  active_node_ids: []
  active_edge_ids: []
  graph_closure_audit_ref:
  graph_conformance_receipt_ref: PENDING_UNTIL_IMPLEMENTATION

causal_value:
  q00_receipt_ref:
  intervention_scope:
  required_components: []
  excluded_components: []
  deferred_components: []
  simple_friction_result:
  memory_scope: EXCLUDED | SHORT | FULL | NOT_APPLICABLE
  transfer_claim_scope: ASSISTED_ONLY | LIMITED_TRANSFER | SUPPORTED_TRANSFER
  cognitive_cost_constraints: []
  cheap_substitute_comparison_ref:

product:
  primary_persona:
  jtbd_version:
  wedge_version:
  product_thesis_version:
  thesis_stack_version:
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
  validation_graph_schema_version:
```

---

## Profile states

### DRAFT
Fields are still being populated from evidence. Production implementation is not authorized.

### CANDIDATE
All required fields are populated, graph reachability is coherent, and the profile can enter promotion review.

### APPROVED
The `MK0_PROMOTION_PACKET` has passed for the same graph snapshot and this exact profile is authorized for implementation.

### SUPERSEDED
A later approved profile replaces this version. Historical implementation/release artifacts continue to reference the profile + graph versions/digests they were built against.

---

## Evidence ownership

| Profile section | Primary authority |
|---|---|
| graph | ADR-0016 + active CVG snapshot + graph closure audit |
| causal_value | Q00 + ADR-0014 + thesis stack |
| product | Q03 constrained by Q00 + closed product contracts |
| regulatory | Q01 |
| data | Q02 |
| quant | Q04 constrained by Q00 |
| moat | Q05 constrained by Q00 |
| risk | closed internal contracts + evidence-driven selected profile |
| operations | closed internal implementation contracts |
| provenance | promotion packet / repository history / CVG |

A field cannot be filled merely because it is convenient for implementation.

---

## Graph binding rule

An `APPROVED` profile must identify one canonical graph version and the exact active node/edge set that authorizes the build.

Before deterministic Phase 0 hashing exists:
- `graph_version` is mandatory;
- `graph_digest` uses the canonical pending placeholder;
- promotion packet and bootstrap profile must reference the same graph version.

After Phase 0 hashing exists:
- `graph_digest` is mandatory and immutable for the approved profile version;
- promotion packet, profile, build metadata and applicable acceptance receipts must agree on that digest;
- a digest mismatch blocks the affected build/release path.

No profile may activate an implementation component that is unreachable from the approved graph or excluded by a governing evidence node.

No P0/P1 active node may be orphaned and every active material implementation path must have a reverse-validation path.

---

## Q00 binding rule

Q00 determines which candidate components are allowed to count as required product complexity.

Examples:
- if Q00 concludes `MEMORY_EXCLUDED`, MK1 may not require persistent memory as a core value mechanism;
- if Q00 concludes `SHORT_MEMORY_SUFFICIENT`, full-history memory cannot be introduced without new evidence;
- if simple friction captures most of the measured benefit, MK1 must implement the narrower validated intervention or reopen Q00;
- if transfer is unsupported, product copy cannot claim that SOPHROSYNE improves independent reasoning outside assisted use;
- if a cheap substitute is non-inferior on the primary outcomes, the current independent-product configuration cannot be approved without a material pivot.

Implementation may not silently reintroduce a component listed in `excluded_components` or make it reachable through the active graph.

---

## Material-change matrix

### Class A — evidence-invalidating

Examples:
- reintroducing a Q00-excluded component as core value;
- materially broadening the intervention beyond Q00 evidence;
- new personalization/recommendation semantics;
- different jurisdiction;
- provider/data family with materially different rights;
- new asset universe requiring different market/session/corporate-action semantics;
- ML added after profile approved with `EXCLUDE`;
- new pricing/entitlement model that changes legal or data-rights classification;
- change to product wedge/persona based on new evidence.

Required action:
1. affected evidence lock/node reopens;
2. affected graph edges move to non-promotable state where applicable;
3. new evidence plan/receipt where required;
4. architecture/graph impact review;
5. new bootstrap-profile version;
6. production implementation pauses for affected scope.

### Class B — internal-semantic / graph-semantic

Examples:
- changing authoritative persistence semantics;
- changing point-in-time rules;
- changing LLM authority;
- changing risk authority;
- changing DecisionRecord immutability;
- changing runtime topology in a way covered by ADR policy;
- adding/removing a P0/P1 graph node;
- changing a material edge relation or closure requirement;
- changing reverse-validation reachability;
- changing contradiction propagation semantics.

Required action:
1. affected internal design/graph node reopens;
2. new/superseding ADR;
3. graph version changes;
4. graph closure audit repeated for impacted dependencies;
5. stale receipts invalidated by `revalidate_on` rules;
6. new bootstrap-profile version if implementation configuration/reachability changes.

### Class C — implementation-conformance

Examples:
- library upgrade with no semantic effect;
- implementation detail within frozen interface/behavior contracts;
- performance optimization preserving semantics;
- refactor preserving external/internal contracts and graph reachability.

Required action:
- normal implementation/test/acceptance receipts;
- current graph/profile reference retained;
- no evidence/design node reopened unless behavior actually changes.

### Class D — editorial/non-semantic

Examples:
- typo fixes;
- non-substantive documentation formatting;
- wording changes that do not alter legal/product/graph meaning.

---

## Build authorization rule

Production MK1 work must identify the bootstrap profile and graph it implements.

Every production feature PR must be able to answer:

```text
bootstrap_profile_id:
graph_version:
graph_digest:
affected_node_ids: []
affected_edge_ids: []
affected_profile_sections:
q00_component_status: REQUIRED | ALLOWED | EXCLUDED | DEFERRED
semantic_change: YES | NO
graph_revalidation_required: YES | NO
requires_revalidation: YES | NO
requires_adr: YES | NO
acceptance_receipts_required: []
```

If a feature cannot identify its governing profile/graph/contracts or has no return path through verification to its governing proposition, the work is not ready for production implementation.

---

## Provider substitution rule

A provider is not interchangeable merely because it exposes the same symbol or OHLCV shape.

A substitution is permitted without reopening Q02 only if the replacement belongs to an already-approved fallback compatibility group whose receipt proves compatible time semantics, identity, rights, freshness, corrections, corporate actions/session behavior and attribution/entitlement requirements.

If substitution changes graph reachability, rights authority or required verification, a new profile/graph version is required according to the material-change matrix.

---

## Asset-universe rule

The asset universe is part of the validated configuration. Adding assets may affect provider rights/cost, exchange/session calendars, corporate actions, liquidity/cost model, benchmark selection, risk policy and product/legal presentation.

Therefore “add one more asset” is not automatically a trivial implementation change and may require graph/profile revalidation.

---

## ML-scope rule

`ml_scope` is explicit:

### INCLUDE
Only when Q04 produced a promoted model/model family and the authoritative role of that model is specified.

### EXCLUDE
MK1 intentionally proceeds without ML as an alpha component. No implementation PR may silently add predictive authority or activate an ML-authority node/edge.

### DEFER
The product proceeds with deterministic intelligence while a later MK/experiment may re-open the ML question.

All three are valid evidence-derived outcomes, but none can compensate for failed Q00 causal value.

---

## Pricing-hypothesis rule

The profile may carry an initial pricing hypothesis, but this is not permanent commercial truth. Positive pricing intent does not override Q00.

---

## Risk-policy binding

The bootstrap profile references an exact `risk_policy_version`. Risk policy remains independent from model conviction and cannot be weakened by evidence/model promotion.

---

## Reproducibility binding

Every quant/research result used by MK1 must be reconstructible from profile references, including Q00 experiment/receipt identity where the result defines product scope.

Graph/profile provenance must also reconstruct which nodes, edges, contracts and receipts authorized the implementation.

---

## Relationship to release artifacts

```text
Q00–Q05 evidence receipts
      |
      v
MK0_PROMOTION_PACKET
      |
      v
MK1_BOOTSTRAP_PROFILE + graph snapshot
      |
      v
Production implementation
      |
      v
Acceptance receipts + GRAPH_CONFORMANCE
      |
      v
Release candidate
      |
      v
Production release
      |
      v
Runtime observations / contradictions
      |
      +------> revalidate/reopen evidence, profile or design
```

A release must never claim a different bootstrap profile or graph snapshot than the one its implemented semantics actually follow.

---

## Approval invariant

An approved profile means:

> **This exact MK1 configuration has passed the evidence gates required to justify implementation, including the core causal-value gate for the complexity it contains, and is bound to one structurally valid Closed Validation Graph snapshot with explicit reverse-validation paths.**

It does not mean profitable, regulation-proof in every jurisdiction, product-market fit proven, moat proven forever, production reliability proven or security proven before implementation receipts exist.
