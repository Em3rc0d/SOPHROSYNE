# Validation System

This directory is the canonical MK0 evidence-execution layer.

## Vocabulary — do not mix these

| Concept | Values |
|---|---|
| Lock registry | OPEN / PARTIAL / CLOSED |
| Evidence lifecycle | OPEN / PRE_REGISTERED / EVIDENCE_RUNNING / REVIEW_READY / FINAL |
| Final evidence decision | CLOSED_PASS / CLOSED_CONDITIONAL / PIVOT_REQUIRED / STOP_CURRENT_CONFIGURATION / INCONCLUSIVE |
| Receipt artifact state | DRAFT / REVIEW_READY / FINAL / SUPERSEDED |
| Promotion packet | DRAFT / REVIEW_READY / APPROVED / REJECTED / SUPERSEDED |
| Bootstrap profile | DRAFT / APPROVED / SUPERSEDED |

Labels such as `SYNTHETIC_TEST_ONLY`, `LEARNING_WEDGE`, or `ML DEFER` describe scope/configuration; they are not alternate evidence-status taxonomies.

## Canonical chain

```text
EVIDENCE_CLOSURE_PROTOCOL
  -> EXPERIMENT_MANIFEST / external review packet
  -> execution + raw evidence
  -> EvidenceReceipt
  -> cross-receipt contradiction log
  -> unit-economics sync
  -> MK0_PROMOTION_PACKET
  -> MK1_BOOTSTRAP_PROFILE
  -> BUILD_READINESS
  -> MK1 implementation
  -> typed AcceptanceReceipts
```

## Core contracts

- `EVIDENCE_CLOSURE_PROTOCOL.md`
- `EVIDENCE_RECEIPT_TEMPLATE.md`
- `CONTRADICTION_LOG_TEMPLATE.md`
- `EVIDENCE_EXECUTION_SEQUENCE.md`
- `RESEARCH_PARTICIPANT_PROTOCOL.md`
- `STATISTICAL_DECISION_RULES.md`
- `MK0_PROMOTION_PACKET.md`
- `MK1_BOOTSTRAP_PROFILE.md`
- `q01/REGULATORY_REVIEW_PACKET.md`
- `q02/DATA_USE_PROFILE_PACKET.md`
- `../../experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`
- `../../experiments/q03/Q03_PREREGISTRATION.md`
- `../../experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`
- `../../experiments/q04/Q04_PREREGISTRATION.md`
- `../../experiments/q05/Q05_PREREGISTRATION.md`
- `../implementation/BUILD_READINESS.md`

## Promotion invariant

Only CLOSED_PASS/CLOSED_CONDITIONAL aggregate Q01–Q05 receipts for one compatible configuration may feed an approved bootstrap. INCONCLUSIVE is honest closure of an evidence attempt, not permission to build.
