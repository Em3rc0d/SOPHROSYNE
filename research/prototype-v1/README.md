# SOPHROSYNE Research Prototype v1.4

## Status

`PRE-MK0 / RESEARCH-ONLY / THROWAWAY / NOT PROMOTABLE EVIDENCE`

This artifact exists only to support Q00/Q03/Q05 research and UAT before MK0 promotion. It is explicitly outside the MK1 production architecture.

## Boundaries

- synthetic / historical-style scenarios only;
- no live trading;
- no order entry;
- no brokerage credentials;
- no personalized investment recommendations;
- no production market-data provider dependency;
- no backend persistence;
- browser-local `localStorage` only;
- records are append-only through the UI but are not cryptographically immutable;
- exported sessions are not promotable evidence unless collected under a frozen preregistered protocol.

## UAT flow

1. Read the scenario and current state.
2. Contrast favorable and contradicting evidence.
3. Inspect uncertainty and invalidator.
4. Record a hypothesis, confidence and change-of-mind condition.
5. Review the local Decision Ledger and export the session JSON.

## Q00 free-test modes

For informal UAT, the tester can switch among:

- `FULL` — full SOPHROSYNE structure;
- `FRICTION` — five-question simple baseline;
- `RAW` — raw information control.

Formal Q00 execution must freeze the assigned arm before observation; the UAT switcher is not part of the promotable experiment protocol.

## Version

`research-prototype-v1.4.0`

## Verification

- HTML parse: PASS
- JavaScript syntax: PASS
- no external JavaScript dependencies
- no backend/API dependencies

## UAT v1.4

- Spanish-facing copy normalized.
- Active depth is explicit and states that more detail does not imply more certainty.
- Canonical internal event/field names remain stable for research export compatibility.


## Automated verification

`verify.mjs` enforces the research boundary without relying on manual QA:
- no live-trading or personalized-recommendation surface;
- no external JavaScript;
- research arms remain present;
- novice quick summary remains present;
- progressive disclosure remains present;
- Q03-compatible core research events remain present;
- JavaScript syntax parses;
- the tested artifact SHA-256 is printed by the verifier.

The GitHub Actions workflow `.github/workflows/research-prototype-smoke.yml` runs this verifier on research-branch changes.

## UAT v1.4

- research controls moved behind progressive disclosure so they do not dominate the product experience;
- beginner-first 20-second summary added: known / missing / responsible reading;
- deeper levels remain available without changing the conclusion state;
- reviewer authority split is documented in `UAT_BOUNDARY.md`.


## UAT v1.4

The novice UAT intentionally attempted a high-confidence, action-like, low-information record. That exposed a research-integrity defect.

v1.4 adds:
- explicit confidence semantics: confidence in the interpretation, not a market probability;
- low-information/repetitive record rejection;
- explicit detection of a stronger user posture when the evidence state remains cautious;
- an acknowledgment step that preserves user agency while making the divergence visible;
- `system_conclusion` and `evidence_alignment` fields in new records;
- human-readable labels in the ledger instead of leaking internal enum values;
- extreme-confidence instrumentation for later calibration review.

These are implementation/research controls only. They do not make the prototype promotable evidence.
