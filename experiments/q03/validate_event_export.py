#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = {
    "event_id","event_name","event_schema_version","occurred_at_utc",
    "experiment_id","experiment_version","session_id","variant_id",
    "prototype_version","prototype_digest","source","promotion_geo_class",
}
VARIANTS = set("ABCDEFGT")
SOURCES = {"UI","MODERATOR","SYSTEM"}
GEO = {"PERU_ELIGIBLE","NON_PERU_EXPLORATORY","UNKNOWN"}

def parse_time(value: str) -> datetime:
    text = value.replace("Z", "+00:00")
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return dt.astimezone(timezone.utc)

def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)

def validate_event(event: dict, promotion_grade: bool) -> None:
    missing = REQUIRED - set(event)
    if missing:
        fail("missing fields: " + ",".join(sorted(missing)))
    if event["event_schema_version"] != "q03-research-event-v1":
        fail("unexpected event_schema_version")
    if event["variant_id"] not in VARIANTS:
        fail("invalid variant_id")
    if event["source"] not in SOURCES:
        fail("invalid source")
    if event["promotion_geo_class"] not in GEO:
        fail("invalid promotion_geo_class")
    parse_time(event["occurred_at_utc"])

    received = event.get("received_at_utc")
    if received is not None:
        if parse_time(received) < parse_time(event["occurred_at_utc"]):
            fail("received_at precedes occurred_at")

    if promotion_grade:
        if not event.get("participant_id"):
            fail("promotion-grade event missing participant_id")
        if received is None:
            fail("promotion-grade event missing received_at_utc")
        if event["prototype_digest"] == "UNFROZEN_REHEARSAL":
            fail("promotion-grade event uses unfrozen prototype digest")
        if event["promotion_geo_class"] == "UNKNOWN":
            fail("promotion-grade event has UNKNOWN geography")

def validate_payload(payload: dict, promotion_grade: bool) -> None:
    events = payload.get("events")
    if not isinstance(events, list):
        fail("export must contain events array")
    if not events:
        fail("events array is empty")

    ids = [e.get("event_id") for e in events]
    if len(ids) != len(set(ids)):
        fail("duplicate event_id")

    for event in events:
        if not isinstance(event, dict):
            fail("event is not object")
        validate_event(event, promotion_grade)

    by_session: dict[str, list[dict]] = {}
    for event in events:
        by_session.setdefault(event["session_id"], []).append(event)

    for session_id, rows in by_session.items():
        names = [r["event_name"] for r in rows]
        if "session_started" not in names:
            fail(f"session {session_id} missing session_started")
        times = [parse_time(r["occurred_at_utc"]) for r in rows]
        if min(times) != parse_time(next(r["occurred_at_utc"] for r in rows if r["event_name"] == "session_started")):
            fail(f"session {session_id} has event before session_started")

    counts = Counter(e["event_name"] for e in events)
    print(json.dumps({
        "status": "PASS",
        "promotion_grade": promotion_grade,
        "event_count": len(events),
        "session_count": len(by_session),
        "event_name_counts": dict(sorted(counts.items())),
    }, indent=2, sort_keys=True))

def self_test() -> None:
    base = {
        "event_id": "e1",
        "event_name": "session_started",
        "event_schema_version": "q03-research-event-v1",
        "occurred_at_utc": "2026-09-17T20:00:00+00:00",
        "received_at_utc": None,
        "experiment_id": "REHEARSAL",
        "experiment_version": "v1",
        "participant_id": None,
        "session_id": "s1",
        "task_id": "SYN-01",
        "variant_id": "F",
        "prototype_version": "research-prototype-v2.2.0",
        "prototype_digest": "UNFROZEN_REHEARSAL",
        "source": "UI",
        "recruitment_cohort": None,
        "promotion_geo_class": "UNKNOWN",
    }
    validate_payload({"events":[base]}, promotion_grade=False)
    try:
        validate_payload({"events":[base]}, promotion_grade=True)
    except SystemExit:
        print("PASS: promotion-grade guard rejects rehearsal event")
    else:
        fail("promotion-grade guard accepted rehearsal event")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("export", nargs="?", type=Path)
    parser.add_argument("--promotion-grade", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if not args.export:
        parser.error("export path required unless --self-test")
    payload = json.loads(args.export.read_text(encoding="utf-8"))
    validate_payload(payload, args.promotion_grade)

if __name__ == "__main__":
    main()
