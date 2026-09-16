# Research Participant Protocol

## Purpose

This protocol governs human-participant research used to close Q03/Q05.

The objective is to collect trustworthy product evidence while minimizing unnecessary financial/personal data, avoiding pressure to transact, and preserving a clean boundary between product research and investment activity.

This is a product-research protocol, not a substitute for any formal institutional ethics review that may become applicable in a later academic/commercial context.

---

## Participant eligibility

Primary Q03/Q05 studies recruit adults `18+`.

Do not recruit minors for investment-product validation.

Every study also applies the experiment-specific inclusion/exclusion criteria in its pre-registered manifest.

---

## Consent before data collection

Before recording any research data, participants receive a plain-language consent notice covering:
- study purpose;
- expected duration/tasks;
- what data will be collected;
- whether interaction telemetry is recorded;
- whether audio/video is recorded, if applicable;
- compensation, if any;
- voluntary participation;
- ability to stop participation;
- data retention/deletion contact/process;
- statement that the study is product research and not investment advice;
- statement that participants are not required or encouraged to trade real money.

Consent version/digest is stored with the experiment artifacts.

---

## Prohibited research practices

Q03/Q05 studies must not:
- ask participants to place a live trade to prove engagement;
- condition compensation on buying/selling an asset;
- request brokerage/exchange passwords, API secrets or seed phrases;
- request full account numbers;
- require exact net worth/income/portfolio value when a coarse category or no financial value is sufficient;
- fabricate urgency or guaranteed outcomes;
- imply the prototype has regulatory approval;
- represent paper/historical results as future performance;
- hide that a pricing fake-door will not complete a charge;
- use deceptive market-performance claims to increase conversion.

---

## Compensation

If participants are compensated:
- compensation is fixed by study participation/completion rules disclosed in advance;
- compensation does not depend on investment performance, simulated strategy return, willingness to pay or favorable feedback;
- withdrawal from a study does not retroactively create a financial penalty beyond clearly disclosed rules for incomplete participation where legally appropriate.

---

## Data minimization

Collect only fields required by the pre-registered analysis.

Prefer:
- age eligibility (`18+`) rather than exact birth date;
- experience bands rather than detailed financial histories;
- self-reported tool categories rather than credentials/account exports;
- coarse portfolio-context categories if truly necessary;
- pseudonymous participant IDs.

Do not collect sensitive personal data merely because it may be “interesting later.”

---

## Participant identity separation

Use separate identifiers:

```text
recruitment/contact identity
        |
        +--> local/private mapping if needed
        |
        v
pseudonymous participant_id
        |
        v
experiment events / responses / analysis
```

Analysis artifacts should use `participant_id`, not names/emails.

The mapping, if retained at all, is more restricted than research telemetry.

---

## Financial-data boundary

Human research may ask about workflow behavior, such as:
- tools/sources used;
- how often the participant researches;
- whether they compare conflicting sources;
- whether they keep notes/history;
- broad product subscriptions;
- broad experience level.

Avoid exact holdings or monetary balances unless a specific experiment has a documented need and consent/retention plan.

If portfolio context is necessary for a prototype, prefer fictional or synthetic cases for comparative tasks.

---

## Study scenario rule

Controlled comprehension/competitive tests should use:
- synthetic scenarios; or
- historical scenarios frozen at a true `as_of` point;
- equivalent underlying evidence across variants.

Participants should not be told what real asset to buy/sell.

A scenario must not be constructed so that one UI variant contains hidden informational advantages absent from the comparator unless that difference is itself the pre-registered treatment.

---

## Researcher interaction script rule

Moderators receive a versioned script defining:
- neutral introduction;
- task instructions;
- allowed clarification;
- prohibited leading prompts;
- when to reveal product context;
- debrief wording.

Moderators must not coach participants toward the intended result.

Any material deviation is recorded in the experiment receipt.

---

## Recording policy

Audio/video/screen recording is opt-in where used and clearly disclosed.

If recording is unnecessary, do not collect it.

Derived notes/transcripts should preserve participant anonymity where practical.

Retention period and deletion behavior are defined before collection.

---

## Telemetry privacy

Experiment analytics must not contain:
- passwords/tokens;
- raw authentication headers;
- brokerage credentials;
- full account identifiers;
- exact portfolio positions unless explicitly required and approved by the experiment manifest;
- unrelated free-form sensitive data.

Free-text fields require review/minimization because participants may volunteer information the study did not request.

---

## Withdrawal / deletion

The study manifest defines:
- point until which a participant can request identifiable raw-data deletion;
- which already-aggregated/anonymized results can no longer reasonably be separated;
- what audit metadata may need to remain to preserve research integrity without retaining unnecessary personal content.

A deletion request must not cause the team to secretly alter denominators. If data are removed under the pre-defined policy, the analysis records that removal transparently.

---

## Recruitment-bias log

Each experiment records recruitment source and relevant selection bias.

Examples:
- developer/technical community;
- finance community;
- university network;
- paid recruitment panel;
- existing waitlist.

A participant pool drawn from one source may not be generalized silently to the broader target market.

---

## Adverse participant signal

Pause/review the study if:
- participants interpret prototype output as personalized instruction despite neutral framing;
- the flow creates pressure to transact;
- participants disclose credentials or sensitive data because UI implies it is required;
- a participant reports confusion about whether the prototype is a broker/adviser;
- research staff cannot explain what is experimental vs production.

These observations are themselves evidence for Q01/Q03 UX boundaries.

---

## Study completion checklist

Before finalizing a participant-based receipt confirm:
- consent artifact version recorded;
- participant eligibility satisfied;
- recruitment source recorded;
- exclusions follow pre-registered rules;
- moderator deviations recorded;
- telemetry uses pseudonymous IDs;
- no prohibited credential/account data was collected;
- compensation was independent from favorable outcome;
- missing/withdrawn data are accounted for;
- raw artifacts have an owner/retention policy;
- no participant behavior was induced through real-money trading pressure.

---

## Final invariant

> Product evidence is stronger when participants are free to disagree, leave, ignore the prototype and behave naturally.

The research process must never create the behavior it is trying to prove.
