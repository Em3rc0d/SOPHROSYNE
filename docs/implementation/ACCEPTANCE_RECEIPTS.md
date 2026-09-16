# MK1 Acceptance Receipt Contract

## Purpose

MK0 closes system decisions. MK1 and beta must prove that implementation conforms to those decisions.

A **receipt** is immutable evidence that a specific implemented surface was tested against a closed contract. Receipts prevent phrases such as “security done”, “observability done” or “replay works” from becoming unauditable status claims.

Receipts are implementation evidence, not substitutes for design decisions.

## Common receipt envelope

Every required receipt records at minimum:

```yaml
receipt_id: string
receipt_type: enum
status: PASS | FAIL | WAIVED
scope: string
environment: local | ci | staging | production
build_digest: string | null
config_version: string | null
schema_or_contract_version: string | null
executed_at_utc: timestamp
executed_by: human-or-service-identity
inputs:
  - immutable identifier/hash/version
checks:
  - id: string
    result: PASS | FAIL | NOT_APPLICABLE
    evidence: immutable reference/hash
failures:
  - code: string
    severity: P0 | P1 | P2 | P3
    description: string
waiver:
  adr_or_risk_acceptance: string | null
expires_at_utc: timestamp | null
revalidate_on:
  - build_change
  - config_change
  - provider_change
  - contract_change
  - security_boundary_change
notes: string | null
```

## Receipt invariants

- `PASS` means every mandatory check for that receipt type passed.
- `FAIL` blocks the promotion gate that requires the receipt.
- `WAIVED` is prohibited for P0/P1 integrity, authorization, rights, replay, anti-leakage or immutable-record guarantees.
- A waiver requires an explicit ADR/risk-acceptance reference and expiry.
- Receipts are append-only. A later run supersedes; it does not rewrite history.
- Build-specific receipts must bind to an immutable artifact digest.
- Provider/data receipts bind to provider capability/schema/data-rights versions where applicable.
- A receipt is invalid after any declared `revalidate_on` trigger until a new receipt passes.

## Required receipt classes

### `RUNTIME_TOPOLOGY`

Proves the implemented deployable boundaries match `REFERENCE_ARCHITECTURE.md`.

Mandatory checks:
- authoritative API boundary identified;
- worker boundaries isolated as designed;
- PostgreSQL is authoritative transactional state;
- object storage is non-authoritative artifact storage;
- LLM path cannot acquire authoritative write/execution capability.

### `API_CONTRACT`

Proves public/internal API semantics match versioned contracts.

Mandatory checks:
- schema validation;
- stable error envelope;
- authorization behavior;
- idempotency semantics;
- optimistic concurrency where specified;
- retry-safe behavior.

### `PROVIDER_CONTRACT`

Proves one provider adapter obeys canonical normalization semantics.

Mandatory checks:
- timestamp mapping;
- identity/symbol mapping;
- sessions/timezones where relevant;
- missing/duplicate/correction behavior;
- rate-limit/failure mapping;
- provenance and rights metadata preservation;
- pathological fixture suite.

### `ANTI_LEAKAGE`

Proves point-in-time guards prevent use of unavailable information.

Mandatory checks:
- `available_at <= as_of` enforcement;
- future revision exclusion;
- feature-availability cutoff;
- overlapping-label purge/embargo behavior where applicable;
- negative fixtures intentionally attempting look-ahead.

This receipt cannot be waived.

### `GOLDEN_REPLAY`

Proves deterministic replay for the approved corpus.

Mandatory checks:
- exact manifest/version resolution;
- deterministic outputs within declared numerical tolerances;
- `KNOWLEDGE_AS_OF_THEN` behavior;
- corrected-history mode remains distinct;
- mismatch fails the receipt.

Required release target: 100% approved deterministic corpus match.

### `QUANT_ACCOUNTING`

Proves hand-computed fixtures for backtest mechanics.

Mandatory checks:
- signal/fill timing;
- fees/spread/slippage;
- position/cash accounting;
- corporate actions where in scope;
- returns/drawdown/benchmark calculations;
- missing-data and warm-up behavior.

### `FAILURE_DEGRADATION`

Proves defined fail-safe behavior under injected faults.

Mandatory checks:
- provider outage/staleness;
- worker retry/dead-letter behavior;
- DB/object-storage degradation;
- model suspension/baseline fallback;
- LLM outage;
- invalid/partial evidence;
- no silent stale/partial finalization.

### `SECURITY_READINESS`

Proves the security baseline is implemented.

Mandatory checks:
- auth/session/ownership tests;
- IDOR/CSRF/XSS/SSRF negative tests;
- least-privilege service/database/provider roles;
- secret scan;
- dependency/container scan disposition;
- hostile-content/LLM isolation tests;
- audit events for privileged changes;
- kill/revoke controls;
- no execution/withdrawal credentials in MK1.

P0/P1 failures block beta.

### `SECRET_ROTATION`

Proves a production-like credential can be revoked and replaced without undocumented manual state.

Mandatory checks:
- revoke old credential;
- provision replacement;
- dependent services recover;
- old credential no longer functions;
- audit trail complete.

### `BACKUP_RESTORE`

Proves recoverability instead of merely configured backups.

Mandatory checks:
- backup artifact exists and is readable;
- restore into isolated environment succeeds;
- integrity/reconciliation checks pass;
- measured RPO/RTO recorded;
- credentials/secrets are not restored insecurely.

### `OBSERVABILITY_SLO`

Proves telemetry is sufficient to operate the system.

Mandatory checks:
- trace/request propagation;
- required metrics emitted;
- dashboards populated from real synthetic/staging traffic;
- urgent alerts fire in controlled test;
- sensitive data absent from logs/traces;
- freshness/degradation visible;
- measured latency/reliability recorded against beta targets.

Target failure does not rewrite the target; it blocks promotion or forces an explicit evidence-backed ADR.

### `INCIDENT_DRILL`

Proves the runbook is executable.

Mandatory scenarios before beta:
- provider/stale-data incident;
- credential compromise/rotation;
- replay mismatch;
- database recovery path;
- rights kill-switch activation.

For each scenario record detection, containment, recovery, owner, timeline and corrective gaps.

### `RIGHTS_CONFIGURATION`

Proves approved commercial rights were translated into enforceable configuration.

Mandatory checks:
- exact provider/data family/version referenced;
- storage/display/derived/redistribution permissions encoded;
- forbidden actions rejected;
- kill switch tested;
- retention behavior tested.

This receipt depends on external Q02 evidence and cannot close Q02 by itself.

### `CI_RELEASE`

Proves artifact promotion semantics.

Mandatory checks:
- immutable build digest;
- SBOM/provenance attached;
- mandatory tests green;
- staging uses exact release artifact;
- production promotion uses same artifact;
- rollback target known and tested.

## Gate mapping

### Start MK1 production implementation

No implementation receipt is required to start coding; the evidence gates in `BUILD_READINESS.md` control start readiness.

### Complete a vertical slice

Requires the relevant subset of:
- API contract;
- provider contract;
- security checks;
- failure/degradation;
- telemetry;
- migration/persistence checks.

### Beta

Beta requires, at minimum, current PASS receipts for:

- `GOLDEN_REPLAY`;
- `ANTI_LEAKAGE`;
- `QUANT_ACCOUNTING` for enabled quant surfaces;
- every enabled provider's `PROVIDER_CONTRACT`;
- `SECURITY_READINESS`;
- `SECRET_ROTATION`;
- `BACKUP_RESTORE`;
- `OBSERVABILITY_SLO`;
- `INCIDENT_DRILL`;
- `RIGHTS_CONFIGURATION` for commercial data;
- `CI_RELEASE`.

## Ownership

Each receipt type has one accountable implementation owner. Ownership may be one person during MK1, but responsibility must be explicit in the receipt.

## Design-closure consequence

Because receipt schemas, triggers and gate effects are defined here, security, observability and operations no longer remain `CLOSED_FOR_DESIGN`. Their design state is simply `CLOSED`; only execution evidence remains pending.