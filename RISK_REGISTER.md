# Risk Register

Scoring: Probability (P), Impact (I), Detectability difficulty (D), each 1–5. Priority = `P × I × D`.

| Risk | P | I | D | Priority | Treatment |
|---|---:|---:|---:|---:|---|
| Regulatory reclassification as investment advice | 4 | 5 | 4 | 80 | Counsel before public beta; avoid personalized action language until cleared. |
| Market-data licensing surprise | 5 | 5 | 3 | 75 | Written rights matrix and derived-data-first architecture. |
| False causal explanations | 4 | 5 | 3 | 60 | Epistemic labels, provenance and audit set. |
| Competitor copies interface | 5 | 3 | 4 | 60 | Moat in evidence graph, audit history, validation data and workflow. |
| Derived-data rules/pricing change | 3 | 5 | 4 | 60 | Contract review, provider abstraction and diversification. |
| Reputational damage after incorrect interpretation | 4 | 5 | 3 | 60 | No certainty framing; immutable decision history; incident process. |
| Backtest overfitting | 5 | 5 | 2 | 50 | OOS, walk-forward, multiple-testing controls, PBO/DSR where applicable. |
| News/social manipulation | 4 | 4 | 3 | 48 | Cross-source validation and bounded sentiment influence. |
| Vendor price shock | 4 | 4 | 3 | 48 | Fallback providers and optional pass-through entitlements. |
| Automation bias by users | 4 | 4 | 3 | 48 | Uncertainty UX, opposing evidence and no-oracle language. |
| Privacy breach | 3 | 5 | 3 | 45 | Data minimization, least privilege, security controls and incident-response receipt. |
| LLM hallucinated confidence | 4 | 5 | 2 | 40 | LLM cannot create probabilities or risk scores; explanation remains downstream-only. |
| Low willingness-to-pay | 4 | 5 | 2 | 40 | Pricing and retention tests before substantial build. |
| High beginner support burden | 3 | 4 | 3 | 36 | Guided UX, progressive disclosure and narrow scope. |
| Geo restrictions / broker availability | 3 | 4 | 3 | 36 | Capability matrix and modular connectors. |
| API/provider shutdown | 4 | 4 | 2 | 32 | Adapter layer, compatible fallbacks, circuit breakers and explicit degradation states. |
| Black swan / flash crash | 3 | 5 | 2 | 30 | Safe mode, stale-data detection, `NO_TRADE`, risk separation and circuit-breaker semantics. |
| Credential compromise in future connected accounts | 3 | 5 | 2 | 30 | Least privilege, no withdrawal permission, kill/revoke paths and secret-rotation receipt. |
| Model drift / regime shift | 5 | 4 | 1 | 20 | Drift monitoring, retrain/retire gates, baseline fallback and no forced signal. |
| Reflexivity at scale | 1 | 4 | 5 | 20 | Avoid universal mass signals; prefer user-defined strategy semantics. |

## Treatment verification

Internal treatments above are no longer architecture placeholders. Their semantics are owned by the corresponding canonical implementation documents.

Where a treatment depends on implemented behavior, proof is carried by typed receipts in `docs/implementation/ACCEPTANCE_RECEIPTS.md` rather than by reopening the design node.

External/empirical risks remain evidence-gated and may still force scope changes.

## Unknown-unknown discipline

Run a pre-mortem at each MK promotion and quarterly during active development. Specifically search for:

- new regulator interpretations of AI-assisted research;
- data vendors changing derived-data or LLM-use terms;
- app-store/payment-provider classification risk;
- cross-border consumer rules based on user location;
- evidence retention/discovery obligations in disputes;
- model-provider restrictions on financial use;
- localization errors changing financial meaning;
- vendor terms that permit display but prohibit embeddings or transformed storage.

A newly discovered risk is not a project failure. Hiding it is.
