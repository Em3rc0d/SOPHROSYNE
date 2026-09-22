# Q00 Market Scenario Internal Audit — v2.3

## Status

INTERNAL_QA_PASS / READY_FOR_R2 / NOT_INDEPENDENT_REVIEW / NOT_EVIDENCE

This audit applies the canonical market-domain foundation and Q00 market-scenario checklist to SYN-01…SYN-08 after the v2.3 hardening pass.

It does not replace R2.

## Defects found and corrected

1. Directional-vote contamination
   - liquidity, stable volatility, raw activity/volume, stale-source coincidence and absence of contradiction were being displayed inside "A favor";
   - v2.3 marks those items non-directional and renders them in a separate context surface.

2. Signal-counting affordance
   - support/opposition counts could be misread as a score;
   - v2.3 explicitly states that item count is not strength, independence or probability.

3. Missing decision context
   - scenarios did not machine-declare mode/horizon/instrument/leverage/execution relevance;
   - v2.3 freezes these fields and writes them into each Decision Record.

4. Unfounded macro wording
   - SYN-01 investor text and the generic change-mind placeholder referred to macro evidence not present in every scenario;
   - removed/replaced with evidence-neutral language.

5. Evidence-dependence ambiguity
   - price-derived indicators could look like independent confirmations;
   - v2.3 adds scenario-specific independence notes and a machine-readable raw-fact domain map.

## Scenario audit

| Scenario | Primary market concept | Internal result | Notes |
|---|---|---|---|
| SYN-01 | trend/momentum vs volume/breadth confirmation | READY_FOR_R2 | momentum + breakout share price-history group; liquidity moved to context |
| SYN-02 | range/reversion vs narrative | READY_FOR_R2 | stable volatility is context, not directional confirmation |
| SYN-03 | stale critical evidence | READY_FOR_R2 | provenance is a completeness condition; liquidity is context |
| SYN-04 | breakout under extreme volatility | READY_FOR_R2 | volatility is non-directional; price/momentum grouped |
| SYN-05 | narrative vs causal attribution | READY_FOR_R2 | repeated narrative explicitly not independent causal support |
| SYN-06 | signal vs liquidity/execution quality | READY_FOR_R2 | execution is PRIMARY; raw volume separated from liquidity |
| SYN-07 | source freshness + independence | READY_FOR_R2 | stale source and absence of contradiction do not count as positive confirmation |
| SYN-08 | regime transfer / historical analogy | READY_FOR_R2 | pattern + momentum grouped; regime variables treated separately |

## Checklist disposition

For all eight scenarios after v2.3:

~~~yaml
A_identity: PASS
B_information_equivalence: PASS_CANDIDATE
C_evidence_taxonomy: PASS
D_technical_correctness: PASS
E_fundamental_correctness: NA
F_execution_correctness:
  SYN-06: PASS
  others: PASS_OR_NA_BY_DECLARED_RELEVANCE
G_risk_correctness: PASS
H_behavioral_trap_integrity: PASS
I_invalidator_quality: PASS_CANDIDATE
J_outcome_blindness: PASS
K_beginner_clarity: PASS_CANDIDATE
terminal_internal_status: READY_FOR_R2
~~~

PASS_CANDIDATE means internally acceptable but specifically expected to be challenged by independent R2 before preregistration.

## Fundamental-analysis limitation

The current eight-case corpus primarily tests market-state/provenance/execution reasoning. It does not adequately validate company fundamental analysis or valuation.

Therefore:
- this audit does not claim fundamental-investing coverage;
- Q00 R2 may require a separate historical/fundamental scenario block before the final promotable corpus is frozen;
- the current corpus may not be described as a complete stock-investing curriculum.

## Machine-readable traceability

experiments/q00/Q00_SCENARIO_DOMAIN_MAP.json maps each raw fact to:
- evidence class;
- independence group;
- directional relevance;
- decision context;
- execution relevance.

This map is a research QA artifact. Final historical scenario materials may supersede it before PRE_REGISTERED.

## Final invariant

> Scenario correctness is judged by what could be defended at the scenario's as_of, not by whether the hidden future outcome later moved in the same direction.
