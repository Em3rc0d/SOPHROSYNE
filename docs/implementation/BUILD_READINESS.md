# MK1 Build Readiness

## Purpose

This gate answers one question: **is one exact evidence-backed MK1 configuration ready for production implementation?** It does not certify business success or future performance.

## Canonical evidence decisions

Only `CLOSED_PASS` and `CLOSED_CONDITIONAL` are promotable. `INCONCLUSIVE`, `PIVOT_REQUIRED`, and `STOP_CURRENT_CONFIGURATION` block the affected configuration.

## Definition of Ready

All items must pass.

### 1. Internal design
- known executable-design locks are closed;
- product thesis/MK1 boundary, domain model, system/API/state contracts, data/market semantics, quant mechanics, failure/degradation, security, observability, test/release, operations and acceptance-receipt contracts are canonical;
- any evidence-forced design reopen has an approved resolution/ADR.

### 2. Q01 legal/commercial boundary
- aggregate Q01 receipt is final and promotable;
- exact reviewed prototype/copy digest matches the candidate build scope;
- applicable securities/advisory classification is externally reviewed;
- applicable privacy/data-protection, consumer/subscription/e-commerce, marketing/claims, payment/invoicing/fiscal and e-contracting domains are either authoritatively cleared/conditioned or the corresponding capability is explicitly disabled;
- `legal_copy_version`, `portfolio_context_scope` and `commercial_activation_constraints` are frozen.

### 3. Q02 data rights and semantics
- aggregate Q02 receipt is final and promotable;
- every production data use maps to an approved `DataUseProfile`;
- provider semantics/freshness profiles and fallback groups are frozen;
- unknown/ambiguous rights remain denied;
- attribution/retention/entitlement/cost obligations are executable;
- rights recheck triggers/effective dates are recorded.

### 4. Q03 product evidence
- aggregate Q03 receipt is final and promotable;
- primary promotion geography/persona/language match the bootstrap target;
- behavioral discovery, comprehension, repeat use and pricing evidence satisfy their pre-registered decision regions;
- exploratory cohorts are not silently generalized;
- any conditional wedge/pricing/persona scope is frozen.

### 5. Q04 research validity
- aggregate Q04 receipt is final and promotable;
- deterministic harness passes all mandatory validity gates;
- point-in-time, accounting/fill, cost, untouched-test and reproduction evidence exists;
- selected production quant surface has a production-semantics compatibility ref to approved Q02 profiles;
- `ml_scope` is frozen as `INCLUDE`, `EXCLUDE` or `DEFER`; EXCLUDE/DEFER create no runtime ML dependency.

### 6. Q05 durability posture
- aggregate Q05 receipt is final and promotable;
- component-specific repeat-use denominators use exposure eligibility;
- moat status is `SUPPORTED` or `LEARNING_WEDGE` with corresponding claim/scale restrictions;
- no surface-only feature is promoted as durable defensibility.

### 7. Statistics / instrumentation / research integrity
- every empirical promotion experiment has a pre-registered manifest;
- statistical-contract version, unit of analysis, denominators, region precedence and missing-data rules are frozen;
- instrumentation/telemetry quality gates pass for primary metrics;
- qualitative coding used in a promotion gate satisfies its pre-registered reliability rule;
- participant consent, eligibility, compensation and retention rules pass the research-participant protocol;
- raw/normalized/analysis artifacts have digests and can reproduce primary decisions.

### 8. Unit economics
- `UNIT_ECONOMICS.md` is synchronized to Q02 provider costs and Q03 pricing evidence plus verified infra/payment/tax/support/compliance assumptions;
- a versioned unit-economics synchronization artifact exists;
- no structural incompatibility is hidden by optimistic scale/TAM assumptions.

### 9. Contradictions
- cross-receipt log exists;
- no P0/P1 item is OPEN, MITIGATING or ACCEPTED_LIMITATION;
- P0/P1 are RESOLVED or superseded by a resolved successor;
- P2/P3 accepted limitations are explicit and represented in the bootstrap where material;
- severity downgrades have evidence and independent review.

### 10. Promotion and bootstrap
- `MK0_PROMOTION_PACKET` is APPROVED;
- `MK1_BOOTSTRAP_PROFILE` is APPROVED and immutable;
- every bootstrap field has receipt/closed-contract/ADR provenance;
- profile jurisdiction is Peru unless a separately revalidated scope explicitly changes it;
- build PRs are required to bind to profile ID+digest.

## Hard blockers

Build remains blocked if any required Q is non-promotable, an applicable external authority is missing, rights are ambiguous, primary human evidence does not match target geography/persona, quant semantics are unreproducible, a P0/P1 contradiction remains, unit economics are structurally unresolved, or a bootstrap value lacks provenance.

## Build authorization

When every section passes:

```text
MK0 evidence for candidate profile -> CLOSED
MK1 production implementation      -> AUTHORIZED FOR THAT PROFILE ONLY
```

Implementation then proves conformance through typed acceptance receipts. It may not use coding to decide an unresolved product/legal/data/evidence question.
