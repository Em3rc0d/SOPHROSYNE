# Pre-Build Falsification Plan

SOPHROSYNE must earn the right to become production software.

The internal design graph is already closed. This plan exists to close the remaining external / empirical locks without lowering gates after evidence appears.

Canonical protocol: `docs/validation/EVIDENCE_CLOSURE_PROTOCOL.md`.

Canonical experiment template: `experiments/EXPERIMENT_MANIFEST_TEMPLATE.md`.

Canonical promotion bundle: `docs/validation/MK0_PROMOTION_PACKET.md`.

---

## Governing rule

Every empirical experiment that can materially affect MK1 scope must be **pre-registered** before outcome data are inspected.

At minimum the manifest freezes:
- exact question;
- hypothesis / failure hypothesis;
- population or market scope;
- sample/dataset plan;
- inclusion/exclusion criteria;
- primary measures;
- decision rule;
- analysis plan;
- known confounders;
- expected evidence artifacts;
- owner and reviewer.

A failed or inconclusive experiment remains in history. It is never deleted or retroactively rewritten.

---

## Q03 — User value / WTP experiments

### E03-A — Behavioral discovery

Target:
- minimum 15 qualified interviews;
- preferred band 20–25.

Observe the current workflow before pitching SOPHROSYNE.

Capture:
- repeated research/decision tasks;
- tools and sources used;
- time/frequency;
- confusion/failure points;
- trust signals;
- current paid products;
- evidence that the problem is behaviorally real rather than merely stated.

Closure use:
- persona;
- JTBD;
- wedge;
- trust requirements.

### E03-B — Translator vs comparison workflow

Compare objective comprehension and workflow friction.

Required primary/diagnostic dimensions:
- comprehension score;
- completion time;
- confidence;
- calibration gap;
- recognition of opposing evidence;
- recognition of stale/missing evidence;
- failure reasons.

Randomization/counterbalancing and exact thresholds are frozen in the experiment manifest before the first outcome is inspected.

### E03-C — Historical Decision Record review

Create true `as_of` records and review them later without rewriting historical reasoning.

Measure:
- whether users can reconstruct why the system reached the historical state;
- whether failed/invalidated scenarios remain understandable;
- whether immutable history improves trust versus a mutable summary;
- whether the feature is actually revisited.

This experiment supports Q03/Q05; it is not a performance backtest.

### E03-D — Pricing / commitment

Candidate bands remain hypotheses:
- Free;
- approximately USD 12;
- approximately USD 19;
- approximately USD 39 where the workflow justifies it.

Distinguish:
- curiosity click;
- waitlist/email intent;
- checkout initiation or equivalent higher-friction intent;
- actual paid pilot if later legally/operationally appropriate.

Survey willingness alone cannot close Q03.

### E03-E — Repeat-use proxy

Run a fixed two-week briefing/prototype with qualified participants.

Measure:
- active days / return sessions;
- voluntary revisits without prompting;
- evidence-view expansion;
- revisit of previous Decision Records;
- uncertainty/invalidation usage;
- abandonment reason;
- replacement vs complement of current workflow.

One-session novelty does not count as repeat-use evidence.

---

## Q04 — Quant experiments

### E04-A — Deterministic baseline harness

Benchmark ladder:

```text
cash / no-trade
  -> buy-and-hold
  -> simple trend
  -> simple momentum
  -> simple mean reversion
  -> multifactor
  -> regime-aware rule
```

Required before ML:
- point-in-time dataset manifest;
- realistic cost model;
- hand-computed accounting/fill fixtures;
- untouched temporal test interval;
- walk-forward evaluation;
- multiple-testing log;
- anti-leakage checks;
- deterministic rerun;
- independent reproduction.

A losing baseline may still validate the harness. Harness validity and alpha are separate questions.

### E04-B — ML incremental value

Run only after E04-A passes.

Pre-register:
- target/label;
- feature availability semantics;
- train/validation/test segmentation;
- strongest eligible deterministic comparator rule;
- primary metric;
- risk/secondary metrics;
- cost assumptions;
- promotion threshold;
- seed policy;
- regime breakdown;
- overfitting controls;
- retirement/failure rule.

ML is rejected as an MK1 alpha component if it does not add robust out-of-sample value after realistic costs and complexity penalties.

`ML EXCLUDED` is a valid successful Q04 closure state.

---

## Q05 — Moat / competitive experiments

### E05-A — Competitive task comparison

Compare SOPHROSYNE against representative existing workflows on the same user task.

Measure:
- comprehension;
- completion time;
- trust calibration;
- repeat-use intent after actual exposure;
- component-level preference;
- whether preference survives removal of branding/marketing language where practical.

Feature-count comparisons do not close Q05.

### E05-B — Retention linkage

Determine which candidate advantages are actually associated with repeat use:
- evidence graph;
- opposing evidence;
- immutable Decision Ledger;
- uncertainty/invalidation;
- progressive disclosure;
- strategy validation;
- longitudinal decision history.

A feature users praise but never revisit is not yet defensibility evidence.

### E05-C — Replicability assessment

For each candidate moat component, record:
- surface-copy difficulty;
- underlying accumulated state/history;
- dependence on generic model access vs proprietary workflow/evidence history;
- compounding effect over time;
- dependency on exclusive or costly data rights;
- competitor parity risk.

---

## Q01 / Q02 external reviews

These are evidence workstreams rather than ordinary experiments.

### Q01 — Legal flow review

Counsel reviews the exact frozen flows/copy defined in `EVIDENCE_CLOSURE_PROTOCOL.md`.

Silence or an informal assumption is not legal clearance.

### Q02 — Data-rights validation

Capture authoritative provider evidence for the exact initial `DataUseProfile`:
- display;
- non-display;
- redistribution;
- derived use;
- retention/cache;
- geography;
- entitlements;
- attribution;
- costs;
- fallback compatibility.

Unknown rights default to denied.

---

## Internal semantic tests allowed before production build

These tests validate design assumptions but do not become production implementation by default.

### Contradiction test

Conflicting evidence must produce uncertainty, opposing evidence or `UNKNOWN`; never invented causality.

### Degraded-data test

Stale/unavailable inputs must trigger explicit degradation or `NO CONCLUSION`, not silent substitution.

### Point-in-time replay test

Historical computation may only use information satisfying `available_at <= as_of` for the intended replay mode.

### Rights-policy fixture test

A denied display/retention/derived-use combination must remain denied through transformations and user-facing assembly.

---

## Promotion rule

Production MK1 implementation starts only when:

1. Q01–Q05 have promotable evidence receipts under `EVIDENCE_CLOSURE_PROTOCOL.md`;
2. every empirical experiment used for closure has a pre-registered manifest;
3. failed/inconclusive evidence is preserved;
4. conditional constraints are promoted into canonical product/data/quant/regulatory docs;
5. the cross-receipt contradiction log has no unresolved P0/P1 item;
6. the exact `MK1_BOOTSTRAP_PROFILE` exists;
7. the `MK0_PROMOTION_PACKET` is approved;
8. `docs/implementation/BUILD_READINESS.md` passes.

The purpose of MK0 is not to prove future business success. It is to falsify weak assumptions early enough that the first production build has an evidence-backed configuration.
