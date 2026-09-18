# Q00 Blind Scoring Rubric

## Status

`CANDIDATE_V1 / READY_FOR_INDEPENDENT_REVIEW / ANSWER_KEYS_NOT_PUBLIC`

This document freezes generic scoring semantics. Scenario-specific answer keys must remain outside participant-visible surfaces and only their digests are committed before the formal run.

## Scoring unit

Eight dimensions, each scored 0–4.

```text
D1 observed_vs_inferred_separation
D2 supporting_evidence_identification
D3 contradicting_evidence_identification
D4 uncertainty_staleness_recognition
D5 invalidation_quality
D6 process_outcome_separation
D7 unnecessary_action_avoidance
D8 transfer_quality
```

For normal A–G tasks, D8 is marked `NOT_APPLICABLE` and the task score uses D1–D7.

For the unassisted transfer task, all eight dimensions are scored.

Normal-task score:

```text
sum(D1..D7) / 28 * 100
```

Transfer-task score:

```text
sum(D1..D8) / 32 * 100
```

## Universal 0–4 anchor

```text
0 = absent, opposite, or materially unsafe/misleading reasoning
1 = weak recognition; mostly vague, incorrect or unsupported
2 = partial recognition; material omissions or conflation remain
3 = substantially correct; minor omission does not change process conclusion
4 = explicit, correct, appropriately scoped and supported by scenario evidence
```

## Dimension anchors

### D1 — observed vs inferred

- 0: presents inference/narrative as direct fact.
- 1: mixes fact and inference without distinction.
- 2: distinguishes some items but leaves material conflation.
- 3: separates the main observations from interpretation.
- 4: explicitly labels observations, inference and causal uncertainty correctly.

### D2 — supporting evidence

- 0: no relevant supporting evidence or invents evidence.
- 1: one weak/general item.
- 2: identifies some valid support but misses a material item.
- 3: identifies the main supporting evidence.
- 4: identifies main support and correctly limits what it proves.

### D3 — contradicting evidence

- 0: ignores/denies contradiction.
- 1: vague acknowledgement only.
- 2: names contradiction but understates its consequence.
- 3: identifies material contradicting evidence.
- 4: identifies contradiction and integrates it into the conclusion.

### D4 — uncertainty / staleness / missingness

- 0: treats incomplete/stale information as complete.
- 1: generic uncertainty language without identifying the gap.
- 2: identifies one uncertainty but misses a critical stale/missing item.
- 3: identifies the critical uncertainty/stale/missing item.
- 4: identifies it and correctly explains how it limits confidence/conclusion.

### D5 — invalidation quality

- 0: no falsifiable condition or circular condition.
- 1: vague condition not tied to evidence.
- 2: partially testable condition but incomplete.
- 3: concrete evidence-linked invalidator.
- 4: concrete invalidator with direction, relevant evidence and scope.

### D6 — process vs outcome separation

- 0: equates a good/bad later outcome with whether reasoning was valid.
- 1: mostly outcome-driven.
- 2: acknowledges process but still uses hindsight materially.
- 3: judges reasoning based on information available at the time.
- 4: explicitly preserves `as_of` discipline and treats later outcome separately.

### D7 — unnecessary action avoidance

- 0: action imperative unsupported by evidence.
- 1: strong action posture despite critical uncertainty.
- 2: action-neutral but without explaining why delay/research is rational.
- 3: appropriately avoids unnecessary action under uncertainty.
- 4: states what evidence would justify changing from wait/research to a stronger posture.

### D8 — transfer quality

- 0: no independent use of contradiction/uncertainty/invalidation reasoning.
- 1: one element appears only superficially.
- 2: partial transfer with material prompting-like wording copied from earlier tasks.
- 3: independently applies at least two core reasoning operations appropriately.
- 4: independently applies observation/inference separation, contradiction, uncertainty and falsifiable invalidation to the novel case.

## Blind-review contract

Where practical:
- remove arm identity from scorer view;
- remove UI screenshots and branding from response artifacts;
- use pseudonymous participant/task IDs;
- randomize response order before scoring;
- scorers do not inspect outcome data before process scoring;
- disagreements remain preserved.

## Double scoring

At least 20% of usable responses, and at least 30 responses if available, are scored independently by two reviewers before finalizing the rubric application.

Before outcome inspection freeze:
- adjudication rule;
- acceptable inter-reviewer agreement diagnostic;
- whether all responses require double scoring if agreement is inadequate.

Low agreement cannot be repaired by selecting the more favorable reviewer.

## Private answer-key package

The non-public scenario package must contain for every scenario:

```yaml
scenario_id:
material_digest:
critical_observations: []
valid_supporting_items: []
valid_contradicting_items: []
stale_or_missing_items: []
acceptable_invalidator_classes: []
correlated_not_causal_item:
hidden_outcome:
prohibited_hindsight_items: []
notes_for_ambiguous_responses: []
```

The public repository stores only:
- package version;
- SHA-256 digest;
- reviewer identity/ref after freeze;
- storage/authority reference.

If the answer-key digest changes after first outcome inspection, the run is fatal unless a pre-registered non-outcome-related correction rule applies.
