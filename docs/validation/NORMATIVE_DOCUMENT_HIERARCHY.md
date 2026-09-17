# Normative Document Hierarchy

## Purpose

SOPHROSYNE has many research, governance, architecture and validation artifacts. This document defines a single authority order so two documents can never silently disagree about the same decision.

The hierarchy applies to MK0 evidence closure and MK1 promotion. It does not replace domain-specific contracts; it determines which artifact is authoritative when scopes overlap.

---

## Authority classes

### L0 — Governance invariants

Authoritative sources:
- `GOVERNANCE.md`
- accepted ADRs, including ADR-0014

These define project-wide invariants and change-control rules. No lower-level artifact may override them.

### L1A — Validation semantic normalization

Authoritative source:
- `docs/validation/CANONICAL_VALIDATION_SPEC.md`

This file normalizes cross-document semantics including lifecycle vocabulary, terminal decisions, promotion eligibility, geography, contradiction severity and provenance rules.

It does **not** replace detailed experiment thresholds, packets, statistical formulas or implementation contracts.

### L1B — Thesis / causal-value authority

Authoritative sources:
- `docs/product/THESIS_STACK.md`
- `docs/validation/Q00_CORE_CAUSAL_VALUE.md`
- `MK0_LOCKS.md`

These define:
- the separation between problem, causal, product, economic and defensibility claims;
- the rule that passing one layer never proves the next;
- the destructive baselines required before complexity can count as product value;
- the scoped kill/pivot behavior of a failed causal-value configuration.

Q03 willingness-to-pay, Q04 sophistication or Q05 moat evidence cannot override a failed Q00 current configuration.

### L1C — Detailed evidence lifecycle

Authoritative sources:
- `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`
- `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`

These define evidence workflow, preregistration, immutable receipts and detailed Q01–Q05 closure requirements.

They remain fully authoritative except where L0/L1A/L1B explicitly constrains the same scope.

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

These may be more specific than L1 but may not redefine lifecycle vocabulary, promotion eligibility, Q00 causal-value conclusions, jurisdictional scope or other higher-level rules.

### L3 — Evidence instances

Authoritative sources:
- frozen experiment manifests;
- Q00 experiment manifests/receipts;
- provider rights profiles;
- counsel review packets;
- finalized `EvidenceReceipt`s;
- contradiction-log entries.

A finalized receipt can close only the scoped question registered by its governing contracts.

### L4 — Promotion truth

Authoritative sources:
- instantiated `docs/validation/MK0_PROMOTION_PACKET.md`
- approved `docs/validation/MK1_BOOTSTRAP_PROFILE.md`
- `docs/validation/BOOTSTRAP_PROVENANCE_MATRIX.md`
- `docs/validation/AUDIT_TRACEABILITY_MATRIX.md`

Promotion artifacts may aggregate and freeze evidence-derived values. They may not reinterpret evidence or fill missing fields by convenience.

The Q00-approved intervention scope and exclusions are build-defining promotion truth.

### L5 — Build and release conformance

Authoritative sources:
- `docs/implementation/BUILD_READINESS.md`
- `docs/implementation/ACCEPTANCE_RECEIPTS.md`
- implementation/release receipts.

These verify that software conforms to an approved bootstrap profile. They cannot reintroduce components excluded by Q00 or change product/legal/data/scientific truth.

---

## Conflict-resolution rule

When two active documents conflict:

1. identify the exact overlapping scope;
2. apply the highest authority level that actually governs that scope;
3. if two documents at the same effective authority conflict, **do not choose one silently**;
4. create a contradiction-log entry;
5. block promotion if severity is P0/P1;
6. update/supersede the losing artifact explicitly;
7. preserve historical versions.

“Newest file wins”, “implementation chose this behavior”, and “the stricter one probably wins” are prohibited conflict-resolution mechanisms unless the governing contract explicitly defines such an intersection rule.

---

## Specificity rule

Specificity is allowed only inside the bounds of higher-level authority.

Examples:
- Q00 may conclude `SHORT_MEMORY_SUFFICIENT`; Q03/Q05 may test that narrowed product but cannot silently restore full persistent memory as a required core feature.
- Q03 may define exact WTP thresholds, but positive WTP cannot convert failed Q00 causal value into a promotable configuration.
- Q05 may identify defensibility only among components that survived Q00/Q01/Q02 constraints.

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
- thesis stack != validated causal effect;
- Q00 schema != Q00 PASS;
- preregistration != result;
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

> There is exactly one active authority path from governance to layered thesis and causal-value validation to evidence to promotion to implementation. No later commercial, technical or moat evidence can rescue a causal-value configuration that the higher-level gate rejected.
