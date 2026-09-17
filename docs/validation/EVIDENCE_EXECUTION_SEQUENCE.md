# MK0 Evidence Execution Sequence

## Purpose

This document turns the closed evidence methodology into an executable order of operations.

The goal is to minimize wasted work, prevent circular validation and ensure later evidence is collected against the same product/data configuration that earlier evidence actually justified.

Production MK1 implementation remains blocked throughout this sequence.

Canonical semantic normalization: `docs/validation/CANONICAL_VALIDATION_SPEC.md`.
Authority hierarchy: `docs/validation/NORMATIVE_DOCUMENT_HIERARCHY.md`.
Layered thesis: `docs/product/THESIS_STACK.md`.
Core causal-value gate: `docs/validation/Q00_CORE_CAUSAL_VALUE.md`.

---

## Execution principles

1. **Run cheap falsification before expensive validation.**
2. **A competent simple baseline must be allowed to defeat SOPHROSYNE.**
3. **Do not collect WTP as if it proves value before Q00 shows incremental causal/product value.**
4. **Do not send external legal reviewers a product flow that Q00/Q03 is likely to replace immediately.**
5. **Do not buy/commit to data before exact product/data needs are sufficiently constrained.**
6. **Do not test ML before the deterministic harness is valid.**
7. **Do not claim moat before core causal value and repeat use exist.**
8. **Do not average contradictions away.**
9. **Every empirical threshold is frozen before outcome inspection.**
10. **Every final result produces an immutable EvidenceReceipt.**
11. **Initial promotable geography is Peru; external evidence cannot silently broaden jurisdiction.**
12. **An `INCONCLUSIVE` result never advances a stage that requires a promotable result.**

---

# Stage 0 — Evidence environment bootstrap

## Required before any Q00/Q03/Q04/Q05 outcome collection

- instantiate `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` per experiment;
- assign experiment ID/version;
- freeze primary measures/decision rules;
- freeze minimum practically meaningful effects;
- freeze recruitment/dataset inclusion/exclusion;
- freeze promotion geography/eligible population where applicable;
- freeze compensation/incentive rules for human research;
- create raw-artifact destination;
- create analysis-artifact destination;
- assign owner + independent reviewer;
- verify no participant/dataset rights constraint is being ignored;
- freeze product/prototype digest used by the experiment.

## Output

`PRE_REGISTERED` manifests only.

No outcome data should be inspected before this stage is complete.

---

# Stage 1 — Q03-A Behavioral Discovery

## Run first

Why:
- cheapest way to falsify the persona/problem;
- prevents building a causal-value experiment for a problem users do not repeatedly experience;
- constrains the tasks used by Q00;
- informs which interaction model Q01 should eventually review.

## Gate

Run `E03-A` from `experiments/q03/Q03_PREREGISTRATION.md`.

### If STOP_CURRENT_CONFIGURATION

- stop Q00/Translator validation for the current persona;
- preserve the stopped configuration receipt;
- update persona/JTBD hypotheses;
- do not continue to Q01 with the old flow.

### If CLOSED_CONDITIONAL

- narrow persona;
- update prototype targeting;
- run Q00 only with the narrowed cohort;
- preserve original evidence as historical scope.

### If CLOSED_PASS

Proceed to Stage 2.

### If INCONCLUSIVE

Resolve sample/recruitment/instrumentation validity and rerun/review as pre-registered. Do not advance on intuition.

---

# Stage 2 — Q00-A Early causal-value falsification + Q03-B representation

This stage deliberately tries to kill unnecessary product complexity before repeat-use, pricing, legal review or provider commitment.

## Q00-A required comparison

At minimum compare the candidate interaction against:
- raw-information control;
- stateless structured assistance;
- the five-question dumb-friction checklist;
- simple prediction/confidence/outcome feedback where the task permits.

Measure preregistered primary outcomes such as:
- calibration;
- contradiction detection;
- uncertainty recognition;
- process/outcome separation;
- unnecessary-action rate;
- task time/cognitive burden.

## Q03-B representation test

Run the objective Translator/Evidence representation comparison in the same evidence family where compatible, but do not let subjective preference substitute for Q00 primary outcomes.

## Gate

### Q00-A STOP_CURRENT_CONFIGURATION

If simple/cheap baselines capture the meaningful effect and no narrower mechanism survives:
- stop the current product configuration;
- do not run pricing, moat, legal or production-data closure for the rejected configuration;
- update product thesis/components before new testing.

### Q00-A CLOSED_CONDITIONAL

If a smaller intervention survives:
- freeze the narrower mechanism;
- remove/defer unsupported complexity;
- ensure subsequent Q03/Q01/Q05 work uses the narrowed configuration.

### Q00-A CLOSED_PASS

Proceed with the candidate mechanism into longitudinal falsification.

### INCONCLUSIVE

Do not advance expensive validation. Resolve evidence quality first.

Q03-B may independently require representation changes; any material change reopens the affected Q00-A comparison.

---

# Stage 3 — Longitudinal causal/product evidence + quant foundation

Once one Q00-A/Q03-B candidate is promotable, parallel tracks may run.

## Track 3A — Q03-C Repeat Use

Run the 14-day repeat-use experiment.

Purpose:
- determine whether novelty becomes repeated workflow use;
- provide behavioral evidence for Q00-B and Q05.

## Track 3B — Q00-B Memory / transfer / outcome-blind falsification

Run the longitudinal destructive tests defined by Q00 as applicable:
- stateless vs simple feedback vs short memory vs full memory;
- hidden-rubric evaluation;
- outcome-blind process-quality test;
- assisted vs unassisted transfer;
- delayed transfer where feasible;
- regime/context transfer where pre-registered;
- cognitive-cost comparison.

Possible scoped findings include:
- `MEMORY_EXCLUDED`;
- `SHORT_MEMORY_SUFFICIENT`;
- `FULL_MEMORY_SUPPORTED`;
- assisted-only value;
- supported transfer;
- current configuration stopped/pivoted.

These component findings do not replace the terminal Q00 decision.

## Track 3C — Q04-A Deterministic Harness

Instantiate one research-permitted data profile and validate the research engine.

Purpose:
- close mechanics before any ML experiment;
- discover provider/data-semantic issues early.

Constraint:
- research-permitted data is not automatically production-permitted.

## Track 3D — Q01 Review Packet Assembly

Prepare but do not finalize external review until Q00/Q03 has frozen the interaction scope.

Assemble:
- F01–F20 flow inventory;
- exact claim/copy set;
- prototype/screens;
- candidate pricing/entitlements;
- privacy/data-flow/consent artifacts;
- candidate subscription/payment/cancellation flow where applicable;
- required authority coverage by legal/compliance surface.

If Q00-B or E03-C materially narrows the interaction/wedge, refresh the packet before external review.

---

# Stage 4 — Q00 final causal decision

Before serious pricing interpretation, final legal review, production rights closure or moat claims, issue the Q00 EvidenceReceipt for the candidate intervention.

Required inputs:
- Q00-A early baseline results;
- Q00-B longitudinal/ablation/transfer results where applicable;
- dependency/effective-sample corrections;
- cognitive-cost analysis;
- realistic cheap/free substitute comparison where operationally available.

## Gate

### CLOSED_PASS
Proceed with the supported intervention scope.

### CLOSED_CONDITIONAL
Proceed only with frozen exclusions/deferred components and claim limitations.

### PIVOT_REQUIRED
Update product thesis/wedge/components and re-run affected downstream evidence.

### STOP_CURRENT_CONFIGURATION
Stop the current independent-product configuration. Do not allow WTP, ML or moat arguments to rescue it.

### INCONCLUSIVE
Do not advance expensive validation that assumes product value is established.

---

# Stage 5 — Q03-D Pricing and Q02 Candidate Data Profiles

Entry condition: Q00 must be promotable for the exact intervention being priced.

## Q03-D Pricing / Commitment

Start pricing signal only after participants can understand the product and Q00 has established material incremental value for the candidate intervention.

Until Q01 authorizes the exact commercial charging flow, pricing evidence is research-only/non-charge and must follow the non-deceptive commitment contract.

Positive pricing intent cannot retroactively rescue weak Q00 evidence.

## Q02 candidate profiles

Enumerate provider/data profiles matching only the Q00/Q03-supported surface.

For each candidate:
- instantiate `docs/validation/q02/DATA_USE_PROFILE_PACKET.md`;
- collect current authority evidence and effective/expiry dates;
- collect quotes/costs;
- model required uses;
- assess fallback compatibility;
- freeze reopen triggers.

Do not purchase data complexity removed by Q00 merely because it was in the original vision.

---

# Stage 6 — Q01 External Legal / Compliance Review

Freeze the exact Q00/Q03-supported candidate interaction set and send `REGULATORY_REVIEW_PACKET.md` to the required qualified external authority set.

Inputs reflect:
- Q00-supported intervention and claim scope;
- Q03-supported Peru persona/wedge;
- candidate pricing/entitlements;
- portfolio-context behavior;
- surviving Translator/Evidence/Strategy semantics;
- actual claims/copy;
- privacy/consent/data flows;
- subscription/payment/cancellation flow where applicable.

If external review materially re-scopes the flow, affected Q00/Q03 evidence may need to be repeated.

---

# Stage 7 — Q02 Production Data Closure

Finalize exact production `DataUseProfile`s only after product surface, Q00 scope, Q01 constraints and pricing assumptions are sufficiently stable.

Q02 promotable closure freezes:
- provider set;
- asset universe;
- data families still required by supported intervention;
- rights/retention/entitlements;
- evidence freshness/review dates;
- cost assumptions;
- fallback groups.

`INCONCLUSIVE` rights are never promotable.

---

# Stage 8 — Q04-B Optional ML

Entry conditions:
- Q04-A `CLOSED_PASS`;
- Q00 has not excluded the proposed ML role as unnecessary complexity;
- intended data use is rights-compatible;
- exact feature availability semantics frozen.

Run ML only if there is still a product reason to do so.

Possible outcomes after a valid harness:
- `INCLUDE`;
- `EXCLUDE`;
- `DEFER`.

ML success cannot rescue failed Q00 causal value.

---

# Stage 9 — Q05 Competitive Durability

Entry conditions:
- Q00 promotable final receipt exists;
- E03-C repeat-use evidence exists;
- candidate flow reflects material Q01 constraints;
- product surface uses Q02-compatible data semantics;
- promoted Q03 persona/geography is frozen.

Q05 may assess defensibility only for components still allowed by Q00/Q01/Q02.

No persistent memory, LLM, translation, backtesting, Decision Record or other feature is moat merely because it exists.

---

# Stage 10 — Unit Economics Synchronization

Synchronize `docs/economics/UNIT_ECONOMICS.md` with:
- Q00-supported scope/cognitive burden;
- Q02 provider/data costs;
- compliance/legal recurring cost assumptions;
- Q03 pricing/commitment evidence;
- infrastructure workload assumptions;
- support burden.

If the validated intervention is useful but structurally nonviable at the observed price/cost structure, T4 economic thesis fails for that configuration even if T2/T3 survive.

---

# Stage 11 — Cross-Receipt Contradiction Review

Review at minimum:
- Q00 supported/excluded components vs Q03 WTP/repeat-use;
- Q00 vs Q04 proposed complexity;
- Q00 vs Q05 moat narrative;
- Q01 vs Q03 interaction/personalization;
- Q02 vs Q04 feature/data requirements;
- Q02 cost vs Q03 price;
- geography/user-class compatibility;
- evidence freshness/expiry;
- evidence-driven selections vs closed internal invariants.

No P0/P1 contradiction may remain open.

---

# Stage 12 — Promotion Packet and Bootstrap Profile

Only after Q00–Q05 applicable evidence is promotable:

1. instantiate `MK0_PROMOTION_PACKET`;
2. attach Q00 and Q01–Q05 final receipts;
3. attach contradiction log;
4. verify provenance/traceability field-by-field;
5. run architecture-impact review;
6. generate `MK1_BOOTSTRAP_PROFILE` from frozen outputs only;
7. verify that Q00 exclusions are encoded as build constraints;
8. verify `BUILD_READINESS` line-by-line;
9. approve or reject the packet.

A missing producer, conflicting producer, stale producer or unpropagated Q00 exclusion blocks approval.

---

# Stage 13 — Production MK1 Authorization

Only an `APPROVED` promotion packet plus `APPROVED` bootstrap profile and a passing `BUILD_READINESS` gate unlock production MK1 implementation.

Promotion is profile-specific, not a permanent authorization for all future SOPHROSYNE configurations.

---

## Parallelism matrix

| Workstream | Can run early? | Must wait for |
|---|---|---|
| E03-A discovery | Yes | Stage 0 |
| Q00-A / E03-B | No | E03-A promotable candidate |
| E03-C repeat use | No | Q00-A/E03-B promotable representation |
| Q00-B memory/transfer | No | Q00-A candidate + sufficient longitudinal design |
| Q03-D pricing | No for promotable interpretation | final/promotable Q00 candidate |
| Q04-A harness | Yes, parallel | research-permitted data + Stage 0 |
| Q04-B ML | No | Q04-A CLOSED_PASS + Q00-compatible role + rights-compatible features |
| Q01 packet assembly | Partial | candidate interaction exists |
| Q01 final external review | No | Q00/Q03 frozen candidate flow/copy/privacy/commercial surface |
| Q02 provider discovery | Yes | candidate needs known enough |
| Q02 final production profile | No | Q00/product/legal/pricing constraints sufficiently stable |
| Q05 | No | final Q00 + repeat-use + stable candidate flow |
| Promotion packet | No | Q00–Q05 applicable gates promotable + contradictions resolved |

---

## Global stop conditions

Pause the affected track immediately when:
- Q00 simple/cheap baselines eliminate material incremental value;
- a fatal legal/data-rights contradiction appears;
- experiment instrumentation invalidates primary measures;
- required authority cannot be obtained;
- point-in-time leakage is discovered in Q04;
- the prototype version materially changes after pre-registration;
- participant/data consent or rights are uncertain;
- a result would require changing a primary threshold after inspection to pass;
- promotion geography/population no longer matches the evidence;
- a build-defining receipt becomes stale/superseded.

Stopping is evidence discipline, not failure.

---

## Final execution invariant

> The next task is always the cheapest valid action that can still falsify the current candidate configuration. SOPHROSYNE earns complexity only after simpler alternatives fail to explain the observed value.
