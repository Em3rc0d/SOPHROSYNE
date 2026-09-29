#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/Lima")
QUALIFYING = {
    "task_answer_submitted",
    "evidence_item_opened",
    "uncertainty_opened",
    "invalidation_opened",
    "decision_record_created",
    "decision_record_opened",
}
REMINDER_EVENTS = {"reminder_delivered"}

def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z","+00:00"))

def local_day(value: str):
    return parse_ts(value).astimezone(TZ).date()

def classify_session(session_start: datetime, reminder_times: list[datetime]) -> str:
    prior=[r for r in reminder_times if r <= session_start]
    if not prior:
        return "UNPROMPTED"
    delta=session_start-max(prior)
    if delta < timedelta(hours=24):
        return "PROMPTED"
    if delta < timedelta(hours=48):
        return "AMBIGUOUS"
    return "UNPROMPTED"

def analyze(payload: dict) -> dict:
    events=payload.get("events",[])
    by_participant=defaultdict(list)
    for e in events:
        pid=e.get("participant_id")
        if pid:
            by_participant[pid].append(e)

    participants={}
    for pid, rows in by_participant.items():
        rows=sorted(rows,key=lambda e:(parse_ts(e["occurred_at_utc"]),e["event_id"]))
        reminders=[parse_ts(e["occurred_at_utc"]) for e in rows if e["event_name"] in REMINDER_EVENTS]
        sessions=defaultdict(list)
        for e in rows:
            sessions[e["session_id"]].append(e)

        active_days=set()
        session_classes={}
        historical_revisit=False
        first_day=None

        for sid, srows in sessions.items():
            srows=sorted(srows,key=lambda e:parse_ts(e["occurred_at_utc"]))
            start_event=next((e for e in srows if e["event_name"]=="session_started"),None)
            if not start_event:
                continue
            start=parse_ts(start_event["occurred_at_utc"])
            day=local_day(start_event["occurred_at_utc"])
            if first_day is None or day < first_day:
                first_day=day
            qualifying=any(e["event_name"] in QUALIFYING for e in srows)
            if qualifying:
                active_days.add(day)
                session_classes[sid]=classify_session(start,reminders)
            if any(e["event_name"]=="decision_record_revisited" for e in srows):
                historical_revisit=True

        unprompted_after_day3=False
        if first_day:
            threshold=first_day+timedelta(days=3)
            for sid,sclass in session_classes.items():
                if sclass!="UNPROMPTED":
                    continue
                start_event=next(e for e in sessions[sid] if e["event_name"]=="session_started")
                if local_day(start_event["occurred_at_utc"]) > threshold:
                    unprompted_after_day3=True

        participants[pid]={
            "active_day_count":len(active_days),
            "multi_day_active":len(active_days)>=3,
            "unprompted_return_after_day3":unprompted_after_day3,
            "historical_record_revisit":historical_revisit,
            "session_attribution":session_classes,
        }

    n=len(participants)
    m1=sum(p["multi_day_active"] for p in participants.values())
    m2=sum(p["unprompted_return_after_day3"] for p in participants.values())
    revisit_eligible=sum(
        any(e.get("event_name")=="decision_record_created" for e in by_participant[pid])
        for pid in participants
    )
    m3=sum(p["historical_record_revisit"] for p in participants.values())
    return {
        "analysis_schema_version":"q03-longitudinal-analysis-v1",
        "study_timezone":"America/Lima",
        "participant_count":n,
        "M1_multi_day_active_rate":{"numerator":m1,"denominator":n,"rate":(m1/n if n else None)},
        "M2_unprompted_revisit_rate":{"numerator":m2,"denominator":n,"rate":(m2/n if n else None)},
        "M3_historical_record_revisit_rate":{"numerator":m3,"denominator":revisit_eligible,"rate":(m3/revisit_eligible if revisit_eligible else None)},
        "participants":participants,
    }

def self_test():
    def ev(eid,name,ts,sid="s1",pid="P1"):
        return {
            "event_id":eid,"event_name":name,"occurred_at_utc":ts,
            "participant_id":pid,"session_id":sid
        }
    payload={"events":[
        ev("1","session_started","2026-09-01T15:00:00Z","s1"),
        ev("2","decision_record_created","2026-09-01T15:05:00Z","s1"),
        ev("3","session_started","2026-09-03T15:00:00Z","s2"),
        ev("4","decision_record_opened","2026-09-03T15:02:00Z","s2"),
        ev("5","reminder_delivered","2026-09-09T13:00:00Z","r1"),
        ev("6","session_started","2026-09-09T16:00:00Z","s3"),
        ev("7","decision_record_opened","2026-09-09T16:01:00Z","s3"),
        ev("8","decision_record_revisited","2026-09-09T16:02:00Z","s3"),
        ev("9","session_started","2026-09-12T16:00:00Z","s4"),
        ev("10","task_answer_submitted","2026-09-12T16:05:00Z","s4"),
    ]}
    result=analyze(payload)
    p=result["participants"]["P1"]
    assert p["active_day_count"]==4
    assert p["multi_day_active"] is True
    assert p["session_attribution"]["s3"]=="PROMPTED"
    assert p["session_attribution"]["s4"]=="UNPROMPTED"
    assert p["unprompted_return_after_day3"] is True
    assert p["historical_record_revisit"] is True
    print(json.dumps({"status":"PASS","result":result},indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("export",nargs="?",type=Path)
    ap.add_argument("--out",type=Path)
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.export:
        ap.error("export required unless --self-test")
    payload=json.loads(args.export.read_text(encoding="utf-8"))
    result=analyze(payload)
    raw=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.out:
        args.out.write_text(raw,encoding="utf-8")
    print(raw,end="")

if __name__=="__main__":
    main()
