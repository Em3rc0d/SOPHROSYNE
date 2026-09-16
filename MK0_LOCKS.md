# MK0 Lock Registry

## Status model

Lock rows use only `OPEN | PARTIAL | CLOSED`. Evidence lifecycle/final decisions are defined separately in `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`. There is no hidden sixth evidence gate.

## External / empirical locks

| Lock | Status | Canonical track | Closure requirement |
|---|---|---|---|
| Problem / product thesis | CLOSED | Foundation | Frozen unless evidence forces pivot |
| Initial persona/JTBD/wedge | PARTIAL | Q03 | Behavioral + comprehension + repeat-use + pricing evidence |
| Peru legal/commercial boundary | OPEN | Q01 | Exact-flow external review, including applicable non-securities commercial domains; no hidden Q06 |
| Custody | CLOSED | Q01 constraint | Excluded from MK1 |
| Live autonomous execution | CLOSED | Q01 constraint | Excluded from MK1 |
| Market-data technical access | CLOSED | Q02 input | Does not imply commercial rights |
| Market-data commercial rights | OPEN | Q02 | Exact production DataUseProfiles with authoritative rights/cost evidence |
| Quant harness validity | PARTIAL | Q04 | Pre-registered deterministic validity/reproduction gates |
| ML incremental value | OPEN | Q04 | Optional; INCLUDE/EXCLUDE/DEFER from preregistered evidence |
| WTP / repeat use | OPEN | Q03 | Aggregate Q03 receipt for target Peru/Spanish MK1 cohort |
| Moat / durability | PARTIAL | Q05 | Comparative + exposure-correct repeat-use + defensibility evidence |
| Unit economics | PARTIAL | Q02 + Q03 | Synchronize provider/compliance/infra/payment/support costs with pricing evidence |
| GTM/channel hypotheses | PARTIAL | Q03 + Q05 | Evidence-driven; not standalone architecture gate |
| TAM/SAM/SOM | OPEN | Non-blocking unless scope changes | Bottom-up observed evidence; cannot fabricate demand |
| Liability/reputation | PARTIAL | Q01 + MK1 beta | Legal claim/terms constraints + implemented controls/incident receipts |

`INCONCLUSIVE` evidence leaves the corresponding lock OPEN/PARTIAL. It never closes a lock.

## Internal executable-design locks

The following method/design contracts are CLOSED:
- product promise and MK1 boundaries;
- domain/system/runtime/API/state contracts;
- data, point-in-time and market-data semantics;
- quant engine mechanics and validation policy;
- failure/degradation/replay/reproducibility;
- security/configuration/observability/operations;
- CI/CD/test/release and acceptance receipts;
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`;
- `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`;
- `docs/validation/EVIDENCE_RECEIPT_TEMPLATE.md`;
- `docs/validation/CONTRADICTION_LOG_TEMPLATE.md`;
- `docs/validation/EVIDENCE_EXECUTION_SEQUENCE.md`;
- `docs/validation/RESEARCH_PARTICIPANT_PROTOCOL.md`;
- `docs/validation/STATISTICAL_DECISION_RULES.md`;
- `docs/validation/q01/REGULATORY_REVIEW_PACKET.md`;
- `docs/validation/q02/DATA_USE_PROFILE_PACKET.md`;
- `experiments/q03/Q03_PREREGISTRATION.md`;
- `experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`;
- `experiments/q04/Q04_PREREGISTRATION.md`;
- `experiments/q05/Q05_PREREGISTRATION.md`;
- `docs/validation/MK0_PROMOTION_PACKET.md`;
- `docs/validation/MK1_BOOTSTRAP_PROFILE.md`;
- `docs/implementation/BUILD_READINESS.md`.

Known internal executable-design nodes remaining: **0**.

## Current promotion state

```text
Internal design graph                 CLOSED
Evidence execution method             CLOSED
External/empirical Q01–Q05 outcomes   OPEN/PARTIAL
MK1 production implementation         BLOCKED
```

This is intentional. No result is fabricated to make the project look complete.

## Hard MK1 invariants

- no custody;
- no live autonomous execution;
- no unapproved personalized recommendation flow;
- no unlicensed data redistribution/use;
- no LLM trading authority or invented probability;
- no historical leakage (`available_at > as_of`);
- no finalized DecisionRecord or EvidenceReceipt mutation;
- no promotion experiment without preregistration;
- no target-geography claim from exploratory cohorts;
- no `INCONCLUSIVE` evidence treated as favorable;
- no P0/P1 contradiction at promotion;
- no manual/unattributed bootstrap values;
- no production implementation outside the approved bootstrap profile;
- no implementation-complete claim without typed acceptance receipts.
