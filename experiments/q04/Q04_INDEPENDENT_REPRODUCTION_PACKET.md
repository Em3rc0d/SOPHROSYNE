# Q04 Independent Reproduction Packet

## Status

`READY_FOR_EXTERNAL_REVIEWER / REAL_DATA_PROFILE_MISSING / NOT_EVIDENCE`

This packet defines G4 independent reproduction before an external reviewer is selected. The reviewer must reproduce the frozen result without manual result editing and without relying on the original author's runtime state.

## Independence boundary

A valid reproducer:
- did not author the executed harness/profile;
- receives only the frozen package and instructions;
- uses a separate machine/runtime or independently provisioned environment;
- does not copy a precomputed result file and call that reproduction;
- records every deviation.

A second run by the same assistant/session is not independent.

## Required frozen package

```text
experiment manifest
dataset manifest
rights/profile refs
dataset files or rights-safe access instructions
dataset SHA-256 digests
calendar/session semantics
available_at semantics
corporate-action semantics
currency semantics
cost model
benchmark versions
golden fixtures
harness/analysis commit
environment lock
expected output schema
NO expected numeric benchmark values visible before reviewer run
```

The original expected outputs are escrowed/hidden until the independent run artifact is frozen.

## Real-data dataset manifest template

```yaml
dataset_id:
dataset_version:
provider_profile_id:
q02_authority_ref:
asset_universe: []
instrument_identifiers: []
data_families: []
bar_or_event_granularity:
date_start:
date_end:
timezone:
session_calendar:
corporate_action_policy:
currency_policy:
provider_timestamp_field:
event_time_semantics:
available_at_semantics:
correction_policy:
missing_interval_policy:
duplicate_policy:
raw_file_digests: {}
normalized_file_digests: {}
normalization_code_commit:
created_at:
frozen_at:
review_by:
```

No promotable dataset may use an unresolved Q02 profile.

## Reproduction procedure

Reviewer:
1. verifies package digests before execution;
2. provisions the environment from the frozen lock;
3. runs golden fixtures first;
4. confirms G1/G2/G5/G6/G7 before benchmark comparison;
5. runs the complete deterministic benchmark ladder;
6. performs the prescribed second identical rerun;
7. freezes their output directory/digests;
8. only then receives the original output digest;
9. compares discrete and numeric outputs using the frozen tolerance contract;
10. signs the reproduction note.

## Required independent output

```yaml
reproduction_id:
reviewer_identity_ref:
independence_statement:
machine_or_environment_ref:
source_commit:
environment_lock_digest:
dataset_manifest_digest:
input_file_digests: {}
golden_fixture_digest:
first_run_output_digest:
second_run_output_digest:
deterministic_rerun_pass:
point_in_time_integrity_pass:
golden_fixture_pass:
cost_monotonicity_pass:
dataset_integrity_pass:
benchmark_sanity_pass:
original_output_revealed_at:
comparison_result: MATCH | MATCH_WITHIN_TOLERANCE | MISMATCH | INCONCLUSIVE
mismatch_details: []
manual_edits_performed: false
deviations: []
review_completed_at:
signature_or_authoritative_ref:
```

## Mismatch rule

- discrete fills/orders/state transitions: exact match;
- canonical deterministic artifact digests: exact match where serialization is frozen;
- derived floats: within fixture/manifest tolerance only;
- no tolerance may be widened after seeing a mismatch;
- any unexplained point-in-time/leakage mismatch is a hard failure;
- any manual editing of result values invalidates G4.

## Current synthetic dry-run bridge

The existing synthetic dry-run hash
`d934d4e706a19f975a865893616723112f452dd9e5ac5ff69a56417cc45711ea`
remains an engineering receipt only.

It may be used to rehearse this packet, but a matching synthetic reproduction does not replace:
- a real frozen point-in-time dataset;
- Q02-compatible data rights;
- independent reproduction of that real profile.

## E04-B boundary

No ML experiment begins for promotion until E04-A reaches `CLOSED_PASS` on the exact real profile.

The valid result may still be `ml_scope: EXCLUDE` or `DEFER`; Q04 does not exist to force ML into MK1.
