# Q03 Research Collector / Export Reference Path

## Status

REHEARSAL_COMPLETE / LOCAL_REFERENCE_ONLY / Q01_SECURITY_PRIVACY_APPROVAL_REQUIRED_FOR_REAL_PARTICIPANTS

Canonical implementation:
- experiments/q03/research_collector.py

This closes the internal engineering question "how will events receive an authoritative receive timestamp, be deduplicated, exported and hashed?" It does not authorize hosting or human-data collection.

## Properties

The reference collector:
- uses only Python standard library;
- binds to loopback by default;
- refuses non-loopback deployment even when the flag is supplied;
- requires bearer token from SOPHROSYNE_RESEARCH_TOKEN;
- stores pseudonymous event data in SQLite;
- adds server-side received_at_utc;
- deduplicates by event_id;
- accepts an idempotent retry only if its client-origin payload is identical;
- rejects event-ID collisions with different payloads;
- has a promotion-grade mode that rejects missing participant identity, UNKNOWN geography and UNFROZEN_REHEARSAL prototype digests;
- exports canonically ordered events;
- computes SHA-256 over the canonical event array;
- rehearses participant deletion;
- keeps no dashboard for outcome peeking.

## Explicit non-production boundary

This reference implementation intentionally refuses public/non-loopback serving.

Before any real participant data:
- Q01 approves notice/consent, retention and deletion semantics;
- security review selects an approved hosted collector or hardens/supersedes this reference;
- storage region/access control/backups/logging are frozen;
- token provisioning and rotation are frozen;
- TLS/reverse proxy/network controls are frozen;
- retention/deletion jobs are tested;
- data processor/subprocessor treatment is reviewed;
- final endpoint/client integration is frozen.

A successful local self-test is engineering evidence only.

## Promotion-grade event path

~~~text
browser/research client
    ↓ stable event_id + frozen prototype_digest
approved HTTPS collector
    ↓ schema + auth + idempotency
server received_at_utc
    ↓ append-only research store / access controls
frozen export
    ↓ canonical ordering
events_sha256
    ↓
DQ checks + exclusion/deviation freeze
    ↓
Q03 analysis
~~~

## Rehearsal command

~~~bash
python experiments/q03/research_collector.py self-test
~~~

Expected properties:
- idempotent retry PASS;
- unfrozen promotion-grade event rejected;
- stable export event digest;
- participant deletion path rehearsed.

## Fail-closed rules

- do not reconstruct lost events from participant memory;
- event collision with changed payload is error;
- collector receive time never overwrites client occurred time;
- public deployment is forbidden by this reference implementation;
- a collector outage cannot be hidden by fabricating receive timestamps;
- deletion after a valid request must produce a new export digest; old immutable evidence packages remain governed by the approved legal/retention protocol rather than silently rewritten.
