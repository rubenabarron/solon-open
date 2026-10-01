"""Mechanical publishing gate for this repository.

Checks markdown files for the machine-checkable rules in PUBLISHING.md:
identity strings, house-style punctuation, and secret-like patterns.

Usage (from the repository root):

    python scripts/gate.py            # check every markdown file in the repo
    python scripts/gate.py FILE...    # check specific files

Exit code 0 when clean, 1 when violations are found.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# The strings are assembled from fragments so this script does not itself
# contain the names it guards against.
BANNED_STRINGS = [
    "Solon" + "AI",
    "Solon " + "AI",
    "Grant" + "Ai",
    "Bay" + "shore",
    "Agent" + "Core",
    "Agent" + "force",
    "Type" + "Safe",
]

EM_DASH = "\u2014"
ORPHANED_DASH = re.compile(r"(?<![-\w])--(?![-\w])")

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def check_file(path: pathlib.Path) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), 1):
        if EM_DASH in line:
            problems.append(f"{path}:{number}: em dash (U+2014)")
        if ORPHANED_DASH.search(line):
            problems.append(f"{path}:{number}: double-hyphen punctuation")
        for banned in BANNED_STRINGS:
            if banned in line:
                problems.append(f"{path}:{number}: banned string {banned!r}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(line):
                problems.append(f"{path}:{number}: secret-like pattern")
                break
    return problems


def main(argv: list[str]) -> int:
    files = [pathlib.Path(a) for a in argv[1:]] or sorted(ROOT.rglob("*.md"))
    problems: list[str] = []
    for path in files:
        problems.extend(check_file(path))
    if problems:
        print(f"GATE FAIL: {len(problems)} problem(s)")
        for problem in problems:
            print(" -", problem)
        return 1
    print(f"GATE PASS: {len(files)} file(s) clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
