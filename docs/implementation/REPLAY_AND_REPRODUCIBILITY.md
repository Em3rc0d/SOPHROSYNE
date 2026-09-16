# Replay and Reproducibility Contract

## Objective

Any finalized quantitative or user-visible analytical artifact must be explainable and, where deterministic inputs are available, reproducible from an explicit version bundle.

## Reproducibility bundle

Every finalized `DecisionRecord`, `BacktestRun`, `Experiment` and `ModelArtifact` must reference or embed:
- data manifest hash;
- source/provider identities;
- normalization versions;
- `as_of` cutoff;
- feature schema/version;
- strategy/risk policy versions where applicable;
- model artifact/version and calibration state where applicable;
- application commit/build identity;
- configuration hash excluding secrets;
- dependency/runtime image digest;
- random seed(s) for stochastic computation;
- artifact content hashes.

## Replay modes

Two historical modes are distinct and must never be conflated.

### `KNOWLEDGE_AS_OF_THEN`
Reconstructs only data legally/technically available at the historical cutoff using original availability timestamps and then-current versions where retained.

Purpose:
- point-in-time research;
- audit of what SOPHROSYNE could have known;
- leakage detection.

### `CORRECTED_HISTORY_NOW`
Uses currently corrected historical data and current approved normalization while preserving disclosure that this is not what was necessarily known then.

Purpose:
- data-quality analysis;
- revised research;
- provider correction impact.

The UI/API must label the selected mode.

## Determinism classes

Artifacts declare one class:
- `BITWISE_DETERMINISTIC` — identical bytes expected under pinned environment;
- `SEMANTICALLY_DETERMINISTIC` — numeric/output equivalence within declared tolerances;
- `STOCHASTIC_REPRODUCIBLE` — pinned seed/environment gives reproducible distribution/run;
- `NONDETERMINISTIC_EXPLANATION` — LLM/natural-language layer; authoritative structured source is reproducible even if prose differs.

LLM prose is never the only retained representation of a financial interpretation.

## Dataset manifests

A dataset manifest contains:
- query/scope definition;
- instrument universe;
- source/version identifiers;
- min/max event and availability times;
- row counts;
- partition/object hashes;
- rights-policy reference;
- exclusions/quarantine counts;
- corporate-action/adjustment policy where relevant.

A backtest cannot be considered valid without a manifest.

## Numerical reproducibility

- money/price/accounting calculations use exact decimals where required;
- statistical/model code declares tolerances where floating-point operations are unavoidable;
- no success criterion may depend on hidden notebook state;
- notebooks may explore, but promoted experiments must run from versioned scripts/modules and manifests.

## Randomness

Every stochastic training/evaluation run persists:
- seed;
- library/runtime versions;
- hardware-sensitive determinism notes where relevant;
- repeated-run variance when exact determinism is not guaranteed.

## Model promotion

Promotion requires reproducible validation from a clean environment. A locally trained model that cannot be rebuilt/revalidated from its manifest is `CANDIDATE` only.

## DecisionRecord replay

A replay command/service must be able to:
1. load the record's version bundle;
2. resolve permitted historical inputs;
3. recompute deterministic components;
4. compare stored vs recomputed values;
5. report exact differences;
6. never overwrite the original record.

Expected result states:
- `MATCH`;
- `MATCH_WITH_TOLERANCE`;
- `INPUT_UNAVAILABLE_RIGHTS`;
- `INPUT_UNAVAILABLE_RETENTION`;
- `VERSION_UNAVAILABLE`;
- `MISMATCH`.

## Golden corpus

Before production beta, maintain a reviewed golden corpus containing representative:
- normal market conditions;
- high volatility;
- stale/missing source states;
- provider corrections;
- rights-restricted evidence;
- contradictory evidence;
- `NO_CONCLUSION` cases;
- `NOT_EVALUABLE` strategy cases.

Every material change to normalization, market-state logic, risk logic or strategy semantics runs against this corpus in CI.

## Retention caveat

Data rights may prevent indefinite retention of raw provider payloads. In that case the system must preserve enough hashes, manifests, derived permitted data and audit metadata to truthfully state the replay limitation instead of pretending full reproducibility.

## Failure rule

If a change causes an unexplained replay mismatch in a previously reproducible golden artifact, release is blocked until the change is understood, accepted through an explicit migration/ADR, and historical semantics remain discoverable.