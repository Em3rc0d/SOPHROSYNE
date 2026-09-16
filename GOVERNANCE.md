# Governance

SOPHROSYNE follows a docs-first, evidence-gated development model.

## Canonical lifecycle

`brainstorming → research/mining → design → architecture → plan → build → test → certification`

Implementation must not silently resolve open product, legal, data-rights or scientific questions.

## MK policy

- **MK0 — Closure & Validation:** define product, evidence base, contracts, risks and kill criteria.
- **MK1 — Evidence MVP:** build only the minimum non-custodial decision-intelligence product needed to test user value and scientific reproducibility.
- **MK2+ — Expansion:** connected data, execution and B2B only after separate gates open.

Each MK has a lock registry. A lock is `CLOSED`, `PARTIAL`, `OPEN` or `FATAL_IF_FAILED`.

## Internal design closure

An internal design lock becomes `CLOSED` only when:

- one canonical artifact owns its semantics;
- invariants and allowed/forbidden behavior are explicit;
- failure/degradation semantics are explicit where applicable;
- versioning/change control is explicit;
- implementation verification obligations are named;
- no high-impact choice is intentionally deferred to feature coding.

A closed internal design lock does **not** claim that unbuilt software has already passed tests.

Implementation proof is tracked separately with immutable typed acceptance receipts defined in `docs/implementation/ACCEPTANCE_RECEIPTS.md`.

Examples:
- security control semantics may be `CLOSED` while `SECURITY_READINESS` is still pending;
- SLO targets and measurement semantics may be `CLOSED` while `OBSERVABILITY_SLO` is still pending;
- incident runbooks may be `CLOSED` while `INCIDENT_DRILL` is still pending.

This separation is governed by ADR-0012.

## Reopen rule

A closed internal node is reopened only when new evidence demonstrates that its canonical decision is invalid, contradictory or insufficient for the selected scope.

Reopening requires:

1. explicit lock status change;
2. affected canonical artifacts identified;
3. downstream dependency review;
4. an ADR when an invariant changes;
5. new closure evidence before implementation proceeds through the affected boundary.

Implementation inconvenience alone is not authority to silently mutate semantics.

## Evidence classes

Important claims should preserve provenance:

- **OFFICIAL** — regulator, statute, exchange/vendor contract or authoritative specification.
- **ACADEMIC** — peer-reviewed paper or strong methodological source.
- **OBSERVED** — directly measured in our experiments.
- **INFERRED** — reasoned conclusion from evidence.
- **HYPOTHESIS** — intentionally unproven proposition awaiting a test.

## Change control

Changes to product promise, regulatory posture, data-rights model, execution authority, probability semantics, quant validation, risk limits, LLM authority, runtime topology, point-in-time semantics, design-closure semantics or critical providers require an ADR or equivalent explicit decision record.

## Promotion rule

A later MK may not redefine an unresolved earlier lock as closed merely because implementation exists.

Likewise, implementation may not redefine a closed design contract merely because a test is hard to pass. The design is reopened explicitly or the implementation is corrected.

> Code is not evidence that the underlying decision was correct.

> A passing receipt is evidence of implementation conformance, not authority to invent new semantics.
