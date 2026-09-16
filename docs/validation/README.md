# Validation System

## Purpose

This directory is the canonical entry point for SOPHROSYNE's MK0 external/empirical validation system.

Internal MK1 architecture is already closed. Validation now answers a narrower question:

> Which exact first-production configuration, if any, has enough legal, data-rights, user-value, scientific and competitive evidence to deserve implementation?

---

## Truth layers

```text
DESIGN TRUTH
  closed internal contracts / ADRs

EVIDENCE TRUTH
  Q01–Q05 receipts

IMPLEMENTATION TRUTH
  acceptance receipts after build
```

Do not substitute one layer for another.

---

## Canonical validation stack

### Governance / lifecycle

- `EVIDENCE_CLOSURE_PROTOCOL.md` — Q01–Q05 lifecycle, authority, receipt semantics and closure states.
- `EVIDENCE_EXECUTION_SEQUENCE.md` — risk-minimizing order in which evidence should actually be collected.
- `EVIDENCE_RECEIPT_TEMPLATE.md` — immutable final evidence record.
- `CONTRADICTION_LOG_TEMPLATE.md` — cross-receipt conflict handling.

### Promotion

- `MK0_PROMOTION_PACKET.md` — final review bundle before implementation can begin.
- `MK1_BOOTSTRAP_PROFILE.md` — exact evidence-derived configuration production MK1 may implement.

### Human research

- `RESEARCH_PARTICIPANT_PROTOCOL.md` — consent, privacy, recruitment and no-real-money-task boundaries.
- `../../experiments/EXPERIMENT_MANIFEST_TEMPLATE.md` — general pre-registration contract.
- `../../experiments/q03/Q03_PREREGISTRATION.md` — fixed Q03 product-decision gates.
- `../../experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md` — reproducible behavioral telemetry semantics.

### Quant research

- `../../experiments/q04/Q04_PREREGISTRATION.md` — deterministic harness gates and optional ML promotion gates.

### Competitive durability

- `../../experiments/q05/Q05_PREREGISTRATION.md` — competitive task, repeat-use linkage and replicability gates.

### External authority packets

- `q01/REGULATORY_REVIEW_PACKET.md` — exact frozen product bundle/questions for qualified Peruvian counsel.
- `q02/DATA_USE_PROFILE_PACKET.md` — provider-by-provider rights/economics/semantics closure unit.

---

## Current validation state

```text
Validation method / machinery        CLOSED

Q01 legal outcome                    OPEN
Q02 production data-rights outcome  OPEN
Q03 user value / WTP / repeat use   OPEN / PARTIAL
Q04 quant baseline / ML increment   OPEN
Q05 moat / durability               PARTIAL

MK0_PROMOTION_PACKET                 NOT YET INSTANTIATED
MK1_BOOTSTRAP_PROFILE                NOT YET APPROVED
Production MK1 implementation        BLOCKED
```

The files in this directory do not fabricate missing evidence. They make it difficult to close a gate without the evidence actually required.

---

## Execution map

```text
Stage 0  preregistration / evidence environment
   |
Stage 1  E03-A behavioral discovery
   |
Stage 2  E03-B Translator comprehension
   |
   +---------------------------+
   |                           |
Stage 3A E03-C repeat use   Stage 3B Q04-A harness
   |                           |
   +------------+--------------+
                |
Stage 4  pricing signal + Q02 candidate profiles
                |
Stage 5  Q01 counsel review
                |
Stage 6  Q02 exact production rights closure
                |
Stage 7  Q04-B optional ML
                |
Stage 8  Q05 durability
                |
Stage 9  unit economics sync
                |
Stage 10 contradiction review
                |
Stage 11 promotion packet + bootstrap profile
                |
Stage 12 production MK1 authorization
```

Parallelism/dependency exceptions are defined in `EVIDENCE_EXECUTION_SEQUENCE.md`.

---

## Required status vocabulary

### Evidence plans

```text
DRAFT
PRE_REGISTERED
RUNNING / EVIDENCE_RUNNING
ANALYSIS / REVIEW_READY
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

## Reviewer separation

Where the protocol requires an independent reviewer, the reviewer must not merely approve a narrative summary. They should be able to reconstruct the relevant decision from:
- pre-registration/authority;
- raw or lawful audit evidence;
- analysis code/artifacts;
- decision rule;
- limitations/adverse evidence.

For Q01/Q02, internal review never replaces the required external/provider authority.

---

## No-outcome-fabrication rule

Never create a receipt marked PASS just to exercise the workflow.

For dry-runs/tests use explicit synthetic identifiers and statuses such as:

```text
SYNTHETIC_TEST_ONLY
NOT_PROMOTION_EVIDENCE
```

Synthetic receipts must be impossible to mistake for production promotion evidence.

---

## Promotion invariant

A production build is authorized only when:

```text
Q01–Q05 promotable final receipts
        +
no unresolved P0/P1 contradiction
        +
approved MK0 promotion packet
        +
approved MK1 bootstrap profile
        +
BUILD_READINESS pass
```

Until then, the correct state is still research/validation.
