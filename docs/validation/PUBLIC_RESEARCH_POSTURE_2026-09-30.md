# Public Research Posture — 2026-09-30

## Status

PUBLIC_RESEARCH_PREVIEW: AUTHORIZED_BY_INTERNAL_RISK_POSTURE

MK0_PROMOTION: BLOCKED

This is an internal operating decision based on public-source research. It is not a legal opinion and does not replace Q01/Q02 authority.

## Public preview lane

A SOPHROSYNE research preview may be publicly deployed when all of the following remain true:

- synthetic or historical-style scenarios only;
- no live brokerage integration;
- no custody;
- no order routing;
- no personalized buy/sell/hold recommendation;
- no individualized portfolio allocation or position sizing;
- no requirement to enter holdings, balances, broker credentials or financial account identifiers;
- no server-side participant telemetry collection;
- browser-local state only;
- no payment or subscription flow;
- no fake-door pricing experiment;
- no raw commercial market-data redistribution;
- explicit research-only / non-advisory boundary remains visible.

The public preview is a product/research artifact, not Q00/Q03 promotable evidence.

## Peru public-source risk posture

The official SMV text defines securities-market intermediation around habitual operations performed for another party, including purchase, sale, placement, distribution, brokerage, commission or negotiation of securities.

Internal product decision:
- do not execute or route transactions for users;
- do not custody assets;
- do not accept brokerage credentials;
- do not present personalized trade instructions;
- do not represent the research prototype as a regulated intermediary/adviser;
- keep outputs centered on evidence, uncertainty, contradiction and process.

This posture is deliberately narrower than what might ultimately be legally permissible.

## Personal-data posture

Until Q01 is independently closed:
- public preview collects no server-side participant data;
- no name/email is required;
- no portfolio or account data is requested;
- local browser state is disposable;
- formal study collection remains separate from the public preview.

For future formal study infrastructure:
- use pseudonymous participant IDs;
- retain any identity mapping separately;
- minimize fields;
- freeze retention/deletion semantics before collection;
- use the Q03 collector only after approved hosting/security/privacy posture.

## Provider posture

The public preview has no external market-data dependency.

Real-data work remains a separate internal research lane:
- provider data may be used only under rights compatible with the exact internal research use;
- raw provider data is never published from the research repository;
- public artifacts contain only synthetic fixtures, rights-safe metadata or permitted non-reconstructable research receipts.

## What public preview may demonstrate

Allowed:
- evidence separation;
- stale/missing information;
- uncertainty;
- invalidators;
- decision records;
- market-domain educational structure;
- synthetic execution/liquidity reasoning;
- synthetic fundamental/valuation reasoning.

Not allowed:
- live price predictions;
- personalized recommendation;
- trade execution;
- implied investment suitability;
- claims of validated alpha;
- claims that MK0/Q00/Q03 are closed.

## Reopen triggers

Reassess this posture if:
- the preview begins collecting server-side human data;
- live/named securities replace synthetic/historical-style cases;
- brokerage connectivity is introduced;
- personalization uses holdings, risk tolerance or financial position;
- payments/pricing experiments are introduced;
- market-data provider content is displayed publicly;
- applicable public law/regulation materially changes.

## Final invariant

> Public research may proceed without pretending that public-source research substitutes for legal/provider authority.


## Public sources used

- SMV — TUO Ley del Mercado de Valores / Article 6 intermediation:
  https://www.smv.gob.pe/ServicioConsultaNormas/uploads/TUO_LMV_DECRETO_SUPREMO_N_020_2023_EF.pdf
- SMV legal-information system:
  https://www.smv.gob.pe/simv/Frm_DetalleSistemaInfoLegal.aspx?CNORMA=DLG0000199600861
- Peru personal-data regulation, Decreto Supremo N.° 016-2024-JUS:
  https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus
- ANPD guide on disassociation/anonymization/pseudonymization:
  https://www.gob.pe/institucion/anpd/informes-publicaciones/7317169-guia-de-disociacion-anonimizacion-y-seudonimizacion-de-datos-personales-para-entidades-publicas

These sources inform the internal fail-closed posture; they do not constitute product-specific legal advice.
