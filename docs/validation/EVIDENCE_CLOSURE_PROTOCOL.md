# MK0 Evidence Closure Protocol

## Purpose

The internal MK1 design graph is closed. MK0 now advances by closing the remaining **external / empirical** locks without fabricating evidence and without allowing implementation to silently decide product, legal, data-rights, commercial or scientific questions.

This document defines the canonical protocol for closing Q01–Q05:

- Q01 — Peru regulatory boundary;
- Q02 — commercial market-data rights;
- Q03 — willingness-to-pay / repeat-use evidence;
- Q04 — deterministic quant baseline / ML incremental value;
- Q05 — moat / competitive durability.

The protocol closes the **method of validation**, not the result. A Q remains open until its required evidence exists and passes review.

---

## Governing distinction

SOPHROSYNE has three different kinds of truth:

1. **Design truth** — an internal contract or architecture decision. This graph is already closed for MK1.
2. **Evidence truth** — an external fact or empirical result that must be observed, contracted, measured or reviewed.
3. **Implementation truth** — proof that built software conforms to closed design, represented by acceptance receipts.

These classes must never be collapsed.

```text
closed design
    |
    +--> external / empirical evidence gate
    |        |
    |        +--> PASS / CONDITIONAL_PASS / PIVOT / STOP
    |
    +--> implementation
             |
             +--> typed acceptance receipts
```

A successful prototype is not legal clearance. A signed provider contract is not user demand. A strong backtest is not proof of a moat. A passing user study is not proof that production code is secure.

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

Post-hoc changes require a new evidence-plan version. Old plans remain immutable.

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

### Immutability

A finalized receipt is not edited in place. Corrections or new evidence create a superseding receipt.

### Provenance

Evidence classes must remain explicit:
- `OFFICIAL`;
- `ACADEMIC`;
- `OBSERVED`;
- `INFERRED`;
- `HYPOTHESIS`.

### Negative evidence

Contradictory evidence is first-class. It cannot be omitted merely because the final decision is PASS.

---

## Authority matrix

| Lock | Evidence authority | Internal reviewer | Self-certification allowed? |
|---|---|---|---|
| Q01 regulatory | qualified Peruvian securities counsel for exact flows/copy | product + architecture | No |
| Q02 data rights | provider contract/terms/quote or written provider confirmation | data architecture + product | No for rights not explicit in authoritative text |
| Q03 WTP / repeat-use | observed target-user behavior and pre-registered experiment output | product research reviewer | Yes for measurement, not for inventing missing observations |
| Q04 quant / ML | reproducible experiment corpus + independent rerun | quant reviewer | No single-run self-certification |
| Q05 moat | observed preference/repeat use + competitor evidence | product strategy reviewer | No claim from interviews alone |

If an external authority is required, silence or ambiguity is **not** PASS.

---

# Q01 — Peru regulatory boundary

## Question

Can the exact proposed MK1 product flows, copy, personalization level and commercial model operate within the intended non-custodial decision-support posture under applicable Peruvian securities-law constraints?

## Required review bundle

Counsel receives frozen representations of:
1. onboarding;
2. profile / portfolio-context inputs;
3. Market Translator;
4. Evidence View;
5. scenario cards;
6. alerts;
7. Strategy Sandbox;
8. paper-validation flows;
9. pricing page;
10. marketing claims;
11. disclaimers / terms;
12. any future connector language shown in MK1 UI.

Text-only descriptions are insufficient where interaction semantics matter. Screens or clickable prototypes should be provided.

## Required questions to counsel

The review must explicitly address whether each flow is best treated as, or risks becoming:
- generalized information;
- personalized recommendation;
- advisory activity;
- intermediation;
- discretionary activity;
- solicitation/distribution issue;
- another regulated behavior relevant to the proposed flow.

Counsel should identify prohibited wording, required wording, required disclaimers and any behavior that must be removed or constrained.

## Decision rule

### CLOSED_PASS

Written review states that the exact frozen MK1 flow can proceed under the intended posture without a material redesign.

### CLOSED_CONDITIONAL

Counsel permits the flow only with explicit product/copy restrictions. Every restriction is promoted into MK1 specification and regression checks.

### PIVOT_REQUIRED

A central flow must materially change, but the product thesis can survive under a narrower interaction model.

### STOP_CURRENT_CONFIGURATION

The proposed MK1 configuration would require a regulatory posture the project is not prepared to assume.

## Frozen outputs

A passing/conditional receipt freezes:
- `RegulatoryFlowProfile` version;
- approved interaction classes;
- forbidden interaction classes;
- approved/forbidden claim lexicon;
- required disclaimers/terms constraints;
- jurisdiction = Peru for this receipt;
- exact screenshots/prototype digest reviewed by counsel.

Any material UX/copy change that changes recommendation/personalization semantics reopens Q01 for the affected flow.

---

# Q02 — Commercial market-data rights

## Question

Can the exact initial production data profile be stored, transformed, displayed, cached and commercially used in the intended product under documented provider rights and costs?

## Unit of closure

Q02 is **not** closed globally for a provider. Closure is scoped to a `DataUseProfile`:

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

## Required evidence

For every field that affects the proposed use:
- authoritative public terms, contract, quote or written provider confirmation;
- effective date/version where available;
- conflict notes if sales/support statements differ from legal terms;
- cost and entitlement assumptions;
- revocation/termination implications;
- fallback constraints.

Unknown rights default to **denied**, not allowed.

## Decision rule

### CLOSED_PASS

Every required use in the exact initial `DataUseProfile` is explicitly allowed and economically compatible with the candidate MK1 model.

### CLOSED_CONDITIONAL

Allowed only with constraints such as delayed display, entitlement checks, no raw redistribution, bounded cache, attribution, geography or user classification. Constraints become executable rights policy.

### PIVOT_REQUIRED

The provider/data family is technically attractive but commercially incompatible; choose another provider, a derived-only product surface or a narrower asset/data profile.

### STOP_CURRENT_CONFIGURATION

No viable provider/profile combination supports the mandatory MK1 data surface within feasible economics or rights constraints.

## Frozen outputs

A passing/conditional receipt freezes:
- initial provider set;
- exact asset universe;
- exact data families;
- fallback compatibility groups;
- `DataRightsRecord` versions;
- entitlement assumptions;
- cost assumptions used by unit economics;
- retention/cache limits;
- user-visible attribution obligations.

Any provider contract/terms change reopens only affected `DataUseProfile`s.

---

# Q03 — Willingness-to-pay and repeat-use

## Question

Do target users repeatedly value the decision-intelligence workflow enough to justify building the MK1 wedge, and is there credible evidence that some will pay at a commercially plausible price?

## Evidence hierarchy

Strongest to weakest:
1. repeated observed use with meaningful task completion;
2. behavior that carries friction/cost (waitlist deposit where legally/operationally appropriate, paid pilot, qualified purchase intent);
3. repeated return to a prototype/briefing;
4. observed preference in blinded/comparative task;
5. interview statements;
6. generic survey enthusiasm.

Statements alone cannot close Q03.

## Required experiments

### E03-A — Behavioral discovery

Minimum target: 15 qualified interviews; preferred completion band: 20–25.

Observe current workflow before presenting SOPHROSYNE. Capture:
- actual decision/research workflow;
- sources used;
- time spent;
- failure/confusion points;
- trust signals;
- current spend/subscriptions;
- repeated tasks rather than hypothetical wants.

### E03-B — Translator comprehension test

Compare a conventional evidence/chart presentation against the SOPHROSYNE Translator/Evidence concept.

Pre-register:
- randomized order or counterbalancing;
- comprehension questions with objective scoring;
- task-completion time;
- confidence rating;
- calibration gap = confidence vs correctness;
- whether opposing evidence/staleness is noticed;
- qualitative failure reasons.

The test must not optimize only for subjective preference.

### E03-C — Repeat-use proxy

Run a fixed two-week decision-intelligence prototype/briefing with qualified participants.

Measure:
- return sessions / active days;
- voluntary revisits without prompting;
- evidence expansion usage;
- revisit of prior Decision Records;
- use of uncertainty/invalidation fields;
- abandonment reason;
- whether the workflow replaces or complements an existing tool.

### E03-D — Pricing / commitment test

Test candidate price bands already documented in `UNIT_ECONOMICS.md` without presenting them as proven prices.

Measure qualified intent by cohort and price; distinguish:
- curiosity click;
- email/waitlist intent;
- checkout initiation or equivalent higher-friction intent;
- actual paid pilot if one is later legally/operationally appropriate.

## Decision rule

Q03 is not reduced to one vanity metric. A closure review must show all of the following:
- the target problem appears repeatedly in observed workflows;
- the SOPHROSYNE representation improves or preserves objective comprehension while reducing meaningful workflow friction;
- repeat-use evidence exists beyond one-session novelty;
- at least one commercially plausible price band has non-trivial qualified intent;
- no severe trust failure appears that contradicts the product thesis.

Before each experiment starts, exact numeric thresholds for its primary measures must be pre-registered in the experiment manifest. They cannot be chosen after seeing results.

### CLOSED_PASS

The combined evidence justifies the current capable-beginner wedge and continued B2C MK1 build.

### CLOSED_CONDITIONAL

Value is observed but only for a narrower persona/use case/price surface. Freeze that narrower wedge into MK1.

### PIVOT_REQUIRED

Users value a materially different workflow, persona or distribution mode. Product docs must change before build.

### STOP_CURRENT_CONFIGURATION

Repeated evidence shows weak problem intensity, poor repeat use and weak commitment across plausible variants.

## Frozen outputs

- primary persona version;
- JTBD version;
- wedge statement;
- required trust features;
- initial pricing hypothesis band;
- validated/rejected channels only as hypotheses at this stage;
- experiment corpus and analysis receipt.

---

# Q04 — Deterministic quant baseline and ML incremental value

## Question

Can the research harness reproduce transparent deterministic baselines under point-in-time semantics and realistic costs, and does ML earn any place in MK1 beyond those baselines?

## Two separate closure decisions

Q04 contains two decisions that must not be conflated:

### Q04-A — baseline harness validity

Must close before any ML promotion decision.

Required proof:
- point-in-time dataset manifest;
- deterministic rerun;
- hand-computed accounting/fill fixtures;
- benchmark ladder implemented from cash/no-trade through transparent rules;
- cost model version;
- untouched test interval;
- walk-forward or equivalent temporal validation;
- multiple-testing log;
- reproducibility by a second run/reviewer.

A baseline can lose money and still validate the harness. Harness validity is not alpha proof.

### Q04-B — ML incremental value

ML remains optional.

Before training/evaluation, pre-register:
- target/label;
- feature availability semantics;
- training/validation/test segmentation;
- best deterministic comparator selection rule;
- primary metric;
- secondary/risk metrics;
- cost assumptions;
- complexity budget;
- promotion threshold;
- failure/retirement rule.

ML is promoted only if it adds robust out-of-sample value versus the strongest eligible transparent baseline after realistic costs, without relying on one regime, one seed or one cherry-picked window.

A model that improves raw return but materially worsens risk, turnover/cost sensitivity, calibration or stability does not automatically pass.

## Decision rule

### CLOSED_PASS — baseline

Research harness and deterministic benchmark corpus are reproducible and leakage controls pass.

### CLOSED_PASS — ML included

A pre-registered ML candidate demonstrates incremental OOS value robust enough to justify its added complexity.

### CLOSED_PASS — ML excluded

The deterministic harness passes, but ML fails to justify itself. MK1 proceeds without an alpha-ML dependency.

### PIVOT_REQUIRED

The chosen data/asset/label formulation is invalid or too weak, requiring a new experiment profile.

### STOP_CURRENT_CONFIGURATION

Research semantics cannot be made reproducible with the selected data/profile, or required data rights make the intended research path unusable.

## Frozen outputs

- baseline dataset manifest;
- asset universe used for the receipt;
- transaction-cost model;
- benchmark ladder versions;
- validation split/walk-forward plan;
- approved primary metrics;
- ML inclusion/exclusion decision;
- model family only if actually promoted;
- no performance marketing claim is created by this receipt.

---

# Q05 — Moat and competitive durability

## Question

Does the proposed trust/evidence/audit workflow create a user preference or workflow advantage that is deeper than localization, generic LLM summarization or cosmetic UI?

## Candidate moat components

Treat each independently:
- evidence graph / opposing evidence;
- immutable Decision Ledger;
- point-in-time replay and provenance;
- progressive beginner-to-quant disclosure;
- explicit uncertainty/invalidation;
- reproducible strategy validation;
- longitudinal personal decision history;
- rights-aware derived intelligence.

No single component is declared a moat by design.

## Required evidence

### Competitive task comparison

Use comparable user tasks against representative competing workflows, not only feature checklists.

Measure:
- comprehension;
- completion time;
- trust calibration;
- return intent;
- preference after repeated exposure;
- which component caused the preference;
- whether preference survives removal of branding/marketing language where practical.

### Retention linkage

A candidate moat must correlate with observed repeat use or workflow dependence. “Users said it was cool” is insufficient.

### Replicability assessment

For each candidate advantage, document:
- how quickly a well-funded competitor could copy the visible interface;
- what underlying data/history/workflow state accumulates over time;
- whether the advantage compounds with Decision Records, evidence history, personalization that stays within approved boundaries, or validation data;
- whether it depends on exclusive rights or merely generic model access.

## Decision rule

### CLOSED_PASS

At least one candidate advantage shows repeat-use/preference evidence and has a defensibility mechanism deeper than surface presentation.

### CLOSED_CONDITIONAL

The product is worth building even though moat evidence is weak; MK1 is explicitly treated as a learning wedge and scale architecture/large GTM spend remain blocked.

### PIVOT_REQUIRED

The durable advantage appears in another persona/workflow/distribution layer.

### STOP_CURRENT_CONFIGURATION

The product remains a thin interchangeable wrapper after repeated comparative evidence and no deeper workflow asset emerges.

## Frozen outputs

- moat hypothesis version;
- supported/unsupported components;
- claims allowed in strategy docs;
- scale-spend constraint;
- next evidence horizon.

---

## Dependency graph

```text
Q01 legal flow -------------------+
                                  |
Q02 data rights ------------------+----> MK1_BOOTSTRAP_PROFILE
                                  |             |
Q03 user value / WTP -------------+             v
                                  |       MK1 production gate
Q04 quant baseline / ML ----------+
                                  |
Q03 repeat-use ----> Q05 moat ----+
```

Parallel work is allowed where evidence is independent, but closure dependencies are strict:
- Q05 cannot be considered strong without Q03 repeat-use evidence;
- Q04 research may run before Q02 commercial closure only on data that is legally/contractually usable for that research purpose;
- Q01 counsel must review the actual interaction model validated by Q03, not a materially different mock;
- Q02 must close on the exact data profile intended for MK1, not a generic provider claim.

---

## MK1 Bootstrap Profile

Once Q01–Q05 reach a promotable state, MK0 creates one immutable candidate `MK1_BOOTSTRAP_PROFILE` containing:

```text
profile_id
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

Implementation may not silently substitute another provider, asset universe, flow, price-sensitive capability, risk policy or ML scope.

Material change requires:
1. impact analysis;
2. affected lock reopened where necessary;
3. new/superseding evidence receipt;
4. new bootstrap-profile version.

---

## Promotion review packet

Before production MK1 begins, the review packet must contain:

1. finalized Q01 receipt;
2. finalized Q02 receipt(s) for every initial production data profile;
3. finalized Q03 experiment bundle;
4. finalized Q04 baseline receipt and explicit ML include/exclude decision;
5. finalized Q05 receipt;
6. contradiction log across all receipts;
7. updated `MK0_LOCKS.md`;
8. updated canonical product/data/quant/regulatory docs;
9. candidate `MK1_BOOTSTRAP_PROFILE`;
10. architecture impact review confirming no new unresolved P0/P1 internal node.

No “overall green” may conceal a failed fatal lock.

---

## Contradiction handling

Evidence can close one question while reopening another.

Examples:
- users strongly prefer personalized ranking, but counsel rejects that flow;
- the best data provider is legally usable but destroys unit economics;
- a quant model works only with a data family whose commercial rights are unavailable;
- the validated persona values the product but not at a viable price;
- moat evidence depends on a workflow removed by regulatory constraints.

When this occurs:
1. record the contradiction explicitly;
2. identify affected locks/docs;
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
- no merging mixed cohorts until cohort definitions are documented;
- no performance or regulatory claim beyond the exact scope of the receipt.

---

## Closure criterion for MK0

MK0 can promote to production MK1 implementation only when:
- Q01–Q05 have promotable final receipts;
- all constraints from conditional receipts are frozen into canonical specs;
- the `MK1_BOOTSTRAP_PROFILE` exists;
- no cross-receipt contradiction capable of materially changing MK1 boundaries remains unresolved;
- `BUILD_READINESS.md` is satisfied;
- no external/empirical result was silently converted into an internal assumption.

At that point MK0 is not claiming that the product will succeed. It is claiming something narrower and defensible:

> **The first production configuration has earned the right to be built.**
