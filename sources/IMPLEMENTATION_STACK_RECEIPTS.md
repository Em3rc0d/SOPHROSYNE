# Implementation Stack Source Receipts

Retrieved: 2026-09-16

Purpose: preserve the authoritative upstream references used to freeze the MK1 runtime lines in `docs/implementation/TECH_STACK.md`.

## Python

- Source: Python.org downloads / release pages.
- Official site: https://www.python.org/downloads/
- Selected line: Python 3.14 stable line.
- Observed at retrieval: Python 3.14.7 was the current stable 3.14 release.
- Decision use: API/workers/quant runtime.
- Confidence: HIGH / OFFICIAL.

## PostgreSQL

- Source: PostgreSQL official download/news pages.
- Official site: https://www.postgresql.org/download/
- Selected line: PostgreSQL 18 stable line.
- Observed at retrieval: PostgreSQL 18.6 was stable; PostgreSQL 19 was still beta and therefore not selected.
- Decision use: authoritative relational store, transactional outbox and durable MK1 job coordination.
- Confidence: HIGH / OFFICIAL.

## Node.js

- Source: Node.js official release/download pages.
- Official site: https://nodejs.org/en/about/previous-releases
- Selected line: Node.js 24 LTS line.
- Observed at retrieval: Node.js 24 was LTS while Node.js 26 was Current.
- Decision use: web runtime/build tooling.
- Confidence: HIGH / OFFICIAL.

## Next.js

- Source: Next.js official support/release communication.
- Official site: https://nextjs.org/blog
- Selected line: Next.js 16 Active LTS line.
- Observed at retrieval: Next.js 16.3.3 was in the Active LTS line; Next.js 15.5 was Maintenance LTS.
- Decision use: web application shell/presentation tier.
- Confidence: HIGH / OFFICIAL.

## Refresh policy

These receipts freeze the **supported major/LTS lines**, not eternal patch versions.

Before implementation begins:
1. resolve the newest security-supported patch in each frozen line;
2. pin exact versions/digests in lockfiles/build files;
3. rerun compatibility and golden suites for any later major-line upgrade;
4. record a new receipt if upstream support status changes materially.

The project does not upgrade to a beta/Current major solely because it is numerically newer.