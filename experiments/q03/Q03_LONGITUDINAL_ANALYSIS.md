# Q03 Longitudinal Analysis Reference

## Status

REHEARSAL_COMPLETE / ANALYSIS_SEMANTICS_EXECUTABLE / REAL_14_DAY_DATA_MISSING

Canonical implementation:
- experiments/q03/q03_longitudinal_metrics.py

The script implements the frozen runbook semantics for:
- local study days in America/Lima;
- qualifying activity;
- PROMPTED / AMBIGUOUS / UNPROMPTED session attribution;
- >=3 active-day classification;
- unprompted return after day 3;
- historical Decision Record revisit;
- M1/M2/M3 numerator/denominator output.

It consumes a frozen Q03 export and does not change raw events.

## Reminder attribution

- no earlier reminder -> UNPROMPTED;
- <24h after latest delivered reminder -> PROMPTED;
- 24h–48h -> AMBIGUOUS;
- >=48h -> UNPROMPTED.

## Important boundary

The script can execute the analysis semantics now, but it cannot manufacture:
- reminder-delivery receipts;
- participant eligibility;
- real non-return behavior;
- 14 elapsed days;
- valid consent.

Those remain empirical/authority blockers.

## Self-test

~~~bash
python experiments/q03/q03_longitudinal_metrics.py --self-test
~~~
