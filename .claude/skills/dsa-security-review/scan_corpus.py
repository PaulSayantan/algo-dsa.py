#!/usr/bin/env python3
"""Static audit of the *executable* corpus content for dangerous calls/imports.

Why this exists: the toolkit runs untrusted code by design. `pytest` executes
every `solution.py`'s `__main__`, and `dsa verify` executes every SOLUTION.md
reference fence — with **no filesystem/network sandbox**, only a wall-clock
timeout (see dsa/executor.py:82 exec / :203 eval, dsa/grader.py timeout). So a
rogue `os.system(...)` or `import socket` committed into the corpus would run on
the next `pytest`/`dsa verify`. This scanner is the cheap pre-exec tripwire.

It parses each file with `ast` (never imports/executes them) and flags calls to
known sinks and imports of dangerous modules. It is intentionally noisy on
*names* and leaves triage to a human: `list.remove()` and `os.remove()` both
surface as `remove`, so the report separates attribute-calls (usually benign
method calls like `deque.remove`) from bare-name calls (`eval(...)`,
`exec(...)`) and dotted os/subprocess calls (`os.system`, the real risk).

Usage (from repo root):

    .venv/bin/python .claude/skills/dsa-security-review/scan_corpus.py
    .venv/bin/python .claude/skills/dsa-security-review/scan_corpus.py --strict   # exit 1 on any HIGH finding

Exit code: 0 if no HIGH-severity findings (or not --strict); 1 if --strict and
any HIGH finding (a bare eval/exec/compile, or an os/subprocess/socket sink).
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROBLEMS = ROOT / "problems"

# Bare-name calls that are always dangerous regardless of receiver.
NAME_SINKS = {"eval", "exec", "compile", "__import__"}
# Dotted attribute calls that are dangerous only on os/subprocess/shutil/etc.
DANGER_ATTR = {"system", "popen", "spawn", "spawnl", "spawnv", "rmtree", "unlink",
               "fork", "kill", "execv", "execve", "call", "run", "Popen",
               "check_output", "check_call", "connect", "urlopen", "loads"}
# Modules whose mere import is worth flagging in learner content.
DANGER_MODS = {"os", "subprocess", "socket", "shutil", "ctypes", "requests",
               "urllib", "pickle", "marshal", "http", "ftplib", "telnetlib"}
# Modules that are legitimately used in DSA solutions (don't flag their import).
BENIGN_MODS = {"sys"}  # e.g. sys.setrecursionlimit in Tarjan SCC — noqa'd upstream

FENCE = re.compile(r"```python\n(.*?)```", re.S)


class Finding:
    __slots__ = ("path", "line", "kind", "detail", "severity")

    def __init__(self, path, line, kind, detail, severity):
        self.path, self.line, self.kind, self.detail, self.severity = (
            path, line, kind, detail, severity)


def scan_source(src: str, path: str, out: list) -> None:
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return
    for n in ast.walk(tree):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            if isinstance(n, ast.ImportFrom):
                mods = [n.module or ""]
            else:
                mods = [a.name for a in n.names]
            for mod in mods:
                base = mod.split(".")[0]
                if base in DANGER_MODS:
                    out.append(Finding(path, n.lineno, "import", f"import {mod}", "HIGH"))
        elif isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id in NAME_SINKS:
                out.append(Finding(path, n.lineno, "call", f"{f.id}()", "HIGH"))
            elif isinstance(f, ast.Attribute) and f.attr in DANGER_ATTR:
                recv = f.value.id if isinstance(f.value, ast.Name) else "?"
                sev = "HIGH" if recv in DANGER_MODS else "LOW"
                out.append(Finding(path, n.lineno, "call", f"{recv}.{f.attr}()", sev))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Audit corpus for dangerous calls/imports")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any HIGH finding")
    ap.add_argument("--show-low", action="store_true", help="list LOW findings too")
    args = ap.parse_args(argv)

    findings: list = []
    nsol = nref = 0
    for sp in sorted(PROBLEMS.rglob("solution.py")):
        nsol += 1
        scan_source(sp.read_text(encoding="utf-8", errors="replace"),
                    str(sp.relative_to(ROOT)), findings)
    for md in sorted(PROBLEMS.rglob("SOLUTION.md")):
        nref += 1
        text = md.read_text(encoding="utf-8", errors="replace")
        for m in FENCE.finditer(text):
            scan_source(m.group(1), str(md.relative_to(ROOT)), findings)

    highs = [f for f in findings if f.severity == "HIGH"]
    lows = [f for f in findings if f.severity == "LOW"]

    print(f"scanned {nsol} solution.py + {nref} SOLUTION.md reference fence(s)")
    print(f"findings: {len(highs)} HIGH, {len(lows)} LOW (benign method calls)")
    if lows:
        print("  LOW breakdown:", dict(Counter(f.detail for f in lows).most_common(10)))
    if highs:
        print("\nHIGH-severity sites (review each — these EXECUTE on pytest/dsa verify):")
        for f in highs:
            print(f"  {f.path}:{f.line}  {f.detail}")
    if args.show_low:
        print("\nLOW-severity sites:")
        for f in lows:
            print(f"  {f.path}:{f.line}  {f.detail}")

    if not highs:
        print("\nOK: no HIGH-severity dangerous calls/imports in executable corpus content.")
    return 1 if (args.strict and highs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
