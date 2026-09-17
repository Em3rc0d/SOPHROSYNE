# MK0 Promotion Packet

## Purpose

This is the canonical shape of the evidence bundle required to promote SOPHROSYNE from MK0 validation into production MK1 implementation.

It is intentionally incomplete until real external/empirical evidence exists. Missing sections remain `PENDING`; they are not inferred from design documents.

---

## Packet identity

```text
packet_id: MK0-PROMOTION-<version>
status: DRAFT | REVIEW_READY | APPROVED | REJECTED | SUPERSEDED
created_at:
reviewed_at:
canonical_commit:
bootstrap_profile_id:
supersedes:
```

The packet references immutable evidence receipts. It does not duplicate or rewrite their results.

---

## Section A — Internal-design baseline

Expected state before this packet can become `REVIEW_READY`:

- internal design graph = `CLOSED`;
- known internal design nodes remaining = `0`;
- no unresolved P0/P1 architecture contradiction;
- accepted ADR set current;
- `BUILD_READINESS.md` current;
- `ACCEPTANCE_RECEIPTS.md` current.

Current canonical source: `MK0_LOCKS.md` and `docs/implementation/BUILD_READINESS.md`.

If evidence forces a material architecture change, the packet returns to `DRAFT` until the affected internal node is reopened, resolved and closed again.

---

## Section B — Q00 Core causal-value receipt

```text
receipt_ref: PENDING
receipt_status: PENDING
validated_intervention_scope: PENDING
simple_friction_result: PENDING
memory_ablation_result: PENDING
hidden_rubric_result: PENDING
transfer_result: PENDING
outcome_blind_result: PENDING
cognitive_cost_result: PENDING
cheap_substitute_result: PENDING
minimum_meaningful_effect_met: PENDING
excluded_components: PENDING
conditional_constraints: PENDING
```

Promotion requirement:
- final state must be `CLOSED_PASS` or `CLOSED_CONDITIONAL`;
- full-product complexity is not required to pass; Q00 may force a narrower intervention;
- a failed current configuration cannot be rescued by Q03 willingness-to-pay, Q04 sophistication or Q05 moat narrative;
- all excluded/deferred components must propagate into the bootstrap profile.

---

## Section C — Q01 Regulatory receipt

```text
receipt_ref: PENDING
receipt_status: PENDING
regulatory_flow_profile: PENDING
jurisdiction: Peru
counsel_identity_or_firm_ref: PENDING
reviewed_prototype_digest: PENDING
approved_interaction_classes: PENDING
forbidden_interaction_classes: PENDING
required_copy_constraints: PENDING
required_disclaimers: PENDING
material_conditions: PENDING
```

Promotion requirement:
- final state must be `CLOSED_PASS` or `CLOSED_CONDITIONAL`;
- every condition must be incorporated into canonical product/UX/API behavior before packet approval.

---

## Section D — Q02 Data-rights receipts

One receipt per initial production `DataUseProfile`.

```text
profiles:
  - receipt_ref: PENDING
    provider: PENDING
    provider_product: PENDING
    asset_universe: PENDING
    data_family: PENDING
    timing_profile: PENDING
    geography: PENDING
    display_rights: PENDING
    non_display_rights: PENDING
    redistribution_rights: PENDING
    derived_use_rights: PENDING
    retention_cache: PENDING
    attribution: PENDING
    entitlement_model: PENDING
    cost_model: PENDING
    fallback_group: PENDING
```

Promotion requirement:
- all mandatory uses explicitly allowed;
- unknown rights treated as denied;
- cost assumptions propagated into `UNIT_ECONOMICS.md`;
- fallback/degradation semantics compatible with architecture.

---

## Section E — Q03 User-value / WTP bundle

```text
behavioral_discovery_receipt: PENDING
translator_comprehension_receipt: PENDING
repeat_use_receipt: PENDING
pricing_commitment_receipt: PENDING
primary_persona_version: PENDING
jtbd_version: PENDING
wedge_version: PENDING
initial_pricing_hypothesis: PENDING
validated_trust_requirements: PENDING
rejected_hypotheses: PENDING
```

Promotion requirement:
- problem observed in real workflows;
- objective comprehension/workflow evidence supports the selected product representation;
- repeat-use evidence exists;
- pricing evidence is stronger than generic survey enthusiasm;
- target persona/wedge is frozen from observed results, not preference of the team;
- Q03 evidence is compatible with the intervention scope that survived Q00.

---

## Section F — Q04 Quant bundle

```text
baseline_harness_receipt: PENDING
golden_fixture_receipt: PENDING
anti_leakage_receipt: PENDING
reproducibility_receipt: PENDING
dataset_manifest: PENDING
asset_universe: PENDING
cost_model_version: PENDING
benchmark_versions: PENDING
primary_metrics: PENDING
ml_decision: PENDING  # INCLUDE | EXCLUDE | DEFER
ml_incremental_value_receipt: PENDING_IF_REQUIRED
```

Promotion requirement:
- deterministic baseline harness reproducible;
- no look-ahead violation;
- exact cost/accounting semantics frozen;
- explicit ML include/exclude/defer decision exists;
- MK1 has no hidden dependency on unvalidated alpha;
- Q04 complexity cannot override Q00 causal-value conclusions.

A valid packet may explicitly contain `ml_decision: EXCLUDE`.

---

## Section G — Q05 Moat bundle

```text
competitive_task_receipt: PENDING
repeat_use_linkage_receipt: PENDING
replicability_assessment: PENDING
moat_hypothesis_version: PENDING
supported_components: PENDING
unsupported_components: PENDING
scale_spend_constraint: PENDING
next_evidence_horizon: PENDING
```

Promotion requirement:
- either a candidate durable advantage has supporting evidence;
- or Q05 is `CLOSED_CONDITIONAL` with MK1 explicitly framed as a learning wedge and scale spend blocked;
- no component removed or weakened by Q00 may still be presented as moat.

Weak moat evidence does not necessarily kill MK1; it blocks pretending that defensibility has been proven.

---

## Section H — Cross-receipt contradiction log

Every contradiction gets an ID.

```text
contradictions:
  - id:
    receipts_in_conflict:
    description:
    severity: P0 | P1 | P2 | P3
    affected_docs:
    resolution:
    residual_risk:
    status: OPEN | RESOLVED | ACCEPTED_LIMITATION
```

Packet cannot be approved while a P0/P1 contradiction remains `OPEN`.

Examples:
- Q03 willingness-to-pay depends on complexity rejected by Q00;
- user preference depends on personalization prohibited by Q01;
- preferred data source invalidates unit economics;
- ML result depends on data use not allowed by Q02;
- validated wedge conflicts with the currently frozen persona;
- moat thesis depends on a feature removed during Q00 or legal re-scope.

---

## Section I — MK1 Bootstrap Profile

The exact implementation configuration is copied by reference from the final evidence outputs.

```text
profile_id: PENDING
q00_intervention_scope: PENDING
q00_excluded_components: PENDING
regulatory_flow_profile: PENDING
primary_persona: PENDING
jtbd: PENDING
wedge: PENDING
pricing_hypothesis: PENDING
asset_universe: PENDING
provider_set: PENDING
data_use_profiles: PENDING
fallback_groups: PENDING
freshness_profiles: PENDING
risk_policy_version: PENDING
quant_baseline_receipt: PENDING
ml_scope: PENDING
moat_status: PENDING
legal_copy_version: PENDING
canonical_source_digests: PENDING
```

No production implementation is authorized against a vague “latest” configuration. It builds against this immutable profile version.

---

## Section J — Architecture impact review

Required questions:

1. Did Q00 remove/require a component that changes system boundaries?
2. Did any evidence introduce a new trust boundary?
3. Did any provider requirement change storage/display/retention architecture?
4. Did counsel impose a flow constraint that changes API/domain semantics?
5. Did the validated persona require a new data family or authority level?
6. Did Q04 add ML into an authoritative path?
7. Did pricing/entitlements create a new authorization boundary?
8. Did fallback selection introduce incompatible semantics?
9. Did any change invalidate an accepted ADR?

Output:

```text
architecture_impact: NONE | NON_MATERIAL | MATERIAL
reopened_internal_nodes: []
new_or_superseding_adrs: []
review_status: PENDING
```

A `MATERIAL` result blocks promotion until affected internal nodes are closed again.

---

## Section K — Final promotion decision

Only one final state is allowed.

### APPROVED

All MK0 promotion requirements are satisfied and production MK1 implementation may begin against the exact bootstrap profile.

### REJECTED — RESEARCH CONTINUES

One or more evidence gates remain insufficient. Research/prototype work continues; production implementation remains blocked.

### PIVOT REQUIRED

Evidence invalidates the current product configuration but supports a materially different candidate. Canonical docs are updated and affected evidence gates reopen.

### STOP

The current program thesis lacks a viable causal/legal/data/commercial/scientific path after repeated falsification.

---

## Approval checklist

A promotion reviewer must be able to answer **yes** to all:

- Is Q00 final and promotable for the exact intervention scope entering MK1?
- Are all Q01–Q05 receipts final and promotable?
- Are conditional constraints frozen into canonical specs?
- Are required external authorities actually present where required?
- Were experiment thresholds pre-registered before outcome inspection?
- Is negative/conflicting evidence preserved?
- Are data rights scoped to exact intended uses?
- Is the quant baseline reproducible independently?
- Is ML explicitly included, excluded or deferred?
- Is the selected persona/wedge supported by observed behavior?
- Are Q03/Q05 conclusions compatible with Q00 exclusions/conditions?
- Are unit-economics assumptions synchronized with provider/pricing evidence?
- Are all P0/P1 contradictions resolved?
- Does the bootstrap profile identify one exact build configuration?
- Does architecture impact review show no unresolved reopened node?
- Does `BUILD_READINESS.md` pass?

If any answer is no, the packet is not approved.

---

## Promotion statement

An approved packet authorizes only the following statement:

> **SOPHROSYNE MK1 has an evidence-backed, causally tested, legally/data-rights-scoped and scientifically reproducible candidate configuration that is ready to be implemented and tested.**

It does **not** authorize claims of profitability, investment performance, regulatory approval beyond the reviewed scope, product-market fit, durable moat or production reliability beyond the evidence actually contained in the receipts.
