# Q01 External Legal / Commercial Review Packet — Peru

## Purpose

This packet presents the exact proposed MK1 flows/copy/commercial posture for external review. It does not contain an internal legal conclusion.

## Packet identity

```yaml
packet_id:
packet_version:
packet_status: DRAFT | FROZEN_FOR_REVIEW | REVIEWING | REVIEW_READY | FINAL | SUPERSEDED
jurisdiction: Peru
candidate_configuration_id:
prototype_digest:
copy_bundle_digest:
pricing_surface_version:
portfolio_context_version:
owner:
```

## Reviewer authority

For each reviewed domain record:

```yaml
domain:
reviewer_or_firm:
qualification_or_role:
authority_scope:
review_date:
written_opinion_or_review_ref:
basis_or_authority_refs: []
limitations: []
```

Securities/advisory classification requires qualified Peruvian securities counsel. Other legal domains use appropriately qualified external expertise where required.

## Exact flow inventory

Freeze screenshots/clickable prototype and wording for at least:
- F01 onboarding and eligibility;
- F02 profile/experience context;
- F03 portfolio-context entry/import/manual input;
- F04 Market Translator;
- F05 Evidence View/supporting/opposing evidence;
- F06 scenario/uncertainty/invalidation cards;
- F07 alerts/watchlists;
- F08 Strategy Sandbox;
- F09 paper/backtest validation;
- F10 portfolio analytics/risk context;
- F11 probability/model surfaces if proposed;
- F12 pricing/entitlements;
- F13 marketing/performance claims;
- F14 disclaimers/terms/consent;
- F15 connector/broker/exchange language;
- F16 LLM/explanation behavior.

Text summaries are insufficient where interaction semantics matter.

## Securities/advisory questions

For each material flow, request written classification/constraints around generalized information, personalization/recommendation, advisory activity, intermediation, discretionary activity, solicitation/distribution and any other relevant behavior. Require prohibited/required wording and conditions, not just a yes/no conclusion.

## Non-securities commercial applicability matrix

```yaml
domains:
  personal_data_privacy:
    status: NOT_APPLICABLE | EXTERNAL_REVIEW_REQUIRED | CLEARED | CLEARED_WITH_CONDITIONS
    reviewer_ref:
    constraints: []
  consumer_subscription_ecommerce:
    status:
    reviewer_ref:
    constraints: []
  marketing_advertising_performance_claims:
    status:
    reviewer_ref:
    constraints: []
  payments_merchant_invoicing_fiscal:
    status:
    reviewer_ref:
    constraints: []
  electronic_contracting_consent_terms:
    status:
    reviewer_ref:
    constraints: []
```

A domain marked `EXTERNAL_REVIEW_REQUIRED` blocks only the affected activation until cleared; the promotion packet must explicitly disable that capability if the rest of MK1 is to proceed without it.

## Mandatory questions

Reviewers must address the exact candidate—not an abstract product category—and identify:
- permitted/forbidden interaction classes;
- personalization boundary;
- portfolio-context boundary;
- claim/copy lexicon;
- disclaimer/terms requirements;
- commercial-activation conditions;
- whether pricing/payment/subscription behavior changes the analysis;
- what future changes would require re-review.

## Final decision

```yaml
final_decision: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE
```

`INCONCLUSIVE` is required when an applicable authority answer is missing or ambiguous.

## Frozen outputs

```yaml
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
external_authority_refs: []
```

## Reopen triggers

Material changes to recommendation/personalization semantics, portfolio-context scope, claims, subscription/payment posture, data-personalization use, reviewed UI/copy or jurisdiction reopen the affected Q01 scope.

Final output is an aggregate Q01 EvidenceReceipt using the canonical receipt template.
