#!/usr/bin/env python3
"""SOPHROSYNE research event collector reference implementation.

Research-only reference path. Defaults to loopback. This is not a production backend
and must not be exposed publicly without a separately approved security/privacy design.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import tempfile
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterable

SCHEMA_VERSION = "q03-research-event-v1"
VARIANTS = set("ABCDEFGT")
SOURCES = {"UI", "MODERATOR", "SYSTEM"}
GEO = {"PERU_ELIGIBLE", "NON_PERU_EXPLORATORY", "UNKNOWN"}
REQUIRED = {
    "event_id", "event_name", "event_schema_version", "occurred_at_utc",
    "experiment_id", "experiment_version", "session_id", "variant_id",
    "prototype_version", "prototype_digest", "source", "promotion_geo_class",
}

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp requires timezone")
    return dt.astimezone(timezone.utc)

def validate_event(event: dict, promotion_grade: bool) -> None:
    missing = REQUIRED - set(event)
    if missing:
        raise ValueError("missing fields: " + ",".join(sorted(missing)))
    if event["event_schema_version"] != SCHEMA_VERSION:
        raise ValueError("unexpected event_schema_version")
    if event["variant_id"] not in VARIANTS:
        raise ValueError("invalid variant_id")
    if event["source"] not in SOURCES:
        raise ValueError("invalid source")
    if event["promotion_geo_class"] not in GEO:
        raise ValueError("invalid promotion_geo_class")
    parse_time(event["occurred_at_utc"])
    if promotion_grade:
        if not event.get("participant_id"):
            raise ValueError("promotion-grade event missing participant_id")
        if event["prototype_digest"] == "UNFROZEN_REHEARSAL":
            raise ValueError("promotion-grade event uses unfrozen prototype digest")
        if event["promotion_geo_class"] == "UNKNOWN":
            raise ValueError("promotion-grade event has UNKNOWN geography")

def connect(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(db_path)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY,
            received_at_utc TEXT NOT NULL,
            participant_id TEXT,
            session_id TEXT NOT NULL,
            event_name TEXT NOT NULL,
            experiment_id TEXT NOT NULL,
            experiment_version TEXT NOT NULL,
            variant_id TEXT NOT NULL,
            prototype_version TEXT NOT NULL,
            prototype_digest TEXT NOT NULL,
            promotion_geo_class TEXT NOT NULL,
            event_json TEXT NOT NULL
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS collector_meta (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)
    con.commit()
    return con

def ingest(con: sqlite3.Connection, event: dict, promotion_grade: bool) -> tuple[str, bool]:
    validate_event(event, promotion_grade)
    received = utc_now()
    canonical = dict(event)
    canonical["received_at_utc"] = received
    if parse_time(received) < parse_time(canonical["occurred_at_utc"]):
        # Client clock can be ahead; preserve both clocks but quarantine impossible large
        # ordering in downstream DQ instead of inventing occurred_at.
        pass
    payload = json.dumps(canonical, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    try:
        con.execute(
            """INSERT INTO events (
                event_id, received_at_utc, participant_id, session_id, event_name,
                experiment_id, experiment_version, variant_id, prototype_version,
                prototype_digest, promotion_geo_class, event_json
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                canonical["event_id"], received, canonical.get("participant_id"),
                canonical["session_id"], canonical["event_name"],
                canonical["experiment_id"], canonical["experiment_version"],
                canonical["variant_id"], canonical["prototype_version"],
                canonical["prototype_digest"], canonical["promotion_geo_class"], payload,
            ),
        )
        con.commit()
        return received, True
    except sqlite3.IntegrityError:
        existing = con.execute("SELECT event_json FROM events WHERE event_id=?", (canonical["event_id"],)).fetchone()
        if not existing:
            raise
        prior = json.loads(existing[0])
        # Idempotent retry is accepted only when client-origin fields match.
        prior.pop("received_at_utc", None)
        retry = dict(event)
        if prior != retry:
            raise ValueError("event_id collision with different payload")
        return json.loads(existing[0])["received_at_utc"], False

def export_events(con: sqlite3.Connection, out_path: Path) -> dict:
    rows = con.execute("SELECT event_json FROM events ORDER BY received_at_utc, event_id").fetchall()
    events = [json.loads(row[0]) for row in rows]
    payload = {
        "export_schema_version": "q03-export-v1",
        "exported_at_utc": utc_now(),
        "events": events,
    }
    canonical_events = json.dumps(events, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    digest = hashlib.sha256(canonical_events).hexdigest()
    payload["events_sha256"] = digest
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"event_count": len(events), "events_sha256": digest, "path": str(out_path)}

def delete_participant(con: sqlite3.Connection, participant_id: str) -> int:
    cur = con.execute("DELETE FROM events WHERE participant_id=?", (participant_id,))
    con.commit()
    return cur.rowcount

class Handler(BaseHTTPRequestHandler):
    server_version = "SophrosyneResearchCollector/1"

    def _json(self, status: int, payload: dict) -> None:
        raw = json.dumps(payload, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def do_POST(self) -> None:
        if self.path != "/events":
            self._json(404, {"error": "not_found"})
            return
        expected = self.server.auth_token  # type: ignore[attr-defined]
        supplied = self.headers.get("Authorization", "")
        if expected and supplied != f"Bearer {expected}":
            self._json(401, {"error": "unauthorized"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 262144:
                raise ValueError("invalid content length")
            data = json.loads(self.rfile.read(length))
            event = data.get("event") if isinstance(data, dict) and "event" in data else data
            received, inserted = ingest(
                self.server.db, event, self.server.promotion_grade  # type: ignore[attr-defined]
            )
            self._json(200, {"status": "accepted", "inserted": inserted, "received_at_utc": received})
        except (ValueError, json.JSONDecodeError) as exc:
            self._json(400, {"error": "invalid_event", "detail": str(exc)})

    def log_message(self, fmt: str, *args) -> None:
        return

def serve(args) -> None:
    token = os.environ.get("SOPHROSYNE_RESEARCH_TOKEN", "")
    if args.host not in {"127.0.0.1", "localhost", "::1"} and not args.allow_non_loopback:
        raise SystemExit("Refusing non-loopback bind without --allow-non-loopback")
    if args.allow_non_loopback:
        raise SystemExit("Non-loopback deployment is intentionally disabled in this reference implementation pending Q01/security approval.")
    if not token:
        raise SystemExit("SOPHROSYNE_RESEARCH_TOKEN is required")
    con = connect(args.db)
    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    httpd.db = con
    httpd.auth_token = token
    httpd.promotion_grade = args.promotion_grade
    print(json.dumps({
        "status": "LISTENING",
        "host": args.host,
        "port": args.port,
        "promotion_grade": args.promotion_grade,
        "db": str(args.db),
    }))
    httpd.serve_forever()

def sample_event(event_id: str = "e1") -> dict:
    return {
        "event_id": event_id,
        "event_name": "session_started",
        "event_schema_version": SCHEMA_VERSION,
        "occurred_at_utc": "2026-09-28T20:00:00Z",
        "received_at_utc": None,
        "experiment_id": "REHEARSAL",
        "experiment_version": "v1",
        "participant_id": "P001",
        "session_id": "S001",
        "task_id": "SYN-01",
        "variant_id": "F",
        "prototype_version": "research-prototype-v2.3.0",
        "prototype_digest": "sha256:candidate-test-digest",
        "source": "UI",
        "recruitment_cohort": "SYNTHETIC_TEST",
        "promotion_geo_class": "PERU_ELIGIBLE",
    }

def self_test() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        con = connect(root / "collector.sqlite3")
        event = sample_event()
        _, inserted1 = ingest(con, event, promotion_grade=True)
        _, inserted2 = ingest(con, event, promotion_grade=True)
        assert inserted1 is True and inserted2 is False
        bad = sample_event("e2")
        bad["prototype_digest"] = "UNFROZEN_REHEARSAL"
        try:
            ingest(con, bad, promotion_grade=True)
        except ValueError:
            pass
        else:
            raise AssertionError("promotion-grade accepted unfrozen digest")
        receipt1 = export_events(con, root / "export1.json")
        receipt2 = export_events(con, root / "export2.json")
        assert receipt1["event_count"] == 1
        assert receipt1["events_sha256"] == receipt2["events_sha256"]
        deleted = delete_participant(con, "P001")
        assert deleted == 1
        receipt3 = export_events(con, root / "export3.json")
        assert receipt3["event_count"] == 0
        print(json.dumps({
            "status": "PASS",
            "idempotent_retry": True,
            "promotion_grade_guard": True,
            "stable_event_digest": True,
            "participant_deletion_rehearsed": True,
        }, indent=2))

def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("serve")
    p.add_argument("--db", type=Path, required=True)
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=8787)
    p.add_argument("--promotion-grade", action="store_true")
    p.add_argument("--allow-non-loopback", action="store_true")

    p = sub.add_parser("export")
    p.add_argument("--db", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("delete-participant")
    p.add_argument("--db", type=Path, required=True)
    p.add_argument("--participant-id", required=True)

    sub.add_parser("self-test")

    args = parser.parse_args()
    if args.cmd == "serve":
        serve(args)
    elif args.cmd == "export":
        con = connect(args.db)
        print(json.dumps(export_events(con, args.out), indent=2))
    elif args.cmd == "delete-participant":
        con = connect(args.db)
        print(json.dumps({"deleted_events": delete_participant(con, args.participant_id)}))
    else:
        self_test()

if __name__ == "__main__":
    main()
