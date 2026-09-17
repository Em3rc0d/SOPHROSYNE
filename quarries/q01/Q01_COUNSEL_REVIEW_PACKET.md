# Q01 Counsel Review Packet — Peru Regulatory Boundary

## Status

`OPEN / EXTERNAL_AUTHORITY_REQUIRED / FATAL_IF_FAILED`

This packet prepares the evidence bundle for qualified Peruvian securities counsel. It is **not** legal advice and cannot close Q01 internally.

Canonical authorities:
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`;
- `docs/regulatory/REGULATORY_BOUNDARY.md`;
- `docs/mvp/MK1_SPEC.md`;
- `docs/product/PRODUCT_THESIS.md`;
- `contracts/validation_graph.yaml`.

---

## 1. Review identity

```yaml
review_id: Q01-PERU-MK1-LEGAL-V1
status: DRAFT
jurisdiction: Peru
owner: Em3rc0d
qualified_counsel: TBD
internal_reviewers:
  - product
  - architecture
review_started_at: null
review_completed_at: null
reviewed_bundle_digest: null
supersedes: null
```

## 2. Exact question for counsel

Can the exact frozen MK1 product flows, copy, personalization level, portfolio context and commercial model operate under the intended **non-custodial financial decision-intelligence / research-support posture** in Peru without requiring a regulatory posture the project is unwilling or unable to assume?

Counsel must classify the actual interaction semantics, not merely the product label chosen by SOPHROSYNE.

## 3. Frozen review bundle

Before submission, attach/version the exact user-facing representations of:

1. onboarding and eligibility flow;
2. user profile and preference inputs;
3. manual/read-only portfolio-context inputs;
4. Market Translator;
5. Evidence View and opposing evidence;
6. scenario/invalidation/uncertainty cards;
7. alerts/notifications and their wording;
8. Strategy Sandbox rule-authoring flow;
9. historical/backtest/paper-validation flow;
10. Decision Ledger / historical records;
11. pricing/subscription page;
12. marketing/landing-page claims;
13. disclaimers, terms and educational copy;
14. any planned connector/import language exposed in MK1;
15. examples of `NO_CONCLUSION`, `NOT_EVALUABLE` and degraded-data states.

Where interaction semantics matter, text descriptions alone are insufficient. Use screenshots or a clickable prototype and record its digest/version.

## 4. Required classification matrix

For each reviewed flow, counsel should record whether it is best treated as or materially risks becoming:

```text
generalized information / research
educational content
descriptive analytics
personalized recommendation or advice
investment advisory activity
intermediation / brokerage-like activity
discretionary management or execution
solicitation / distribution / promotion issue
another regulated or restricted financial activity
outside scope / requires separate specialist review
```

Ambiguity must be recorded as a condition or unresolved issue, never treated as clearance.

## 5. Required legal questions

Counsel review should explicitly answer:

### Interaction semantics
- Which user inputs, if any, can cause a descriptive flow to become a personalized recommendation/advisory flow?
- Does manual/read-only portfolio context change classification?
- Does ranking, prioritizing or suppressing instruments based on user circumstances change classification?
- Which alert semantics are acceptable and which cross into actionable recommendation?
- Does a user-authored deterministic rule that reports `TRIGGERED / NOT_TRIGGERED / NOT_EVALUABLE` create a different posture than system-authored advice?
- Are historical/backtest/paper-validation surfaces permissible under the intended posture and with what copy constraints?

### Product authority
- Which forms of phrasing such as “buy”, “sell”, “best”, “recommended”, “safe”, “should”, probability/confidence or personalized suitability language must be prohibited or constrained?
- Are there specific requirements for uncertainty, risk, source attribution or disclaimers?
- Does an LLM explanation layer change classification if it is restricted to explaining finalized structured evidence and cannot create trading authority?

### Commercial model
- Does subscription pricing, premium access, alerts or feature gating materially affect the legal characterization?
- Are there restrictions on marketing claims, testimonials, performance claims or comparative claims?
- Are there consumer-protection or disclosure obligations that must become product requirements?

### Boundary conditions
- What exact features would require a new legal review before shipping?
- What changes would require licensing/registration, a regulated partner or another operating model?
- Are there cross-border limitations relevant to users located outside Peru even if the initial promotable geography is Peru?

## 6. Required counsel deliverables

A Q01 closure candidate requires a written artifact that includes:

- counsel identity/qualification and engagement scope;
- laws/regulations/guidance relied on and date of review;
- exact product/prototype bundle reviewed by version/digest;
- flow-by-flow classification;
- approved interaction classes;
- forbidden interaction classes;
- mandatory constraints;
- approved/forbidden claim lexicon or redlines;
- required disclosures/disclaimers/terms changes;
- unresolved ambiguity requiring further work;
- explicit triggers that reopen the review;
- final scoped conclusion.

An email or meeting summary may support the record but cannot substitute for a sufficiently specific written review if it does not address the exact flows.

## 7. Decision mapping

### `CLOSED_PASS`
Written review supports the exact frozen MK1 flow under the intended posture without material redesign.

### `CLOSED_CONDITIONAL`
The configuration may proceed only with explicit restrictions. Every condition becomes a frozen MK1 requirement and regression obligation.

### `PIVOT_REQUIRED`
A central interaction model must materially change, but a narrower product configuration remains viable.

### `STOP_CURRENT_CONFIGURATION`
The proposed configuration requires a regulatory posture the project is not prepared to assume.

### `INCONCLUSIVE`
Counsel cannot reach a sufficiently scoped conclusion from the submitted materials or specialist questions remain unresolved. This state is not promotable.

## 8. Frozen outputs on closure

A PASS/CONDITIONAL receipt must freeze:

```yaml
RegulatoryFlowProfile_version:
approved_interaction_classes: []
forbidden_interaction_classes: []
required_copy_constraints: []
required_disclosures: []
required_terms_constraints: []
reviewed_prototype_digest:
legal_opinion_ref:
legal_opinion_digest:
jurisdiction: Peru
reopen_triggers: []
```

These values flow into `MK1_BOOTSTRAP_PROFILE` and acceptance/regression requirements.

## 9. Reopen triggers

Q01 reopens for affected scope when a material change occurs in:
- personalization or recommendation semantics;
- portfolio-context use;
- alert semantics;
- strategy rule authorship/authority;
- execution/connectivity posture;
- pricing/commercial model where legally relevant;
- user-visible claims/disclaimers;
- target jurisdiction;
- material law/regulatory guidance;
- the exact interaction surface reviewed by counsel.

## 10. Non-bypass invariant

Internal product confidence, a prototype, user demand, successful engineering, disclaimers written without counsel or absence of enforcement are **not** substitutes for the required external authority.

Q01 remains `OPEN` until qualified counsel produces an adequately scoped written review and the resulting constraints have been reconciled with the rest of Q00–Q05.
