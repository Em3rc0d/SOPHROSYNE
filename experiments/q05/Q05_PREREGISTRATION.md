# Q05 Pre-Registration — Moat and Competitive Durability

## Purpose

Q05 tests whether SOPHROSYNE creates a workflow advantage deeper than localization, generic LLM summarization or cosmetic interface design.

A feature is not a moat because it is technically interesting or users say it looks good. A candidate advantage must show:
- user preference or repeat-use linkage;
- no material comprehension/trust regression;
- a defensibility mechanism deeper than visible UI alone.

Q05 may close conditionally as a **learning wedge** even if durable moat evidence is not yet strong enough for scale claims.

---

# Candidate moat components

Pre-register the candidate set before the comparative test:

```text
C01 evidence graph with supporting/opposing evidence
C02 immutable Decision Ledger
C03 point-in-time provenance/replay
C04 uncertainty + invalidation semantics
C05 progressive beginner-to-quant disclosure
C06 reproducible strategy validation
C07 longitudinal personal decision history
C08 rights-aware derived intelligence
```

A component may be removed as `NOT_IN_CANDIDATE_MK1` before testing. Do not add a winning-looking component after results are visible.

---

# E05-A — Competitive Task Comparison

## Question

After actually using both workflows on matched tasks, do target users prefer SOPHROSYNE for reasons traceable to candidate moat components rather than branding/style alone?

## Comparator selection

Before recruitment, freeze at least one representative competing workflow that can perform a materially similar research task.

Comparator selection must not deliberately choose a weak or irrelevant product.

Record:
- product/workflow name;
- version/date;
- features available to the participant;
- why it is a fair comparison;
- any unavoidable asymmetry.

## Design

Within-participant, counterbalanced use of SOPHROSYNE and comparator on matched scenarios/tasks.

Where practical:
- remove product branding from final preference questions;
- equalize task instructions;
- give equivalent onboarding time;
- avoid describing one workflow as “AI-powered”, “safer” or “better”.

## Sample

```yaml
target_usable_n: 44
minimum_usable_n: 36
```

Primary participants should match the Q03 frozen persona definition.

## Primary measures

### M1 — post-use workflow preference

Participant chooses which workflow they would prefer for the tested recurring task after using both.

### M2 — preference reason attribution

The participant must identify the feature/workflow reason before seeing the internal candidate-moat labels.

Internal reviewers map free-text/behavioral evidence to C01–C08 using a frozen coding rubric.

### M3 — comprehension guardrail

Objective comprehension must be non-inferior: SOPHROSYNE mean score may not be worse by more than `5 percentage points` versus comparator.

### M4 — calibration guardrail

Mean confidence-calibration gap may not be worse by more than `5 percentage points`.

## PASS contribution

E05-A passes when all hold:
- SOPHROSYNE observed preference rate `>= 65%`;
- lower bound of the two-sided 80% Wilson interval for the preference rate is `> 50%`;
- M3 passes;
- M4 passes;
- at least one C01–C08 component is independently attributable as a substantive preference reason by `>= 35%` of usable participants.

The interval is a pragmatic early-product gate, not a population-certainty claim.

## CONDITIONAL

Preference `>= 55%` but full PASS not reached, with no guardrail failure: candidate advantage remains a learning hypothesis.

## STOP evidence

Strong negative evidence when:
- SOPHROSYNE preference `< 40%`; or
- comprehension is worse by `>= 10 percentage points`; or
- confidence calibration materially worsens under the stop condition defined in E03-B.

## INCONCLUSIVE

Minimum sample not reached or results fall between declared regions.

---

# E05-B — Repeat-Use Linkage

## Question

Are the candidate moat components actually used by people who return over time, or are they merely praised during a one-session demo?

## Data source

Primary source: participants from the valid E03-C 14-day repeat-use experiment.

Do not use one-session interview praise as a substitute.

## Eligible repeat user

A participant who was active on at least 3 distinct days during E03-C.

## Measures per component

For each C01–C08:

```text
U1 repeat_user_adoption_rate
 = repeat users who used component in >=2 sessions / repeat users

U2 stated_return_reason_rate
 = repeat users who independently cite the component/workflow effect as one reason for returning / repeat users

U3 longitudinal_use_rate
 = repeat users who use the component after day 7 / repeat users
```

## Strong linkage threshold

A component has strong repeat-use linkage when all hold:
- `U1 >= 60%`;
- `U2 >= 40%`;
- `U3 >= 40%`;
- at least 12 repeat users exist in the denominator.

This is an association signal, not proof that the component causally caused retention.

## Moderate linkage

- `U1 >= 40%`; and
- at least one of U2/U3 meets `30%`.

Moderate linkage may support `CLOSED_CONDITIONAL`, not a strong moat claim.

## Negative evidence

A component is not retention-supported when:
- `U1 < 25%` with at least 12 repeat users; or
- usage disappears almost entirely after day 7.

Preserve this result even if users praised the feature in interviews.

---

# E05-C — Replicability / Defensibility Assessment

## Purpose

Separate visible feature appeal from mechanisms that may compound or resist trivial replication.

For each C01–C08 classify the strongest supported mechanism.

```yaml
component_id:
surface_copyability:
  class: HOURS_DAYS | WEEKS | MONTHS_PLUS | UNKNOWN
  rationale:

mechanism_classes:
  surface_ui_only: YES | NO
  workflow_integration: YES | NO
  accumulated_user_history: YES | NO
  accumulated_evidence_or_validation_corpus: YES | NO
  point_in_time_provenance_history: YES | NO
  provider_or_rights_constraint: YES | NO
  distribution_or_community_asset: YES | NO
  switching_cost_from_longitudinal_state: YES | NO

requires_generic_llm_only: YES | NO
requires_nontrivial_operational_history: YES | NO
observed_repeat_use_linkage: NONE | MODERATE | STRONG
key_competitor_counterexample:
residual_copy_risk:
```

## Defensibility categories

### SURFACE_ONLY

Visible implementation is easy to copy and no meaningful accumulated state/workflow/history mechanism is supported.

### WORKFLOW_EMBEDDED

Advantage depends on integrated workflow semantics and repeated user behavior, but competitors could plausibly recreate it with sustained product work.

### STATE_COMPOUNDING

Value grows through longitudinal decision/evidence/history state that cannot be reproduced instantly for an existing user.

### EVIDENCE_COMPOUNDING

Value grows through reproducibility, validation, provenance or evidence assets accumulated over time.

### RIGHTS_OR_DISTRIBUTION_CONSTRAINED

Advantage materially depends on non-trivial licensed data, distribution/community or other externally constrained access.

No category is presumed permanent.

## Assessment rule

An internal reviewer cannot classify a component above `SURFACE_ONLY` solely because its code is complex. The mechanism must be supported by actual workflow/data/history evidence.

---

# Q05 aggregate decision

## CLOSED_PASS

All must hold:
- E05-A PASS;
- at least one candidate component has `STRONG` E05-B repeat-use linkage;
- that component is classified as at least `WORKFLOW_EMBEDDED`, `STATE_COMPOUNDING`, `EVIDENCE_COMPOUNDING` or `RIGHTS_OR_DISTRIBUTION_CONSTRAINED` with documented evidence;
- the advantage does not depend on a Q01-prohibited flow or Q02-unapproved data use;
- no unresolved P0/P1 contradiction remains.

This supports a **candidate durability thesis**, not a claim of permanent monopoly or uncopyability.

## CLOSED_CONDITIONAL — LEARNING_WEDGE

Allowed when:
- E05-A is PASS or CONDITIONAL with no trust/comprehension stop condition;
- repeat-use evidence supports real product value;
- no component yet has enough evidence for a durable moat claim.

Freeze:
- `moat_status: LEARNING_WEDGE`;
- no strong defensibility marketing claim;
- large scale/GTM spending remains evidence-gated;
- next evidence horizon is mandatory.

This is a valid MK1 promotion state because MK1 can be used to learn whether longitudinal workflow state compounds.

## PIVOT_REQUIRED

Use when durable advantage consistently appears in a materially different persona, workflow or distribution model than the proposed MK1.

## STOP_CURRENT_CONFIGURATION

Use when repeated comparative evidence shows the product is interchangeable with existing workflows, repeat-use is weak, and no deeper workflow/state/evidence asset emerges.

## INCONCLUSIVE

Insufficient sample/repeat-user denominator or mixed results that do not satisfy the defined regions.

---

# Marketing / strategy claim constraints

Before Q05 `CLOSED_PASS`, do not write canonical strategy language asserting that SOPHROSYNE “has a moat”.

Allowed evidence-level language:
- “candidate moat”;
- “supported workflow advantage”;
- “learning wedge”;
- “repeat-use-linked component”;
- “surface-copy risk remains high”.

Even after PASS, claims must remain scoped to the observed evidence and time period.

---

## Q05 frozen outputs

```yaml
moat_receipt_ref:
moat_status: SUPPORTED | LEARNING_WEDGE
supported_components:
  - component_id:
    repeat_use_linkage:
    defensibility_category:
unsupported_components:
scale_spend_constraint:
claims_allowed:
claims_forbidden:
next_evidence_horizon:
competitor_snapshot_ref:
```

These outputs feed `MK1_BOOTSTRAP_PROFILE`.
