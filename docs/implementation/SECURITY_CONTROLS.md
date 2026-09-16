# MK1 Security Controls

## Security objective

Protect user data, provider credentials, research integrity and evidence provenance while keeping the LLM/explanation layer unable to gain financial or infrastructure authority.

## Trust boundaries

```text
Internet / Browser
      |
      v
Web boundary
      |
      v
Core API --------> PostgreSQL
  |  |                 |
  |  +-------------> Object Storage
  |
  +----> Worker boundary ----> External providers
  |
  +----> Explanation boundary ----> LLM provider
```

External provider data and user-provided text are **untrusted content** even when the provider itself is trusted.

## Identity and session controls

- Managed OIDC/OAuth-compatible identity provider.
- Authorization Code + PKCE where applicable.
- Server-managed sessions using `Secure`, `HttpOnly`, appropriate `SameSite` cookies.
- Session rotation after authentication/security-sensitive events.
- Short-lived access/session material with explicit revocation path.
- MFA required for administrative/research-privileged production roles where supported.
- No auth tokens or financial provider credentials in browser local storage.

## Authorization

Authorization is enforced server-side per resource and action.

Roles/capabilities are least-privilege:
- standard user;
- research/operator;
- administrator;
- service identities with narrowly scoped machine permissions.

Opaque IDs do not replace ownership checks.

User-owned tables carry ownership/tenant fields and are protected through application-layer authorization plus database policy/constraint tests. Administrative bypass paths are explicit and audited.

## Secrets

- Secrets never live in Git, images, client bundles, logs or test fixtures.
- Production secrets come from the deployment platform's secret manager.
- Separate secrets by environment and provider.
- Provider credentials have minimal scope; withdrawals/order execution credentials are absent in MK1.
- Rotation/revocation procedure is documented and tested.
- CI uses short-lived credentials where supported.

## Network and egress

- Database/object storage are not publicly writable.
- Provider outbound calls originate from controlled backend/worker services.
- User input cannot select arbitrary URLs.
- Provider base URLs are allowlisted configuration.
- SSRF defenses reject private/link-local/metadata destinations for any feature that accepts a URL.
- Timeouts, body-size limits and redirect limits are mandatory for outbound requests.

## Input/content safety

All external text—news, filings, social content, provider descriptions, user annotations—is data, not instructions.

Before LLM use:
- content is clearly delimited/typed;
- instruction-following authority remains in system-owned prompts/config;
- untrusted content cannot enable tools, change policies or request secrets;
- structured authoritative facts are supplied separately from narrative content;
- output is schema validated before display.

Prompt-injection text can at most affect a rejected explanation attempt; it must never alter strategy/risk/model/data-rights state.

## LLM isolation

The LLM layer:
- has no database write credentials;
- has no provider trading credentials;
- has no direct order/custody APIs;
- cannot modify risk limits or StrategyVersion semantics;
- cannot invent probability fields accepted by authoritative schemas;
- receives the minimum structured context needed for explanation;
- returns non-authoritative prose only.

If an explanation fails validation, the authoritative structured product remains usable.

## Web application controls

- strict Content Security Policy tuned for actual dependencies;
- output escaping/sanitization for all untrusted/provider/user content;
- CSRF protection for cookie-authenticated mutations;
- frame-ancestor/clickjacking protection;
- secure referrer policy;
- upload size/type controls if uploads are introduced;
- no secret/source-provider payload embedding in rendered HTML.

## API controls

- strict schema validation and unknown-field policy by endpoint;
- request/body size limits;
- rate limiting/abuse controls by user/IP/service as appropriate;
- idempotency for retryable mutations;
- authorization before resource existence detail is leaked where practical;
- generic external error details; internal traces stay server-side;
- database queries parameterized; dynamic identifiers allowlisted.

## Database controls

- TLS to managed database where supported;
- separate migration and runtime roles;
- runtime role cannot perform schema administration;
- finalized DecisionRecords protected from update/delete through privileges/triggers/policies as appropriate;
- backups encrypted by platform/provider;
- sensitive fields minimized rather than encrypted blindly inside the application;
- no raw passwords stored by SOPHROSYNE.

## Object storage controls

- private buckets by default;
- server-side encryption provided by storage platform;
- short-lived signed URLs only when user download is needed;
- immutable/content-hashed artifact naming;
- bucket policies separate environments;
- raw provider payload retention obeys DataRightsRecord.

## Supply chain

- lockfiles committed;
- dependency vulnerability scanning;
- container/base images pinned for production builds;
- SBOM produced for release artifacts;
- CI actions/dependencies pinned where practical;
- secret scanning;
- branch protections and required reviews for critical security/config paths.

## Audit events

Audit at minimum:
- login/security-sensitive session actions;
- role/permission changes;
- provider credential/config changes;
- rights kill-switch changes;
- model approval/suspension/deployment;
- StrategyVersion approval/archive;
- production feature-flag changes;
- admin access to user-owned data;
- backup/restore and incident actions.

Audit records contain identifiers and action metadata, not secret values.

## Data privacy/minimization

MK1 collects only data required for product operation/research.

- Manual portfolio context avoids unnecessary identity/financial-account details.
- Analytics events must not include raw portfolio positions unless explicitly required and justified.
- Logs/traces redact sensitive fields.
- Data export/deletion requirements are mapped before public beta according to applicable law/policy.

## Vulnerability severity gate

Before production:
- unresolved exploitable Critical/P0: release blocked;
- High/P1 affecting auth, user isolation, provenance, rights or privileged paths: release blocked;
- lower severities require owner, remediation target and risk acceptance where not fixed immediately.

## Incident containment

Immediate kill/revoke controls must exist for:
- compromised provider credential;
- compromised model/explanation provider integration;
- suspect data source;
- rights violation;
- affected endpoint/feature;
- privileged account/session.

Containment takes priority over preserving feature availability.

## Security readiness receipt

Before real credentials or beta users:
1. threat model reviewed against implemented topology;
2. auth/IDOR/CSRF/XSS/SSRF tests green;
3. secret scan clean;
4. dependency/container scan accepted;
5. provider credentials prove least privilege;
6. LLM hostile-content tests green;
7. backup + secret rotation drills completed;
8. incident owner and runbook identified.

`SECURITY_AND_AI_RISK.md` remains the policy-level source; this document is the implementation control baseline.