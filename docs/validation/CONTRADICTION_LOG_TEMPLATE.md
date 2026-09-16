# Cross-Receipt Contradiction Log

## Purpose

Cross-Q conflicts are first-class evidence. They are never averaged into an artificial overall PASS.

## Record

```yaml
contradiction_id:
status: OPEN | MITIGATING | RESOLVED | ACCEPTED_LIMITATION | SUPERSEDED
initial_severity: P0 | P1 | P2 | P3
current_severity: P0 | P1 | P2 | P3
severity_change_rationale:
severity_change_evidence_refs: []
severity_change_reviewer:
opened_at:
closed_at:
owner:
independent_reviewer:
receipts_in_conflict: []
locks_affected: []
bootstrap_sections_affected: []
statement:
why_the_results_conflict:
candidate_resolutions: []
selected_resolution:
rationale:
verification_refs: []
canonical_docs_affected: []
reopened_internal_nodes: []
reopened_evidence_locks: []
new_or_superseding_adrs: []
residual_limitations: []
```

## Severity

- **P0** — unauthorized/legal/data-rights incompatible, scientifically invalid, or hard trust-boundary violation.
- **P1** — materially changes product scope, unit economics, core value, provider/asset profile or bootstrap configuration.
- **P2** — secondary/optimization conflict that can remain behind an explicit limitation without changing core MK1 boundaries.
- **P3** — minor discrepancy with no material effect on scope or trust boundaries.

Severity is based on impact, not convenience. A downgrade requires new evidence, rationale and independent review.

## Promotion rules

- P0/P1 must be `RESOLVED` or `SUPERSEDED` by a resolved successor before promotion.
- P0/P1 may not use `ACCEPTED_LIMITATION` to bypass promotion gates.
- `ACCEPTED_LIMITATION` is permitted only for P2/P3, with an owner, residual-risk statement and bootstrap constraint where material.
- A contradiction is not resolved because one receipt was preferred subjectively.

## Valid resolution patterns

Narrow scope; change provider/data profile; exclude/defer ML; re-run affected user evidence after a material UX/legal/data change; reopen internal design with an ADR; or stop the current configuration.

## Anti-gaming

Do not merge distinct contradictions into vague risk wording, silently downgrade severity, drop inconvenient evidence, reinterpret external authority beyond scope, change test windows/thresholds after inspection, or use implementation effort as a resolution argument.
