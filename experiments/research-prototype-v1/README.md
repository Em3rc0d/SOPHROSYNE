# SOPHROSYNE Pre-MK0 Research Prototype

## Status

`PRE-MK0 / RESEARCH-ONLY / THROWAWAY / NOT PROMOTABLE EVIDENCE`

This is the canonical interactive research artifact used to prepare Q00/Q03/Q05 studies. It is explicitly outside the MK1 production architecture.

## Current version

`research-prototype-v2.3.0`

## Q00 rehearsal coverage

The artifact now exposes all required Q00 arm identities:

- A — raw information;
- B — stateless structured assistant;
- C — five-question friction checklist;
- D — simple prediction/confidence/outcome feedback;
- E — short-memory SOPHROSYNE;
- F — full candidate SOPHROSYNE;
- G — conventional-workflow comparator shell.

G remains a **non-promotable proxy** until an exact external comparator snapshot/version is frozen under the preregistration.

The rehearsal corpus contains eight scenario instances. Seven feed the A–G Williams assignment and SYN-05 is reserved for unassisted transfer. Outcomes remain hidden during the task and are revealed only in arm D after a record is saved.

v2.3 additionally separates directional evidence from non-directional market context, declares mode/horizon/instrument/leverage/execution relevance for every scenario, and stores that context in Decision Records.

## Rehearsal locking

Informal UAT allows arm switching.

A rehearsal assignment can be frozen in the browser with query parameters such as:

```
?arm=F&locked=1&participant=<opaque-id>&order=SYN-03,SYN-01,SYN-06,SYN-02,SYN-04,SYN-07,SYN-08
```

This is an implementation mechanism only. It does not make a run preregistered or promotable.

## Captured research fields

New records include:
- arm/scenario/version identity;
- completion seconds;
- workload rating;
- help-requested flag;
- hypothesis and change-of-mind condition;
- confidence in interpretation;
- process posture;
- evidence alignment;
- simple prediction for arm D;
- hidden-outcome feedback event where applicable;
- decision context, horizon, instrument class and leverage class;
- evidence-class set for the scenario.

## Boundaries

- synthetic / historical-style scenarios only;
- no live trading or order entry;
- no brokerage credentials or account data;
- no personalized investment recommendations;
- no production market-data dependency;
- no backend persistence;
- browser-local `localStorage` only;
- exported sessions are not promotable evidence unless collected under a frozen preregistered protocol.

## Reviewer authority

See `UAT_BOUNDARY.md`.

- novice/non-specialist: comprehension and cognitive load;
- market-domain reviewer: market coherence and practical workflow;
- quant/engineering: calculations, point-in-time semantics, leakage, reproducibility and instrumentation;
- Q00 evidence: incremental causal value versus frozen baselines.

No reviewer class substitutes for another.

## Integrity controls

The instrument rejects low-information/repetitive reasoning records, maps internal enums to human-readable labels, and records explicit divergence when a participant chooses a stronger posture than the scenario evidence supports. It does not prevent disagreement.

## Verification

Run:

```bash
node experiments/research-prototype-v1/verify.mjs
```

GitHub Actions runs the same verifier on branch changes.

Current engineering identity is taken from the exact Git commit/blob used by the reviewer packet and final freeze. Branch-head strings in this README are intentionally not treated as durable authority.

The final Q00 material digest remains unfrozen until independent review, comparator-G authority, scenario review and preregistration closure.
