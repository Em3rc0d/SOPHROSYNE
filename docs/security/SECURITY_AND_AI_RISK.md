# Security & AI Risk

## Credential policy

If connected accounts ever exist:
- encrypt secrets with dedicated key management;
- never log secrets;
- least privilege;
- no withdrawal permission;
- IP allowlists where supported;
- rotation/revocation;
- connector isolation;
- user-visible disconnect/revoke.

## Future execution safety

Any later live engine requires deterministic order flow, idempotency, pre-trade checks, position/order limits, max-loss controls, stale-data detection, venue-status detection, circuit breakers, a global kill switch, reconciliation, partial-fill handling, bounded retries and an immutable audit trail.

## LLM isolation

LLMs can summarize and explain structured evidence.

LLMs cannot:
- create executable orders;
- choose position size;
- invent probability/confidence;
- bypass risk limits;
- mutate deterministic strategy semantics.

## Prompt injection and hostile content

News, social and web content are untrusted inputs. External text is data, not instructions.

Required flow:

`untrusted content → parsing/sanitization → entity/event extraction → source validation → structured evidence → quant/risk engines → explanation`

Never build `article → LLM agent → broker`.

## Market manipulation

Explicitly test resilience against pump-and-dump campaigns, coordinated social spam, fake whale alerts, duplicated fake news, wash-trading and spoofing-like patterns. Sentiment must never be the sole execution trigger.

## Privacy

Portfolio holdings and financial behavior are sensitive personal data. Apply minimization, purpose limitation, retention controls, deletion/export, processor inventory and incident response from the first connected-data prototype.
