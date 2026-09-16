# Q03 Pre-Registration — User Value, Repeat Use and Pricing

## Shared promotion scope

```yaml
primary_promotion_geography: Peru
primary_study_language: Spanish
primary_persona: capable beginner / intermediate self-directed investor
statistical_contract: docs/validation/STATISTICAL_DECISION_RULES.md
participant_protocol: docs/validation/RESEARCH_PARTICIPANT_PROTOCOL.md
instrumentation_contract: experiments/q03/Q03_INSTRUMENTATION_CONTRACT.md
```

Spanish-speaking participants outside Peru may be exploratory but cannot silently close the Peru MK1 scope.

# E03-A — Behavioral Discovery

## Sample

```yaml
target_primary_n: 24
minimum_usable_primary_n: 20
secondary_exploratory_target_n: 4-8
```

Primary and exploratory cohorts are reported separately.

## Measures
Frozen coding rubric captures recurring research/decision task, current workaround, frequency, material friction/time/confusion/trust failure, current paid tool evidence and evidence that the problem is behavioral rather than hypothetical.

Coding used for promotion follows the qualitative reliability rule in the statistical contract.

## PASS
At least 20 usable primary participants and the frozen threshold bundle in the instantiated manifest is met for recurring problem/workaround/friction evidence. The exact numeric rule is frozen before the first outcome is inspected.

## STOP / PIVOT / INCONCLUSIVE
STOP only under the frozen strong-negative region; PIVOT when another persona/workflow consistently dominates; otherwise underpowered/mixed/coding-invalid evidence is INCONCLUSIVE.

# E03-B — Translator / Evidence Representation

Within-participant, counterbalanced comparison of conventional representation versus the frozen SOPHROSYNE candidate on matched synthetic or true point-in-time cases.

Primary measures: objective comprehension, completion time, confidence-calibration gap, opposing-evidence recognition and staleness/missing-evidence recognition. Scoring rubric and exact PASS/CONDITIONAL/STOP boundaries are frozen in the instantiated manifest. Guardrail regression cannot be rescued by subjective preference.

# E03-C — 14-Day Repeat Use

## Sample / behavior
Freeze target/minimum sample, reminder policy, timezone, qualifying activity and exclusion rules before start.

Primary metrics:
- `M1`: proportion active on >=3 distinct days;
- `M2`: proportion with >=1 unprompted revisit on study days 4–14;
- `M3`: proportion with >=1 historical Decision Record revisit.

## Decision regions

### PASS
All hold: `M1 >= 50%`, `M2 >= 35%`, `M3 >= 30%`, minimum usable sample and telemetry quality gates pass.

### CONDITIONAL
If not PASS and not STOP: `M1 >= 40%` and at least one of `M2 >= 35%` or `M3 >= 30%`, with no trust/validity stop condition.

### STOP
`M1 < 25%`, or (`M1 < 40%` and `M2 < 15%`) with valid telemetry and no external disruption sufficient to invalidate the study.

### INCONCLUSIVE
Every remaining region, minimum sample failure, or material/FATAL instrumentation validity failure.

Decision precedence: validity -> if invalid INCONCLUSIVE; otherwise STOP -> PASS -> CONDITIONAL -> INCONCLUSIVE.

# E03-D — Pricing / Commitment

Before exposure freeze, per band: displayed amount/currency, billing period, tax/fee inclusion presentation, trial/refund semantics if shown, entitlement matrix, pricing copy digest, assignment method and commitment-friction definition.

A pre-counsel fake-door may collect non-charging research intent only and must disclose that no charge occurs. Real payment/paid pilot occurs only after Q01 and operational requirements permit it.

For each band report qualified exposure, curiosity click, higher-friction commitment start and completed real commitment if legally/operationally valid. Survey WTP alone cannot pass.

Exact PASS/CONDITIONAL/STOP thresholds by band are frozen before outcome inspection. Missing/ambiguous commitment semantics are INCONCLUSIVE.

# E03-E — Historical Decision Record Diagnostic

Diagnostic/supportive study of whether users can reconstruct historical reasoning, understand invalidated scenarios and revisit immutable records. It supports Q03/Q05 but does not replace E03-C or count as a performance backtest.

# Aggregate Q03 decision

- **CLOSED_PASS**: E03-A/B/C are CLOSED_PASS, E03-D has at least one CLOSED_PASS band, no unresolved P0/P1 contradiction.
- **CLOSED_CONDITIONAL**: E03-A/B/C/D are each in `{CLOSED_PASS, CLOSED_CONDITIONAL}`, at least one is conditional, no required component is inconclusive, and no unresolved P0/P1 exists. Freeze the narrower persona/use/pricing constraints.
- **PIVOT_REQUIRED**: strong evidence supports a materially different persona/workflow/distribution/pricing configuration.
- **STOP_CURRENT_CONFIGURATION**: preregistered strong-negative evidence rejects the current candidate across mandatory value/repeat-use/commitment dimensions.
- **INCONCLUSIVE**: any mandatory component remains inconclusive or the combined evidence falls outside declared promotable/pivot/stop regions.

Final Q03 output is one aggregate EvidenceReceipt referencing all component receipts.

## Frozen outputs

```yaml
q03_receipt_ref:
primary_persona_version:
jtbd_version:
wedge_version:
primary_promotion_geography: Peru
primary_study_language: Spanish
required_trust_features: []
pricing_hypothesis_band:
pricing_surface_version:
supported_workflow_constraints: []
rejected_workflow_constraints: []
```
