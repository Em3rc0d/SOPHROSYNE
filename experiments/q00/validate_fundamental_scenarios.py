#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "experiments/q00/fundamental-scenarios/manifest.json"
ALLOWED = {"FUNDAMENTAL","VALUATION","PRICE","MOMENTUM","VOLUME","VOLATILITY","LIQUIDITY","BREADTH","MACRO","EVENT","POSITIONING","PORTFOLIO","EXECUTION","PROVENANCE"}

def req(name, cond):
    if not cond:
        raise SystemExit(f"FAIL: {name}")
    print(f"PASS: {name}")

data=json.loads(PATH.read_text(encoding="utf-8"))
rows=data.get("scenarios",[])
req("three candidate fundamental scenarios", len(rows)==3)
req("unique ids", len({r["scenario_id"] for r in rows})==3)
for row in rows:
    facts=row.get("facts",[])
    req(f"{row['scenario_id']} investment context", row.get("decision_context")=="INVESTMENT")
    req(f"{row['scenario_id']} no leverage", row.get("leverage")=="NONE")
    req(f"{row['scenario_id']} seven facts", len(facts)==7)
    req(f"{row['scenario_id']} canonical classes", all(f.get("class") in ALLOWED for f in facts))
    req(f"{row['scenario_id']} fundamental coverage", sum(f.get("class")=="FUNDAMENTAL" for f in facts)>=3)
    req(f"{row['scenario_id']} valuation coverage", any(f.get("class")=="VALUATION" for f in facts))
    req(f"{row['scenario_id']} provenance", any(f.get("class")=="PROVENANCE" for f in facts))
    req(f"{row['scenario_id']} reasoning anchors", len(row.get("expected_reasoning",[]))>=4)
    req(f"{row['scenario_id']} invalidators", len(row.get("invalidator_classes",[]))>=3)
    req(f"{row['scenario_id']} hidden outcome", bool(row.get("hidden_outcome")))
print("Q00 fundamental supplement: PASS")
