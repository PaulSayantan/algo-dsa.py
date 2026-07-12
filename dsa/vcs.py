"""Thin, dependency-free git helpers used by ``dsa submit`` / ``dsa revise``.

Everything here shells out to ``git`` via ``git -C <root> ...`` so the calls work
regardless of the process's current working directory. The two capabilities the
rest of the toolkit needs are:

* **Recover a solution's pristine stub** — every ``solution.py`` in this corpus
  first entered git as an unimplemented template, so the blob from the commit
  that *added* the file is exactly that template (helper classes intact, the
  entrypoint empty). :func:`first_add_blob` returns it. This is the only faithful
  way to reset a file to "no solution": AST-stubbing would also wipe the provided
  ``ListNode``/``build`` harness helpers.
* **Commit a single file** — :func:`commit_path` stages and commits *only* the
  given path, leaving any other staged/working changes untouched.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List, Optional, Tuple


class GitError(Exception):
    """A git invocation failed (non-zero exit)."""


def _run(
    root: Path, args: List[str], *, check: bool = True, timeout: Optional[float] = None
) -> subprocess.CompletedProcess:
    """Run ``git -C <root> <args...>`` and capture text output.

    ``stdin`` is detached (``DEVNULL``) so git can never block indefinitely on an
    interactive prompt (a commit/gpg passphrase read from stdin, a hung hook awaiting
    input, a credential helper) — the CLI would otherwise freeze with no output since
    ``capture_output`` hides stderr. A per-call ``timeout`` (used on ``commit``, where
    a hook could hang) is surfaced as :class:`GitError`, the type callers already
    handle, rather than a raw ``TimeoutExpired`` traceback.
    """
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True,
            text=True,
            stdin=subprocess.DEVNULL,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        raise GitError(f"git {' '.join(args)} timed out after {timeout}s") from e
    if check and proc.returncode != 0:
        raise GitError(
            f"git {' '.join(args)} failed ({proc.returncode}): {proc.stderr.strip() or proc.stdout.strip()}"
        )
    return proc


def is_git_repo(root: Path) -> bool:
    """True if ``root`` is inside a git working tree."""
    proc = _run(root, ["rev-parse", "--is-inside-work-tree"], check=False)
    return proc.returncode == 0 and proc.stdout.strip() == "true"


def toplevel(root: Path) -> Path:
    """Absolute path of the git repository root containing ``root``."""
    proc = _run(root, ["rev-parse", "--show-toplevel"])
    return Path(proc.stdout.strip())


def _top_and_rel(root: Path, path: Path) -> Tuple[Path, str]:
    """Return ``(git_toplevel, path_relative_to_toplevel)``.

    All pathspec-bearing git commands are then run with ``-C <toplevel>`` so the
    ``-C`` cwd and the relative pathspec share one reference frame. Git resolves
    both pathspecs (``git log/status/add -- <p>``) and object paths
    (``git show <sha>:<p>``) relative to the invocation cwd/toplevel, so anchoring
    at the toplevel keeps them consistent even when the workspace root is a
    *subdirectory* of a larger repository (root != toplevel).
    """
    top = toplevel(root)
    rel = path.resolve().relative_to(top).as_posix()
    return top, rel


def first_add_blob(root: Path, path: Path) -> Optional[str]:
    """Return the file's content as it was first committed, or ``None``.

    Finds the earliest commit that added ``path`` (``--diff-filter=A --reverse``)
    and returns that blob via ``git show <sha>:<relpath>``. For this workspace
    that first blob is the pristine stub template, so restoring it removes any
    solution the learner has since written while preserving the template exactly.
    """
    top, rel = _top_and_rel(root, path)
    log = _run(
        top,
        ["log", "--diff-filter=A", "--reverse", "--format=%H", "--", rel],
        check=False,
    )
    if log.returncode != 0:
        return None
    shas = [line for line in log.stdout.splitlines() if line.strip()]
    if not shas:
        return None
    show = _run(top, ["show", f"{shas[0]}:{rel}"], check=False)
    if show.returncode != 0:
        return None
    return show.stdout


def path_differs_from_head(root: Path, path: Path) -> bool:
    """True if ``path``'s working-tree content differs from HEAD (or is untracked)."""
    top, rel = _top_and_rel(root, path)
    # `git status --porcelain` reports tracked modifications AND untracked files.
    # Distinguish a *failed* status (e.g. a corrupt index) from a genuinely clean tree:
    # both leave stdout empty, but treating a failure as "no difference" would make
    # commit_path silently skip the commit and report a false "already committed",
    # hiding the learner's uncommitted work. Surface the failure instead — cmd_submit
    # already catches GitError around commit_path.
    status = _run(top, ["status", "--porcelain", "--", rel], check=False)
    if status.returncode != 0:
        raise GitError(
            f"git status failed ({status.returncode}): "
            f"{status.stderr.strip() or status.stdout.strip()}"
        )
    return bool(status.stdout.strip())


def commit_path(root: Path, path: Path, message: str) -> Optional[str]:
    """Stage and commit *only* ``path``. Returns the new commit sha.

    Returns ``None`` (a no-op) when ``path`` already matches HEAD so there is
    nothing to commit. Other staged/working-tree changes are left untouched: the
    pathspec on ``git commit`` records just this one file.
    """
    top, rel = _top_and_rel(root, path)
    if not path_differs_from_head(root, path):
        return None
    _run(top, ["add", "--", rel])
    # commit can invoke pre-commit/commit-msg hooks; bound it so a hanging hook turns
    # into a GitError rather than freezing the CLI. The limit is generous so a slow-
    # but-progressing hook (e.g. a test suite) is not spuriously killed.
    _run(top, ["commit", "-m", message, "--", rel], timeout=120)
    head = _run(top, ["rev-parse", "HEAD"])
    return head.stdout.strip()
