# Q01 Regulatory Review Packet — Peru

## Purpose

This packet is the exact artifact bundle to send to qualified Peruvian securities counsel for Q01.

It does **not** contain a legal conclusion. Every legal-classification field remains `PENDING` until counsel reviews the frozen product flows/copy represented by this packet.

Canonical policy: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.

---

## 1. Review identity

```yaml
review_id: Q01-LEGAL-<version>
status: DRAFT | FROZEN_FOR_COUNSEL | COUNSEL_REVIEWING | REVIEW_READY | FINAL | SUPERSEDED
jurisdiction: Peru
product_version:
prototype_or_flow_digest:
marketing_copy_digest:
terms_disclaimer_digest:
pricing_surface_digest:
created_at:
frozen_at:
counsel_or_firm_ref:
internal_owner:
supersedes:
```

Counsel reviews an exact frozen representation. Material UX/copy changes require a new version or explicit supplemental review.

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
- no LLM authority over orders, risk limits or probabilities.

If the actual prototype differs from any item above, update this section before counsel review.

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

If a flow does not exist, mark `NOT_IN_CANDIDATE_MK1`; do not leave ambiguity.

---

## 4. Per-flow counsel matrix

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
geo_or_user_eligibility_constraints: []
external_registration_or_license_implication: PENDING
counsel_notes:
authority_refs: []
```

The packet intentionally asks for classifications and constraints; SOPHROSYNE does not answer these fields itself.

---

## 5. Questions counsel must explicitly address

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

Request examples of:
- acceptable contextualization;
- unacceptable recommendation-like personalization;
- wording/features that materially alter classification.

### Q01.3 — Strategy Sandbox

Does allowing users to define deterministic rules, backtest them and observe paper-only strategy state create different obligations than merely showing market information?

What changes if the platform supplies templates versus user-authored rules?

### Q01.4 — Alerts

What distinctions matter between:
- factual data alert;
- rule-trigger alert;
- scenario-change alert;
- instrument-specific action-oriented alert;
- personalized ranking alert?

### Q01.5 — Portfolio context

What constraints apply if users manually enter positions or connect a read-only account in a future MK?

Does risk/concentration analytics based on those positions alter legal characterization?

### Q01.6 — Performance / backtest / model claims

What disclosures or restrictions are required when presenting:
- historical strategy results;
- paper-validation results;
- benchmark comparisons;
- calibrated probabilities;
- model performance statistics?

What language must be avoided?

### Q01.7 — LLM explanation

Does plain-language explanation of already-computed structured outputs introduce different risk if the LLM remains non-authoritative?

What disclaimers/controls should be visible or contractual?

### Q01.8 — Marketing and pricing

Which product claims, landing-page statements, subscription descriptions or “AI/quant” wording could imply a regulated service beyond the intended posture?

Does subscription pricing versus another compensation model matter to the reviewed posture?

### Q01.9 — Terms / disclaimers

Which disclaimers are required, and which limitations cannot be cured merely with a disclaimer?

### Q01.10 — Future expansion triggers

Which future changes must automatically trigger fresh legal review, including potentially:
- broker/exchange connectivity;
- personalized recommendations;
- automated execution;
- copy trading;
- custody;
- options/futures/leverage workflows;
- B2B white-label/API distribution;
- other jurisdictions?

---

## 6. Claim lexicon review

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
- regulated status or approval.

No synonym substitution is allowed after review without checking whether meaning changed.

---

## 7. Decision mapping

Counsel does not need to use SOPHROSYNE status labels, but the internal reviewer maps written findings to one of:

### CLOSED_PASS

Exact candidate MK1 flow may proceed under the intended posture without material redesign.

### CLOSED_CONDITIONAL

Flow may proceed only with explicit constraints. Every condition becomes a frozen product/API/copy requirement.

### PIVOT_REQUIRED

A central interaction must materially change but the thesis can survive under a narrower configuration.

### STOP_CURRENT_CONFIGURATION

The exact candidate configuration would require a regulatory posture the project is not prepared to assume.

`INCONCLUSIVE` is used when counsel cannot give a sufficiently scoped answer from the materials supplied.

---

## 8. Frozen outputs from Q01

A final promotable receipt must output:

```yaml
regulatory_flow_profile_id:
approved_flow_ids: []
conditionally_approved_flow_ids: []
forbidden_flow_ids: []
approved_interaction_classes: []
forbidden_interaction_classes: []
approved_claims_or_patterns: []
forbidden_claims_or_patterns: []
required_disclaimers: []
required_terms_constraints: []
required_recordkeeping_or_consent: []
geo_or_user_eligibility_constraints: []
mandatory_re_review_triggers: []
reviewed_artifact_digests: []
```

These outputs feed `MK1_BOOTSTRAP_PROFILE` and product regression requirements.

---

## 9. Internal consistency check after counsel response

Before Q01 finalization:

- compare counsel constraints against Q03-tested experience;
- compare constraints against pricing/entitlement design;
- compare against `SYSTEM_CONTRACTS.md` and `MK1_SPEC.md`;
- create contradiction records for every material mismatch;
- reopen affected internal nodes only if counsel invalidates a design invariant;
- do not reinterpret counsel silence as approval;
- do not broaden a flow-specific answer to unreviewed features.

---

## Final invariant

> Q01 closes only for the exact product representation counsel actually reviewed.

This packet is a request for qualified external legal review, not legal advice generated by SOPHROSYNE or by its engineering team.
