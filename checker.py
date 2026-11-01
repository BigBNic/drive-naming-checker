#!/usr/bin/env python3
"""Drive Naming Checker v1.0
Real-time gate: refuses to save any file whose name violates
YYYY-MM-DD_project-slug_plain-title.ext
Zero tolerance. Bad name = no save, blocker report only.
"""

import re
import sys
from datetime import datetime

PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}_[a-z0-9]+(-[a-z0-9]+)*_[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$"
)

ID_STRING = re.compile(r"[a-zA-Z0-9_-]{15,}")


def validate_filename(name: str) -> tuple[bool, str]:
    """Return (ok, reason). ok=False means BLOCK."""
    if not name or name.strip() != name:
        return False, "empty or padded name"
    if ID_STRING.search(name) and not re.match(r"^\d{4}-\d{2}-\d{2}_", name):
        # long letter-number combos that aren't a date prefix = ID leak
        if re.search(r"[a-zA-Z].*\d{4,}|\d{4,}.*[a-zA-Z]", name):
            if not re.match(r"^\d{4}-\d{2}-\d{2}_", name):
                return False, f"ID-string detected in filename: {name}"
    if not PATTERN.match(name):
        return False, (
            f"name does not match YYYY-MM-DD_project-slug_plain-title.ext: {name}"
        )
    # date must be plausible
    try:
        datetime.strptime(name[:10], "%Y-%m-%d")
    except ValueError:
        return False, f"invalid date prefix: {name[:10]}"
    return True, "clean"


def check_prompt(prompt: str, rules: list[str]) -> list[str]:
    """Score a bot prompt against hard rules. Returns list of violations."""
    hits = []
    lowered = prompt.lower()
    for rule in rules:
        # simple keyword gate; expand per rule type later
        key = rule.split()[0].lower() if rule.split() else ""
        if key and key not in lowered and rule.lower()[:20] not in lowered:
            # only flag if the rule's core subject is absent
            if any(w in lowered for w in rule.lower().split()[:3]):
                continue
            hits.append(f"rule not addressed: {rule[:80]}")
    return hits


def main():
    if len(sys.argv) < 2:
        print("usage: checker.py <filename> [prompt-text]")
        sys.exit(2)
    name = sys.argv[1]
    ok, reason = validate_filename(name)
    if not ok:
        print(f"BLOCK: {reason}")
        sys.exit(1)
    print(f"PASS: {name}")
    if len(sys.argv) > 2:
        violations = check_prompt(sys.argv[2], [])
        for v in violations:
            print(f"PROMPT-FLAG: {v}")
    sys.exit(0)


if __name__ == "__main__":
    main()
