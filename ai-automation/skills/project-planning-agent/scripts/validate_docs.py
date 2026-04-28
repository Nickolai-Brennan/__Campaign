#!/usr/bin/env python3
"""
validate_docs.py — Validates that all required planning documents exist and are non-empty.

Usage:
    python scripts/validate_docs.py <project_docs_dir>

Example:
    python scripts/validate_docs.py ./docs

Exits with code 0 if all required documents are present and non-empty.
Exits with code 1 if any required documents are missing or empty.
"""

import sys
import os
from pathlib import Path

REQUIRED_DOCS = {
    "root": [
        "00-project-summary.md",
    ],
    "research": [
        "market-research.md",
        "competitor-research.md",
        "user-research.md",
        "problem-research.md",
        "keyword-research.md",
        "monetization-research.md",
        "content-research.md",
        "technical-research.md",
        "opportunity-summary.md",
    ],
    "planning": [
        "project-brief.md",
        "project-proposal.md",
        "prd.md",
        "mvp-scope.md",
        "feature-list.md",
        "user-stories.md",
        "user-flows.md",
        "roadmap.md",
        "risk-checklist.md",
        "success-metrics.md",
    ],
    "organization": [
        "file-structure-plan.md",
        "tool-stack-options.md",
        "selected-stack.md",
        "task-breakdown.md",
        "milestone-plan.md",
        "roles-and-agents.md",
        "dependency-map.md",
        "build-order.md",
        "decision-log.md",
    ],
    "gates": [
        "research-complete-checklist.md",
        "mvp-approval-checklist.md",
        "stack-approval-checklist.md",
        "build-readiness-checklist.md",
        "handoff-checklist.md",
    ],
    "handoff": [
        "build-agent-handoff.md",
    ],
}

# Minimum number of non-whitespace characters for a document to be considered non-empty
MIN_CONTENT_CHARS = 50


def check_docs(docs_dir: Path) -> tuple[list[str], list[str], list[str]]:
    """Returns (missing, empty, ok) lists of document paths."""
    missing = []
    empty = []
    ok = []

    for folder, files in REQUIRED_DOCS.items():
        if folder == "root":
            base = docs_dir
        else:
            base = docs_dir / folder

        for filename in files:
            filepath = base / filename
            rel_path = str(filepath.relative_to(docs_dir.parent))

            if not filepath.exists():
                missing.append(rel_path)
            else:
                content = filepath.read_text(encoding="utf-8").strip()
                non_ws = len(content.replace("\n", "").replace(" ", "").replace("#", ""))
                if non_ws < MIN_CONTENT_CHARS:
                    empty.append(rel_path)
                else:
                    ok.append(rel_path)

    return missing, empty, ok


def print_results(missing: list[str], empty: list[str], ok: list[str]) -> None:
    total = len(missing) + len(empty) + len(ok)
    print(f"\n{'='*60}")
    print(f"  Project Planning Agent — Document Validation Report")
    print(f"{'='*60}")
    print(f"  Total expected: {total}")
    print(f"  ✅ Present and complete: {len(ok)}")
    print(f"  ⚠️  Present but empty/stub: {len(empty)}")
    print(f"  ❌ Missing: {len(missing)}")
    print(f"{'='*60}\n")

    if ok:
        print("✅ Complete documents:")
        for path in sorted(ok):
            print(f"   {path}")
        print()

    if empty:
        print("⚠️  Empty or stub documents (need content):")
        for path in sorted(empty):
            print(f"   {path}")
        print()

    if missing:
        print("❌ Missing documents (not yet created):")
        for path in sorted(missing):
            print(f"   {path}")
        print()


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <project_docs_dir>")
        print(f"Example: python {sys.argv[0]} ./docs")
        return 1

    docs_dir = Path(sys.argv[1]).resolve()

    if not docs_dir.exists():
        print(f"Error: docs directory not found: {docs_dir}")
        return 1

    if not docs_dir.is_dir():
        print(f"Error: path is not a directory: {docs_dir}")
        return 1

    missing, empty, ok = check_docs(docs_dir)
    print_results(missing, empty, ok)

    if missing or empty:
        issues = len(missing) + len(empty)
        print(f"Validation failed: {issues} document(s) need attention.\n")
        return 1

    print("All required documents are present and complete. Ready for handoff.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
