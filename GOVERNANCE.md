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

## Evidence classes

Important claims should preserve provenance:

- **OFFICIAL** — regulator, statute, exchange/vendor contract or authoritative specification.
- **ACADEMIC** — peer-reviewed paper or strong methodological source.
- **OBSERVED** — directly measured in our experiments.
- **INFERRED** — reasoned conclusion from evidence.
- **HYPOTHESIS** — intentionally unproven proposition awaiting a test.

## Change control

Changes to product promise, regulatory posture, data-rights model, execution authority, probability semantics, quant validation, risk limits, LLM authority or critical providers require an ADR or equivalent explicit decision record.

## Promotion rule

A later MK may not redefine an unresolved earlier lock as closed merely because implementation exists.

> Code is not evidence that the underlying decision was correct.
