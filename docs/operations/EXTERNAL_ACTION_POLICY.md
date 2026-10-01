# External Action Policy

## Status

ACTIVE PROJECT OPERATING RULE

## Default interpretation of execution commands

Commands such as:
- "ejecuta";
- "dale";
- "ve para adelante";
- "haz todo";
- "continúa";

authorize internal/technical execution only unless the user explicitly says otherwise.

Default-allowed internal/technical actions:
- public web research;
- repository edits;
- tests and CI;
- static analysis;
- local/research artifacts;
- preview deployment to existing technical infrastructure such as Vercel when deployment is part of the requested technical execution;
- reading public documentation and making reversible internal design decisions.

## Explicit authorization required

Never infer permission for:
- sending email;
- sending DMs/messages;
- submitting contact forms;
- contacting reviewers, lawyers, vendors, providers or other third parties;
- accepting meetings;
- accepting terms/contracts;
- starting a paid engagement;
- purchasing subscriptions/data/connects/services;
- making payments;
- posting to social accounts;
- applying to jobs/proposals;
- accepting legal/commercial commitments;
- sending material in the user's name.

Required authorization must name the external action, e.g.:
- "envía ese correo";
- "contacta a X";
- "compra el plan";
- "publica ese post".

## Research rule

When an external fact can be investigated from public sources:
1. research it independently;
2. prefer official/primary sources;
3. record uncertainty;
4. make the safest reversible internal decision;
5. do not contact anyone merely because public information is incomplete.

If authority truly cannot be established publicly:
- leave the formal gate open;
- choose a fail-closed product posture;
- continue any safe internal/public-preview lane that does not require that authority.

## Final invariant

> Lack of certainty is not permission to contact someone.

External communication is a separate user-authorized action.
