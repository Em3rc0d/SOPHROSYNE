# MK0 Evidence Closure Protocol

## Purpose

This is the canonical evidence-governance contract for closing Q01–Q05 before production MK1 implementation. It distinguishes design truth, evidence truth, and implementation truth. A prototype, contract, backtest, interview, or code change cannot substitute for the evidence class it does not represent.

## Canonical status vocabularies

### Lock registry
`OPEN | PARTIAL | CLOSED`

### Evidence lifecycle
`OPEN -> PRE_REGISTERED -> EVIDENCE_RUNNING -> REVIEW_READY -> FINAL`

### Final evidence decision
`CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE`

`INCONCLUSIVE` is a first-class final decision for a completed but non-decisive evidence attempt. It never promotes a configuration. A new or superseding evidence attempt is required.

### Receipt artifact state
`DRAFT | REVIEW_READY | FINAL | SUPERSEDED`

Artifact state and evidence decision are different fields and must never be collapsed.

## Final-decision semantics

- **CLOSED_PASS** — the exact scoped claim is supported strongly enough for promotion.
- **CLOSED_CONDITIONAL** — promotion is allowed only with explicit, testable constraints that are frozen into canonical docs and the bootstrap profile.
- **PIVOT_REQUIRED** — the current configuration is unsupported, but a materially different candidate remains plausible.
- **STOP_CURRENT_CONFIGURATION** — the exact proposed configuration must not proceed.
- **INCONCLUSIVE** — evidence is insufficient, invalid, underpowered, ambiguous, or not authoritative enough to decide.

No final decision may be inferred from implementation effort, sunk cost, stakeholder preference, or absence of contrary evidence.

## EvidenceReceipt contract

Every final Q decision has an immutable `EvidenceReceipt` containing at least:

```yaml
receipt_id:
lock_id: Q01 | Q02 | Q03 | Q04 | Q05
lock_version:
receipt_state: DRAFT | REVIEW_READY | FINAL | SUPERSEDED
final_decision: CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE | null
question:
scope:
pre_registration_or_review_ref:
pre_registration_digest:
authority_or_source:
started_at:
completed_at:
owner:
independent_reviewer:
sample_or_dataset:
inclusion_exclusion_rules:
primary_measures:
secondary_measures:
decision_rule:
raw_artifact_refs:
analysis_artifact_refs:
results:
limitations:
adverse_or_conflicting_evidence:
frozen_outputs:
canonical_docs_updated:
contradiction_ids:
supersedes:
```

A finalized receipt is immutable. Corrections create a superseding receipt. Negative and inconclusive evidence is retained.

## Authority matrix

| Lock | Required authority | Internal review | Self-certification |
|---|---|---|---|
| Q01 legal/commercial boundary | qualified external reviewer for each applicable legal domain; securities classification must use qualified Peruvian securities counsel | product + architecture | No |
| Q02 market-data rights | provider contract/terms/quote or written provider confirmation | data architecture + product | No where rights are not explicit |
| Q03 user value/WTP/repeat use | observed behavior under pre-registered experiments | product research | Measurement only |
| Q04 quant/ML | reproducible experiment corpus + independent rerun | quant | No single-run certification |
| Q05 moat/durability | observed comparative/repeat-use evidence + competitor evidence | product strategy | No claim from interviews alone |

Silence, ambiguity, missing authority, or undocumented assumptions are never favorable evidence.

# Q01 — Peru legal and commercial boundary

## Question

Can the exact proposed MK1 product, copy, personalization level, data/portfolio-context handling, pricing and commercial activation operate under the intended non-custodial decision-support posture in Peru without assuming a regulatory or commercial posture that SOPHROSYNE has not approved?

## Required flow review

Freeze and review the exact MK1 flow/copy/prototype digest covering onboarding, portfolio context, Market Translator, Evidence View, scenarios, alerts, Strategy Sandbox, paper validation, pricing, marketing claims, disclaimers/terms and connector language.

### Securities/advisory classification
Qualified Peruvian securities counsel must address, for each material flow, whether it is generalized information, personalized recommendation, advisory activity, intermediation, discretionary activity, solicitation/distribution, or another relevant category; plus prohibited/required wording and constraints.

### Non-securities applicability matrix
Q01 also records whether the following domains are `NOT_APPLICABLE`, `EXTERNAL_REVIEW_REQUIRED`, `CLEARED`, or `CLEARED_WITH_CONDITIONS` for the proposed commercial activation:
- personal-data/privacy handling, including portfolio context and telemetry;
- consumer/e-commerce/subscription terms, cancellation/refund where applicable;
- marketing/advertising/performance claims;
- payment/merchant, invoicing/fiscal operational requirements where applicable;
- electronic contracting, consent and terms acceptance.

A securities lawyer may flag another domain but does not automatically become the authority for that domain. Appropriate external expertise is required where the applicability matrix says review is required. This is part of Q01, not a hidden sixth gate.

## Decisions

- `CLOSED_PASS`: all applicable legal/commercial domains for the exact frozen scope are cleared without material redesign.
- `CLOSED_CONDITIONAL`: explicit constraints permit promotion; every condition is frozen into product/copy/configuration and regression checks.
- `PIVOT_REQUIRED`: a central flow/commercial posture must materially change.
- `STOP_CURRENT_CONFIGURATION`: the configuration requires a posture the project will not assume.
- `INCONCLUSIVE`: required authority, scope, or answer remains unavailable/ambiguous.

## Frozen outputs

```yaml
regulatory_flow_profile:
jurisdiction: Peru
approved_interaction_classes:
forbidden_interaction_classes:
required_copy_constraints:
required_disclaimers:
legal_copy_version:
portfolio_context_scope:
commercial_activation_constraints:
non_securities_applicability_refs:
reviewed_prototype_digest:
external_authority_refs:
```

Any material change in personalization, recommendation semantics, copy/claims, portfolio-context scope or commercial activation reopens Q01 for the affected scope.

# Q02 — Production market-data rights

Q02 closes only exact `DataUseProfile`s, never a provider globally. Each profile freezes provider/product, instrument family, asset universe, historical/realtime/delay, user class/geography, storage/cache/display/non-display/redistribution/derived/model use, retention, attribution, costs, fallback compatibility and provider semantics.

Unknown rights default to denied.

- `CLOSED_PASS`: every mandatory use is explicitly authorized and economically compatible.
- `CLOSED_CONDITIONAL`: only with executable rights/entitlement/attribution/cache/geography constraints.
- `PIVOT_REQUIRED`: select another provider/profile or narrower/derived-only surface.
- `STOP_CURRENT_CONFIGURATION`: no viable rights/economic profile supports mandatory MK1 data needs.
- `INCONCLUSIVE`: required authoritative terms, contract, quote, or clarification is missing/ambiguous.

Frozen outputs include provider set, exact asset universe/data families, `DataRightsRecord` refs, `ProviderSemanticsProfile` refs, freshness profiles, entitlement assumptions, costs, retention/cache limits, attribution, fallback groups and rights recheck triggers.

# Q03 — User value, repeat use and willingness to pay

The current numeric preregistration in `experiments/q03/Q03_PREREGISTRATION.md` is authoritative for Q03 thresholds. Earlier narrative sample suggestions do not override it.

Q03 requires observed behavioral evidence for problem intensity, comprehension/workflow value, repeat use and commercially plausible pricing commitment. Statements or survey enthusiasm alone cannot close Q03.

For MK1 promotion the primary evidence geography is Peru and primary study language is Spanish unless a future bootstrap explicitly changes jurisdiction and reopens affected Q01/Q03/Q05 scope. Other cohorts are exploratory unless separately pre-registered for promotion.

A final aggregate Q03 EvidenceReceipt references E03-A/B/C/D and any diagnostic E03-E receipts.

Frozen outputs include persona/JTBD/wedge, required trust features, primary promotion geography/language, pricing surface/version, initial price hypothesis, and supported/rejected workflow constraints.

# Q04 — Deterministic harness and optional ML

Q04-A validates research mechanics, not profitability. Q04-B is optional and may end with `ml_scope: INCLUDE | EXCLUDE | DEFER`.

The detailed preregistration in `experiments/q04/Q04_PREREGISTRATION.md` is authoritative for gates. ML can be excluded or deferred while Q04 closes successfully if the deterministic harness is valid and MK1 has no ML runtime dependency.

An aggregate Q04 EvidenceReceipt must state production-semantics compatibility between the research profile and selected Q02 production profiles for any quant surface promoted into MK1.

`INCONCLUSIVE` applies when required data/profile/reproduction/validity evidence is insufficient without itself proving infeasibility.

# Q05 — Competitive durability

The detailed preregistration in `experiments/q05/Q05_PREREGISTRATION.md` is authoritative. A moat is not established by code complexity, interface preference, or one-session praise.

Q05 requires comparative evidence, repeat-use linkage using exposure-correct denominators, and a defensibility mechanism deeper than surface UI. `LEARNING_WEDGE` is a valid conditional outcome with scale/claim constraints. `INCONCLUSIVE` applies when sample, exposure denominator, or mixed evidence cannot support a defined region.

# Cross-receipt contradictions

Every material cross-Q conflict is recorded under `docs/validation/CONTRADICTION_LOG_TEMPLATE.md`.

- P0/P1 items must be `RESOLVED` or `SUPERSEDED` by a resolved successor before promotion.
- `ACCEPTED_LIMITATION` is permitted only for P2/P3.
- Severity cannot be silently downgraded.
- A positive receipt cannot override another authority by majority vote.

# Promotion

Production MK1 is authorized only when:
1. Q01–Q05 aggregate decisions are each `CLOSED_PASS` or `CLOSED_CONDITIONAL` for the same compatible candidate configuration;
2. no required Q is `INCONCLUSIVE`, `PIVOT_REQUIRED`, or `STOP_CURRENT_CONFIGURATION`;
3. all material conditions are promoted into canonical docs;
4. unit economics are synchronized from Q02/Q03 and verified operational assumptions;
5. no P0/P1 contradiction remains unresolved;
6. `MK0_PROMOTION_PACKET` is approved;
7. one immutable evidence-derived `MK1_BOOTSTRAP_PROFILE` is approved;
8. `BUILD_READINESS` passes.

Evidence authorizes one exact configuration, never a generic permission to build.
