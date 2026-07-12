---
name: dsa-security-review
description: Run a security and vulnerability review of the dsa workspace. Use when asked to do a security review, security check, vulnerability scan, audit the corpus for dangerous code, check dependencies for CVEs, or assess the arbitrary-code-execution / sandbox risk of the grader.
---

This workspace's security model is unusual and must be understood before
reviewing it: **the toolkit executes untrusted code on purpose.** `pytest` runs
every `solution.py`'s `__main__`, and `dsa verify` runs every SOLUTION.md
reference fence, through `exec`/`eval` ([dsa/executor.py:82](../../../dsa/executor.py#L82)
and [:203](../../../dsa/executor.py#L203)). The **only** containment is a
subprocess wall-clock timeout ([dsa/grader.py](../../../dsa/grader.py)) — there is
**no filesystem or network sandbox.** So the primary risk is not a classic
web-app vuln; it is *"whose code am I about to run, and what can it reach?"*

All paths are relative to the repo root. Use `.venv/bin/python`.

## The review, in order

### 1. Audit the executable corpus (the repo-specific check)

Any dangerous call committed into a `solution.py` or a SOLUTION.md reference runs
on the next `pytest`/`dsa verify`. Scan for it with the committed AST scanner
(it parses, never executes):

```bash
.venv/bin/python .claude/skills/dsa-security-review/scan_corpus.py
```

Current clean baseline (verified this session):

```
scanned 1380 solution.py + 1380 SOLUTION.md reference fence(s)
findings: 0 HIGH, 0 LOW (benign method calls)
OK: no HIGH-severity dangerous calls/imports in executable corpus content.
```

- **HIGH** = a bare `eval`/`exec`/`compile`/`__import__`, an `import` of
  `os`/`subprocess`/`socket`/`shutil`/`ctypes`/`urllib`/`pickle`/…, or a dotted
  sink on those modules (`os.system`, `subprocess.run`, `socket.connect`).
- **LOW** = an attribute call whose *name* is suspicious but receiver is benign
  (`list.remove`, `deque.remove`) — reported so you can eyeball, not block.
- Use in CI / pre-merge as a gate: `--strict` exits non-zero on any HIGH finding.
  `--show-low` lists the LOW sites.

The scanner has teeth — verified by planting `import os` / `import socket` /
`os.system(...)` / `eval(...)` in a temp problem (all flagged HIGH, `--strict`
exited 1) while a sibling `list.remove()` stayed LOW.

> Triage note from this repo: the only non-obvious real hits are benign. All
> `.remove(` calls are `list`/`set`/`deque.remove`; the single `import sys`
> ([tarjan-scc](../../../problems/stacks/advanced/tarjan-scc/problem-01-count-and-list-sccs/solution.py))
> is a legitimate `setrecursionlimit` bump, already `# noqa`'d. Neither is an
> `os`/`subprocess` import, so both are correctly *not* HIGH.

### 2. Confirm the sandbox boundary (know what "run the corpus" grants)

The grader gives executed code **full FS/network access**; only the timeout
contains it. Verified this session with a probe: a "solution" that did
`open(<tmpfile>, "w").write(...)` **succeeded** (arbitrary FS write), while a
`while True: pass` solution was **killed at the timeout** (`load_error='timeout
after 3.0s'`). Implications for any review:

- **Never run `pytest` / `dsa verify` / the driver on corpus content from an
  untrusted source (PR, fork, paste) without reading it first** — grading *is*
  code execution. Run `scan_corpus.py --strict` first; it does not execute.
- If stronger isolation is ever needed, the fix is a real sandbox around
  `grade_source_sandboxed` (seccomp/container/no-network), not more parsing.
  Document, don't silently assume containment.

### 3. Dependency vulnerabilities (CVEs)

Deps are tiny (`PyYAML` runtime; `pytest`/`ruff` dev). `pip-audit` isn't
preinstalled — install it into the venv and scan:

```bash
.venv/bin/python -m pip install -q pip-audit
.venv/bin/python -m pip_audit
# → No known vulnerabilities found   (verified this session)
```

### 4. Static bug/lint pass on the toolkit

Pyflakes catches the real code-smell bugs (unused/undefined names). Note the repo
lint is not fully clean; see the `dsa-toolkit-dev` skill for the baseline.

```bash
.venv/bin/ruff check dsa --select F,E9,S    # S = flake8-bandit-style security rules
# → Found 6 errors (all benign-by-design, verified this session — see below)
```

Expect **6 S-findings, none actionable**: `S311` ×2 (`random` used for
shuffling/sampling, never crypto), `S603`+`S607` (the `git` subprocess in
`dsa/vcs.py` — list args, no `shell=True`, stdin detached), and `S112` (a
`try/except/continue` in `dsa/cli.py`). The `exec`/`eval` sites do **not** appear
here — they are already annotated `# noqa: S102/S307` in `dsa/executor.py` as
intended design. A *new* S-finding outside these is worth reviewing.

### 5. Secret scan

No secrets belong in this repo (no services, no credentials). Confirm none crept
in (matches in CLI help text / comments are expected, not real secrets):

```bash
grep -rn -iE "(api[_-]?key|secret|password|-----BEGIN)" dsa/ build/gen/*.py conftest.py tests/ \
  | grep -viE "help=|#|\"\"\""    # → (no real secrets; verified clean this session)
```

## What is NOT a vulnerability here (don't file these)

- **`exec`/`eval` in `dsa/executor.py`.** It is the toolkit's entire purpose
  (grading arbitrary learner code). It is deliberately subprocess-isolated with a
  timeout and stdout/stderr silenced. Flag the *absence* of the timeout as a
  regression, not its presence.
- **`subprocess` in `dsa/vcs.py`.** All git calls pass an argument *list* (no
  `shell=True`), detach stdin (`DEVNULL`, so no hang on a credential prompt), and
  bound `commit` with a timeout. No shell-injection surface.
- **`# noqa: S102/S307`** on the exec/eval lines — intentional suppressions.

## Gotchas

- **Reviewing = reading, never running, untrusted content.** The one tool safe on
  unread code is `scan_corpus.py` (pure AST). Everything else executes it.
- **`pip-audit` needs network** (queries the PyPI advisory DB). Offline it errors;
  that's an environment limit, not a clean result — don't report "no vulns" if it
  couldn't reach the DB.
- **The scanner is name-based and deliberately conservative.** It flags `import
  os` even when unused; that's intended (an import in learner content is worth a
  human glance). Triage LOW/benign by hand rather than loosening it.
