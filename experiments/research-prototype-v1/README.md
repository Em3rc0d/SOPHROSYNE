# SOPHROSYNE Pre-MK0 Research Prototype

## Status

`PRE-MK0 / RESEARCH-ONLY / THROWAWAY / NOT PROMOTABLE EVIDENCE`

This is the single canonical interactive research artifact used to prepare Q00/Q03/Q05 studies. It is explicitly outside the MK1 production architecture and cannot be promoted merely because it is useful.

## Current version

`research-prototype-v1.4.0`

## Boundaries

- synthetic / historical-style scenarios only;
- no live trading or order entry;
- no brokerage credentials or account data;
- no personalized investment recommendations;
- no production market-data dependency;
- no backend persistence;
- browser-local `localStorage` only;
- records are append-only through the UI, not cryptographically immutable;
- exported sessions are not promotable evidence unless collected under a frozen preregistered protocol.

## Reviewer authority

See `UAT_BOUNDARY.md`.

- novice/non-specialist: comprehension and cognitive load;
- market-domain reviewer: market coherence and practical workflow;
- quant/engineering: calculations, point-in-time semantics, leakage, reproducibility and instrumentation;
- Q00 evidence: incremental causal value versus frozen baselines.

No reviewer class substitutes for another.

## Verification

Run:

```bash
node experiments/research-prototype-v1/verify.mjs
```

GitHub Actions also runs the verifier on changes to this artifact.

## UAT findings incorporated through v1.4

- Spanish-first visible copy;
- progressive depth with explicit “more detail does not imply more certainty” semantics;
- novice 20-second known/missing/responsible-reading summary;
- research controls separated from the product-facing path;
- local decision-history semantics corrected (not falsely called cryptographically immutable);
- human-readable process labels;
- confidence clarified as confidence in interpretation, not market probability;
- low-information/repetitive records rejected;
- stronger-than-evidence user postures remain allowed but must be recorded as explicit divergence;
- extreme-confidence and divergence events are instrumented for later calibration research.

These controls improve the instrument. They do not close any evidence gate.
