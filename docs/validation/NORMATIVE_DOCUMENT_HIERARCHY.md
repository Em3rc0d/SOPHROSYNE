# Normative Document Hierarchy

## Purpose

SOPHROSYNE has many research, governance, architecture and validation artifacts. This document defines a single authority order so two documents can never silently disagree about the same decision.

The hierarchy applies to MK0 evidence closure and MK1 promotion. It does not replace domain-specific contracts; it determines which artifact is authoritative when scopes overlap.

---

## Authority classes

### L0 — Governance invariants

Authoritative sources:
- `GOVERNANCE.md`
- accepted ADRs

These define project-wide invariants and change-control rules. No lower-level artifact may override them.

### L1A — Validation semantic normalization

Authoritative source:
- `docs/validation/CANONICAL_VALIDATION_SPEC.md`

This file exists only to normalize cross-document semantics that were found inconsistent during the MK0 evidence-execution audit, including:
- evidence lifecycle vocabulary;
- terminal decision vocabulary;
- promotion eligibility;
- Peru promotion geography;
- Q01 legal/compliance breadth;
- Q03 cohort/geography corrections;
- Q04 aggregate `INCONCLUSIVE` semantics;
- Q05 exposure-aware denominators;
- bootstrap provenance requirements;
- contradiction severity.

It does **not** replace detailed experiment thresholds, packets, statistical formulas or implementation contracts.

When and only when a lower validation artifact conflicts with `CANONICAL_VALIDATION_SPEC.md` on one of the normalization topics above, the canonical normalization governs until the lower artifact is explicitly revised/superseded.

### L1B — Lock and lifecycle detail

Authoritative sources:
- `MK0_LOCKS.md`
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`

These define what remains open, detailed evidence requirements, closure workflow and promotion structure.

They remain fully authoritative except for a normalization conflict explicitly covered by L1A.

### L2 — Domain validation contracts

Authoritative sources:
- `docs/validation/q01/REGULATORY_REVIEW_PACKET.md`
- `docs/validation/q02/DATA_USE_PROFILE_PACKET.md`
- `experiments/q03/Q03_PREREGISTRATION.md`
- `experiments/q04/Q04_PREREGISTRATION.md`
- `experiments/q05/Q05_PREREGISTRATION.md`
- `docs/validation/STATISTICAL_DECISION_RULES.md`
- `docs/validation/RESEARCH_PARTICIPANT_PROTOCOL.md`
- `experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md`

These may be more specific than L1 but may not redefine lifecycle vocabulary, promotion eligibility, jurisdictional promotion scope or other L1 normalization rules.

### L3 — Evidence instances

Authoritative sources:
- frozen experiment manifests;
- provider rights profiles;
- counsel review packets;
- finalized `EvidenceReceipt`s;
- contradiction-log entries.

A finalized receipt can close only the scoped question registered by its governing L1/L2 contracts.

### L4 — Promotion truth

Authoritative sources:
- instantiated `docs/validation/MK0_PROMOTION_PACKET.md`
- approved `docs/validation/MK1_BOOTSTRAP_PROFILE.md`
- `docs/validation/BOOTSTRAP_PROVENANCE_MATRIX.md`
- `docs/validation/AUDIT_TRACEABILITY_MATRIX.md`

Promotion artifacts may aggregate and freeze evidence-derived values. They may not reinterpret evidence or fill missing fields by convenience.

The provenance/traceability matrices constrain where bootstrap values may come from; they do not create evidence themselves.

### L5 — Build and release conformance

Authoritative sources:
- `docs/implementation/BUILD_READINESS.md`
- `docs/implementation/ACCEPTANCE_RECEIPTS.md`
- implementation/release receipts.

These verify that software conforms to an approved bootstrap profile. They cannot change product, legal, data-rights, scientific or commercial truth.

---

## Conflict-resolution rule

When two active documents conflict:

1. identify the exact overlapping scope;
2. apply the highest authority level that actually governs that scope;
3. apply L1A only to its explicitly enumerated normalization topics;
4. if two documents at the same effective authority conflict, **do not choose one silently**;
5. create a contradiction-log entry;
6. block promotion if severity is P0/P1;
7. update/supersede the losing artifact explicitly;
8. preserve historical versions.

“Newest file wins”, “implementation chose this behavior”, and “the stricter one probably wins” are prohibited conflict-resolution mechanisms unless the governing contract explicitly defines such an intersection rule.

---

## Specificity rule

Specificity is allowed only inside the bounds of higher-level authority.

Example:
- L1A says empirical final decisions are `CLOSED_PASS`, `CLOSED_CONDITIONAL`, `PIVOT_REQUIRED`, `STOP_CURRENT_CONFIGURATION` or `INCONCLUSIVE`.
- Q03 may define exact numeric criteria for those outcomes.
- Q03 may **not** invent another promotable terminal state.

---

## Archive rule

Historical drafts and pre-audit versions may be preserved under an archive path for provenance.

Archived material is:
- immutable evidence of design history;
- useful for diff/audit/recovery;
- **non-normative** unless explicitly re-promoted through governance.

Every archive root must contain a README that states that archived files do not govern current behavior.

---

## Evidence-vs-design rule

A document may define how evidence will be evaluated without claiming the evidence exists.

Therefore:
- preregistration != result;
- schema != receipt;
- legal review packet != legal opinion;
- DataUseProfile template != licensed right;
- bootstrap schema != approved bootstrap profile;
- provenance matrix != populated bootstrap;
- acceptance-receipt schema != passing implementation receipt.

---

## Jurisdiction rule

The initial MK1 promotion scope is Peru unless a promotion packet explicitly freezes another reviewed jurisdiction.

Evidence collected outside Peru may be exploratory or supportive, but cannot by itself authorize Peru-specific legal/commercial claims where jurisdiction matters.

---

## Audit-report rule

`docs/validation/AUDIT_CLOSURE_REPORT.md` records audit findings and the design-audit verdict. It is **not** itself an authority source for product/legal/data/scientific truth.

If the audit report describes a rule that is not represented in an authoritative L0–L5 contract, the report is incomplete and the rule is not considered frozen until the authoritative contract is updated.

---

## Final invariant

> There is exactly one active authority path from governance to normalized validation semantics to evidence to promotion to implementation. Historical detail is preserved, but historical drafts and audit prose do not compete with current truth.
