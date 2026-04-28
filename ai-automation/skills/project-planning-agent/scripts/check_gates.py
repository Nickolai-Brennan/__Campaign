#!/usr/bin/env python3
"""
check_gates.py — Checks gate checklist completion in docs/gates/.

Reads each checklist markdown file and counts checked vs unchecked items.
Reports which items are still unchecked and whether the gate can be passed.

Usage:
    python scripts/check_gates.py <project_docs_dir>

Example:
    python scripts/check_gates.py ./docs

Exits with code 0 if all gate items are checked.
Exits with code 1 if any gate items are unchecked.
"""

import sys
import re
from pathlib import Path

GATE_FILES = [
    "research-complete-checklist.md",
    "mvp-approval-checklist.md",
    "stack-approval-checklist.md",
    "build-readiness-checklist.md",
    "handoff-checklist.md",
]

CHECKED_PATTERN = re.compile(r"^\s*-\s*\[x\]", re.IGNORECASE)
UNCHECKED_PATTERN = re.compile(r"^\s*-\s*\[ \]")


def parse_checklist(filepath: Path) -> tuple[list[str], list[str]]:
    """Returns (checked_items, unchecked_items) from a markdown checklist file."""
    checked = []
    unchecked = []

    text = filepath.read_text(encoding="utf-8")
    for line in text.splitlines():
        if CHECKED_PATTERN.match(line):
            item = re.sub(r"^\s*-\s*\[x\]\s*", "", line, flags=re.IGNORECASE).strip()
            checked.append(item)
        elif UNCHECKED_PATTERN.match(line):
            item = re.sub(r"^\s*-\s*\[ \]\s*", "", line).strip()
            unchecked.append(item)

    return checked, unchecked


def check_gates(gates_dir: Path) -> dict:
    """Returns a results dict keyed by gate filename."""
    results = {}

    for gate_file in GATE_FILES:
        filepath = gates_dir / gate_file

        if not filepath.exists():
            results[gate_file] = {
                "status": "missing",
                "checked": [],
                "unchecked": [],
                "total": 0,
            }
            continue

        checked, unchecked = parse_checklist(filepath)
        total = len(checked) + len(unchecked)
        status = "pass" if unchecked == [] and total > 0 else ("empty" if total == 0 else "fail")

        results[gate_file] = {
            "status": status,
            "checked": checked,
            "unchecked": unchecked,
            "total": total,
        }

    return results


def print_results(results: dict) -> None:
    all_pass = all(r["status"] == "pass" for r in results.values())

    print(f"\n{'='*60}")
    print(f"  Project Planning Agent — Gate Checklist Report")
    print(f"{'='*60}\n")

    for gate_file, result in results.items():
        gate_name = gate_file.replace("-", " ").replace(".md", "").title()
        status = result["status"]

        if status == "missing":
            icon = "❌"
            label = "FILE MISSING"
        elif status == "empty":
            icon = "⚠️ "
            label = "NO ITEMS FOUND"
        elif status == "pass":
            icon = "✅"
            label = f"PASS ({result['total']}/{result['total']} checked)"
        else:
            done = len(result["checked"])
            total = result["total"]
            label = f"BLOCKED ({done}/{total} checked)"
            icon = "🚫"

        print(f"{icon} {gate_name}")
        print(f"   Status: {label}")

        if result["unchecked"]:
            print(f"   Unchecked items:")
            for item in result["unchecked"]:
                print(f"     - [ ] {item}")

        print()

    print(f"{'='*60}")
    if all_pass:
        print("  ✅ All gates passed — build handoff is cleared.\n")
    else:
        blocked = [f for f, r in results.items() if r["status"] != "pass"]
        print(f"  🚫 {len(blocked)} gate(s) not yet cleared — handoff is blocked.\n")


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <project_docs_dir>")
        print(f"Example: python {sys.argv[0]} ./docs")
        return 1

    docs_dir = Path(sys.argv[1]).resolve()
    gates_dir = docs_dir / "gates"

    if not docs_dir.exists():
        print(f"Error: docs directory not found: {docs_dir}")
        return 1

    if not gates_dir.exists():
        print(f"Error: gates directory not found: {gates_dir}")
        print(f"  Expected: {gates_dir}")
        print(f"  Run the planning agent through Phase 6 first.")
        return 1

    results = check_gates(gates_dir)
    print_results(results)

    all_pass = all(r["status"] == "pass" for r in results.values())
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
