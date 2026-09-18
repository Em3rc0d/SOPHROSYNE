# Q00 Recruitment and Moderator Packet

## Status

`DRAFT_FOR_Q01_AND_INDEPENDENT_REVIEW / DO_NOT_RECRUIT_YET`

This packet is operationally complete but may not be used for promotable recruitment until the Q01 privacy/consent review approves the exact research flow.

## Primary eligibility screener

Use neutral wording. Do not describe SOPHROSYNE features before eligibility.

Required:
1. Are you 18 years old or older? `YES` required.
2. Do you currently reside in Peru for the primary study cohort? `YES` required for promotable primary cohort.
3. In the last 90 days, have you independently researched stocks, ETFs, cryptoassets or other market instruments at least three times for your own learning/decision process? `YES` required.
4. Do you work professionally as an investment adviser, portfolio manager, securities broker or institutional trader? `YES` -> exploratory expert cohort, not primary retail cohort.
5. Have you previously worked on or seen internal SOPHROSYNE research materials, answer keys or scoring rubrics? `YES` -> exclude primary cohort.
6. Have you participated in this exact Q00 experiment version before? `YES` -> exclude duplicate.

Do not request account balances, holdings, broker credentials, exact income or net worth.

## Experience band

Collected for stratified descriptive reporting only:

```text
E0: < 6 months
E1: 6-12 months
E2: >1-3 years
E3: >3 years
```

Experience band may not be used post hoc to exclude unfavorable outcomes.

## Recruitment channels

Use at least two channels where practical.

Candidate channel classes:
- general university/alumni network of adults;
- Peru retail-investing communities;
- paid participant panel;
- general professional/social network.

Record channel per participant. Project insiders are not promotable primary participants.

## Neutral invitation copy

> Participa en un estudio de experiencia de usuario sobre cómo las personas interpretan información de mercados. La actividad usa casos sintéticos o históricos, no requiere operar dinero real y no brinda recomendaciones personalizadas. Buscamos adultos de 18 años o más en Perú que hayan investigado mercados por cuenta propia recientemente. La participación es voluntaria y cualquier compensación, si aplica, depende únicamente de completar las actividades definidas, no de tus respuestas ni de resultados de inversión.

Final wording requires Q01/privacy approval before use.

## Moderator opening script

1. Confirm participant ID and eligibility; do not read private contact identity into the research recording.
2. Present the approved consent notice and record consent version/digest.
3. State:
   - this is product research;
   - cases are synthetic/historical-style;
   - there is no need to buy, sell or hold anything;
   - there is no correct investment action being requested;
   - we are evaluating reasoning/workflow, not market expertise.
4. Explain that some interfaces differ by assignment and the moderator cannot explain which one is expected to perform better.
5. Begin only after consent.

## Allowed clarifications

Moderator may explain:
- interface mechanics;
- where a button is;
- the literal meaning of a study instruction;
- that the participant may stop.

Moderator may not:
- explain market terminology unless the frozen study protocol explicitly exposes that definition equally;
- identify supporting/opposing evidence;
- suggest a conclusion;
- tell the participant to increase/decrease confidence;
- reveal hidden outcome;
- compare the participant to other participants.

Every substantive clarification is logged.

## Task script

For each assigned task:

> Revisa únicamente la información disponible en esta pantalla. Explica qué crees que puede afirmarse, qué te genera duda y qué evidencia podría hacerte cambiar de opinión. No necesitas decidir comprar o vender.

Arm-specific UI provides the assigned treatment. Moderator does not supplement it.

## Transfer task

Use the `transfer=1` assignment.

Moderator says only:

> Este caso debe resolverse sin ayuda estructurada. Usa únicamente la información mostrada y responde con tu propio razonamiento.

No reminder of the five-question checklist or SOPHROSYNE structure is allowed.

## Debrief

After all primary tasks:
- explain that interfaces were experimental variants;
- explain that no result was investment advice;
- do not reveal aggregate outcomes while recruitment is active;
- provide approved privacy/deletion contact/process;
- record adverse/confusion feedback separately from primary scoring.

## Adverse signal / pause rule

Pause the participant session and flag for study review if the participant:
- believes the prototype is telling them to trade real money;
- attempts to enter credentials/account data;
- appears confused about whether SOPHROSYNE is a broker/adviser after clarification;
- is discovered to be under 18;
- sees answer-key material;
- experiences a technical failure affecting treatment equivalence.

## Compensation

If used:
- fixed before recruitment;
- independent of favorable feedback, confidence, arm, price intent or outcome;
- disclosed before participation;
- exact amount/method reviewed under the applicable research/legal flow.

## Required logs

```text
participant_id
eligibility_result
recruitment_channel
experience_band
consent_version_digest
sequence_id
study_started_at
study_completed_at
moderator_deviation_refs
technical_failure_refs
withdrawal_flag
exclusion_reason
compensation_status_if_applicable
```

Contact identity stays in a separate restricted mapping if needed.
