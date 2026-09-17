# SOPHROSYNE Pre-MK0 Research Prototype v1

## Status

`RESEARCH_PROTOTYPE / THROWAWAY / NOT_PRODUCTION / NOT_EVIDENCE`

This artifact is explicitly allowed by `docs/implementation/BUILD_READINESS.md`: throwaway/prototype UX for causal, behavioral and legal review, outside production architecture.

It must not be reclassified as MK1 production code merely because it is useful.

## Test surface

- Market Translator comprehension.
- Supporting vs opposing evidence inspection.
- Visible uncertainty and invalidators.
- Progressive disclosure: Beginner -> Investor -> Trader -> Quant.
- Immutable-in-session Decision Record interaction.
- Local Decision Ledger revisit behavior.
- Q03-compatible local interaction events.
- Q00 presentation variants over the same scenario family:
  - `?arm=raw`
  - `?arm=friction`
  - `?arm=full`

Default: `?arm=full`.

## Hard boundaries

- synthetic / historical-style scenarios only;
- no live data dependency;
- no brokerage/exchange credentials;
- no real orders or custody;
- no personalized buy/sell recommendation;
- no calibrated probability claims;
- no provider-rights assumption;
- no backend transmission of research data;
- localStorage only;
- exported sessions are not promotable evidence unless collected later under a frozen preregistered protocol with required authority/review.

## Q03 event compatibility

The prototype emits local events including `session_started`, `evidence_expanded`, `opposing_evidence_opened`, `uncertainty_opened`, `invalidation_opened`, `decision_record_created`, `decision_record_revisited`, and `session_ended`.

## Run

Open `index.html` directly or serve this directory statically.

```bash
python -m http.server 4173
```

## Promotion consequence

None. This artifact does not close Q00-Q05 and does not authorize Phase 0 or MK1 production implementation.
