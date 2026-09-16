# Observability and SLOs

## Purpose

Observability must answer four questions without opening the database manually:
1. Is the platform serving users correctly?
2. Is the market evidence fresh and complete enough to trust?
3. Can a specific DecisionRecord be traced back to its exact inputs and code path?
4. Are failures local, systemic, provider-driven or model-driven?

## Telemetry contract

Every web/API/worker operation propagates:
- `trace_id`;
- `request_id`;
- authenticated actor/service id where appropriate and privacy-safe;
- operation/job id;
- instrument/data-family identifiers when non-sensitive;
- deployment/build version.

Logs are structured JSON. Secrets, provider tokens, raw auth headers, personal portfolio contents and unrestricted provider payloads are prohibited from logs.

## Core metrics

### Platform
- API request rate, latency and error rate by route/status/code;
- active sessions and auth failures;
- DB pool saturation, transaction duration, lock waits and replication/backup health;
- worker queue depth, oldest job age, lease expirations and dead-letter count;
- object-storage errors and artifact hash mismatches.

### Data plane
- ingestion lag by provider/data family/instrument;
- freshness-state counts (`FRESH`, `STALE`, `EXPIRED`);
- quarantine rate and reasons;
- duplicate/reconciliation rate;
- provider capability health/circuit state;
- rights-denied artifact attempts;
- timestamp anomalies.

### Decision intelligence
- DecisionRecord assembly latency;
- finalization success vs `NO_CONCLUSION` / `REJECTED_INCOMPLETE`;
- provenance coverage percentage;
- probability outputs by calibration status;
- replay match/mismatch counts;
- model baseline-fallback rate;
- explanation rejection/validation rate.

### Research
- backtest job duration/failure rate;
- dataset manifest creation failures;
- look-ahead guard failures;
- experiment reproducibility pass rate;
- model calibration/drift gate status.

## Initial SLOs for beta readiness

These are engineering targets, not external contractual promises.

### Authoritative API
- monthly availability target: `>= 99.9%` excluding planned maintenance;
- p95 latency for ordinary read endpoints from ready projections: `< 500 ms`;
- p99 latency for those reads: `< 1500 ms`;
- mutation endpoints that enqueue research work may return `202` rather than block.

### Data freshness
Freshness SLOs are data-family specific. For the initial market-bar profile:
- 1-minute crypto bars: 99% normalized within 2 minutes of provider availability;
- daily ETF bars: available before the configured next decision cycle;
- news/macro/on-chain families define independent thresholds and are never forced into one universal freshness number.

A provider outage can consume the freshness error budget but cannot be hidden from user-visible state.

### DecisionRecord integrity
- 100% finalized records have non-null `as_of`, provenance lineage and version bundle;
- 100% user-visible probabilities reference an approved calibration artifact;
- 0 known finalized records mutate in place;
- 0 accepted records with rights-forbidden display lineage;
- replay match rate for the deterministic golden corpus: 100% before release.

### Job reliability
- 99.5% of normal jobs complete without manual intervention within their declared deadline;
- retry/dead-letter behavior is measured separately; retrying is not counted as first-attempt success.

## Error budgets

When a critical SLO exhausts its rolling error budget:
- feature work affecting that surface pauses;
- only reliability/remediation work proceeds until budget recovers or SLO is formally revised through evidence/ADR.

## Alerts

Page/urgent alerts are reserved for user-impacting or integrity-impacting conditions:
- authoritative API unavailable;
- database durability/backup failure;
- widespread ingestion expiry for required data;
- rights kill switch activated unexpectedly;
- unexplained DecisionRecord replay mismatch;
- finalized-record mutation attempt;
- elevated auth/security failures;
- job backlog exceeding hard freshness deadlines.

Non-urgent tickets/dashboards cover:
- single non-critical provider degradation;
- increasing quarantine rate below hard threshold;
- model drift warning before suspension;
- rising cost/latency trends.

## Dashboards

Minimum dashboards:
1. platform health;
2. provider/data freshness;
3. job pipeline;
4. DecisionRecord integrity and degradation;
5. research/replay quality;
6. security/audit anomalies;
7. unit-cost telemetry by major workload.

## Synthetic checks

Production-like monitoring must continuously verify:
- public app shell loads;
- authenticated API health through a synthetic non-user account;
- one representative read-only market-state path;
- object-storage read/write for a disposable synthetic artifact;
- database write/read via a dedicated health transaction;
- provider health endpoints without consuming excessive quotas.

Synthetic checks never create market recommendations or contaminate real user analytics.

## Trace retention and sampling

- errors, security events, rights denials and replay mismatches: retain at high fidelity;
- ordinary successful traffic: sampled according to cost;
- financial/user-private fields remain excluded regardless of sampling level.

## Release observability gate

A feature is not production-ready until:
- metrics exist for success/failure/degradation;
- at least one useful dashboard panel exists;
- alerts are defined for integrity-threatening failure modes;
- logs include trace/request correlation;
- on-call/runbook points to the owning module and recovery procedure.