# Failure and Degradation Contract

SOPHROSYNE must fail **closed, explicit and auditable**. The system must prefer `NO_CONCLUSION`, `NOT_EVALUABLE` or degraded read-only output over silently fabricating freshness, confidence or completeness.

## Global rules

1. Never relabel cached historical output as current.
2. Never replace missing evidence with LLM-generated content.
3. Never silently switch to a provider with different semantics or insufficient data rights.
4. Never complete a DecisionRecord when required provenance/version lineage is missing.
5. Retry only operations classified as retry-safe and idempotent.
6. After retry budget exhaustion, move work to an inspectable terminal state; no infinite loops.
7. Every degradation state is user-visible when it affects interpretation quality.

## Failure matrix

| Failure | System response | User-visible state | Recovery |
|---|---|---|---|
| Primary provider timeout | bounded retry; use compatible fallback only if pre-approved | `DEGRADED` or unchanged if fallback equivalent | health probe + reconciliation |
| All providers unavailable | stop fresh state generation | `PROVIDER_DEGRADED` / `NO_CONCLUSION` | automatic retry with backoff |
| Required data stale | refuse fresh DecisionRecord | `DATA_STALE` | ingest/reconcile |
| Optional data stale | compute only if state profile permits | `DEGRADED` + missing dimensions | ingest/reconcile |
| Provider schema drift | quarantine new payloads | affected data unavailable | adapter update + replay fixtures |
| Duplicate provider event | idempotently ignore semantic duplicate | none | automatic |
| Timestamp anomaly / future data | quarantine | coverage gap | operator inspection |
| Rights record suspended/revoked | block new display/use immediately | `RIGHTS_RESTRICTED` | new verified rights record |
| Database unavailable | no authoritative writes; reads only if safe cache policy permits | service unavailable/degraded | DB recovery |
| Transaction commit uncertain | resolve through idempotency key before retry | pending/retryable | reconciliation |
| Worker crash mid-job | lease expires; job becomes reclaimable | pending | another worker claims |
| Repeated worker failure | dead-letter after configured attempts | operation failed | operator/research review |
| Model artifact unavailable | use approved deterministic baseline if semantics permit | baseline/degraded | model restore |
| Model drift gate breached | suspend model | baseline/degraded | revalidation/new artifact |
| LLM unavailable | structured authoritative output remains available | explanation unavailable | retry later |
| LLM policy/validation failure | discard generation | explanation unavailable | regenerate or deterministic template |
| Object storage unavailable | do not finalize artifact-dependent operations | pending/failed | retry/reconcile |
| Auth provider unavailable | existing valid sessions may follow configured grace policy; no new login | login unavailable | provider recovery |
| Clock skew outside tolerance | reject/quarantine affected ingestion/workers | degraded | NTP/platform repair |

## Provider fallback requirements

A fallback route must be declared before production and include:
- same canonical instrument mapping;
- compatible timestamp semantics;
- compatible adjustment methodology where relevant;
- compatible resolution/coverage;
- verified rights for the exact use;
- normalization tests proving acceptable equivalence;
- explicit source lineage in downstream records.

Fallback must not merge sources into one fake homogeneous history without provenance.

## Freshness classes

Each data family defines:
- `fresh_window`;
- `stale_window`;
- `hard_expiry`;
- whether stale data may contribute to `DEGRADED` outputs;
- whether stale data invalidates the full state.

These thresholds are configuration under version control and become part of the DecisionRecord version bundle.

## Retry policy

Retries require all of:
- operation is idempotent or protected by an idempotency key;
- error is classified retryable;
- bounded exponential backoff with jitter;
- provider rate-limit headers respected;
- maximum attempts/deadline defined.

Validation, rights denial, semantic schema mismatch and deterministic calculation failures are not blindly retried.

## Circuit breaking

Provider capabilities maintain health state. Repeated failures open a capability-level circuit and prevent request storms. Half-open probes are isolated from user requests.

## Reconciliation jobs

Periodic reconciliation verifies:
- ingestion gaps;
- outbox events without completed side effects;
- expired worker leases;
- DecisionRecords referencing missing artifacts;
- object-storage hashes;
- provider corrections;
- retention/rights obligations;
- stale materialized projections.

Reconciliation may repair derived state, but may not mutate finalized DecisionRecords.

## Kill switches

Administrative controls must support immediate disablement by:
- provider;
- data family;
- model version;
- feature/endpoint;
- explanation generation;
- strategy evaluation class.

Kill switches default to fail-closed and are audited.

## Recovery invariants

After any outage:
- no duplicate finalized user artifact for one idempotent request;
- no data gap may be silently hidden;
- no event is considered processed only because it was claimed;
- replay from authoritative data must converge to the same deterministic result for the same version bundle;
- user-facing historical timestamps remain the original ones, not recovery time.

## Disaster-recovery minimum for MK1

Before production beta:
- automated database backups with restore test;
- object storage versioning or equivalent immutable recovery;
- documented RPO/RTO targets;
- restoration rehearsal in staging;
- secrets re-provisioning procedure;
- provider credential revocation procedure;
- incident communications template.

No backup is considered valid until a restore has succeeded in a clean environment.