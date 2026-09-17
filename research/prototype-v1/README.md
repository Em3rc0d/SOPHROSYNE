# SOPHROSYNE Research Prototype v1.2

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

`research-prototype-v1.2.0`

## Verification

- HTML parse: PASS
- JavaScript syntax: PASS
- no external JavaScript dependencies
- no backend/API dependencies

## UAT v1.2

- Spanish-facing copy normalized.
- Active depth is explicit and states that more detail does not imply more certainty.
- Canonical internal event/field names remain stable for research export compatibility.
