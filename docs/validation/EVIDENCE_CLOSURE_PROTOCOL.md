# MK0 Evidence Closure Protocol

## Purpose

The internal MK1 design graph is structurally closed for pre-build. MK0 now advances by closing the remaining **external / empirical** locks without fabricating evidence and without allowing implementation to silently decide product, legal, data-rights, commercial or scientific questions.

This document defines the canonical closure protocol for **Q00–Q05**:

- Q00 — core causal value against simple baselines;
- Q01 — Peru regulatory boundary;
- Q02 — commercial market-data rights;
- Q03 — willingness-to-pay / repeat-use evidence;
- Q04 — deterministic quant baseline / optional ML increment;
- Q05 — moat / competitive durability.

This protocol closes the **method of validation**, not any lock result. A Q remains open until its required evidence exists, survives review and produces an immutable receipt.

Detailed execution authority remains in:

- `experiments/q00/Q00_PREREGISTRATION.md`;
- `quarries/q01/Q01_COUNSEL_REVIEW_PACKET.md`;
- `quarries/q02/Q02_DATA_RIGHTS_REVIEW_PACKET.md`;
- `experiments/q03/Q03_PREREGISTRATION.md`;
- `experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`;
- `experiments/q04/Q04_PREREGISTRATION.md`;
- `experiments/q05/Q05_PREREGISTRATION.md`;
- `docs/validation/CANONICAL_VALIDATION_SPEC.md`;
- `docs/validation/STATISTICAL_DECISION_RULES.md`.

If this protocol conflicts with `CANONICAL_VALIDATION_SPEC.md` on lifecycle vocabulary, aggregate outcomes, geography, evidence authority or promotion eligibility, the canonical validation specification wins.

---

## Governing distinction

SOPHROSYNE keeps three truth classes separate:

1. **Design truth** — internal architecture, contracts and bounded decisions.
2. **Evidence truth** — external facts or empirical results that must be observed, contracted, measured or reviewed.
3. **Implementation truth** — proof that built software conforms to closed design, represented by acceptance receipts.

They must never be collapsed.

```text
closed design
    |
    +--> external / empirical evidence gate
    |        |
    |        +--> CLOSED_PASS
    |        +--> CLOSED_CONDITIONAL
    |        +--> PIVOT_REQUIRED
    |        +--> STOP_CURRENT_CONFIGURATION
    |        +--> INCONCLUSIVE
    |
    +--> implementation
             |
             +--> typed acceptance receipts
```

A successful prototype is not legal clearance. A signed provider contract is not user demand. A strong backtest is not proof of a moat. A passing user study is not proof that production code is secure. A sophisticated downstream experiment cannot rescue a failed causal or fatal upstream gate.

---

## Evidence lifecycle

Every external / empirical lock follows one lifecycle:

```text
OPEN
  -> PRE_REGISTERED
  -> EVIDENCE_RUNNING
  -> REVIEW_READY
  -> CLOSED_PASS
     or CLOSED_CONDITIONAL
     or PIVOT_REQUIRED
     or STOP_CURRENT_CONFIGURATION
     or INCONCLUSIVE
```

### OPEN

The question exists but exact evidence collection is not yet frozen.

### PRE_REGISTERED

Before outcome inspection, freeze as applicable:

- question / hypothesis;
- scope and geography;
- authority required;
- sample or dataset;
- primary and secondary measures;
- decision thresholds / rule;
- inclusion and exclusion criteria;
- analysis plan;
- expected artifacts;
- known confounders;
- version/digest.

A material change after preregistration requires a new version. The prior version remains immutable.

### EVIDENCE_RUNNING

Evidence is being collected. Decision rules cannot be rewritten to rescue the hypothesis.

### REVIEW_READY

Required artifacts exist and can be independently checked.

### CLOSED_PASS

Evidence supports the exact scoped claim strongly enough for promotion.

### CLOSED_CONDITIONAL

Only a constrained configuration may proceed. Every constraint becomes a frozen MK1 requirement and graph/profile restriction.

### PIVOT_REQUIRED

The current configuration is unsupported, but a materially narrower or different configuration remains plausible. Affected canonical docs and graph reachability must change before a replacement evidence version begins.

### STOP_CURRENT_CONFIGURATION

The exact proposed configuration cannot proceed.

### INCONCLUSIVE

Evidence is insufficient, underpowered, corrupted, materially confounded or otherwise unable to support a terminal promotional decision. `INCONCLUSIVE` never auto-promotes.

---

## Evidence receipt contract

Every final evidence decision produces an immutable `EvidenceReceipt` with at least:

```text
receipt_id
lock_id
lock_version
experiment_or_review_id
status
question
scope
pre_registration_ref
pre_registration_digest
started_at
completed_at
owner
independent_reviewer
authority_or_source
sample_or_dataset
inclusion_exclusion_rules
primary_measures
secondary_measures
decision_rule
raw_artifact_refs
analysis_artifact_refs
results
limitations
adverse_or_conflicting_evidence
final_decision
frozen_outputs
canonical_docs_updated
supersedes
```

Finalized receipts are not edited in place. Corrections or new evidence create superseding receipts.

Evidence provenance remains explicit: `OFFICIAL`, `ACADEMIC`, `OBSERVED`, `INFERRED`, `HYPOTHESIS`.

Negative and contradictory evidence is first-class and cannot be omitted because the aggregate decision is favorable.

---

## Authority matrix

| Lock | Required evidence authority | Internal review | Self-certification |
|---|---|---|---|
| Q00 causal value | preregistered comparative/ablation evidence under frozen tasks, baselines and scoring | product research + validation reviewer | no terminal promotion from one unreviewed favorable run |
| Q01 regulatory | qualified Peruvian securities counsel for exact frozen flows/copy | product + architecture | no |
| Q02 data rights | authoritative provider terms/contract/quote or written provider confirmation | data architecture + product | no for rights not explicit in authoritative evidence |
| Q03 WTP/repeat-use | observed target-user behavior + preregistered experiment output | product research reviewer | measurement may be internal; observations may not be invented |
| Q04 quant/ML | reproducible experiment corpus + independent rerun/review | quant reviewer | no single-run promotion |
| Q05 moat | observed preference/repeat use + competitive evidence | product strategy reviewer | interviews alone are insufficient |

Where external authority is required, silence or ambiguity is **not `CLOSED_PASS`**.

---

# Q00 — Core causal value

## Question

Does the full candidate SOPHROSYNE intervention create material incremental decision-process value over simpler and cheaper substitutes under controlled, non-production tasks?

## Required evidence

Follow `experiments/q00/Q00_PREREGISTRATION.md` and preserve destructive comparison against applicable arms:

- raw-information control;
- stateless structured assistance;
- five-question deliberate-friction baseline;
- simple feedback;
- short-memory SOPHROSYNE;
- full candidate SOPHROSYNE;
- strongest realistic cheap/free substitute frozen before outcome inspection.

Required analyses include simple-friction ablation, memory ablation, outcome-blind evaluation, hidden-rubric evaluation, assisted-vs-unassisted transfer, regime/context transfer, dependence correction, cognitive/time-cost comparison, cheap-substitute comparison and the economic bridge to Q03.

The study evaluates decision-process quality, not live investment performance. It does not require real-money trading.

## Decision rules

- `CLOSED_PASS` — material incremental value survives the preregistered baselines and cognitive/time-cost boundary.
- `CLOSED_CONDITIONAL` — only a narrower intervention or subset of components earns support; unsupported complexity is excluded/deferred.
- `PIVOT_REQUIRED` — most value is explained by a materially simpler intervention or different workflow/configuration.
- `STOP_CURRENT_CONFIGURATION` — the current full-product configuration fails to establish meaningful incremental value.
- `INCONCLUSIVE` — sample, instrumentation, independence, validity or evidence quality is insufficient.

Q03 willingness-to-pay, Q04 modeling sophistication and Q05 defensibility **cannot rescue a failed Q00 configuration**.

## Frozen outputs

A promotable receipt freezes:

- validated intervention scope;
- component inclusion/exclusion decisions;
- simple-friction result;
- memory result;
- transfer scope such as `ASSISTED_ONLY` where applicable;
- cognitive/time-cost boundary;
- cheap-substitute result;
- minimum meaningful effect rule/result;
- implications for Q03/Q04/Q05;
- constraints propagated into graph reachability and `MK1_BOOTSTRAP_PROFILE`.

---

# Q01 — Peru regulatory boundary

## Question

Can the exact proposed MK1 flows, copy, personalization level and commercial model operate within the intended non-custodial decision-support posture under applicable Peruvian legal/regulatory constraints?

## Required authority

Follow `quarries/q01/Q01_COUNSEL_REVIEW_PACKET.md`. Qualified counsel must review the exact frozen interaction model and applicable commercial legal surfaces. Text-only descriptions are insufficient where interaction semantics matter.

## Decision rules

- `CLOSED_PASS` — written review permits the exact frozen configuration under the intended posture without material redesign.
- `CLOSED_CONDITIONAL` — only explicit product/copy/legal constraints make the configuration permissible; each becomes a frozen requirement.
- `PIVOT_REQUIRED` — a central flow must materially change, but a narrower product posture remains viable.
- `STOP_CURRENT_CONFIGURATION` — the proposed configuration requires a posture the project is not prepared to assume.
- `INCONCLUSIVE` — required authority, scope coverage or exact-flow review is incomplete or ambiguous.

## Frozen outputs

A promotable receipt freezes the `RegulatoryFlowProfile`, approved/forbidden interaction classes, approved/forbidden claim lexicon, required disclaimers/terms/consent constraints, jurisdiction, eligibility constraints and exact reviewed artifact digest.

A material interaction/copy change that changes recommendation, personalization or regulated semantics reopens the affected scope.

---

# Q02 — Commercial market-data rights

## Question

Can the exact initial production data profile be stored, transformed, displayed, cached and commercially used under documented provider rights and feasible costs?

## Unit of closure

Q02 closes per versioned `DataUseProfile`, never “for a provider in general”. At minimum the profile covers:

```text
provider
provider_product
instrument_family
asset_universe
historical_or_realtime
delay_profile
user_classification
geography
raw_storage
cache_ttl
display
non_display
redistribution
derived_use
model_or_embedding_use
retention
attribution
entitlements
cost_model
termination_or_revocation
fallback_compatibility
```

Unknown rights default to **DENY**.

## Decision rules

- `CLOSED_PASS` — every required use is explicitly allowed and economically compatible with the candidate MK1 profile.
- `CLOSED_CONDITIONAL` — use is allowed only with explicit rights/entitlement/cache/attribution/geography/user-class restrictions that become executable policy.
- `PIVOT_REQUIRED` — the provider/data family is commercially incompatible; choose another provider, derived-only surface or narrower profile.
- `STOP_CURRENT_CONFIGURATION` — no viable provider/profile combination supports the mandatory MK1 data surface within feasible economics/rights constraints.
- `INCONCLUSIVE` — authoritative evidence is missing, contradictory or insufficient for a required use.

Technical API accessibility never proves commercial-use rights.

## Frozen outputs

A promotable receipt freezes provider set, exact asset universe, data families, fallback compatibility groups, `DataRightsRecord` versions, entitlement assumptions, cost assumptions, retention/cache limits and attribution obligations.

Provider contract/terms changes reopen only affected profiles, but any bootstrap depending on them remains blocked until reconciliation completes.

---

# Q03 — User value, repeat use and willingness to pay

## Question

Do target users repeatedly value the Q00-surviving decision-intelligence workflow enough to justify building the MK1 wedge, and is there credible evidence that some will pay at a commercially plausible price?

Execution authority: `experiments/q03/Q03_PREREGISTRATION.md` and `experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`.

Statements alone cannot close Q03. Promotable evidence must include observed workflow/problem evidence, objective comprehension/friction evidence, repeat-use beyond novelty, qualified pricing/commitment evidence and no severe trust failure contradicting the thesis.

## Decision rules

- `CLOSED_PASS` — evidence supports the current promotable persona/wedge and continued B2C MK1 build.
- `CLOSED_CONDITIONAL` — value exists only for a narrower persona/use case/price surface.
- `PIVOT_REQUIRED` — users value a materially different workflow, persona or distribution model.
- `STOP_CURRENT_CONFIGURATION` — repeated evidence shows weak problem intensity, poor repeat use and weak commitment across plausible variants.
- `INCONCLUSIVE` — minimum usable evidence is not reached or primary instrumentation is not promotion-grade.

## Frozen outputs

Primary persona, JTBD, wedge, trust requirements, pricing-hypothesis band, permitted channel hypotheses and experiment corpus/analysis receipt. These outputs may not reintroduce Q00-rejected components.

---

# Q04 — Deterministic quant baseline and optional ML increment

## Question

Can the research harness reproduce transparent deterministic baselines under point-in-time semantics and realistic costs, and does any ML component earn a place beyond those baselines?

Execution authority: `experiments/q04/Q04_PREREGISTRATION.md`.

Q04-A and Q04-B are separate decisions and must not be conflated.

## Q04-A — Baseline harness validity

Required proof includes point-in-time dataset manifest, deterministic rerun, hand-computed accounting/fill fixtures, transparent benchmark ladder, cost-model version, untouched temporal test interval, temporal/walk-forward validation, multiple-testing log and independent reproduction.

A baseline may lose money and still validate the harness. Harness validity is not alpha proof.

Q04-A uses only canonical aggregate outcomes:

- `CLOSED_PASS` — harness and deterministic benchmark corpus are reproducible and leakage controls pass.
- `PIVOT_REQUIRED` — chosen data/asset/research formulation requires a material redesign.
- `STOP_CURRENT_CONFIGURATION` — research semantics cannot be made reproducible or the selected path is unusable.
- `INCONCLUSIVE` — evidence is insufficient to validate the harness.

Q04-B cannot authorize ML promotion unless Q04-A is `CLOSED_PASS`.

## Q04-B — ML scope

After Q04-A passes, record a separate field:

```text
ml_scope = INCLUDE | EXCLUDE | DEFER
```

- `INCLUDE` only when a preregistered candidate adds robust out-of-sample value versus the strongest eligible transparent baseline after realistic costs and complexity penalties.
- `EXCLUDE` when ML fails to justify its added complexity; this does not invalidate a successful deterministic Q04 closure.
- `DEFER` when the deterministic harness is valid but optional ML evidence is intentionally postponed or insufficient for inclusion.

The aggregate Q04 receipt still uses the canonical outcome vocabulary. `ml_scope` is a frozen output, not an alternative outcome vocabulary.

Q04 complexity cannot override Q00 conclusions or reintroduce Q00-excluded product complexity without a superseding evidence path.

## Frozen outputs

Dataset manifest, asset universe, cost model, benchmark versions, validation plan, approved metrics, explicit `ml_scope`, and model family only if `ml_scope = INCLUDE`. No performance-marketing claim is created by this receipt.

---

# Q05 — Moat and competitive durability

## Question

Does the Q00-surviving trust/evidence/audit workflow create repeatable preference or workflow advantage deeper than localization, generic LLM summarization or cosmetic UI?

Execution authority: `experiments/q05/Q05_PREREGISTRATION.md`.

Candidate components are evaluated independently. Competitive task comparison, retention linkage and replicability assessment are required; feature-count comparisons and interview enthusiasm alone are insufficient.

## Decision rules

- `CLOSED_PASS` — at least one candidate advantage shows repeat-use/preference evidence and a defensibility mechanism deeper than surface presentation.
- `CLOSED_CONDITIONAL` — the product remains worth building as a learning wedge, but scale architecture/large GTM spend stay blocked.
- `PIVOT_REQUIRED` — durable advantage appears in another persona/workflow/distribution layer.
- `STOP_CURRENT_CONFIGURATION` — the product remains a thin interchangeable wrapper after repeated comparative evidence.
- `INCONCLUSIVE` — competitive, longitudinal or exposure-aware evidence is insufficient.

A component excluded or materially weakened by Q00 cannot remain a promotable moat claim without a new/superseding evidence path.

## Frozen outputs

Moat-hypothesis version, supported/unsupported components, allowed strategy claims, scale-spend constraint and next evidence horizon.

---

## Dependency graph

```text
Q00 core causal value ------------+
                                   |
Q01 legal flow --------------------+
                                   |
Q02 data rights -------------------+----> MK1_BOOTSTRAP_PROFILE
                                   |             |
Q03 user value / WTP --------------+             v
                                   |       MK1 production gate
Q04 quant baseline / ML -----------+
                                   |
Q03 repeat-use ----> Q05 moat -----+
```

Parallel work is allowed where evidence is independent, but closure dependencies are strict:

- Q00 independently gates promotion; Q03/Q04/Q05 cannot compensate for a failed Q00 configuration.
- Q03/Q04/Q05 must describe only the intervention/components that survived Q00 where that dependency is material.
- Q05 cannot be considered strong without Q03 repeat-use evidence.
- Q04 research may run before Q02 commercial closure only on data legally/contractually usable for that research purpose.
- Q01 counsel must review the actual interaction model surviving Q00 and validated by Q03, not a materially different mock.
- Q02 must close on the exact data profile intended for MK1, not a generic provider statement.

---

## MK1 Bootstrap Profile

Once Q00–Q05 reach promotable states, MK0 creates one immutable candidate `MK1_BOOTSTRAP_PROFILE` containing at minimum:

```text
profile_id
q00_intervention_scope
q00_excluded_components
regulatory_flow_profile
primary_persona
jtbd
wedge
initial_pricing_hypothesis
asset_universe
provider_set
data_use_profiles
fallback_groups
freshness_profiles
risk_policy_version
quant_baseline_receipt
ml_scope
moat_status
legal_copy_version
canonical_source_digests
graph_version
graph_digest_when_available
created_at
```

The profile is the exact evidence-derived configuration production implementation is allowed to build.

Implementation may not silently substitute another intervention scope, provider, asset universe, flow, price-sensitive capability, risk policy or ML scope.

Material change requires impact analysis, reopening affected locks where necessary, superseding evidence receipt(s), graph impact analysis and a new bootstrap-profile version.

---

## Promotion review packet

Before production MK1 begins, the canonical packet must contain:

1. finalized Q00 causal-value receipt;
2. finalized Q01 regulatory receipt;
3. finalized Q02 receipt(s) for every initial production data profile;
4. finalized Q03 experiment bundle;
5. finalized Q04 baseline receipt and explicit `ml_scope`;
6. finalized Q05 receipt;
7. contradiction log across all receipts;
8. updated `MK0_LOCKS.md`;
9. updated canonical product/data/quant/regulatory docs;
10. candidate `MK1_BOOTSTRAP_PROFILE`;
11. architecture/graph impact review confirming no unresolved reachable P0/P1 node or required edge.

The exact packet shape is governed by `docs/validation/MK0_PROMOTION_PACKET.md`.

No aggregate “green” may conceal a failed causal or fatal lock.

---

## Contradiction handling

Evidence can close one question while reopening another.

Examples:

- Q03 willingness-to-pay depends on complexity rejected by Q00;
- users prefer personalization that Q01 counsel rejects;
- the best data provider is legally usable but destroys unit economics;
- Q04 depends on a data family Q02 does not authorize commercially;
- the validated persona values the product but not at a viable price;
- Q05 depends on a component removed by Q00 or Q01 constraints.

When contradiction occurs:

1. record it explicitly;
2. identify affected locks/docs/nodes/edges;
3. do not average incompatible results into a favorable decision;
4. pivot/re-scope and version the affected evidence plan(s);
5. regenerate the bootstrap only after blocking contradictions are resolved.

---

## Anti-gaming rules

- no changing primary metrics after outcomes are visible;
- no deleting failed or inconclusive experiment versions;
- no substituting survey intent for observed repeat use;
- no treating provider sales language as overriding contradictory authoritative terms;
- no treating legal silence as clearance;
- no promoting ML from in-sample or single-window superiority;
- no calling localization alone a moat;
- no using implementation effort already spent as evidence to lower a gate;
- no using Q03/Q04/Q05 success to rescue a failed Q00 configuration;
- no retaining a Q00-rejected component in moat, pricing, architecture or bootstrap claims without a new evidence path;
- no mixing cohorts without a preregistered pooling rule;
- no performance, rights or regulatory claim beyond the exact scope of its receipt.

---

## Closure criterion for MK0

MK0 can promote to production MK1 implementation only when:

- Q00–Q05 have promotable immutable final receipts;
- all constraints/exclusions from conditional receipts are frozen into canonical specs and graph reachability;
- the `MK1_BOOTSTRAP_PROFILE` exists;
- no unresolved P0/P1 cross-receipt contradiction can materially change MK1 boundaries;
- the `MK0_PROMOTION_PACKET` is approved for the exact graph/profile snapshot;
- `docs/implementation/BUILD_READINESS.md` passes;
- no external/empirical result has been silently converted into an internal assumption.

At that point MK0 does not claim that the product will succeed. It claims something narrower and defensible:

> **The first production configuration has earned the right to be built.**
