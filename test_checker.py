#!/usr/bin/env python3
"""Tests for Drive Naming Checker. Run: python test_checker.py"""

from checker import validate_filename, check_prompt

PASS = [
    "2026-11-01_hairflip_mockup-deck.pptx",
    "2026-10-27_hard-rules.md",
    "2026-09-15_poundtown_blueprint.pdf",
]
FAIL = [
    "t01.png",
    "untitled.docx",
    "CATALOG_INDEX_2026-11-01.md",
    "SMS_BACKUP_v6.txt",
    "1f429c61-47f1-417d-9300-a26cc4a1f778.docx",
    "random-file-name-with-id-abc123def456.md",
]


def run():
    failed = 0
    for n in PASS:
        ok, reason = validate_filename(n)
        if not ok:
            print(f"FAIL (expected pass): {n} -> {reason}")
            failed += 1
        else:
            print(f"PASS: {n}")
    for n in FAIL:
        ok, reason = validate_filename(n)
        if ok:
            print(f"FAIL (expected block): {n}")
            failed += 1
        else:
            print(f"BLOCKED: {n} -> {reason}")
    if failed:
        print(f"\n{failed} test(s) failed")
        return 1
    print("\nAll tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
