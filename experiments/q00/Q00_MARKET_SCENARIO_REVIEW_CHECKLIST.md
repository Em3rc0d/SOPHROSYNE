# Q00 Market Scenario Review Checklist

## Status

`CANDIDATE V1 / INTERNAL MARKET-DOMAIN QA / INDEPENDENT REVIEW STILL REQUIRED`

Canonical baseline:
- `docs/quant/MARKET_DOMAIN_FOUNDATION.md`
- `mining-site/market/2026-09-21-course-synthesis.md`

Purpose: permit the project to design and internally reject weak market scenarios without asking the project owner to act as a trading expert.

This checklist does not replace Q00 R2 independent market-domain review.

---

# A. Scenario identity

Required:

```yaml
scenario_id:
instrument_type:
instrument_id_or_synthetic_class:
decision_context: INVESTMENT | SWING_TRADE | INTRADAY | EXECUTION_ONLY | RESEARCH_ONLY
horizon:
leverage: NONE | MARGIN | SHORT | DERIVATIVE | OTHER
as_of:
hidden_outcome: true
```

Fail if context/horizon is ambiguous enough that the same evidence would imply materially different reasoning across horizons.

---

# B. Information equivalence

PASS only if:
- A–G receive equivalent underlying facts except the pre-registered treatment;
- one arm does not receive hidden directional information;
- no wording labels one interface superior;
- no arm receives later outcome information;
- timestamps/freshness are preserved.

---

# C. Evidence taxonomy

Every material fact maps to at least one canonical evidence class.

Review:
- fundamental;
- valuation;
- price;
- momentum;
- volume;
- volatility;
- liquidity;
- breadth;
- macro;
- event;
- positioning;
- execution;
- provenance.

Fail if the scenario calls multiple transformations of the same underlying series "independent confirmation".

---

# D. Technical-analysis correctness

Check:
- trend window is declared;
- momentum calculation is defined or qualitatively bounded;
- volume comparison baseline exists;
- volatility is not labeled bullish/bearish by itself;
- support/resistance is not a guaranteed barrier;
- indicators are not translated into deterministic future movement;
- technical signal does not become a probability unless calibrated.

Reject phrases such as:
- "RSI guarantees reversal";
- "MACD confirms the price will rise";
- "three bullish indicators = high probability" without calibration.

---

# E. Fundamental correctness

When company fundamentals matter, check:
- metric has period/source;
- earnings vs cash flow are not conflated;
- debt/balance sheet is represented where material;
- valuation statement identifies basis;
- analyst estimate/forecast is labeled inferred;
- growth is not automatically cheapness;
- good company != good stock at every price.

---

# F. Liquidity / execution correctness

When execution is material:
- bid/ask semantics valid;
- spread and/or depth considered;
- order type semantics correct;
- market price is not assumed to equal fill;
- limit order can fail to execute;
- stop trigger is not guaranteed fill price;
- volume is not used as a complete liquidity proxy;
- costs/slippage are not silently omitted where they can reverse interpretation.

If execution is not part of the task, explicitly mark `NOT_MATERIAL_TO_PRIMARY_REASONING`.

---

# G. Risk / portfolio correctness

Check:
- volatility != direction;
- drawdown/risk is separated from expected return;
- leverage is explicit;
- concentration/portfolio impact is not personalized unless allowed;
- stop-loss is not presented as complete risk control;
- scenario does not ask novice users to infer position size.

---

# H. Behavioral traps

A scenario may intentionally include:
- salient narrative;
- recent move;
- apparent consensus;
- outcome temptation;
- stale confirmation;
- correlated signals.

But the answer key must identify the trap before participant outcomes are observed.

The scenario must not depend on diagnosing a participant.

---

# I. Invalidation

A valid invalidator:
- is observable;
- is linked to the hypothesis;
- could plausibly change the interpretation;
- is not circular;
- is not simply "price goes against me."

Prefer:
"updated source contradicts the assumed demand improvement"
over:
"sell if price falls 5%" unless the scenario is specifically an execution/risk-rule task.

---

# J. Outcome-blindness

The hidden future outcome:
- is excluded from task materials;
- cannot be inferred from filenames/metadata;
- is not used by scorers during process scoring;
- can show that good reasoning lost money;
- can show that bad reasoning made money.

Fail if "correct answer" means "picked the eventual direction."

---

# K. Beginner clarity

A beginner should be able to distinguish:
- observation;
- uncertainty;
- inference;
- what evidence would matter next.

Do not require unexplained specialist jargon to pass a process-quality task.

Depth modes may add technical detail but cannot change the underlying conclusion/evidence.

---

# L. Review result

```yaml
scenario_id:
review_version:
reviewer:
A_identity: PASS | FAIL
B_information_equivalence: PASS | FAIL
C_evidence_taxonomy: PASS | FAIL
D_technical_correctness: PASS | FAIL | NA
E_fundamental_correctness: PASS | FAIL | NA
F_execution_correctness: PASS | FAIL | NA
G_risk_correctness: PASS | FAIL
H_behavioral_trap_integrity: PASS | FAIL
I_invalidator_quality: PASS | FAIL
J_outcome_blindness: PASS | FAIL
K_beginner_clarity: PASS | FAIL
terminal_internal_status: READY_FOR_R2 | REWORK | REJECT
notes: []
```

`READY_FOR_R2` requires no FAIL.

Independent R2 can still reject a scenario that passes internal QA.

---

## Final invariant

> A market scenario is a controlled reasoning instrument, not a disguised signal.

Its answer key evaluates market reasoning under the information available at the time, never whether the participant guessed the next price move.
