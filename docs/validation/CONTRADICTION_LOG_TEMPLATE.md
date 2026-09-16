# Cross-Receipt Contradiction Log Template

## Purpose

A positive result in one evidence track may conflict with another track. This log prevents those conflicts from being averaged away into an artificial overall PASS.

Every contradiction capable of changing MK1 scope, legal posture, data rights, economics, quant validity or moat claims receives an explicit ID and lifecycle.

---

## Contradiction record

```yaml
contradiction_id:
status: OPEN | MITIGATING | RESOLVED | ACCEPTED_LIMITATION | SUPERSEDED
severity: P0 | P1 | P2 | P3
opened_at:
closed_at:
owner:
independent_reviewer:

receipts_in_conflict:
  -
locks_affected:
  -
bootstrap_sections_affected:
  -

statement:
why_the_results_conflict:

candidate_resolutions:
  - option:
    evidence_required:
    product_or_architecture_impact:
    residual_risk:

selected_resolution:
rationale:

canonical_docs_affected:
  -
reopened_internal_nodes:
  -
reopened_evidence_locks:
  -
new_or_superseding_adrs:
  -

verification_refs:
  -
residual_limitations:
```

---

## Severity

### P0

Contradiction would make the proposed configuration unauthorized, legally/data-rights incompatible, scientifically invalid or capable of violating a hard trust boundary.

Examples:
- Q01 counsel rejects the personalization flow preferred in Q03;
- Q02 forbids a data use required by the proposed product surface;
- Q04 depends on information unavailable at the historical `as_of` cutoff;
- proposed resolution would give an LLM forbidden authority.

P0 blocks promotion immediately.

### P1

Contradiction materially changes product scope, unit economics, core user value, provider/asset profile or the evidence-derived bootstrap configuration.

Examples:
- Q03 supports a persona that requires a data family not economically viable under Q02;
- the candidate moat depends on a feature removed by regulatory constraints;
- the only Q04-valid model requires a provider/profile not approved for MK1.

P1 blocks promotion until resolved.

### P2

Contradiction affects optimization or secondary scope but can safely remain behind an explicit limitation without changing core MK1 boundaries.

P2 must have an owner and treatment but need not block promotion if the promotion packet records the accepted limitation.

### P3

Minor discrepancy with no material effect on MK1 scope or trust boundaries. Track for completeness.

---

## Lifecycle

```text
OPEN
  -> MITIGATING
  -> RESOLVED
     or ACCEPTED_LIMITATION
     or SUPERSEDED
```

A contradiction is not `RESOLVED` because one receipt was preferred subjectively. Resolution requires evidence, re-scope or explicit removal of the conflicting dependency.

---

## Resolution patterns

### Narrow scope

Example: a flow is legally acceptable only without personalized ranking. Remove that behavior, update the product profile and re-test affected Q03/Q05 assumptions.

### Change provider/data profile

Example: preferred data use is prohibited or uneconomic. Select another candidate profile, close Q02 for it and re-run affected Q04/Q03 tests if semantics change.

### Exclude ML

Example: ML only works with rights-incompatible features. Preserve Q04-A baseline closure and set `ml_scope: EXCLUDE` or `DEFER`.

### Re-run user evidence

Example: legal/data changes materially alter the tested experience. Previous Q03 receipt remains historically valid for its old scope, but a new scoped receipt is required.

### Stop current configuration

If no compatible resolution preserves mandatory product value and trust constraints, mark the affected configuration `STOP_CURRENT_CONFIGURATION` rather than weakening a fatal gate.

---

## Promotion invariant

`MK0_PROMOTION_PACKET` cannot become `APPROVED` while any P0 or P1 contradiction is `OPEN` or `MITIGATING`.

A P2/P3 item may remain only when:
- the limitation is explicit;
- it does not contradict a fatal/hard invariant;
- residual risk is accepted by the appropriate reviewer;
- the bootstrap profile contains any necessary constraint.

---

## Anti-gaming rules

- do not merge multiple contradictions into vague “risk” wording;
- do not close a contradiction by dropping the weaker-looking evidence without justification;
- do not reinterpret an external authority beyond its scope;
- do not use sunk implementation effort as a resolution argument;
- do not resolve data-rights conflicts with an undocumented assumption;
- do not resolve quant conflicts by changing the test interval after inspection;
- do not label a P0/P1 conflict P2 merely to unblock promotion.
