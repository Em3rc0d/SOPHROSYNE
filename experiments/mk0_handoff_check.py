#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "experiments/q00/Q00_EXECUTION_KIT.md",
    "experiments/q00/Q00_PREREGISTRATION.md",
    "experiments/q00/Q00_SAMPLE_AND_ASSIGNMENT_PLAN.md",
    "experiments/q00/Q00_SCORING_RUBRIC.md",
    "experiments/q00/Q00_MARKET_SCENARIO_REVIEW_CHECKLIST.md",
    "experiments/q00/Q00_MARKET_SCENARIO_AUDIT_V1.md",
    "experiments/q00/Q00_SCENARIO_DOMAIN_MAP.json",
    "experiments/q00/Q00_REVIEWER_HANDOFF.md",
    "experiments/q00/Q00_RECRUITMENT_AND_MODERATOR_PACKET.md",
    "experiments/q00/generate_assignment.py",
    "experiments/q00/Q00_G_COMPARATOR_FREEZE_SHEET.md",
    "experiments/q03/Q03_EXECUTION_KIT.md",
    "experiments/q03/Q03_PREREGISTRATION.md",
    "experiments/q03/Q03_14_DAY_RUNBOOK.md",
    "experiments/q03/q03_event.schema.json",
    "experiments/q03/validate_event_export.py",
    "experiments/q04/Q04_PREREGISTRATION.md",
    "experiments/q04/Q04_DRY_RUN_RECEIPT.md",
    "experiments/q04/Q04_INDEPENDENT_REPRODUCTION_PACKET.md",
    "experiments/q05/Q05_EXECUTION_KIT.md",
    "experiments/q05/Q05_PREREGISTRATION.md",
    "experiments/q05/Q05_COMPONENT_EXPOSURE_CONTRACT.md",
    "docs/validation/q01/REGULATORY_REVIEW_PACKET.md",
    "docs/validation/q01/COUNSEL_COVER_NOTE.md",
    "docs/validation/q02/DATA_USE_PROFILE_PACKET.md",
    "docs/validation/q02/PROVIDER_INQUIRY_TEMPLATE.md",
    "docs/validation/MK0_EXTERNAL_HANDOFF_READINESS.md",
    "docs/quant/MARKET_DOMAIN_FOUNDATION.md",
    "mining-site/market/2026-09-21-course-synthesis.md",
    "mining-site/external/2026-09-17-public-source-refresh.md",
    "mining-site/competitors/2026-09-17-tradingview-comparator-snapshot.md",
]

def require(name: str, condition: bool) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {name}")
    print(f"PASS: {name}")

for rel in REQUIRED:
    require(f"required artifact {rel}", (ROOT / rel).is_file())

q00 = (ROOT / "experiments/q00/Q00_PREREGISTRATION.md").read_text(encoding="utf-8")
q03 = (ROOT / "experiments/q03/Q03_PREREGISTRATION.md").read_text(encoding="utf-8")
q04_receipt = (ROOT / "experiments/q04/Q04_DRY_RUN_RECEIPT.md").read_text(encoding="utf-8")
q05 = (ROOT / "experiments/q05/Q05_PREREGISTRATION.md").read_text(encoding="utf-8")
status = (ROOT / "docs/validation/MK0_EXECUTION_STATUS.md").read_text(encoding="utf-8")
prototype = (ROOT / "experiments/research-prototype-v1/index.html").read_text(encoding="utf-8")
public_refresh = (ROOT / "mining-site/external/2026-09-17-public-source-refresh.md").read_text(encoding="utf-8")
market_foundation = (ROOT / "docs/quant/MARKET_DOMAIN_FOUNDATION.md").read_text(encoding="utf-8")
market_checklist = (ROOT / "experiments/q00/Q00_MARKET_SCENARIO_REVIEW_CHECKLIST.md").read_text(encoding="utf-8")
market_audit = (ROOT / "experiments/q00/Q00_MARKET_SCENARIO_AUDIT_V1.md").read_text(encoding="utf-8")
scenario_domain_map = json.loads((ROOT / "experiments/q00/Q00_SCENARIO_DOMAIN_MAP.json").read_text(encoding="utf-8"))

require("Q00 remains DRAFT", "status: DRAFT" in q00)
require("Q00 candidate sample plan bound", "target_sample_size: 84" in q00 and "minimum_usable_sample: 70" in q00)
require("Q00 seven-arm prototype", all(f'data-arm="{arm}"' in prototype for arm in "ABCDEFG"))
require("Q00 transfer mode", "unassisted_transfer" in prototype and "SYN-05" in prototype)
require("Q00 eight scenarios", all(f"SYN-0{i}" in prototype for i in range(1, 9)))
require("prototype v2.3", "research-prototype-v2.3.0" in prototype)
require("Q03 runbook bound", "Q03_14_DAY_RUNBOOK.md" in q03)
require("Q04 synthetic receipt remains inconclusive", "INCONCLUSIVE / DRY_RUN_ONLY / NOT_PROMOTABLE" in q04_receipt)
require("Q05 exposure contract bound", "Q05_COMPONENT_EXPOSURE_CONTRACT.md" in q05)
require("MK0 remains blocked", "MK0_PROMOTION: BLOCKED" in status and "MK1_PRODUCTION_IMPLEMENTATION: NOT_AUTHORIZED" in status)
require("public refresh cannot promote", "PUBLIC_PRECHECK_ONLY / NOT_EXTERNAL_AUTHORITY / NOT_PROMOTABLE" in public_refresh)
require("market domain separates price from value", "Price is not value" in market_foundation or "Price is not value" in market_foundation.title())
require("market scenario QA rejects disguised signals", "controlled reasoning instrument, not a disguised signal" in market_checklist)
require("market scenario audit ready for R2", "INTERNAL_QA_PASS / READY_FOR_R2" in market_audit)
require("prototype separates neutral context from votes", "Contexto no direccional" in prototype and "no es una puntuación" in prototype)

valid_evidence_classes = {
    "FUNDAMENTAL","VALUATION","PRICE","MOMENTUM","VOLUME","VOLATILITY","LIQUIDITY",
    "BREADTH","MACRO","EVENT","POSITIONING","PORTFOLIO","EXECUTION","PROVENANCE",
}
scenario_rows = scenario_domain_map.get("scenarios", [])
require("scenario domain map version matches prototype", scenario_domain_map.get("prototype_version") == "research-prototype-v2.3.0")
require("scenario domain map covers exactly SYN-01..08", {r.get("scenario_id") for r in scenario_rows} == {f"SYN-0{i}" for i in range(1,9)})
require("every scenario maps seven raw facts", all(len(r.get("raw_fact_map", [])) == 7 for r in scenario_rows))
require("scenario map evidence classes are canonical", all(
    fact.get("evidence_class") in valid_evidence_classes
    for row in scenario_rows for fact in row.get("raw_fact_map", [])
))
require("scenario map has explicit independence groups", all(
    bool(fact.get("independence_group"))
    for row in scenario_rows for fact in row.get("raw_fact_map", [])
))
require("scenario map has no hidden leverage", all(row.get("leverage") == "NONE" for row in scenario_rows))
require("SYN-06 is execution-only", any(
    row.get("scenario_id") == "SYN-06" and row.get("decision_context") == "EXECUTION_ONLY" and row.get("execution_relevance") == "PRIMARY"
    for row in scenario_rows
))

g_sheet = (ROOT / "experiments/q00/Q00_G_COMPARATOR_FREEZE_SHEET.md").read_text(encoding="utf-8")
q01_cover = (ROOT / "docs/validation/q01/COUNSEL_COVER_NOTE.md").read_text(encoding="utf-8")
q02_inquiry = (ROOT / "docs/validation/q02/PROVIDER_INQUIRY_TEMPLATE.md").read_text(encoding="utf-8")

require("G comparator remains explicitly unfrozen", "NOT_FROZEN" in g_sheet and "INDEPENDENT_REVIEW_REQUIRED" in g_sheet)
require("Q01 still requires external authority", "EXTERNAL" in q01_cover or "counsel" in q01_cover.lower())
require("Q02 still requires provider authority", "PROVIDER AUTHORITY REQUIRED" in q02_inquiry)

generator_path = ROOT / "experiments/q00/generate_assignment.py"
spec = importlib.util.spec_from_file_location("q00_assignment", generator_path)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

seqs = module.williams_sequences()
module.validate_sequences(seqs)
rows = module.make_assignments(84, 20260917)
module.validate_assignments(rows, 84)

seq_counts = Counter(
    r["sequence_id"]
    for r in rows
    if r["order_index"] == 1
)
require("84 participants create 6 per Williams sequence", set(seq_counts.values()) == {6} and len(seq_counts) == 14)

transfer_rows = [r for r in rows if r["task_type"] == "TRANSFER"]
prior = Counter(r["prior_F_exposure"] for r in transfer_rows)
require("transfer prior-F balance is 42/42", prior[True] == 42 and prior[False] == 42)

arm_counts = Counter(r["arm_id"] for r in rows if r["task_type"] == "ARM")
require("every arm has 84 observations at target N", set(arm_counts.values()) == {84} and len(arm_counts) == 7)

print("MK0 external-handoff integrity: PASS")
