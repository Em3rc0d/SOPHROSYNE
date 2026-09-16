# MK1 Operations Runbook

## Incident objective

Protect correctness, user trust, legal/data-rights compliance and evidence integrity before preserving feature availability.

## Severity

- `P0` — confirmed or likely compromise of user isolation, evidence integrity, rights/compliance, irreversible data loss, or unauthorized financial authority.
- `P1` — major user-facing outage, required market data expired broadly, replay mismatch affecting released logic, database durability risk, or security incident without confirmed compromise.
- `P2` — partial degradation with safe fallback, localized provider failure, growing backlog that is still inside deadlines.
- `P3` — non-urgent defect or operational debt with no current integrity/user-impact risk.

## First 10-minute procedure

1. Identify whether impact concerns security, data rights, data correctness, availability or model behavior.
2. Open incident record with UTC start time, owner and severity.
3. Preserve logs/traces/config/build identities; do not destroy evidence while troubleshooting.
4. Activate the narrowest safe kill switch when integrity or rights may be affected.
5. Stop new artifact finalization if correctness cannot be established.
6. Confirm whether finalized historical DecisionRecords remain immutable and readable.
7. Establish user-visible degradation rather than silently serving stale/partial results.
8. Record every privileged/manual action in the incident timeline.

## Core runbooks

### Provider outage / stale required data

Symptoms:
- freshness alerts;
- circuit open;
- increasing `DATA_STALE` / `PROVIDER_DEGRADED`.

Actions:
1. check provider capability health and rate-limit state;
2. verify local ingestion pipeline before blaming provider;
3. enable only pre-approved semantically/rights-compatible fallback;
4. if no valid fallback, stop fresh DecisionRecord finalization for affected profiles;
5. reconcile missing intervals after recovery;
6. run gap and duplicate checks before returning to healthy.

Never backfill an outage with a different source while erasing source lineage.

### Provider schema drift

1. Quarantine new incompatible payloads.
2. Disable affected capability if normalization correctness is uncertain.
3. Capture a minimal fixture when retention rights allow.
4. Update adapter/schema mapping and contract tests.
5. Replay quarantined data through staging.
6. Re-enable only after normalization/golden checks pass.

### Rights suspension/revocation

Treat unexpected rights loss as P0/P1 depending on exposure.

1. Activate provider/data-family rights kill switch.
2. Block new display/derived use immediately.
3. Identify affected cached/raw content and retention obligations.
4. Preserve audit metadata without continuing forbidden display.
5. Obtain new verified `DataRightsRecord` before reactivation.
6. Review whether historical user-visible artifacts require masking/removal under contract.

### Replay mismatch

Unexplained mismatch of a deterministic golden/finalized artifact is at least P1.

1. Stop promotion of affected algorithm/model/config.
2. Compare data manifest, build digest, config, normalization and dependency versions.
3. Determine whether mismatch is data correction, version absence, numerical tolerance or semantic regression.
4. Never rewrite original DecisionRecord to make replay pass.
5. Fix or create explicit semantic version/ADR if change was intentional.
6. Expand regression corpus with the discovered case.

### Database outage/saturation

1. Stop write-dependent finalization; do not route authoritative writes to an unverified substitute.
2. Check managed DB health, pool exhaustion, lock waits and storage/capacity.
3. Shed non-critical/research load before user-critical paths.
4. If failover occurs, verify recovery point and application idempotency state.
5. Run consistency/reconciliation checks before clearing incident.

Initial beta engineering targets to prove in staging:
- database `RPO <= 15 minutes`;
- database/service `RTO <= 60 minutes` for recoverable infrastructure failure.

These are not considered achieved until restore/failover exercises measure them.

### Worker backlog / crashed workers

1. Measure oldest job age against semantic deadline, not only queue length.
2. Verify leases are expiring/reclaimable.
3. Scale workers only after ruling out poison jobs/provider rate limits/database contention.
4. Dead-letter deterministic failures instead of retry storms.
5. Reconcile outputs after recovery.

### Model drift / invalid model behavior

1. Suspend model version.
2. Route to approved deterministic baseline where allowed.
3. Surface degraded/baseline state.
4. Preserve input/output manifests for investigation.
5. Revalidate on independent OOS data before any redeployment.

### LLM outage or unsafe explanation

1. Disable explanation generation if validation failure rate is elevated.
2. Continue serving authoritative structured market/evidence/ledger data.
3. Do not replace failed explanations with unvalidated text from another model automatically.
4. Restore only after schema/policy tests pass.

LLM outage is not allowed to become a core market-state outage.

### Credential compromise

1. Kill affected integration.
2. Revoke credential at provider/secret source.
3. Rotate and re-provision least-privilege credential.
4. Review provider/audit logs for misuse.
5. Search for accidental exposure in Git/logs/artifacts.
6. Re-enable after validation.

### Authentication/authorization anomaly

Potential cross-user access is P0.

1. Disable affected route/session class if necessary.
2. Revoke suspect privileged/user sessions.
3. Preserve audit logs.
4. Verify ownership and authorization checks with a reproduction test.
5. Determine affected users/resources.
6. Patch and add regression test before reopening.

### Object storage corruption/unavailability

1. Stop finalization of artifact-dependent operations.
2. Verify content hashes/versioning.
3. Restore immutable objects from provider/versioned backup where possible.
4. For reproducible artifacts, regenerate only from verified manifests and record new storage identity without altering original lineage.

## Recovery checklist

Before closing an incident:
- health/freshness metrics normal;
- backlog reconciled;
- no unexplained data gaps/duplicates;
- rights status valid;
- golden replay for affected surfaces passes;
- synthetic checks pass;
- kill switches intentionally reset;
- user-visible stale/degraded labels no longer apply;
- incident timeline complete.

## Communications

For user-impacting P0/P1 incidents, prepare factual status communication containing:
- affected capability;
- start/end or ongoing state;
- whether historical data/DecisionRecords were affected;
- whether security/privacy/data-rights impact is known;
- remediation state.

Do not speculate about financial impact or market outcomes.

## Postmortem

P0/P1 require a blameless technical postmortem with:
- timeline;
- trigger and contributing conditions;
- why safeguards did/did not contain impact;
- detection latency;
- user/integrity/rights impact;
- corrective actions with owners;
- new test/alert/runbook item;
- whether architecture or SLO assumptions change.

The incident is not considered fully resolved until high-priority corrective actions are tracked.