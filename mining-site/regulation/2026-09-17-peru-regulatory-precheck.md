# Peru Regulatory Precheck — 2026-09-17

## Status

`PUBLIC_SOURCE_PRECHECK / NOT_LEGAL_CLEARANCE`

This artifact records official public-source facts that narrow Q01. It does **not** classify SOPHROSYNE legally and cannot replace qualified Peruvian securities counsel.

## Receipt R-Q01-001 — SMV market-intermediation boundary

```yaml
receipt_id: receipt_q01_smv_secondary_market_20260917
title: SMV secondary-market and SAB role
source: https://www.smv.gob.pe/OrientacionyEducacion/MercadoSecundario.aspx
accessed_at: 2026-09-17
provenance_class: OFFICIAL
claim: SMV states that investors buying or selling exchange-traded securities must use a Sociedad Agente de Bolsa (SAB), and lists client identification, profile evaluation and investment recommendation among SAB functions.
confidence: high
related_locks: [Q01]
related_quarries: [Q01]
commercial_or_legal_constraints:
  - This fact does not determine whether SOPHROSYNE's non-custodial research flows constitute regulated advice or intermediation.
supersedes: null
superseded_by: null
```

### Extracted implications

- Exchange execution/intermediation is outside the intended MK1 posture and remains excluded.
- Personalized suitability/recommendation semantics are a high-risk boundary that counsel must classify from the exact product flows.
- A product label such as “decision intelligence” cannot substitute for flow-by-flow legal analysis.

## Receipt R-Q01-002 — Peru personal-data regulation

```yaml
receipt_id: receipt_q01_anpd_ds016_2024_20260917
title: Reglamento de la Ley 29733 — DS 016-2024-JUS
source: https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus
accessed_at: 2026-09-17
provenance_class: OFFICIAL
claim: Decreto Supremo 016-2024-JUS approves the current regulation of Peru's Personal Data Protection Law 29733.
confidence: high
related_locks: [Q01]
related_quarries: [Q01]
commercial_or_legal_constraints:
  - Portfolio context, profile data, telemetry and research history must be reviewed as personal-data processing before production.
supersedes: null
superseded_by: null
```

### Extracted implications

Q01 counsel/privacy review must explicitly cover:
- profile and preference inputs;
- manual/read-only portfolio context;
- Decision Ledger history;
- telemetry/experiment data;
- retention/deletion;
- consent/legal basis;
- cross-border processors/providers;
- security and breach obligations.

## Receipt R-Q01-003 — 2026 Peru e-commerce / dark-pattern changes

```yaml
receipt_id: receipt_q01_indecopi_dl1729_20260917
title: Indecopi summary of DL 1729 e-commerce consumer changes
source: https://www.gob.pe/institucion/indecopi/noticias/1352010-por-primera-vez-el-codigo-de-proteccion-del-consumidor-introduce-cambios-para-garantizar-un-comercio-electronico-sin-practicas-abusivas
accessed_at: 2026-09-17
provenance_class: OFFICIAL
claim: Indecopi reports that DL 1729, effective from 2026-02-13, modified Peru's consumer-protection framework for e-commerce, including prohibitions on coercive digital practices such as involuntary subscriptions and requirements for accessible complaint channels.
confidence: high
related_locks: [Q01, Q03]
related_quarries: [Q01, Q03]
commercial_or_legal_constraints:
  - Pricing, subscription, cancellation, complaint and checkout UX must be reviewed before a paid pilot.
supersedes: null
superseded_by: null
```

Supporting current-process source:
- https://www.gob.pe/institucion/indecopi/noticias/1412832-indecopi-inicia-consulta-publica-para-mejorar-reglas-del-comercio-electronico-y-frenar-practicas-enganosas

The June 2026 Indecopi notice described rulemaking work to operationalize DL 1729. Counsel must verify the final state in force at the time of the paid flow.

## Q01 pre-counsel conclusion

Public sources support the existing fail-closed posture:

```yaml
q01_public_precheck: COMPLETE
legal_classification: UNRESOLVED
paid_flow_clearance: UNRESOLVED
personalized_recommendation_clearance: UNRESOLVED
portfolio_context_clearance: UNRESOLVED
external_authority_required: true
promotion_status: OPEN
```

No public-source inference in this file may be promoted to `CLOSED_PASS` or `CLOSED_CONDITIONAL` without the written review required by `quarries/q01/Q01_COUNSEL_REVIEW_PACKET.md`.