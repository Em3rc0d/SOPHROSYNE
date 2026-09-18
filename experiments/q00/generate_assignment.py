#!/usr/bin/env python3
"""Generate deterministic Q00 participant assignments.

Research-only. No participant identities should be placed in this file.
The formal run must freeze the seed and commit before outcome inspection.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from collections import Counter
from pathlib import Path

ARMS = list("ABCDEFG")
ARM_SCENARIOS = ["SYN-01", "SYN-02", "SYN-03", "SYN-04", "SYN-06", "SYN-07", "SYN-08"]
TRANSFER_SCENARIO = "SYN-05"

# First-order carryover-balanced Williams base for n=7.
BASE = [0, 1, 6, 2, 5, 3, 4]


def williams_sequences() -> list[list[str]]:
    seqs: list[list[str]] = []
    for shift in range(7):
        seqs.append([ARMS[(x + shift) % 7] for x in BASE])
    rev = list(reversed(BASE))
    for shift in range(7):
        seqs.append([ARMS[(x + shift) % 7] for x in rev])
    return seqs


def validate_sequences(seqs: list[list[str]]) -> None:
    assert len(seqs) == 14
    assert all(sorted(s) == ARMS for s in seqs)

    positions = Counter()
    transitions = Counter()
    arm_scenario = Counter()

    for sid, seq in enumerate(seqs, start=1):
        for pos, arm in enumerate(seq):
            positions[(pos, arm)] += 1
            arm_scenario[(arm, ARM_SCENARIOS[pos])] += 1
        for left, right in zip(seq, seq[1:]):
            transitions[(left, right)] += 1

    assert set(positions.values()) == {2}, positions
    assert len(transitions) == 42 and set(transitions.values()) == {2}, transitions
    assert len(arm_scenario) == 49 and set(arm_scenario.values()) == {2}, arm_scenario


def task_rows(sequence_id: int, arm_sequence: list[str]) -> list[dict]:
    rows: list[dict] = []
    # First seven Williams sequences get transfer immediately before F;
    # reversed seven get transfer immediately after F.
    transfer_before_f = sequence_id <= 7

    arm_tasks = [
        {
            "task_type": "ARM",
            "arm_id": arm,
            "scenario_id": ARM_SCENARIOS[pos],
            "prior_F_exposure": None,
        }
        for pos, arm in enumerate(arm_sequence)
    ]

    f_index = arm_sequence.index("F")
    insert_at = f_index if transfer_before_f else f_index + 1
    prior_f = not transfer_before_f
    arm_tasks.insert(
        insert_at,
        {
            "task_type": "TRANSFER",
            "arm_id": "T",
            "scenario_id": TRANSFER_SCENARIO,
            "prior_F_exposure": prior_f,
        },
    )

    for order_index, row in enumerate(arm_tasks, start=1):
        row["order_index"] = order_index
        row["sequence_id"] = f"W{sequence_id:02d}"
        row["assignment_locked"] = True
    return arm_tasks


def make_assignments(n: int, seed: int) -> list[dict]:
    if n < 1:
        raise ValueError("n must be >= 1")

    seqs = williams_sequences()
    validate_sequences(seqs)

    sequence_slots = [i for i in range(14) for _ in range((n + 13) // 14)]
    rng = random.Random(seed)
    rng.shuffle(sequence_slots)
    sequence_slots = sequence_slots[:n]

    assignments: list[dict] = []
    for participant_index, seq_idx in enumerate(sequence_slots, start=1):
        participant_id = f"P{participant_index:03d}"
        for row in task_rows(seq_idx + 1, seqs[seq_idx]):
            assignments.append({"participant_id": participant_id, **row})

    return assignments


def validate_assignments(rows: list[dict], n: int) -> None:
    by_p: dict[str, list[dict]] = {}
    for row in rows:
        by_p.setdefault(row["participant_id"], []).append(row)

    assert len(by_p) == n
    assert all(len(v) == 8 for v in by_p.values())

    for participant_rows in by_p.values():
        arms = [r["arm_id"] for r in participant_rows if r["task_type"] == "ARM"]
        assert sorted(arms) == ARMS
        transfers = [r for r in participant_rows if r["task_type"] == "TRANSFER"]
        assert len(transfers) == 1 and transfers[0]["scenario_id"] == TRANSFER_SCENARIO

    counts = Counter(r["sequence_id"] for r in rows if r["order_index"] == 1)
    if n % 14 == 0:
        assert len(set(counts.values())) == 1, counts


def write_outputs(rows: list[dict], output_dir: Path, seed: int, n: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "q00_assignments.csv"
    json_path = output_dir / "q00_assignments.json"
    manifest_path = output_dir / "q00_assignment_manifest.json"

    fields = [
        "participant_id",
        "sequence_id",
        "order_index",
        "task_type",
        "arm_id",
        "scenario_id",
        "prior_F_exposure",
        "assignment_locked",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    json_payload = json.dumps(rows, indent=2, sort_keys=True)
    json_path.write_text(json_payload + "\n", encoding="utf-8")

    digest = hashlib.sha256(json_payload.encode("utf-8")).hexdigest()
    manifest = {
        "schema_version": "q00-assignment-v1",
        "seed": seed,
        "participant_count": n,
        "williams_sequence_count": 14,
        "tasks_per_participant": 8,
        "arm_scenarios": ARM_SCENARIOS,
        "transfer_scenario": TRANSFER_SCENARIO,
        "assignment_sha256": digest,
        "note": "Freeze this seed, generator commit, and digest before first promotable participant.",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=84)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/q00"))
    args = parser.parse_args()

    rows = make_assignments(args.n, args.seed)
    validate_assignments(rows, args.n)
    write_outputs(rows, args.output_dir, args.seed, args.n)


if __name__ == "__main__":
    main()
