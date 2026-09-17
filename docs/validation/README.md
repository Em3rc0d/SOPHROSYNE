# Validation System

## Purpose

This directory is the canonical entry point for SOPHROSYNE's MK0 external/empirical validation system.

Internal MK1 architecture is already closed. Validation now answers:

> Which exact first-production configuration, if any, has enough **causal-value, legal, data-rights, user-value, scientific and competitive evidence** to deserve implementation?

---

## Read this first — authority path

The active authority chain is:

1. `NORMATIVE_DOCUMENT_HIERARCHY.md` — defines which document wins when scopes overlap.
2. `CANONICAL_VALIDATION_SPEC.md` — normalizes cross-document semantics found inconsistent during audit.
3. `../product/THESIS_STACK.md` — separates problem, causal, product, economic and defensibility claims.
4. `Q00_CORE_CAUSAL_VALUE.md` — destructive baseline/ablation gate for incremental product value.
5. `EVIDENCE_CLOSURE_PROTOCOL.md` — detailed Q01–Q05 closure protocol.
6. Q-specific packets/preregistrations/statistical/instrumentation contracts — exact domain rules.
7. immutable `EvidenceReceipt`s + contradiction log — observed evidence truth.
8. `MK0_PROMOTION_PACKET.md` — aggregate promotion decision including Q00.
9. `MK1_BOOTSTRAP_PROFILE.md` — exact configuration authorized to build.
10. `../implementation/BUILD_READINESS.md` — implementation authorization gate.

Supporting provenance controls:
- `BOOTSTRAP_PROVENANCE_MATRIX.md` — allowed producers for build-defining fields;
- `AUDIT_TRACEABILITY_MATRIX.md` — field-by-field producer/authority/reopen mapping;
- `AUDIT_CLOSURE_REPORT.md` — audit findings/history, **not** an authority source by itself.

No other route may authorize production MK1.

---

## Truth layers

```text
DESIGN TRUTH
  closed internal contracts / ADRs

EVIDENCE TRUTH
  Q00–Q05 receipts

IMPLEMENTATION TRUTH
  acceptance receipts after build
```

Do not substitute one layer for another.

---

## Canonical validation stack

### Thesis / causal value

- `../product/THESIS_STACK.md` — T0–T5 layered claims and scoped kill rules.
- `Q00_CORE_CAUSAL_VALUE.md` — simple-friction, memory-ablation, transfer, outcome-blind, cognitive-cost and cheap-substitute tests.

### Governance / lifecycle

- `NORMATIVE_DOCUMENT_HIERARCHY.md` — document authority and conflict-resolution order.
- `CANONICAL_VALIDATION_SPEC.md` — lifecycle/outcome/geography/denominator/provenance normalization.
- `EVIDENCE_CLOSURE_PROTOCOL.md` — Q01–Q05 lifecycle, authority, receipt semantics and detailed closure requirements.
- `EVIDENCE_EXECUTION_SEQUENCE.md` — risk-minimizing order in which evidence should actually be collected.
- `EVIDENCE_RECEIPT_TEMPLATE.md` — immutable final evidence record.
- `CONTRADICTION_LOG_TEMPLATE.md` — cross-receipt conflict handling.

### Promotion

- `MK0_PROMOTION_PACKET.md` — final review bundle; Q00 is mandatory before build authorization.
- `MK1_BOOTSTRAP_PROFILE.md` — exact evidence-derived configuration production MK1 may implement.
- `BOOTSTRAP_PROVENANCE_MATRIX.md` — allowed producer/compatibility rules for bootstrap fields.
- `AUDIT_TRACEABILITY_MATRIX.md` — end-to-end source and reopen rules.

### Human research

- `RESEARCH_PARTICIPANT_PROTOCOL.md` — consent, privacy, recruitment and no-real-money-task boundaries.
- `../../experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` — general pre-registration contract.
- `../../experiments/q03/Q03_PREREGISTRATION.md` — fixed Q03 product-decision gates.
- `../../experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md` — reproducible behavioral telemetry semantics.

### Quant research

- `STATISTICAL_DECISION_RULES.md` — computation semantics shared by empirical/quant gates.
- `../../experiments/q04/Q04_PREREGISTRATION.md` — deterministic harness gates and optional ML promotion gates.

### Competitive durability

- `../../experiments/q05/Q05_PREREGISTRATION.md` — competitive task, repeat-use linkage and replicability gates.

### External authority packets

- `q01/REGULATORY_REVIEW_PACKET.md` — exact frozen product bundle/questions for qualified Peruvian counsel and other applicable legal specialists.
- `q02/DATA_USE_PROFILE_PACKET.md` — provider-by-provider rights/economics/semantics closure unit.

---

## Current validation state

```text
Internal MK1 design graph             CLOSED
Validation method / machinery        CLOSED FOR DESIGN
Validation authority hierarchy       CLOSED
Thesis layering / Q00 method          CLOSED FOR DESIGN
Bootstrap provenance contract        CLOSED

Q00 core causal value                 OPEN
Q01 legal/compliance outcome          OPEN
Q02 production data-rights outcome    OPEN
Q03 user value / WTP / repeat use     OPEN / PARTIAL
Q04 quant baseline / ML increment     OPEN
Q05 moat / durability                 PARTIAL

MK0_PROMOTION_PACKET                   NOT YET INSTANTIATED
MK1_BOOTSTRAP_PROFILE                  NOT YET APPROVED
Production MK1 implementation          BLOCKED
```

`CLOSED FOR DESIGN` means the validation method is specified; it does **not** mean the real-world outcome is positive.

The files in this directory do not fabricate missing evidence. They make it difficult to close a gate without the evidence actually required.

---

## Core falsification order

Before interpreting WTP, ML sophistication or moat as proof that the product deserves to exist, Q00 asks whether the intervention beats simpler/cheaper substitutes.

```text
simple/raw baselines
      ↓
Q00 causal value
      ↓
Q03 product/WTP evidence
Q04 optional complexity
Q05 defensibility
      ↓
Q01/Q02 still independently fatal where applicable
      ↓
promotion packet
      ↓
bootstrap profile
      ↓
build readiness
```

Q00 may narrow the product. A valid `CLOSED_CONDITIONAL` can explicitly remove long memory, ML or other complexity while preserving a smaller causal intervention.

---

## Required status vocabulary

### Evidence artifact lifecycle

```text
DRAFT
PRE_REGISTERED
EVIDENCE_RUNNING
REVIEW_READY
FINAL
SUPERSEDED
```

### Final evidence decisions

```text
CLOSED_PASS
CLOSED_CONDITIONAL
PIVOT_REQUIRED
STOP_CURRENT_CONFIGURATION
INCONCLUSIVE
```

Only `CLOSED_PASS` and appropriately constrained `CLOSED_CONDITIONAL` are promotable.

`INCONCLUSIVE` never auto-promotes.

### Product lock registry

Use only:

```text
OPEN
PARTIAL
CLOSED
```

Fatality/blocking belongs in `Promotion role`, not by inventing new status names.

---

## Evidence artifact conventions

Recommended instance layout:

```text
experiments/
  <experiment_id>/
    manifest.md|yaml
    raw/
    normalized/
    analysis/
    figures/
    receipt.md|yaml

validation-receipts/
  q00/
  q01/
  q02/
  q03/
  q04/
  q05/

promotion/
  <packet_id>/
    packet.md|yaml
    contradictions.md|yaml
    bootstrap-profile.md|yaml
```

Instance directories should be created when evidence execution begins; the repository currently contains contracts/templates, not fabricated results.

---

## No-outcome-fabrication rule

Never create a receipt marked PASS just to exercise the workflow.

For dry-runs/tests use explicit synthetic identifiers and statuses such as:

```text
SYNTHETIC_TEST_ONLY
NOT_PROMOTION_EVIDENCE
```

---

## Promotion invariant

A production build is authorized only when:

```text
Q00 promotable final receipt
        +
Q01–Q05 applicable promotable final receipts
        +
no unresolved P0/P1 contradiction
        +
approved MK0 promotion packet
        +
approved MK1 bootstrap profile
        +
BUILD_READINESS pass
```

Every non-null bootstrap value must be traceable to a valid evidence receipt, closed internal contract or accepted ADR.

No positive WTP, ML result or moat narrative may override failed Q00 causal value for the current configuration.

Until then, the correct state is still research/validation.
