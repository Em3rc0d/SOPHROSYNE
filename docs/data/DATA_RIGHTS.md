# Data Rights Architecture

## Principle

**Technical API access does not imply commercial display, non-display, redistribution, caching or derived-data rights.**

Every production dataset needs a rights record covering:
- provider;
- instrument/coverage;
- historical rights;
- real-time/delayed rights;
- display rights;
- non-display rights;
- redistribution rights;
- derived-data rights;
- retention/caching;
- attribution;
- user classification/entitlements;
- geography;
- cost;
- fallback provider.

## Architecture consequences

1. Prefer derived intelligence over rebuilding a raw charting feed.
2. Never treat scraping as a licensing strategy.
3. Data provenance must survive every transformation.
4. Cache only where contracts allow it.
5. Critical datasets need fallback providers or graceful degradation.
6. Provider-specific data must be removable without rewriting the domain model.

## Provider notes for MK0

- US exchanges distinguish distributor, subscriber, non-display and derived-data uses.
- Retail-friendly APIs may have terms that differ materially for commercial/B2B products.
- Crypto public APIs must be checked for caching, redistribution, region and branding rules.
- News rights are separate from rights to store embeddings, derived event objects or transformed text.

## Hard gate

No paid public beta may expose a production data family until written provider terms/quotes have been captured in the data-rights registry.
