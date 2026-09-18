# Q00 Independent Reviewer Handoff

## Status

`READY_TO_SEND / EXTERNAL_REVIEW_REQUIRED / NOT_EVIDENCE`

## Required reviewer roles

### R1 — research-method reviewer

Minimum:
- not an author of the Q00 instrument/analysis code;
- competent in experimental design and repeated/crossover measurements;
- able to review assignment, missing-data, uncertainty and multiplicity rules;
- no material incentive tied to SOPHROSYNE passing.

### R2 — market-domain content reviewer

Minimum:
- practical or research experience interpreting market evidence;
- reviews scenario plausibility, terminology and information equivalence across arms;
- does **not** decide participant outcomes or rewrite scenarios after seeing results.

One person may satisfy both only if independence and competence are documented. Preferred: two different reviewers.

## Reviewer package

Send:
- `Q00_PREREGISTRATION.md`;
- `Q00_EXECUTION_KIT.md`;
- `Q00_SAMPLE_AND_ASSIGNMENT_PLAN.md`;
- `Q00_SCORING_RUBRIC.md`;
- `generate_assignment.py`;
- prototype candidate under `experiments/research-prototype-v1/`;
- candidate G comparator execution sheet;
- participant protocol and draft moderator/recruitment packet;
- statistical decision rules;
- exact branch/commit identity.

Do not send participant outcome data before design signoff.

## Mandatory R1 questions

R1 must answer explicitly:
1. Is the 14-sequence Williams assignment correctly balanced for seven arms?
2. Is participant the correct independence unit?
3. Are 84 target / 70 minimum rules acceptable for this early causal gate and the declared interval/materiality logic?
4. Are P1/P2/P3 thresholds frozen and interpretable?
5. Is the participant-stratified bootstrap appropriate?
6. Are missing-data/exclusion rules fail-closed?
7. Does the transfer insertion allow the declared `prior_F_exposure` contrast without outcome leakage?
8. Are carryover/learning effects sufficiently balanced/diagnosed?
9. Does the simple-friction 80% destruction rule remain correctly implemented?
10. Can any secondary analysis accidentally rescue a failed primary gate?

Allowed dispositions per question:
`PASS | PASS_WITH_CHANGE | FAIL | INCONCLUSIVE`.

## Mandatory R2 questions

R2 must answer explicitly:
1. Are all scenario facts plausible enough for behavioral evaluation?
2. Are A–G presentations equivalent in underlying information except for the intended treatment?
3. Does any arm accidentally contain extra directional information?
4. Are supporting/opposing/uncertainty labels economically coherent?
5. Are invalidators meaningful without becoming trading instructions?
6. Is the transfer scenario materially different enough to test transfer?
7. Does G fairly represent the frozen comparator state?
8. Are any terms likely to be misunderstood by non-experts?
9. Does any scenario invite hindsight leakage?
10. Are hidden answer-key claims defensible?

## Reviewer change control

Before outcome inspection:
- changes may be accepted and create a new candidate version;
- every material change updates digests;
- review repeats for affected sections.

After outcome inspection:
- no material design/rubric change is allowed to rescue the run;
- a material defect makes the affected result `INCONCLUSIVE` and requires a superseding experiment version.

## Signoff record

```yaml
review_id:
reviewer_role:
reviewer_identity_ref:
independence_statement:
competence_basis:
materials_commit:
materials_digests: {}
review_started_at:
review_completed_at:
disposition: PASS | PASS_WITH_CHANGE | FAIL | INCONCLUSIVE
required_changes: []
known_limitations: []
conflicts_of_interest: []
signature_or_authoritative_ref:
```

Q00 cannot become `PRE_REGISTERED` while any mandatory reviewer disposition is unresolved.
