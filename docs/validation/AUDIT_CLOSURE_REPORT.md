# MK0 Evidence Execution — Audit Closure Report

## Audit scope

This review audits the complete `docs/mk0-evidence-execution` design layer against `main` and against SOPHROSYNE's closed internal contracts.

The purpose is not to declare Q01–Q05 factually closed. It is to determine whether the **method for closing them** is internally coherent, non-regressive, reproducible, fail-closed and capable of generating one unambiguous MK1 bootstrap configuration.

## Baseline preserved

The audited branch preserves the detailed pre-audit specification depth and does not delete/replace the closed internal architecture in `main`.

The earlier audit draft that compressed canonical documents was rejected. The final design layers normalization, evidence-execution packets, provenance and traceability on top of the existing closed architecture rather than replacing it.

---

## Findings closed by this audit

### A01 — Dual outcome taxonomies

**Finding:** root and leaf documents used different words for equivalent evidence decisions.

**Resolution:** one final outcome vocabulary is normative:

`CLOSED_PASS | CLOSED_CONDITIONAL | PIVOT_REQUIRED | STOP_CURRENT_CONFIGURATION | INCONCLUSIVE`.

Artifact lifecycle is separate from outcome.

### A02 — `INCONCLUSIVE` not globally representable

**Finding:** local protocols could produce `INCONCLUSIVE` while the root lifecycle did not formally include it.

**Resolution:** `INCONCLUSIVE` is now a first-class final evidence decision and never promotes MK1.

### A03 — Q02 status mismatch

**Finding:** Q02 described an inconclusive result without a universally representable final outcome.

**Resolution:** Q02 now directly represents `INCONCLUSIVE`; required unknown rights remain denied and stale authority blocks promotion.

### A04 — Q04 aggregate ambiguity

**Finding:** E04-A could be inconclusive while aggregate Q04 had no explicit corresponding state.

**Resolution:** E04-A `INCONCLUSIVE` blocks aggregate Q04 and ML evaluation. ML INCLUDE/EXCLUDE/DEFER remains subordinate to a passed deterministic harness. E04-B `INCONCLUSIVE` is explicitly distinct from `DEFER`.

### A05 — Q03 primary-sample inconsistency

**Finding:** E03-A minimum usable primary sample was 20 while the planned primary target could be only 16.

**Resolution:** promotable E03-A targets 20–24 primary participants, minimum 20 usable primary, plus 4–8 exploratory participants.

### A06 — Geographic evidence leakage

**Finding:** LATAM/global evidence could be mistakenly used to authorize a Peru-scoped product.

**Resolution:** initial promotion geography is Peru. Non-Peru evidence is exploratory/supportive unless a preregistered Peru confirmation satisfies the relevant gate. Telemetry carries a coarse `promotion_geo_class`, not precise location.

### A07 — Pricing/legal sequencing

**Finding:** pricing experimentation could be interpreted as permission to charge before legal review.

**Resolution:** before Q01 authorizes the exact paid flow, pricing testing is research-only/non-charge. Paid pilots require legal/operational authorization of the actual subscription/payment flow.

### A08 — Research-compensation bias

**Finding:** participant incentives could contaminate willingness-to-pay / commitment evidence.

**Resolution:** compensation cannot depend on desired behavior, WTP, favorable feedback, return frequency or commitment. Potentially contaminated economic-intent evidence cannot be the sole promotable pricing basis.

### A09 — Q05 denominator bias

**Finding:** component adoption could divide by repeat users who were never exposed to the component.

**Resolution:** Q05 component metrics use eligible **exposed** repeat users. Instrumentation now records component eligibility, exposure and use explicitly; missing exposure is not interpreted as non-adoption.

### A10 — Qualitative Q05 negative threshold

**Finding:** “usage disappears almost entirely” was not executable.

**Resolution:** default negative longitudinal threshold is `U3 < 15%` with the preregistered minimum eligible-exposed denominator.

### A11 — Legal review too securities-centric

**Finding:** a commercial MK1 also creates potentially applicable privacy, consumer, subscription, billing, payment and marketing surfaces.

**Resolution:** Q01 remains one Peru launch-law lock but directly requires every applicable legal/commercial surface to be reviewed by a competent external authority or explicitly marked `NOT_APPLICABLE` with rationale. Q01 flow inventory now covers F01–F20, including privacy, telemetry consent, subscription/cancellation and complaints/refunds.

### A12 — Bootstrap fields without explicit producers

**Finding:** build-defining fields could require human interpretation during promotion.

**Resolution:** `BOOTSTRAP_PROVENANCE_MATRIX.md` and `AUDIT_TRACEABILITY_MATRIX.md` map every field family to allowed evidence/internal producers, compatibility rules and reopen triggers.

### A13 — Contradiction severity ambiguity

**Finding:** promotion could theoretically proceed while important cross-receipt conflicts remained.

**Resolution:** P0/P1 contradictions block promotion; safe scope intersections may narrow configuration but cannot broaden evidence.

### A14 — Instrumentation integrity

**Finding:** telemetry defects could silently produce behavioral PASS results.

**Resolution:** primary telemetry has explicit schema/prototype/duplicate/clock/denominator/reminder/test-account gates. >10% defect impact on an E03-C primary metric prevents PASS absent a preregistered recovery rule/new experiment. Component exposure integrity has its own fail-closed rule for Q05.

### A15 — Regression introduced by audit itself

**Finding:** the first correction pass improved consistency but compressed deep canonical documents.

**Resolution:** rejected. The final branch preserves existing closed contracts and adds non-regressive normalization/validation artifacts. The final diff is audited for accidental deletions/compressions before merge.

### A16 — Validation authority conflict

**Finding:** a semantic normalizer could become a second undocumented source of truth if precedence were unclear.

**Resolution:** `NORMATIVE_DOCUMENT_HIERARCHY.md` defines L0–L5 authority. `CANONICAL_VALIDATION_SPEC.md` is L1A only for explicitly enumerated normalization topics; detailed root/domain contracts remain authoritative within their scopes. Audit prose is explicitly non-authoritative.

### A17 — Leaf contracts depended too much on an overlay

**Finding:** even with canonical normalization, Q01–Q05 could remain locally ambiguous if readers missed the overlay.

**Resolution:** critical corrections were pushed into the leaf contracts themselves:
- Q01 full Peru commercial/legal authority coverage and `INCONCLUSIVE`;
- Q02 `INCONCLUSIVE`, evidence freshness/expiry and reopen rules;
- Q03 Peru cohort/sample/compensation/pricing constraints;
- Q04 aggregate fail-closed `INCONCLUSIVE` semantics;
- Q05 exposure-aware denominators, explicit negative threshold and evidence freshness.

The normalizer now protects cross-document consistency rather than rescuing locally broken preregistrations.

### A18 — Execution sequence lagged behind hardened contracts

**Finding:** the original sequence still referenced F01–F16, generic counsel review and incomplete outcome handling.

**Resolution:** the execution sequence now uses F01–F20, competent authority coverage by legal surface, Peru promotion scope, current data-rights evidence, explicit `INCONCLUSIVE` handling, exposure-aware Q05 and provenance-matrix verification before promotion.

### A19 — Q05 instrumentation could not prove its own denominator

**Finding:** Q05 required eligible-exposed denominators but telemetry lacked canonical eligibility/exposure events.

**Resolution:** instrumentation now includes `component_eligible`, `component_exposed`, `component_used`, exposure-rule versioning, geography/cohort integrity and reproducible eligible-exposed denominator reconstruction.

---

## Normative authority audit

The valid authority chain is:

```text
L0 governance / ADR invariants
  -> L1A semantic normalization
  -> L1B lock + detailed closure protocol
  -> L2 Q-specific/statistical/instrumentation contracts
  -> L3 evidence instances / receipts
  -> L4 promotion packet + bootstrap provenance
  -> L5 build/readiness/acceptance conformance
```

No document wins merely because it is newer. Same-level conflicts must enter the contradiction log.

---

## End-to-end promotion audit

The only valid chain is:

```text
pre-registration
  -> evidence collection
  -> immutable EvidenceReceipt
  -> cross-receipt contradiction review
  -> MK0_PROMOTION_PACKET
  -> provenance + traceability verification
  -> MK1_BOOTSTRAP_PROFILE
  -> BUILD_READINESS
  -> implementation
  -> typed acceptance receipts
```

No alternate route was accepted.

---

## Evidence authority audit

- Q01 requires qualified external authority for every applicable Peru legal/commercial surface; securities/advisory review remains mandatory where applicable but does not substitute for privacy/consumer/payment expertise outside its competence.
- Q02 requires current authoritative provider terms/contracts/quotes/written confirmations for required commercial rights; unknown/stale rights do not promote.
- Q03 requires observed target-user behavior under preregistered Peru-compatible gates; incentives cannot manufacture WTP.
- Q04 requires reproducible point-in-time quantitative evidence and independent reproduction; ML is optional and subordinate to a valid deterministic harness.
- Q05 requires comparative/repeat-use evidence with valid exposure-aware denominators; interviews or technical complexity alone are insufficient.

---

## Scientific integrity audit

The statistical contract preserves:

- exact numerator/denominator reporting;
- Wilson interval rules;
- participant-level aggregation;
- calibration-gap semantics;
- dependence-aware market bootstrap;
- transaction-cost stress;
- frozen seeds/search budget;
- multiple-testing logging;
- no final-test tuning;
- protocol-deviation handling;
- reproducible artifact digests.

Q03/Q05 human evidence also preserves:
- pre-registered cohort/geography;
- compensation integrity;
- explicit exposure opportunity;
- reminder attribution;
- pseudonymous telemetry;
- no real-money trading requirement.

---

## Data/licensing integrity audit

Q02 now fails closed on:
- unknown mandatory rights;
- stale/superseded authority;
- expired commercial quote assumptions when current cost matters;
- unreviewed model/embedding/LLM use;
- incompatible fallback semantics;
- unreviewed geography/user classification;
- retention/cache/display/derived use outside the approved profile.

A technical API connection is never treated as a commercial right.

---

## Safety/trust audit

Nothing in this validation layer changes the already closed internal invariants:

- LLM is downstream explanation, not financial authority;
- probabilities are not invented by an LLM;
- no live autonomous trading in MK1;
- no custody in MK1;
- unknown data rights deny use;
- risk remains independent from model conviction;
- Decision Records remain immutable and point-in-time reproducible;
- causal wording must respect OBSERVED / ATTRIBUTED / INFERRED / CORRELATED / UNKNOWN semantics.

Human validation likewise never requires participants to make live investment decisions or expose credentials.

---

## Current project status

### Closed for design / method

- Internal MK1 design graph.
- Normative validation authority hierarchy.
- Method for collecting/reviewing Q01–Q05 evidence.
- Q01/Q02 external-review packet structures.
- Q03/Q04/Q05 preregistered decision methodology.
- Statistical and instrumentation semantics for the currently designed experiments.
- Promotion-chain architecture.
- Bootstrap provenance/traceability architecture.
- Contradiction handling semantics.
- Evidence-execution sequencing.

### Intentionally not closed

Actual external/empirical outcomes:

- Q01 Peru legal/compliance evidence;
- Q02 commercial data-rights evidence;
- Q03 real user-value / retention / pricing evidence;
- Q04 executed quant-harness / optional ML evidence;
- Q05 executed moat/durability evidence.

These cannot be truthfully marked PASS before the evidence exists.

---

## Merge criteria for this audit layer

The evidence-execution design is suitable for merge only if final branch verification shows:

- branch is not behind `main`;
- no accidental deletion/compression of the closed internal architecture;
- Q01–Q05 outcome vocabulary is compatible with the normative hierarchy;
- leaf contracts contain the critical fail-closed corrections, not only an overlay;
- README points to the single authority path;
- provenance/traceability matrices have no orphan build-defining field families;
- no P0/P1 design contradiction remains unresolved;
- the PR introduces documentation/contracts only and does not silently introduce product implementation.

---

## Final conclusion

**DESIGN AUDIT: PASS — NON-REGRESSIVE, FAIL-CLOSED, WITH EXTERNAL EVIDENCE STILL OPEN.**

This PASS certifies the validation architecture and the method used to decide future promotion. It does not certify legal permissibility, commercial demand, data rights, quantitative performance or competitive durability.

> SOPHROSYNE is ready to execute MK0 evidence collection under a controlled evidence system, but it is not yet authorized to treat Q01–Q05 as solved or to promote a production MK1 configuration.
