# MK0 Evidence Closure Protocol

## Purpose

The internal MK1 design graph is closed. MK0 now advances by closing the remaining **external / empirical** locks without fabricating evidence and without allowing implementation to silently decide product, legal, data-rights, commercial or scientific questions.

This document defines the canonical protocol for closing **Q00–Q05**:

- Q00 — core causal value against simple baselines;
- Q01 — Peru regulatory boundary;
- Q02 — commercial market-data rights;
- Q03 — willingness-to-pay / repeat-use evidence;
- Q04 — deterministic quant baseline / ML incremental value;
- Q05 — moat / competitive durability.

The protocol closes the **method of validation**, not the result. A Q remains open until its required evidence exists and passes review.

Detailed experiment/review artifacts remain authoritative for execution:
- `experiments/q00/Q00_PREREGISTRATION.md`;
- `quarries/q01/Q01_COUNSEL_REVIEW_PACKET.md`;
- `quarries/q02/Q02_DATA_RIGHTS_REVIEW_PACKET.md`;
- `experiments/q03/Q03_PREREGISTRATION.md`;
- `experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`;
- `experiments/q04/Q04_PREREGISTRATION.md`;
- `experiments/q05/Q05_PREREGISTRATION.md`.

---

## Governing distinction

SOPHROSYNE has three different kinds of truth:

1. **Design truth** — an internal contract or architecture decision.
2. **Evidence truth** — an external fact or empirical result that must be observed, contracted, measured or reviewed.
3. **Implementation truth** — proof that built software conforms to closed design, represented by acceptance receipts.

These classes must never be collapsed.

```text
closed design
    |
    +--> external / empirical evidence gate
    |        |
    |        +--> PASS / CONDITIONAL_PASS / PIVOT / STOP / INCONCLUSIVE
    |
    +--> implementation
             |
             +--> typed acceptance receipts
```

A successful prototype is not legal clearance. A signed provider contract is not user demand. A strong backtest is not proof of a moat. A passing user study is not proof that production code is secure. A sophisticated downstream experiment cannot rescue a failed core causal-value gate.

---

## Evidence lock lifecycle

Every external / empirical lock follows this lifecycle:

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

Before observing outcome data, the evidence plan freezes:
- hypothesis / question;
- scope;
- authority required;
- sample or dataset;
- primary and secondary measures;
- decision thresholds or decision rule;
- exclusion criteria;
- expected artifacts;
- known confounders;
- version/digest.

Post-hoc material changes require a new evidence-plan version. Old plans remain immutable.

### EVIDENCE_RUNNING

Data, legal opinion, contract terms or experiment observations are being collected. The decision rule cannot be rewritten to rescue the hypothesis.

### REVIEW_READY

Required artifacts exist and can be independently checked.

### CLOSED_PASS

Evidence supports the exact scoped claim strongly enough for MK1 promotion.

### CLOSED_CONDITIONAL

The scoped configuration may proceed only with explicit constraints. Those constraints become frozen MK1 requirements.

### PIVOT_REQUIRED

The current hypothesis is not supported, but a narrower or materially different product configuration remains plausible. Affected canonical docs must be updated before a replacement experiment starts.

### STOP_CURRENT_CONFIGURATION

The exact proposed configuration cannot proceed. This is fatal to the configuration, not automatically fatal to SOPHROSYNE as a program.

### INCONCLUSIVE

Required evidence is insufficient, underpowered, corrupted, materially confounded or otherwise unable to support a terminal decision. `INCONCLUSIVE` never auto-promotes to PASS.

---

## Evidence receipt schema

Every closure decision must produce an immutable `EvidenceReceipt`.

Required fields:

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

Contradictory evidence is first-class and cannot be omitted merely because the final decision is favorable.

---

## Authority matrix

| Lock | Evidence authority | Internal reviewer | Self-certification allowed? |
|---|---|---|---|
| Q00 causal value | pre-registered comparative/ablation evidence under frozen tasks, baselines and scoring | product research + validation reviewer | No terminal promotion from a single unreviewed favorable run |
| Q01 regulatory | qualified Peruvian securities counsel for exact flows/copy | product + architecture | No |
| Q02 data rights | provider contract/terms/quote or written provider confirmation | data architecture + product | No for rights not explicit in authoritative text |
| Q03 WTP / repeat-use | observed target-user behavior and pre-registered experiment output | product research reviewer | Yes for measurement, not for inventing missing observations |
| Q04 quant / ML | reproducible experiment corpus + independent rerun | quant reviewer | No single-run self-certification |
| Q05 moat | observed preference/repeat use + competitor evidence | product strategy reviewer | No claim from interviews alone |

If an external authority is required, silence or ambiguity is **not** PASS.

---

# Q00 — Core causal value against simple baselines

## Question

Does the full candidate SOPHROSYNE intervention create material incremental decision-process value over simpler and cheaper substitutes under controlled, non-production tasks?

## Required evidence

The promotable experiment must follow `experiments/q00/Q00_PREREGISTRATION.md` and preserve destructive comparison against, where applicable:
- raw-information control;
- stateless structured assistance;
- five-question friction checklist;
- simple feedback;
- short-memory SOPHROSYNE;
- full candidate SOPHROSYNE;
- strongest realistic cheap/free substitute.

Required analyses include simple-friction, memory, outcome-blind, hidden-rubric, assisted-vs-unassisted transfer, regime/context transfer, dependence correction, cognitive/time cost, cheap-substitute comparison and the economic bridge to Q03.

The study evaluates decision-process quality, not live investment performance. No real-money trading is required.

## Decision rule

### CLOSED_PASS

The candidate intervention demonstrates preregistered, material incremental value beyond competent simple baselines while remaining within the allowed cognitive/time-cost boundary.

### CLOSED_CONDITIONAL

Only a narrower intervention or subset of components earns causal support. Unsupported complexity is excluded or deferred and those exclusions become frozen MK1 constraints.

### PIVOT_REQUIRED

Most value is explained by a materially simpler intervention, different workflow or different product configuration.

### STOP_CURRENT_CONFIGURATION

The current full-product configuration fails to establish meaningful incremental value against competent simple/cheap substitutes.

### INCONCLUSIVE

The preregistered minimum sample, instrumentation, independence, validity or evidence quality is insufficient for a terminal decision.

Q03 willingness-to-pay, Q04 modeling sophistication or Q05 defensibility evidence **cannot rescue a failed Q00 result**.

## Frozen outputs

A passing/conditional receipt freezes:
- validated intervention scope;
- component inclusion/exclusion decisions;
- simple-friction result;
- memory result;
- transfer scope (`ASSISTED_ONLY` where applicable);
- cognitive/time-cost boundary;
- cheap-substitute result;
- minimum meaningful effect rule/result;
- implications for Q03/Q04/Q05;
- exact constraints propagated into `MK1_BOOTSTRAP_PROFILE` and graph reachability.

---

# Q01 — Peru regulatory boundary

## Question

Can the exact proposed MK1 product flows, copy, personalization level and commercial model operate within the intended non-custodial decision-support posture under applicable Peruvian securities-law constraints?

## Required review bundle

Counsel receives frozen representations of onboarding, profile/portfolio context, Market Translator, Evidence View, scenario cards, alerts, Strategy Sandbox, paper-validation flows, pricing, marketing claims, disclaimers/terms and future connector language exposed in MK1 UI.

Text-only descriptions are insufficient where interaction semantics matter. Screens or clickable prototypes should be provided.

The review must explicitly classify whether each flow is generalized information, personalized recommendation, advisory activity, intermediation, discretionary activity, solicitation/distribution issue or another relevant regulated behavior, and identify prohibited/required wording and constraints.

## Decision rule

- `CLOSED_PASS`: written review states the exact frozen MK1 flow can proceed under the intended posture without material redesign.
- `CLOSED_CONDITIONAL`: counsel permits the flow only with explicit product/copy restrictions; each restriction is promoted into MK1 specification and regression checks.
- `PIVOT_REQUIRED`: a central flow must materially change, but the product thesis survives under a narrower interaction model.
- `STOP_CURRENT_CONFIGURATION`: the proposed configuration would require a regulatory posture the project is not prepared to assume.

## Frozen outputs

A passing/conditional receipt freezes the `RegulatoryFlowProfile`, approved/forbidden interaction classes, approved/forbidden claim lexicon, required disclaimers/terms constraints, jurisdiction = Peru, and the exact reviewed prototype/screens digest.

Any material UX/copy change that changes recommendation/personalization semantics reopens Q01 for the affected flow.

---

# Q02 — Commercial market-data rights

## Question

Can the exact initial production data profile be stored, transformed, displayed, cached and commercially used in the intended product under documented provider rights and costs?

## Unit of closure

Q02 is scoped to a `DataUseProfile`, not globally to a provider:

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
cost_model
fallback_compatibility
```

For every material field, authoritative public terms, contract, quote or written provider confirmation must exist, with effective date/version where available, conflict notes, cost/entitlement assumptions, termination implications and fallback constraints.

Unknown rights default to **denied**.

## Decision rule

- `CLOSED_PASS`: every required use in the exact initial profile is explicitly allowed and economically compatible.
- `CLOSED_CONDITIONAL`: allowed only with explicit rights/entitlement/cache/attribution/geography/user-class constraints that become executable policy.
- `PIVOT_REQUIRED`: the provider/data family is commercially incompatible; choose another provider, derived-only surface or narrower profile.
- `STOP_CURRENT_CONFIGURATION`: no viable provider/profile combination supports the mandatory MK1 data surface within feasible economics or rights constraints.

## Frozen outputs

A passing/conditional receipt freezes provider set, asset universe, data families, fallback compatibility groups, `DataRightsRecord` versions, entitlement assumptions, unit-economics cost assumptions, retention/cache limits and user-visible attribution obligations.

Any provider contract/terms change reopens only affected profiles.

---

# Q03 — Willingness-to-pay and repeat-use

## Question

Do target users repeatedly value the decision-intelligence workflow enough to justify building the surviving MK1 wedge, and is there credible evidence that some will pay at a commercially plausible price?

## Evidence hierarchy

Strongest to weakest:
1. repeated observed use with meaningful task completion;
2. behavior that carries friction/cost;
3. repeated return to a prototype/briefing;
4. observed preference in blinded/comparative task;
5. interview statements;
6. generic survey enthusiasm.

Statements alone cannot close Q03.

Required experiments and exact thresholds are governed by `experiments/q03/Q03_PREREGISTRATION.md` and `experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`.

## Decision rule

A promotable closure must show that the target problem appears repeatedly in observed workflows, the representation improves or preserves objective comprehension while reducing meaningful workflow friction, repeat-use exists beyond novelty, at least one commercially plausible price band has non-trivial qualified intent, and no severe trust failure contradicts the thesis.

- `CLOSED_PASS`: evidence supports the current capable-beginner wedge and continued B2C MK1 build.
- `CLOSED_CONDITIONAL`: value exists only for a narrower persona/use case/price surface; freeze that narrower wedge.
- `PIVOT_REQUIRED`: users value a materially different workflow, persona or distribution mode.
- `STOP_CURRENT_CONFIGURATION`: repeated evidence shows weak problem intensity, poor repeat use and weak commitment across plausible variants.
- `INCONCLUSIVE`: minimum usable evidence is not reached.

## Frozen outputs

Primary persona, JTBD, wedge, required trust features, initial pricing-hypothesis band, validated/rejected channel hypotheses and experiment corpus/analysis receipt. All must remain compatible with the Q00-surviving intervention scope.

---

# Q04 — Deterministic quant baseline and ML incremental value

## Question

Can the research harness reproduce transparent deterministic baselines under point-in-time semantics and realistic costs, and does ML earn any place in MK1 beyond those baselines?

Q04 contains two decisions that must not be conflated.

### Q04-A — baseline harness validity

Must close before any ML promotion decision. Required proof includes point-in-time dataset manifest, deterministic rerun, hand-computed accounting/fill fixtures, transparent benchmark ladder, cost-model version, untouched temporal test interval, walk-forward/equivalent temporal validation, multiple-testing log and independent reproduction.

A baseline can lose money and still validate the harness. Harness validity is not alpha proof.

### Q04-B — ML incremental value

ML remains optional. Before evaluation, target/label, feature-availability semantics, splits, deterministic comparator rule, primary and risk metrics, costs, complexity budget, promotion threshold and failure/retirement rule must be preregistered.

ML is promoted only if it adds robust out-of-sample value versus the strongest eligible transparent baseline after realistic costs without dependence on one regime, one seed or one cherry-picked window.

## Decision rule

- `CLOSED_PASS — baseline`: harness and deterministic benchmark corpus are reproducible and leakage controls pass.
- `CLOSED_PASS — ML included`: ML demonstrates preregistered incremental OOS value sufficient to justify added complexity.
- `CLOSED_PASS — ML excluded`: deterministic harness passes but ML does not justify itself; MK1 proceeds without an alpha-ML dependency.
- `PIVOT_REQUIRED`: chosen data/asset/label formulation is invalid or too weak.
- `STOP_CURRENT_CONFIGURATION`: research semantics cannot be made reproducible or required data rights make the path unusable.

Q04 complexity cannot override Q00 causal-value conclusions.

## Frozen outputs

Baseline dataset manifest, asset universe, cost model, benchmark versions, validation plan, approved metrics, explicit ML include/exclude/defer decision, and model family only if actually promoted. No performance-marketing claim is created by this receipt.

---

# Q05 — Moat and competitive durability

## Question

Does the proposed trust/evidence/audit workflow create a user preference or workflow advantage deeper than localization, generic LLM summarization or cosmetic UI?

Candidate components are evaluated independently: evidence graph/opposing evidence, immutable Decision Ledger, point-in-time replay/provenance, progressive disclosure, explicit uncertainty/invalidation, reproducible strategy validation, longitudinal decision history and rights-aware derived intelligence.

No component is declared a moat by design.

Required evidence is governed by `experiments/q05/Q05_PREREGISTRATION.md` and must include competitive task comparison, retention linkage and replicability assessment.

## Decision rule

- `CLOSED_PASS`: at least one candidate advantage shows repeat-use/preference evidence and a defensibility mechanism deeper than surface presentation.
- `CLOSED_CONDITIONAL`: product is worth building as a learning wedge but moat evidence remains weak; scale architecture/large GTM spend stay blocked.
- `PIVOT_REQUIRED`: durable advantage appears in another persona/workflow/distribution layer.
- `STOP_CURRENT_CONFIGURATION`: product remains a thin interchangeable wrapper after repeated comparative evidence and no deeper workflow asset emerges.

No component removed or weakened by Q00 may remain represented as moat evidence.

## Frozen outputs

Moat-hypothesis version, supported/unsupported components, claims permitted in strategy docs, scale-spend constraint and next evidence horizon.

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
- Q00 independently gates promotion; Q03/Q04/Q05 cannot compensate for a failed Q00 configuration;
- Q03/Q04/Q05 must describe only the intervention/components that survived Q00 where that dependency is material;
- Q05 cannot be considered strong without Q03 repeat-use evidence;
- Q04 research may run before Q02 commercial closure only on data legally/contractually usable for that research purpose;
- Q01 counsel must review the actual interaction model surviving Q00 and validated by Q03, not a materially different mock;
- Q02 must close on the exact data profile intended for MK1, not a generic provider claim.

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
created_at
```

The bootstrap profile is the exact evidence-derived configuration that production implementation is allowed to build.

Implementation may not silently substitute another intervention scope, provider, asset universe, flow, price-sensitive capability, risk policy or ML scope.

Material change requires impact analysis, reopening affected locks where necessary, superseding evidence receipt(s) and a new bootstrap-profile version.

---

## Promotion review packet

Before production MK1 begins, the review packet must contain:

1. finalized Q00 causal-value receipt;
2. finalized Q01 regulatory receipt;
3. finalized Q02 receipt(s) for every initial production data profile;
4. finalized Q03 experiment bundle;
5. finalized Q04 baseline receipt and explicit ML include/exclude/defer decision;
6. finalized Q05 receipt;
7. contradiction log across all receipts;
8. updated `MK0_LOCKS.md`;
9. updated canonical product/data/quant/regulatory docs;
10. candidate `MK1_BOOTSTRAP_PROFILE`;
11. architecture/graph impact review confirming no unresolved reachable P0/P1 internal node or required edge.

No “overall green” may conceal a failed fatal or causal gate.

The canonical packet shape is `docs/validation/MK0_PROMOTION_PACKET.md`.

---

## Contradiction handling

Evidence can close one question while reopening another.

Examples:
- Q03 willingness-to-pay depends on complexity rejected by Q00;
- users strongly prefer personalization, but Q01 counsel rejects that flow;
- the best data provider is legally usable but destroys unit economics;
- a quant model works only with a data family whose commercial rights are unavailable;
- the validated persona values the product but not at a viable price;
- moat evidence depends on a component removed by Q00 or a workflow removed by regulatory constraints.

When this occurs:
1. record the contradiction explicitly;
2. identify affected locks/docs/nodes/edges;
3. do not average incompatible results into PASS;
4. pivot/re-scope and issue new evidence-plan versions;
5. regenerate the bootstrap profile only after contradictions are resolved.

---

## Anti-gaming rules

- no changing primary metrics after results are visible;
- no deleting failed experiment versions;
- no substituting survey intent for observed repeat use;
- no treating a provider salesperson statement as overriding contradictory contract text;
- no treating legal silence as clearance;
- no promoting ML from in-sample or single-window superiority;
- no calling localization alone a moat;
- no using implementation effort already spent as evidence to lower a gate;
- no using Q03/Q04/Q05 success to rescue a failed Q00 configuration;
- no retaining a Q00-rejected component in moat, pricing, architecture or bootstrap claims without a new/superseding evidence path;
- no merging mixed cohorts until cohort definitions are documented;
- no performance or regulatory claim beyond the exact scope of the receipt.

---

## Closure criterion for MK0

MK0 can promote to production MK1 implementation only when:
- Q00–Q05 have promotable final receipts;
- all constraints/exclusions from conditional receipts are frozen into canonical specs and graph reachability;
- the `MK1_BOOTSTRAP_PROFILE` exists;
- no cross-receipt contradiction capable of materially changing MK1 boundaries remains unresolved;
- the `MK0_PROMOTION_PACKET` is approved for the exact graph/profile snapshot;
- `BUILD_READINESS.md` is satisfied;
- no external/empirical result was silently converted into an internal assumption.

At that point MK0 is not claiming that the product will succeed. It is claiming something narrower and defensible:

> **The first production configuration has earned the right to be built.**
