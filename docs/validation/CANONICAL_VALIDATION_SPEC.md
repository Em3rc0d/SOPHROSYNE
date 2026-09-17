# Canonical Validation Specification

## Status and precedence

This document is the normative semantic layer for MK0 external/empirical validation. It does **not** replace the detailed packets, preregistrations, statistical rules, instrumentation contracts, promotion packet, bootstrap profile or build-readiness contract. Those documents retain their full detail.

When a supporting validation document conflicts with this file on lifecycle vocabulary, decision outcome, geography, denominator semantics, evidence authority or promotion eligibility, **this file wins** until the conflict is incorporated into a future superseding canonical revision.

No rule in this file closes Q00–Q05 by itself. Evidence still has to exist.

---

## 1. One lifecycle, one outcome vocabulary

Artifact lifecycle and decision outcome are different fields.

### Evidence artifact lifecycle

```text
DRAFT
PRE_REGISTERED
EVIDENCE_RUNNING
REVIEW_READY
FINAL
SUPERSEDED
```

### Final decision outcome

Exactly one of:

```text
CLOSED_PASS
CLOSED_CONDITIONAL
PIVOT_REQUIRED
STOP_CURRENT_CONFIGURATION
INCONCLUSIVE
```

`INCONCLUSIVE` is a valid terminal result for an experiment/review version but **never authorizes MK1 promotion**. A new evidence version may be run later.

Aliases such as `PASS`, `CONDITIONAL_PASS`, `STOP`, `FAIL` or `FINAL` must not be used as aggregate Q outcomes unless explicitly mapped to the canonical vocabulary.

---

## 2. Promotion eligibility

Only `CLOSED_PASS` and `CLOSED_CONDITIONAL` receipts may contribute affirmative promotion evidence.

`PIVOT_REQUIRED`, `STOP_CURRENT_CONFIGURATION` and `INCONCLUSIVE` block promotion of the affected configuration.

No Q may be treated as closed from prose, issue comments, screenshots, demos or undocumented verbal approval. Closure requires an immutable `EvidenceReceipt` with the authoritative artifacts and decision rule attached.

No unresolved P0 or P1 contradiction may exist in the cross-receipt contradiction log at promotion time.

Evidence supporting one configuration does not authorize a broader configuration.

Q00 is an independent causal gate. Q03 willingness-to-pay, Q04 modeling sophistication or Q05 defensibility evidence cannot compensate for a failed Q00 configuration.

---

## 3. Geography and population scope

Initial MK1 promotion is **Peru-scoped** unless a later promotion packet explicitly freezes another jurisdiction after equivalent evidence.

Therefore:

- Q00 primary promotable causal-value evidence must use the Peru target population or a pre-registered Peru confirmation cohort sufficient for the gate; non-Peru evidence may remain exploratory/supportive only.
- Q01 legal authority is Peru-specific.
- Q03 primary promotable demand evidence must represent the Peru target population or contain a pre-registered Peru confirmation cohort large enough to satisfy the relevant gate.
- Non-Peru LATAM/global participants may be exploratory, diagnostic or comparative but cannot silently substitute for Peru evidence.
- Q05 promotable preference/moat evidence must use the Q03-frozen persona and the same promotion geography, or explicitly remain exploratory.
- Q02 geography/user classification must be compatible with the promoted Peru configuration.

Any generalization beyond the observed population is prohibited in canonical claims.

---

## 4. Q00 — core causal-value scope

Q00 tests whether the candidate SOPHROSYNE intervention creates material incremental decision-process value beyond simpler and cheaper substitutes under controlled, non-production tasks.

Detailed execution authority: `experiments/q00/Q00_PREREGISTRATION.md`.

A promotable Q00 run must preserve, where applicable, destructive comparison against:
- raw-information control;
- stateless structured assistance;
- five-question deliberate-friction baseline;
- simple feedback;
- short-memory SOPHROSYNE;
- full candidate SOPHROSYNE;
- strongest realistic cheap/free substitute frozen before outcome inspection.

Required analyses include simple-friction ablation, memory ablation, outcome-blind evaluation, hidden-rubric evaluation, assisted-vs-unassisted transfer, regime/context transfer, dependence correction, cognitive/time-cost comparison, cheap-substitute comparison and the economic bridge to Q03.

Canonical Q00 rules:
- if the five-question friction arm captures at least 80% of the preregistered benefit attributable to the full candidate on the mandatory decision rule, full-complexity causal advantage is not established for the tested scope;
- if short-memory and full-memory variants do not differ materially, full memory is not earned;
- if assisted performance improves but preregistered unassisted transfer does not, claims remain `ASSISTED_ONLY`;
- if a competent cheap/free substitute is non-inferior within the preregistered margin, the current independent full-product configuration is not promotable without material narrowing/pivot;
- a small quality gain may fail when added time/effort exceeds the preregistered acceptable cognitive-cost boundary.

A `CLOSED_CONDITIONAL` Q00 receipt may promote a narrower intervention only if excluded/deferred components are propagated into canonical specs, graph reachability and the `MK1_BOOTSTRAP_PROFILE`.

A failed or inconclusive Q00 blocks promotion of the affected configuration regardless of downstream Q03/Q04/Q05 results.

---

## 5. Q01 — legal/compliance scope

Q01 remains one lock, but the review bundle must address all **applicable MK1 commercial legal surfaces**, not only investment-advice classification.

At minimum the authoritative review packet must resolve or explicitly mark not applicable:

1. securities/advisory/recommendation/intermediation posture;
2. product claims and financial marketing wording;
3. personal-data/privacy implications of portfolio, profile, telemetry and research data;
4. consumer/e-commerce/subscription obligations applicable to the paid flow;
5. payment/billing constraints where a paid pilot or subscription is activated;
6. terms, disclaimers, consent and recordkeeping requirements;
7. user/geographic eligibility restrictions;
8. re-review triggers for broker connectivity, execution, custody, copy trading, leverage/derivatives, B2B distribution or new jurisdictions.

Different specialists may provide different sub-opinions. The final Q01 receipt must enumerate the authority covering each applicable surface. Silence is not approval.

A disclaimer cannot cure a feature that counsel classifies as impermissible under the chosen posture.

Pricing experiments performed before commercial clearance must remain research-only/non-charge unless the exact charging flow is independently authorized.

---

## 6. Q02 — data rights semantics

Q02 closes per versioned `DataUseProfile`, never “for a provider in general”.

For each production profile, authoritative evidence must cover all applicable dimensions:

- provider/product;
- instrument family and exact universe;
- historical/realtime/delay;
- geography and end-user classification;
- raw storage and retention;
- cache TTL;
- display and non-display use;
- external redistribution;
- derived-data use;
- embeddings/model/LLM use where applicable;
- attribution;
- entitlements;
- commercial cost model;
- termination/revocation consequences;
- fallback compatibility.

`UNKNOWN` rights resolve to `DENY` until authoritative evidence says otherwise.

Q02 result vocabulary includes `INCONCLUSIVE`.

A provider or terms change reopens only affected profiles but blocks any bootstrap profile depending on them until reconciliation completes.

---

## 7. Q03 — demand, comprehension, repeat use and pricing

The detailed Q03 preregistration remains authoritative for numeric thresholds except the corrections below.

### E03-A primary sample correction

The primary cohort must itself be capable of satisfying the minimum usable primary gate.

Use:

```yaml
target_n: 28-32
minimum_usable_primary_n: 20
primary_cohort_target: 20-24
secondary_exploratory_target: 4-8
```

Exploratory participants do not count toward the primary minimum unless pooling was pre-registered before outcome inspection.

### Compensation

Participant compensation must never depend on desired behavior, return frequency, preference, willingness to pay or commitment outcome.

Any pricing/commitment cohort in which compensation could materially distort economic intent must be stratified and analyzed separately; it cannot be the sole evidence for a promotable paid-band conclusion.

### Pricing

Before Q01 permits a real charging flow, E03-D may measure only non-deceptive research intent / high-friction commitment without executing a charge.

A real paid pilot becomes stronger evidence only after the exact paid flow is legally and operationally permitted.

### Promotion geography

Promotable Q03 evidence must satisfy the geography rule in section 3.

### Q00 compatibility

Persona, wedge, pricing and repeat-use evidence used for promotion must describe the intervention scope/components that survived Q00. Q03 cannot reintroduce Q00-rejected complexity by commercial preference alone.

---

## 8. Q04 — quant harness and ML aggregation

Q04-A and Q04-B remain distinct.

### Q04-A

Valid aggregate outcomes:

```text
CLOSED_PASS
PIVOT_REQUIRED
STOP_CURRENT_CONFIGURATION
INCONCLUSIVE
```

If E04-A is `INCONCLUSIVE`, aggregate Q04 cannot close for MK1 and Q04-B cannot authorize ML promotion.

### Q04-B

ML remains optional. After Q04-A passes:

```text
ml_scope = INCLUDE | EXCLUDE | DEFER
```

`EXCLUDE` or `DEFER` can coexist with a successful Q04 closure; they do not invalidate SOPHROSYNE.

All numeric Q04 promotion gates remain governed by the detailed preregistration and `STATISTICAL_DECISION_RULES.md`.

No Q04 result creates a future-performance or profitability marketing claim.

Q04 complexity cannot override Q00 causal-value conclusions or reintroduce a Q00-excluded product component without a superseding evidence path.

---

## 9. Q05 — moat denominators and wording

The detailed Q05 preregistration remains authoritative except for these corrections.

### Exposure-aware component denominators

For candidate component `Cxx`, adoption/longitudinal rates use only eligible repeat users who actually had a valid opportunity to access that component under the frozen prototype configuration.

```text
U1 = exposed eligible repeat users using component in >=2 sessions
     / exposed eligible repeat users

U3 = exposed eligible repeat users using component after day 7
     / exposed eligible repeat users
```

U2 uses the same exposure-aware denominator unless the manifest pre-registers and justifies another denominator.

The denominator and exposure rule must be reproducible from telemetry.

### “Usage disappears” threshold

Replace qualitative wording with a numeric default:

```text
negative longitudinal evidence if U3 < 15%
```

with at least the preregistered minimum denominator. A future manifest may freeze another threshold before outcomes are inspected.

### Claim discipline

Technical complexity alone is not defensibility. `LEARNING_WEDGE` remains a valid `CLOSED_CONDITIONAL` state; it does not authorize “we have a moat” marketing language or large scale-spend assumptions.

A component excluded or materially weakened by Q00 cannot remain a promotable moat claim without a new/superseding evidence path.

---

## 10. Statistical and instrumentation precedence

`docs/validation/STATISTICAL_DECISION_RULES.md` defines computation semantics unless an experiment manifest freezes a justified alternative **before outcome inspection**.

Key invariants include:

- full precision for decisions;
- explicit numerator/denominator;
- participant-level aggregation where repeated observations would otherwise inflate n;
- Wilson interval semantics as documented;
- per-participant calibration gap before averaging;
- dependence-aware resampling for market returns;
- frozen seeds/search budgets;
- no sequential peeking unless preregistered;
- fatal protocol deviation => `INCONCLUSIVE` / rerun.

Q00/Q03/Q05 telemetry is promotion-grade only if the relevant instrumentation/data-quality gates pass. If an instrumentation defect affects more than 10% of observations required by a primary metric, that metric cannot pass without a preregistered recovery rule or a new experiment version.

---

## 11. Bootstrap provenance contract

Every non-null field in `MK1_BOOTSTRAP_PROFILE` must trace to an allowed producer:

| Bootstrap field family | Required producer(s) |
|---|---|
| Q00 intervention scope / excluded components | Q00 |
| jurisdiction / eligible users | Q01 + promotion packet |
| primary persona / JTBD / wedge | Q03, constrained by Q00 |
| pricing hypothesis / paid-flow constraint | Q03 + Q01, constrained by Q00 scope |
| provider / data families / rights / entitlements / retention / attribution | Q02 |
| exact asset universe | intersection of Q02-authorized universe and Q04-validated universe |
| freshness / staleness profile | Q02 production profile + closed internal market-data semantics |
| portfolio-context scope | Q01 + closed product scope contract |
| legal copy / claims / disclaimers / consent constraints | Q01 |
| baseline harness / cost model / benchmark versions | Q04 |
| `ml_scope` / promoted model family | Q04 |
| moat status / supported components / scale-spend constraint | Q05, constrained by Q00 |
| risk-policy version | closed internal risk contract + promotion packet |
| feature flags / excluded features | combined Q00–Q05 constraints + promotion packet |

If two producers disagree, create a contradiction record. Do not choose manually during implementation.

---

## 12. Contradiction severity and resolution

Canonical severity:

```text
P0  would make promoted configuration illegal, unauthorized, unsafe, scientifically invalid or materially impossible
P1  materially changes scope, economics, persona, data rights, claims or promoted model behavior
P2  bounded non-blocking inconsistency with documented mitigation
P3  editorial/metadata inconsistency with no effect on promoted behavior
```

P0/P1 must be resolved before `MK0_PROMOTION_PACKET` approval.

Resolution may narrow the bootstrap configuration. It may never widen evidence by interpretation.

Examples include Q03 demand for complexity rejected by Q00, Q05 moat claims depending on Q00-excluded components, legal rejection of a preferred Q03 flow, or Q04 dependence on Q02-denied data.

---

## 13. Promotion chain

There is one authorization path:

```text
pre-registered Q00–Q05 evidence
  -> immutable EvidenceReceipts
  -> contradiction review
  -> approved MK0_PROMOTION_PACKET
  -> immutable MK1_BOOTSTRAP_PROFILE
  -> BUILD_READINESS
  -> MK1 implementation
```

No issue label, branch name, prototype, demo, verbal decision or isolated PASS can bypass the chain.

The bootstrap profile is fail-closed: an unresolved required field is `BLOCKED`, not “implementation choice”.

---

## 14. Evidence freshness and re-open triggers

A previously closed receipt reopens for the affected scope when material assumptions change, including:

- Q00 intervention composition, comparison baseline, task corpus, scoring semantics or target population when the prior causal conclusion would no longer apply;
- law/regulatory interpretation or reviewed product semantics;
- provider terms, product, entitlement or geography;
- persona/wedge or paid-flow material change;
- asset universe or point-in-time data semantics;
- model target/feature family when relevant to Q04;
- comparator landscape when a Q05 claim depends on stale competitor evidence.

Each receipt must record `evidence_as_of` and, where meaningful, a `review_by` or explicit event-triggered refresh rule.

---

## 15. Safety boundary

Nothing in MK0 evidence closure authorizes:

- custody;
- live autonomous execution;
- LLM-originated orders;
- LLM-invented probabilities;
- personalized action recommendations outside Q01-approved scope;
- use of unlicensed market data;
- performance guarantees.

Those remain governed by the closed internal architecture and future promotion gates.

---

## Final invariant

> MK0 evidence does not prove that SOPHROSYNE knows the future. It proves, configuration by configuration, that the candidate intervention has survived its causal gate and may be built under explicit legal, data, user-value, scientific and strategic constraints without silently inventing missing evidence.
