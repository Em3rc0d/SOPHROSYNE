# MK0 Evidence-to-Bootstrap Traceability Matrix

## Purpose

This matrix proves that every field required to authorize MK1 has exactly one legitimate producer, an authority class, a source receipt and an invalidation rule.

A bootstrap field with no producer is `UNRESOLVED`. A field with multiple conflicting producers creates a contradiction-log item and blocks promotion.

---

## Product fields

| Bootstrap field | Producer | Authority | Required evidence | Reopens when |
|---|---|---|---|---|
| `product.primary_persona` | Q03 | observed user evidence | Q03 aggregate promotable receipt | validated cohort materially changes |
| `product.jtbd_version` | Q03 | observed user evidence | Q03 receipt | JTBD changes materially |
| `product.wedge_version` | Q03 | observed user evidence | Q03 receipt | persona/use-case changes |
| `product.product_thesis_version` | closed product contract + Q03 consistency check | design + evidence | canonical thesis + no contradiction | evidence falsifies thesis |
| `product.mk1_spec_version` | product contract after Q01/Q03 incorporation | governance | exact canonical spec digest | material product-flow change |
| `product.pricing_hypothesis` | Q03 + economics sync | observed behavior | pricing/commitment receipt + economics review | price/entitlement changes legal/data/user class |

---

## Regulatory fields

| Bootstrap field | Producer | Authority | Required evidence | Reopens when |
|---|---|---|---|---|
| `regulatory.jurisdiction` | Promotion Packet | governance | `Peru` for initial MK1 | market expansion |
| `regulatory.regulatory_flow_profile` | Q01 | external qualified counsel | written review of exact frozen flows | material UX/copy/personalization change |
| `approved_interaction_classes` | Q01 | external qualified counsel | explicit counsel classification | flow semantics change |
| `forbidden_interaction_classes` | Q01 | external qualified counsel | explicit counsel classification | flow semantics change |
| `required_copy_constraints` | Q01 | external qualified counsel | reviewed user-facing copy/claims | material copy semantics change |
| `required_disclaimers` | Q01 | external qualified counsel | reviewed terms/disclaimers | commercial/legal scope changes |
| `legal_receipt_ref` | Q01 | external qualified counsel | finalized EvidenceReceipt | receipt superseded |

Q01 must cover the applicable MK1 commercial/legal surface, not only securities-advice classification. The review packet must explicitly classify or mark out-of-scope/handled-by-specialist for privacy/data protection, consumer/e-commerce claims, subscription/payment terms and other applicable launch obligations.

---

## Data fields

| Bootstrap field | Producer | Authority | Required evidence | Reopens when |
|---|---|---|---|---|
| `data.asset_universe` | Q02 + Q04 compatibility check | provider rights + research evidence | approved DataUseProfiles + Q04 manifest | asset family expands |
| `data.provider_set` | Q02 | provider authoritative terms/contract | approved profiles | provider/product changes |
| `data.data_use_profiles` | Q02 | provider authoritative terms/contract | one promotable receipt per required profile | rights/terms/use changes |
| `data.fallback_groups` | Q02 | provider/data architecture evidence | compatibility evidence | fallback semantics change |
| `data.freshness_profiles` | Q02 + internal market-data contract | rights/provider behavior + design | profile-specific freshness capability | provider/timing changes |
| `data.entitlement_model` | Q02 | provider terms/contract | entitlement obligations | user classification/product changes |
| `data.attribution_requirements` | Q02 | provider terms/contract | attribution obligations | provider terms change |
| `data.data_rights_receipt_refs` | Q02 | external authoritative evidence | final receipts | any receipt superseded |

Unknown rights are denied. Provider substitution is not allowed merely because schemas look similar.

---

## Quant fields

| Bootstrap field | Producer | Authority | Required evidence | Reopens when |
|---|---|---|---|---|
| `quant.baseline_receipt_ref` | Q04-A | reproducible empirical evidence | all mandatory harness gates pass | dataset/accounting semantics change |
| `dataset_manifest_ref` | Q04-A | reproducible empirical evidence | point-in-time dataset manifest | data/profile changes |
| `transaction_cost_model_version` | Q04-A | empirical/model contract | frozen cost model | execution/data universe changes |
| `benchmark_versions` | Q04-A | empirical/model contract | frozen benchmark ladder | comparator semantics change |
| `primary_metrics` | Q04-A/Q04-B | preregistered method | frozen metric definitions | research question changes |
| `ml_scope` | Q04-B | empirical evidence | `INCLUDE`, `EXCLUDE`, or `DEFER` | later evidence explicitly reopens ML |
| `ml_receipt_ref` | Q04-B | empirical evidence | required only if promoted/decision receipt exists | model family/authority changes |

Q04 cannot authorize performance marketing claims.

---

## Risk fields

| Bootstrap field | Producer | Authority | Required evidence | Reopens when |
|---|---|---|---|---|
| `risk.risk_policy_version` | closed internal risk contract + selected evidence profile | design | exact frozen policy version | limits/authority semantics change |
| `portfolio_context_scope` | Q01 + Q03 + internal product contract | external legal + user evidence + design | allowed personalization scope | portfolio usage semantics change |
| `stale_data_behavior` | internal market-data/risk contracts | design | closed contract version | authoritative behavior changes |
| `no_conclusion_policy` | internal risk/domain contracts | design | closed contract version | decision authority changes |

No model or evidence receipt may bypass risk policy.

---

## Moat fields

| Bootstrap field | Producer | Authority | Required evidence | Reopens when |
|---|---|---|---|---|
| `moat.moat_receipt_ref` | Q05 | empirical/competitive evidence | final Q05 receipt | competitor/product state materially changes |
| `moat.status` | Q05 | empirical/competitive evidence | `SUPPORTED` or `LEARNING_WEDGE` mapping | Q05 superseded |
| `supported_components` | Q05 | empirical evidence | comparative + repeat-use evidence | component evidence changes |
| `unsupported_components` | Q05 | empirical evidence | preserved negative evidence | new validated evidence |
| `scale_spend_constraint` | Q05 | strategy governance | conditional closure constraints | durability evidence strengthens/weakens |

---

## Operations fields

| Bootstrap field | Producer | Authority | Required evidence |
|---|---|---|---|
| `operations.implementation_sequence_version` | closed implementation contract | design | canonical version |
| `acceptance_receipt_contract_version` | closed verification contract | design | canonical version |
| `initial_environment_profile` | promotion architecture-impact review | design + evidence-derived selection | exact environment profile |

Operational acceptance results are post-build receipts and do not belong to MK0 evidence truth.

---

## Provenance fields

| Bootstrap field | Producer | Authority | Required evidence |
|---|---|---|---|
| `provenance.mk0_promotion_packet_ref` | Promotion Packet | governance | approved packet |
| `source_digests` | receipts/packet | immutable provenance | complete digest set |
| `adr_set_digest` | repository | governance | accepted ADR set digest |
| `canonical_doc_digests` | repository | governance | exact promotion commit docs |

---

## Q03 geography constraint

The initial MK1 jurisdiction is Peru. Therefore Q03 must either:

1. include a pre-registered Peru primary cohort large enough to support the promoted persona/wedge; or
2. explicitly classify non-Peru evidence as exploratory/supportive and run a Peru confirmation gate before promotion.

A LATAM/global pooled result cannot silently become Peru product truth.

---

## Q05 denominator constraint

Component adoption/linkage metrics must use **eligible exposed repeat users** as the denominator when progressive disclosure or feature assignment means not every repeat user could encounter the component.

Required denominator metadata:
- component eligibility rule;
- exposure event/rule;
- eligible-exposed repeat-user count;
- adoption numerator;
- longitudinal-use numerator;
- independent-return-reason numerator.

A component cannot fail or pass because users were counted who had no opportunity to use it.

---

## Terminal-state constraint

Evidence lifecycle terminal decisions are exactly:
- `CLOSED_PASS`
- `CLOSED_CONDITIONAL`
- `PIVOT_REQUIRED`
- `STOP_CURRENT_CONFIGURATION`
- `INCONCLUSIVE`

Only `CLOSED_PASS` and appropriately constrained `CLOSED_CONDITIONAL` are promotable.

`INCONCLUSIVE` is never auto-promoted, never silently converted to conditional, and never treated as evidence against the hypothesis unless the preregistration explicitly defines that interpretation.

---

## Promotion invariant

Before `MK0_PROMOTION_PACKET = APPROVED`, every required bootstrap field must be:
- populated;
- traceable to the producer above;
- backed by a final promotable receipt or closed internal contract;
- free of unresolved P0/P1 contradictions;
- valid for the same product version, geography, data profile and asset universe.

If any field fails those conditions, the bootstrap profile remains `DRAFT` or `CANDIDATE` and production MK1 remains blocked.
