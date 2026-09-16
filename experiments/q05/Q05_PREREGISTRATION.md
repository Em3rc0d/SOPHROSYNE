# Q05 Pre-Registration — Competitive Durability

## Scope

Primary Q05 promotion population inherits Q03 persona, `Peru` geography and `Spanish` language. Other geographies are exploratory unless separately preregistered. Comparator tasks must be language-accessible and fair; localization alone cannot count as moat.

Candidate components are frozen before testing: evidence graph, immutable Decision Ledger, point-in-time provenance/replay, uncertainty/invalidation, progressive disclosure, reproducible strategy validation, longitudinal decision history and rights-aware derived intelligence.

# E05-A — Competitive task comparison

Within-participant, counterbalanced comparison with at least one representative materially similar workflow. Freeze comparator version/date, task parity, onboarding time, branding treatment and coding rubric.

```yaml
target_usable_n: 44
minimum_usable_n: 36
```

Primary measures: workflow preference, independently stated reason attribution, objective comprehension guardrail and confidence-calibration guardrail.

Reason coding used for promotion follows the qualitative-reliability contract.

### PASS contribution
All hold:
- observed SOPHROSYNE preference >=65%;
- lower bound of two-sided 80% Wilson interval >50%;
- comprehension mean is not worse by >5 percentage points;
- calibration gap is not worse by >5 percentage points;
- at least one frozen component is independently attributable by >=35% of usable participants.

### CONDITIONAL
Preference >=55%, no guardrail stop, but full PASS not reached.

### STOP
Valid strong-negative region: preference <40%, or comprehension worse by >=10 percentage points, or the preregistered material calibration stop condition.

All other/minimum-sample/coding-invalid outcomes are INCONCLUSIVE. Precedence: validity -> STOP -> PASS -> CONDITIONAL -> INCONCLUSIVE.

# E05-B — Repeat-use linkage

Primary source is valid E03-C longitudinal telemetry.

For each component define denominator as `eligible_exposed_repeat_users`, not all repeat users. A user is eligible only when the component was validly exposed before the measured outcome. Progressive-disclosure non-exposure is reported separately, not counted as failure.

Metrics:
- U1 adoption in >=2 sessions / eligible exposed repeat users;
- U2 independently stated return-reason / eligible exposed repeat users;
- U3 component use after day 7 / eligible exposed repeat users.

### Strong linkage
All hold: U1>=60%, U2>=40%, U3>=40%, denominator >=12.

### Moderate linkage
U1>=40% and at least one of U2/U3>=30%, with declared denominator.

### Negative evidence
With denominator >=12: U1<25% or U3<10%.

If denominator <12, that component cannot support a strong-linkage PASS. It is INCONCLUSIVE for strong linkage. A separately preregistered extension cohort may add observations only with identical treatment/instrumentation and a pooling rule frozen before extension outcomes.

Association is not causal proof.

# E05-C — Defensibility assessment

For each component record surface copyability, workflow integration, accumulated user/evidence/provenance history, switching cost, distribution/community asset, provider/rights dependency, generic-model dependency, repeat-use linkage, competitor counterexample and residual copy risk.

Categories: `SURFACE_ONLY | WORKFLOW_EMBEDDED | STATE_COMPOUNDING | EVIDENCE_COMPOUNDING | RIGHTS_OR_DISTRIBUTION_CONSTRAINED`.

Code complexity alone cannot classify above SURFACE_ONLY. A category above SURFACE_ONLY requires actual workflow/history/evidence support and independent reviewer signoff. `RIGHTS_OR_DISTRIBUTION_CONSTRAINED` requires materially scarce/non-trivial access or distribution—not a generic purchasable license available equally to competitors.

# Aggregate Q05 decision

- `CLOSED_PASS`: E05-A PASS; >=1 component has STRONG E05-B linkage; that same component has supported category above SURFACE_ONLY; it does not depend on Q01-prohibited/Q02-unapproved behavior; no unresolved P0/P1.
- `CLOSED_CONDITIONAL` / `LEARNING_WEDGE`: E05-A PASS/CONDITIONAL with no trust stop; repeat-use evidence supports real value; durable moat remains unproven; strong moat claims and large scale/GTM spending remain constrained with a next evidence horizon.
- `PIVOT_REQUIRED`: durable advantage appears in a materially different persona/workflow/distribution model.
- `STOP_CURRENT_CONFIGURATION`: valid repeated evidence shows interchangeability, weak repeat use and no deeper state/workflow/evidence asset.
- `INCONCLUSIVE`: insufficient sample/exposure denominator or mixed evidence outside the declared regions.

Final output is one aggregate Q05 EvidenceReceipt.

## Frozen outputs

```yaml
q05_receipt_ref:
moat_status: SUPPORTED | LEARNING_WEDGE
supported_components: []
unsupported_components: []
scale_spend_constraint:
claims_allowed: []
claims_forbidden: []
next_evidence_horizon:
competitor_snapshot_ref:
```
