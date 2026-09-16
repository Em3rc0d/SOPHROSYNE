# Configuration and Secrets Contract

## Goal

Configuration must be explicit, typed, environment-scoped and reproducible. Secrets must be injectable and rotatable without code changes.

## Configuration classes

### Versioned non-secret configuration
Examples:
- freshness thresholds;
- feature flags/defaults;
- enabled instrument universe;
- market-state profile;
- risk policy parameters;
- provider capability routing;
- retry/timeouts;
- job deadlines;
- logging/telemetry sampling;
- UI disclosure defaults.

Rules:
- stored in repository or a versioned configuration artifact;
- schema validated at application startup;
- config version/hash included in derived artifact version bundles;
- production changes reviewed and auditable.

### Secrets
Examples:
- database credentials;
- OIDC client secret where required;
- market-data provider keys;
- object-storage credentials;
- LLM provider key;
- telemetry exporter credentials.

Rules:
- supplied from platform secret store/environment injection;
- never committed to Git;
- never stored in client bundles;
- never printed by diagnostics;
- separate per environment;
- individually rotatable;
- least-privilege scopes.

### Dynamic operational controls
Examples:
- kill switches;
- temporarily disabled provider capability;
- suspended model version;
- emergency feature disablement.

Rules:
- authoritative server-side store;
- audited actor/time/reason;
- safe default after control-store failure is defined per flag;
- critical kill switches default fail-closed.

## Startup validation

`api` and `worker` fail startup if mandatory configuration is missing, malformed or semantically inconsistent.

Startup checks include:
- environment identity;
- database DSN present;
- migration/schema compatibility;
- allowed origins/hosts;
- provider adapter configuration syntax;
- secret references present without echoing values;
- object-storage bucket/config;
- OIDC issuer/audience;
- feature/config schema version;
- clock/timezone fixed to UTC semantics.

A process must not start in a half-configured production state.

## Environment separation

`local`, `ci`, `staging`, `production` use distinct:
- databases;
- storage buckets/prefixes;
- OIDC tenants/apps where practical;
- provider credentials;
- encryption/platform secrets;
- telemetry destinations or environment labels.

Production secrets are unavailable to CI pull-request jobs.

## Config precedence

Canonical precedence is explicit and minimal:
1. compiled safe defaults for non-sensitive low-risk values;
2. versioned environment config;
3. deployment-time environment variables for operational wiring;
4. secret-store values for secrets;
5. audited dynamic controls for runtime kill/suspend actions.

No undocumented developer-local override exists in production.

## Secret rotation

Every production secret class must have a rotation procedure that states:
- owner;
- rotation method;
- whether dual-key overlap is supported;
- validation check;
- rollback/revoke procedure;
- downstream services requiring restart/reload.

Provider-key rotation is rehearsed in staging before beta.

## Secret compromise response

On suspected compromise:
1. activate affected feature/provider kill switch if required;
2. revoke credential at source;
3. issue replacement with least privilege;
4. update secret store;
5. restart/reload affected service;
6. verify audit/provider logs;
7. search application telemetry for misuse without exposing secret value;
8. open incident/postmortem.

## Local development

Repository may include `.env.example` with variable names and safe placeholders only.

Local setup must work with test/sandbox credentials and synthetic fixtures. Developers must not need production secrets to run ordinary tests.

## Typed settings

Both Python and web applications expose a single typed settings module rather than scattered environment lookups.

Unknown production configuration keys should be surfaced in validation where practical to catch typos.

## Rights-sensitive configuration

A data provider is not enabled merely because a key exists. Activation requires:
- provider adapter enabled;
- verified active `DataRightsRecord` for the requested capability/use;
- environment entitlement mapping;
- health state acceptable.

Credentials and legal entitlement are separate concepts.

## Configuration change gate

Any configuration capable of changing user-visible financial semantics—freshness, risk parameters, model routing, strategy feature definitions, data source routing—must be versioned and reviewed like code. Its version/hash becomes part of DecisionRecord/research lineage.