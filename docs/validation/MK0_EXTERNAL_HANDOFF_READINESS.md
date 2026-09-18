# MK0 External Handoff Readiness

## Status

INTERNAL_PRE_HANDOFF_HARDENING: CLOSED_CANDIDATE

MK0_PROMOTION: BLOCKED

This document answers one narrow question:

> Is every currently known internal artifact needed to request the remaining external authority / empirical evidence prepared, traceable and fail-closed?

Current answer: **yes, subject to independent review of the candidate packets themselves**.

This is not an MK0 promotion receipt.

## Gate matrix

| Gate | Internal handoff state | External / empirical blocker |
|---|---|---|
| Q00 causal value | READY_FOR_INDEPENDENT_REVIEW — seven-arm prototype v2.2, eight-case corpus, Williams assignment generator, candidate sample/analysis thresholds, scoring rubric, recruitment/moderator packet, reviewer handoff | independent methods + market review, exact G comparator freeze, Q01-approved participant flow, adult Peru cohort, actual run |
| Q01 Peru boundary | READY_TO_SEND_AFTER_FLOW_DIGESTS — regulatory packet + counsel cover note + public-source refresh | qualified Peru counsel/privacy/consumer authority tied to exact frozen flows |
| Q02 data rights | READY_TO_SEND — DataUseProfile packet + provider inquiry template + public-source refresh | executed/written provider authority and current commercial quote for exact use profiles |
| Q03 repeat use / WTP | READY_FOR_Q01_AND_INDEPENDENT_REVIEW — 14-day runbook, telemetry contract, prototype rehearsal events | Q01-approved consent/retention, promotion-grade collector/export receipt path, adults, 14-day observation, pricing evidence |
| Q04 quant harness | READY_FOR_EXTERNAL_REPRODUCTION_HANDOFF — prereg, synthetic dry-run, independent reproduction packet | Q02-compatible real point-in-time dataset/profile + independent reviewer/run path |
| Q05 durability | READY_FOR_INDEPENDENT_REVIEW — comparator snapshot candidate, execution kit, component exposure contract | Q03 persona/repeat-use receipt, exact comparator execution state, adult participants, independent review, Q01/Q02 compatibility |

## Internal artifacts added for handoff hardening

~~~text
experiments/q00/Q00_SAMPLE_AND_ASSIGNMENT_PLAN.md
experiments/q00/Q00_SCORING_RUBRIC.md
experiments/q00/Q00_REVIEWER_HANDOFF.md
experiments/q00/Q00_RECRUITMENT_AND_MODERATOR_PACKET.md
experiments/q00/generate_assignment.py
experiments/q00/Q00_G_COMPARATOR_FREEZE_SHEET.md

experiments/q03/Q03_14_DAY_RUNBOOK.md
experiments/q03/q03_event.schema.json
experiments/q03/validate_event_export.py

experiments/q04/Q04_INDEPENDENT_REPRODUCTION_PACKET.md

experiments/q05/Q05_COMPONENT_EXPOSURE_CONTRACT.md

docs/validation/q01/COUNSEL_COVER_NOTE.md
docs/validation/q02/PROVIDER_INQUIRY_TEMPLATE.md

mining-site/external/2026-09-17-public-source-refresh.md
~~~

## Q00 candidate design identity

~~~yaml
prototype_semver: research-prototype-v2.2.0
treatment_arms: [A, B, C, D, E, F, G]
unassisted_transfer_variant: T
arm_task_scenarios: [SYN-01, SYN-02, SYN-03, SYN-04, SYN-06, SYN-07, SYN-08]
transfer_scenario: SYN-05
williams_sequences: 14
target_usable_n: 84
minimum_usable_n: 70
target_per_sequence: 6
minimum_per_sequence: 5
primary_independence_unit: participant
~~~

Nothing above becomes immutable until the independent reviewer and Q01-required research authority are resolved and the experiment is actually promoted from DRAFT to PRE_REGISTERED.

## Explicit non-closures

The following are **not** claimed by this hardening pass:

- legal permission in Peru;
- provider commercial/data rights;
- willingness to pay;
- organic retention;
- causal product value;
- market-model validity on real data;
- ML incremental value;
- moat/durability;
- profitability;
- MK1 build authorization.

## Remaining external action queue

### External authority

1. Fill exact product/research flow digests and send Q01 packet to qualified Peru counsel/reviewers.
2. Send one Q02 inquiry per exact provider/product/data family; obtain contract/order-form/written licensing authority and quote.
3. Independent Q00 R1/R2 review; apply changes before any outcome inspection.
4. Freeze Q00 G exact comparator execution state after reviewer approval.
5. Freeze Q03 consent/privacy/retention and collector/export path.

### Empirical execution

6. Recruit eligible adults only after Q01 research clearance.
7. Run Q00 under frozen assignments/material digests.
8. Run Q03 longitudinal observation for the full 14-day window.
9. Instantiate Q04 on a Q02-compatible real point-in-time data profile and obtain independent reproduction.
10. Run Q05 only against the persona/repeat-use state actually supported by Q03.

## No-shortcut rules

- A user UAT session is not Q00 evidence unless it was collected under the frozen protocol.
- A public terms page is not Q02 authority when the exact use requires a contract/custom license.
- A public law page is not a legal opinion for the product.
- Synthetic Q04 success is not a real-data G4 reproduction.
- Same-session Decision Record reopening is not retention.
- Component availability is not exposure.
- Exposure is not adoption.
- Adoption is not causation.
- Positive Q03/Q04/Q05 evidence cannot rescue failed Q00.
- No external response may be broadened beyond the exact reviewed scope.

## Reopen rule

Reopen this readiness assessment when:
- any Q00 primary threshold/assignment/scoring semantic changes;
- research participant data collection changes;
- provider/asset/data-family scope changes;
- comparator state changes materially;
- Q01 constraints invalidate a tested flow;
- Q02 constraints invalidate a data-dependent surface;
- a new P0/P1 contradiction appears.

## Final invariant

> The next honest blockers are external authority and real observations, not missing internal handoff design.

If an external reviewer finds a material defect, the affected internal node reopens rather than being defended.
