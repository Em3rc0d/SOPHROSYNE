# Q01 Regulatory Review Packet — Peru

## Purpose

This packet is the exact artifact bundle to send to qualified Peruvian counsel for Q01.

It does **not** contain a legal conclusion. Every legal-classification/compliance field remains `PENDING` until the relevant qualified external authority reviews the frozen product flows/copy represented by this packet.

Canonical policy: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.
Semantic normalization: `docs/validation/CANONICAL_VALIDATION_SPEC.md`.

Q01 is one consolidated launch-law lock. Securities/advisory analysis is mandatory, but Q01 also requires every other legal/commercial surface that actually applies to the candidate MK1 to be either reviewed by a competent specialist or explicitly classified `NOT_APPLICABLE` with rationale. Silence is not approval.

---

## 1. Review identity

```yaml
review_id: Q01-LEGAL-<version>
status: DRAFT | FROZEN_FOR_COUNSEL | COUNSEL_REVIEWING | REVIEW_READY | CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE | SUPERSEDED
jurisdiction: Peru
product_version:
prototype_or_flow_digest:
marketing_copy_digest:
terms_disclaimer_digest:
privacy_notice_digest:
consent_flow_digest:
pricing_surface_digest:
payment_or_checkout_flow_digest:
created_at:
evidence_as_of:
frozen_at:
reviewed_at:
review_by:
internal_owner:
supersedes:
```

Counsel reviews an exact frozen representation. Material UX/copy/commercial-flow changes require a new version or explicit supplemental review.

`INCONCLUSIVE` is a valid outcome where the materials or authority coverage are insufficient; it never promotes.

---

## 2. Product posture presented to counsel

Describe factually, without assuming legal classification:

- non-custodial product;
- no MK1 live autonomous execution;
- no custody of client assets/funds;
- manual/read-only portfolio context candidate;
- market/evidence translation;
- scenarios and uncertainty;
- deterministic user-defined strategy sandbox;
- historical backtesting and paper validation;
- optional validated model outputs only if separately promoted;
- LLM downstream explanation only;
- no LLM authority over orders, risk limits or probabilities;
- consumer-facing subscription may be proposed only if separately reviewed as applicable;
- personal/financial context and research telemetry are processed only within the reviewed privacy/data-protection posture.

If the actual prototype differs from any item above, update this section before external review.

---

## 3. Frozen flow inventory

Each flow gets an immutable ID and artifact digest.

| Flow ID | User-visible flow | Required artifact | Status |
|---|---|---|---|
| F01 | landing / product claims | screenshots + copy | PENDING |
| F02 | onboarding | screenshots/clickable flow | PENDING |
| F03 | user profile / experience context | screenshots + field schema | PENDING |
| F04 | manual/read-only portfolio context | screenshots + field schema | PENDING |
| F05 | Market Translator | screenshots + sample outputs | PENDING |
| F06 | Evidence View | screenshots + provenance behavior | PENDING |
| F07 | scenarios / uncertainty / invalidation | screenshots + output schema | PENDING |
| F08 | alerts / notifications | examples + trigger semantics | PENDING |
| F09 | Strategy Sandbox | screens + rule semantics | PENDING |
| F10 | backtest output | screens + claims/copy | PENDING |
| F11 | paper-validation output | screens + claims/copy | PENDING |
| F12 | optional probability/model output | screens/schema if in candidate MK1 | PENDING |
| F13 | pricing / entitlements | screens + feature matrix | PENDING |
| F14 | disclaimers / terms / consent | full copy | PENDING |
| F15 | educational/help content | representative copy | PENDING |
| F16 | future connector language visible in MK1 | screens/copy if any | PENDING |
| F17 | privacy notice / data-subject controls | notice + data-flow map + rights UX | PENDING |
| F18 | subscription / checkout / cancellation | screens + terms + payment flow | PENDING |
| F19 | research telemetry / analytics consent | event schema + retention + consent/notice | PENDING |
| F20 | support / complaints / refund handling | policy + user-facing flow | PENDING |

If a flow does not exist, mark `NOT_IN_CANDIDATE_MK1`; do not leave ambiguity.

---

## 4. External authority coverage matrix

Every applicable row must have an identified authority/reviewer. One lawyer/firm may cover multiple rows, but competence is not assumed merely because securities advice is covered.

| Surface | Required disposition | External authority/ref |
|---|---|---|
| securities / investment-advice / recommendation / intermediation posture | REVIEWED or NOT_APPLICABLE | PENDING |
| marketing / financial-product claims | REVIEWED or NOT_APPLICABLE | PENDING |
| privacy / personal-data processing | REVIEWED or NOT_APPLICABLE | PENDING |
| portfolio/financial-context handling | REVIEWED or NOT_APPLICABLE | PENDING |
| consumer / e-commerce / subscription terms | REVIEWED or NOT_APPLICABLE | PENDING |
| payments / billing / refunds / cancellation | REVIEWED or NOT_APPLICABLE | PENDING |
| consent / notice / recordkeeping | REVIEWED or NOT_APPLICABLE | PENDING |
| age / geography / user eligibility | REVIEWED or NOT_APPLICABLE | PENDING |
| cross-border vendors/data transfer where applicable | REVIEWED or NOT_APPLICABLE | PENDING |
| complaint/support obligations where applicable | REVIEWED or NOT_APPLICABLE | PENDING |

A row may be `NOT_APPLICABLE` only with an explicit rationale tied to the frozen candidate configuration.

Before any real charge, the exact subscription/checkout/payment flow must have the required authority coverage. Research-only fake-door pricing does not itself authorize charging.

---

## 5. Per-flow counsel matrix

Counsel should answer each applicable row for each flow ID.

```yaml
flow_id:
legal_classification_assessment:
  generalized_information: PENDING
  personalized_recommendation_risk: PENDING
  investment_advice_or_equivalent_risk: PENDING
  intermediation_risk: PENDING
  discretionary_activity_risk: PENDING
  solicitation_or_distribution_risk: PENDING
  consumer_or_subscription_risk: PENDING
  personal_data_or_privacy_risk: PENDING
  other_relevant_classification: PENDING

permitted_as_presented: PENDING
permit_conditions: []
prohibited_behaviors_or_wording: []
required_wording_or_disclaimers: []
user_suitability_or_profile_requirements: []
recordkeeping_requirements: []
consent_or_disclosure_requirements: []
marketing_constraints: []
pricing_or_compensation_constraints: []
payment_subscription_constraints: []
privacy_data_constraints: []
geo_or_user_eligibility_constraints: []
external_registration_or_license_implication: PENDING
counsel_notes:
authority_refs: []
```

The packet intentionally asks for classifications and constraints; SOPHROSYNE does not answer these fields itself.

---

## 6. Questions external counsel/reviewers must explicitly address

### Q01.1 — Information vs recommendation boundary

For F05–F12, which combinations of:
- user portfolio context;
- user-stated goals/preferences;
- instrument-specific output;
- ranked/scored opportunities;
- action-oriented wording;
- alerts;
- model probabilities;

materially change the legal characterization of the flow?

### Q01.2 — Personalization

Which user inputs may be used to contextualize information without crossing into a different regulated posture, if any?

Request examples of acceptable contextualization, unacceptable recommendation-like personalization and wording/features that materially alter classification.

### Q01.3 — Strategy Sandbox

Does allowing users to define deterministic rules, backtest them and observe paper-only strategy state create different obligations than merely showing market information? What changes if templates are platform-supplied versus user-authored?

### Q01.4 — Alerts

What distinctions matter between factual data alerts, rule-trigger alerts, scenario-change alerts, instrument-specific action-oriented alerts and personalized ranking alerts?

### Q01.5 — Portfolio context

What constraints apply if users manually enter positions or connect a read-only account in a future MK? Does risk/concentration analytics based on those positions alter legal characterization or privacy obligations?

### Q01.6 — Performance / backtest / model claims

What disclosures or restrictions are required when presenting historical strategy results, paper-validation results, benchmark comparisons, calibrated probabilities and model performance statistics? What language must be avoided?

### Q01.7 — LLM explanation

Does plain-language explanation of already-computed structured outputs introduce different risk if the LLM remains non-authoritative? What disclosures/controls should be visible or contractual?

### Q01.8 — Marketing and pricing

Which product claims, landing-page statements, subscription descriptions or “AI/quant” wording could imply a regulated service beyond the intended posture? Does compensation/subscription structure affect classification?

### Q01.9 — Terms / disclaimers

Which disclaimers are required, and which limitations cannot be cured merely with a disclaimer?

### Q01.10 — Privacy / personal-data processing

For F03/F04/F17/F19 and any relevant system telemetry, determine the applicable requirements for:
- lawful basis/consent/notice;
- purpose limitation;
- retention/deletion;
- data-subject access/correction/deletion/portability where applicable;
- sensitive/financial-context handling;
- processor/vendor obligations;
- cross-border transfers;
- incident/breach handling;
- analytics/research reuse;
- minors/age eligibility if applicable to launch.

The review should identify which exact categories the candidate MK1 is allowed to collect and which are unnecessary/prohibited.

### Q01.11 — Consumer / e-commerce / subscription

For F13/F18/F20, identify applicable requirements around:
- pre-contract information;
- price/tax/renewal disclosure;
- cancellation;
- refund policy;
- recurring subscription consent;
- complaints/support;
- misleading or unfair commercial practices;
- free trial/fake-door/paid-pilot wording where applicable.

### Q01.12 — Payments / billing

If a real paid pilot or subscription is activated, identify requirements affecting checkout, payment processor use, receipts/invoicing, billing descriptors, refunds/chargebacks and data minimization around payment information.

SOPHROSYNE should not store raw card data merely to implement subscriptions.

### Q01.13 — Research pricing before commercial launch

Confirm whether non-deceptive fake-door/high-friction commitment testing that does not execute a charge is permissible under the reviewed research design and what disclosure/consent wording is required.

### Q01.14 — Future expansion triggers

Which future changes automatically trigger fresh legal review, including broker/exchange connectivity, personalized recommendations, automated execution, copy trading, custody, options/futures/leverage, B2B white-label/API distribution, materially different AI agent behavior or new jurisdictions?

---

## 7. Claim lexicon review

Counsel receives the exact user-facing lexicon and classifies each candidate phrase.

```yaml
claim:
context:
status: PENDING  # ALLOWED | ALLOWED_WITH_CONDITION | PROHIBITED | NEEDS_CONTEXT
required_revision:
rationale:
authority_ref:
```

Include at minimum all words/phrases that could imply:
- recommendation;
- prediction;
- personalized suitability;
- guaranteed or expected return;
- automated investing;
- advisory relationship;
- regulated status or approval;
- safety/low-risk outcomes;
- superiority or accuracy unsupported by evidence;
- misleading free/paid/subscription terms.

No synonym substitution is allowed after review without checking whether meaning changed.

---

## 8. Decision mapping

External reviewers do not need to use SOPHROSYNE status labels, but the internal reviewer maps the complete authority bundle to exactly one aggregate outcome:

### CLOSED_PASS

Exact candidate MK1 flow may proceed under the intended posture without material redesign, and every applicable legal/commercial surface has an authoritative disposition.

### CLOSED_CONDITIONAL

Flow may proceed only with explicit constraints. Every condition becomes a frozen product/API/copy/privacy/payment requirement.

### PIVOT_REQUIRED

A central interaction or commercial/legal posture must materially change but the thesis can survive under a narrower configuration.

### STOP_CURRENT_CONFIGURATION

The exact candidate configuration would require a regulatory/commercial posture the project is not prepared to assume.

### INCONCLUSIVE

Authority coverage is incomplete, qualified reviewers cannot reach a sufficiently scoped conclusion, or materials supplied are insufficient. This never promotes.

---

## 9. Frozen outputs from Q01

A final promotable receipt must output:

```yaml
regulatory_flow_profile_id:
jurisdiction: Peru
approved_flow_ids: []
conditionally_approved_flow_ids: []
forbidden_flow_ids: []
approved_interaction_classes: []
forbidden_interaction_classes: []
approved_claims_or_patterns: []
forbidden_claims_or_patterns: []
required_disclaimers: []
required_terms_constraints: []
required_privacy_constraints: []
required_payment_subscription_constraints: []
required_recordkeeping_or_consent: []
geo_or_user_eligibility_constraints: []
mandatory_re_review_triggers: []
external_authority_coverage: []
reviewed_artifact_digests: []
evidence_as_of:
review_by:
```

These outputs feed `MK1_BOOTSTRAP_PROFILE` and product regression requirements.

---

## 10. Internal consistency check after external responses

Before Q01 finalization:

- verify every applicable authority-coverage row is resolved;
- compare external constraints against Q03-tested experience;
- compare constraints against pricing/entitlement design;
- compare constraints against data/telemetry handling and Q02;
- compare against `SYSTEM_CONTRACTS.md` and `MK1_SPEC.md`;
- create contradiction records for every material mismatch;
- reopen affected internal nodes only if external authority invalidates a design invariant;
- do not reinterpret silence as approval;
- do not broaden a flow-specific answer to unreviewed features;
- ensure the exact paid flow remains disabled until its relevant reviews are promotable.

---

## 11. Mandatory re-review triggers

At minimum re-review the affected scope when:
- recommendation/personalization semantics materially change;
- portfolio-context data use expands;
- claims, alerts or probability presentation materially change;
- privacy/data categories, purposes, retention or vendors materially change;
- paid/subscription/payment flow materially changes;
- age/geography eligibility changes;
- live connectivity/execution/custody/copy trading/leverage/derivatives are introduced;
- B2B/API distribution creates a materially different posture;
- a new jurisdiction is targeted;
- applicable law/regulatory interpretation or counsel assumptions materially change.

---

## Final invariant

> Q01 closes only for the exact product, legal/commercial surface and authority coverage actually reviewed.

This packet is a request for qualified external legal/compliance review, not legal advice generated by SOPHROSYNE or by its engineering team.
