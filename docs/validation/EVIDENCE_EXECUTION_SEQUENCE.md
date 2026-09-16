# MK0 Evidence Execution Sequence

## Purpose

This document turns the closed evidence methodology into an executable order of operations.

The goal is to minimize wasted work, prevent circular validation and ensure later evidence is collected against the same product/data configuration that earlier evidence actually justified.

Production MK1 implementation remains blocked throughout this sequence.

---

## Execution principles

1. **Run cheap falsification before expensive validation.**
2. **Do not send counsel a product flow that user evidence is likely to replace immediately.**
3. **Do not buy/commit to data before exact product/data needs are sufficiently constrained.**
4. **Do not test ML before the deterministic harness is valid.**
5. **Do not claim moat before repeat use exists.**
6. **Do not average contradictions away.**
7. **Every empirical threshold is frozen before outcome inspection.**
8. **Every final result produces an immutable EvidenceReceipt.**

---

# Stage 0 — Evidence environment bootstrap

## Required before any Q03/Q04/Q05 outcome collection

- instantiate `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` per experiment;
- assign experiment ID/version;
- freeze primary measures/decision rules;
- freeze recruitment/dataset inclusion/exclusion;
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
- cheapest way to falsify the persona/wedge;
- prevents polishing a Translator for a problem users do not repeatedly experience;
- informs which interaction model Q01 should eventually review.

## Gate

Run `E03-A` from `experiments/q03/Q03_PREREGISTRATION.md`.

### If STOP

- stop Translator/UX validation for the current persona;
- create Q03 receipt;
- update persona/JTBD hypotheses;
- reopen affected product-evidence rows;
- do not continue to Q01 with the old flow.

### If CONDITIONAL

- narrow persona;
- update prototype targeting;
- continue only with the narrowed cohort.

### If PASS

Proceed to Stage 2.

---

# Stage 2 — Q03-B Translator / Evidence Representation

Run the objective comprehension/efficiency comparison against the frozen candidate representation.

## Gate

### STOP

Rework representation; do not use the failed representation for:
- Q01 counsel review;
- E03-C repeat-use;
- E05 comparative moat evidence.

### CONDITIONAL

Freeze narrowed task/cohort and repeat the material parts that changed.

### PASS

The candidate interaction is stable enough for repeat-use evidence and preliminary legal packaging.

---

# Stage 3 — Parallel foundation tracks

Once E03-B is at least promotable for one candidate interaction, three tracks can run in parallel where practical.

## Track 3A — Q03-C Repeat Use

Run 14-day repeat-use experiment.

Purpose:
- determine whether novelty becomes repeated workflow use;
- provide required input to Q05.

## Track 3B — Q04-A Deterministic Harness

Instantiate one research-permitted data profile and validate the research engine.

Purpose:
- close mechanics before any ML experiment;
- discover provider/data-semantic issues early.

Constraint:
- data used must be allowed for the research purpose even if Q02 commercial production rights are not yet closed.

## Track 3C — Q01 Review Packet Assembly

Prepare but do not necessarily finalize counsel review until the exact interaction/prototype digest is frozen.

Assemble:
- F01–F16 flow inventory;
- exact claim/copy set;
- prototype/screens;
- pricing/entitlement candidate;
- disclaimers/terms candidate.

If E03-C materially changes the interaction/wedge, refresh the packet before freezing for counsel.

---

# Stage 4 — Q03-D Pricing and Q02 Candidate Data Profiles

## Q03-D Pricing / Commitment

Start Stage-1 pricing signal only after participants can understand the product being priced.

Do not collect payment until the commercial flow is legally/operationally appropriate.

The purpose is to constrain:
- viable price hypotheses;
- entitlement structure;
- unit-economics assumptions.

## Q02 candidate profiles

Now enumerate provider/data profiles matching the validated product surface rather than generic market-data wish lists.

For each candidate:
- instantiate `docs/validation/q02/DATA_USE_PROFILE_PACKET.md`;
- collect authority evidence;
- collect quotes/costs;
- model required uses;
- assess fallback compatibility.

Do not choose a provider solely because its technical API is convenient.

---

# Stage 5 — Q01 Counsel Review

Freeze the exact candidate MK1 interaction set and send `REGULATORY_REVIEW_PACKET.md` to qualified counsel.

Inputs should reflect:
- Q03-supported persona/wedge;
- candidate pricing/entitlements;
- portfolio-context behavior;
- Translator/Evidence/Strategy Sandbox semantics;
- any model/probability surface still proposed;
- actual claims/copy.

## After counsel response

Create:
- Q01 EvidenceReceipt;
- constraints promoted into canonical product/copy/API docs;
- contradictions against Q03/Q02/Q04 as needed.

If counsel requires material UX re-scope, affected user evidence may need to be re-run for the changed flow.

---

# Stage 6 — Q02 Production Data Closure

Finalize exact production `DataUseProfile`s only after:
- product surface is sufficiently stable;
- Q01 conditions that affect display/personalization are known;
- pricing/unit-economics assumptions are concrete enough to evaluate provider cost.

## Required result

One of:
- viable primary provider/profile + approved fallback group(s);
- viable primary profile with explicit no-fallback degradation behavior;
- pivot to narrower/derived-only data surface;
- stop current configuration if mandatory rights/economics cannot be satisfied.

Q02 closure freezes:
- provider set;
- asset universe;
- data families;
- rights/retention/entitlements;
- cost assumptions;
- fallback groups.

---

# Stage 7 — Q04-B Optional ML

Entry conditions:
- Q04-A PASS;
- dataset/profile used for intended MK1 model role is rights-compatible for that use;
- exact feature availability semantics frozen.

Run ML only if there is still a product reason to do so.

Possible successful outcomes:
- `INCLUDE`;
- `EXCLUDE`;
- `DEFER`.

Do not delay MK1 merely because ML fails if deterministic intelligence already satisfies the product thesis.

---

# Stage 8 — Q05 Competitive Durability

Entry conditions:
- E03-C repeat-use evidence exists;
- candidate flow reflects material Q01 constraints;
- product surface uses Q02-compatible data semantics;
- enough of the experience is stable for a fair comparative task.

Run:
- E05-A competitive task;
- E05-B repeat-use linkage;
- E05-C replicability assessment.

A valid outcome may be:
- supported candidate moat;
- `LEARNING_WEDGE` conditional closure;
- pivot;
- stop current configuration.

---

# Stage 9 — Unit Economics Synchronization

Before promotion, synchronize `docs/economics/UNIT_ECONOMICS.md` with observed/authoritative inputs:
- Q02 provider/data costs;
- compliance/legal recurring cost assumptions where known;
- Q03 pricing/commitment evidence;
- infrastructure workload assumptions;
- payment fees/tax assumptions if applicable and verified;
- support burden observed in Q03.

Do not treat TAM or optimistic conversion as a substitute for unit economics.

If the candidate is structurally nonviable at the validated price/data configuration, create a contradiction and pivot before build.

---

# Stage 10 — Cross-Receipt Contradiction Review

Instantiate `docs/validation/CONTRADICTION_LOG_TEMPLATE.md` for every material mismatch.

Review at minimum:
- Q01 vs Q03 interaction/personalization;
- Q01 vs pricing/claims;
- Q02 vs Q04 feature/data requirements;
- Q02 cost vs Q03 price;
- Q03 repeat-use vs Q05 moat hypothesis;
- Q05 supported advantage vs Q01/Q02 constraints;
- any evidence-driven selection vs closed internal design invariants.

No P0/P1 contradiction may remain open.

---

# Stage 11 — Promotion Packet and Bootstrap Profile

Only after Q01–Q05 are promotable:

1. instantiate `MK0_PROMOTION_PACKET`;
2. attach final EvidenceReceipts;
3. attach contradiction log;
4. run architecture-impact review;
5. generate candidate `MK1_BOOTSTRAP_PROFILE` from frozen outputs only;
6. verify `BUILD_READINESS` line-by-line;
7. approve or reject the packet.

No manual value should be inserted into the bootstrap profile without a receipt/closed-contract source.

---

# Stage 12 — Production MK1 Authorization

Only an `APPROVED` promotion packet plus `APPROVED` bootstrap profile unlocks production MK1 implementation.

At that moment:

```text
MK0 validation execution  -> CLOSED FOR THIS PROFILE
MK1 production build      -> OPEN
Q01–Q05 historical receipts -> immutable
future material change    -> reopens affected scope
```

---

## Parallelism matrix

| Workstream | Can run early? | Must wait for |
|---|---|---|
| E03-A discovery | Yes | Stage 0 |
| E03-B Translator test | No | E03-A promotable candidate |
| E03-C repeat use | No | E03-B promotable representation |
| E03-D pricing | Partial | users understand product; legal boundary respected |
| Q04-A harness | Yes, parallel | research-permitted data + Stage 0 |
| Q04-B ML | No | Q04-A PASS + rights-compatible intended features |
| Q01 packet assembly | Partial | candidate interaction exists |
| Q01 final review | No | frozen candidate flow/copy |
| Q02 provider discovery | Yes | candidate product needs known enough |
| Q02 final production profile | No | product/legal/pricing constraints sufficiently stable |
| Q05 | No | repeat-use evidence + stable candidate flow |
| Promotion packet | No | Q01–Q05 promotable + contradictions resolved |

---

## Global stop conditions

Pause the affected track immediately when:
- a fatal legal/data-rights contradiction appears;
- experiment instrumentation invalidates primary measures;
- required authority cannot be obtained;
- point-in-time leakage is discovered in Q04;
- the prototype version materially changes after pre-registration;
- participant/data consent or rights are uncertain;
- a result would require changing a primary threshold after inspection to pass.

Stopping is evidence discipline, not failure.

---

## Final execution invariant

> The next task is always the cheapest valid action that can still falsify the current candidate configuration.

This keeps MK0 from becoming an endless research program while also preventing premature production code.
