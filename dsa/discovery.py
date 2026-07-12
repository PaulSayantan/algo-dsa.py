"""Discover problem folders under ``problems/`` and build :class:`Problem`s."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Iterator, List, Optional

from .model import Problem


def workspace_root(start: Optional[Path] = None) -> Path:
    """Locate the workspace root (the dir containing ``problems/``).

    Walks up from ``start`` (or this file) until a ``problems`` directory is
    found, so the toolkit works regardless of the current working directory.
    """
    here = (start or Path(__file__)).resolve()
    for parent in [here, *here.parents]:
        if (parent / "problems").is_dir():
            return parent
    # Fallback: two levels up from dsa/discovery.py -> repo root.
    return Path(__file__).resolve().parents[1]


def _problem_from_dir(root: Path, d: Path) -> Problem:
    rel = d.relative_to(root / "problems")
    parts = rel.parts  # e.g. ("arrays","beginner","linear-search","problem-01-...")
    if not parts:
        # A solution.py directly under problems/ (rel == ".") has no category segment;
        # reject it so callers can skip rather than crash with IndexError.
        raise ValueError(f"not a problem directory (no category segment): {d}")
    category = parts[0]
    if category == "paradigms":
        difficulty_tier = ""
        # paradigms/ nests one level shallower (no difficulty tier), but a solution.py
        # sitting directly in problems/paradigms/ still has no algorithm segment; guard
        # it the same way the else-branch already guards its deeper indices.
        algorithm = parts[1] if len(parts) > 1 else ""
        slug = parts[-1]
    else:
        difficulty_tier = parts[1] if len(parts) > 1 else ""
        algorithm = parts[2] if len(parts) > 2 else ""
        slug = parts[-1]
    return Problem(
        id=str(rel),
        path=d,
        category=category,
        difficulty_tier=difficulty_tier,
        algorithm=algorithm,
        slug=slug,
    )


def iter_problems(root: Optional[Path] = None) -> Iterator[Problem]:
    """Yield every problem folder (one containing a ``solution.py``).

    Uses ``os.walk`` with an ``onerror`` callback (rather than ``Path.rglob``, which
    silently swallows ``PermissionError``/``OSError``) so an unreadable subtree is
    reported to stderr instead of quietly dropping problems — a full-corpus scan must
    not print "Verified N" while some problems were never enumerated. A directory that
    can't be parsed into a Problem is skipped with a warning rather than aborting the
    whole walk.
    """
    root = root or workspace_root()
    problems_dir = root / "problems"

    def _onerror(err: OSError) -> None:
        print(f"warning: skipping unreadable path during discovery: {err}", file=sys.stderr)

    found: List[Path] = []
    # followlinks=False preserves the previous rglob behavior of not descending symlinks.
    for dirpath, _dirs, files in os.walk(problems_dir, onerror=_onerror, followlinks=False):
        if "solution.py" in files:
            found.append(Path(dirpath))
    for d in sorted(found):
        try:
            yield _problem_from_dir(root, d)
        except ValueError as err:
            print(f"warning: skipping malformed problem directory: {err}", file=sys.stderr)


def find_problems(
    root: Optional[Path] = None,
    *,
    category: Optional[str] = None,
    algorithm: Optional[str] = None,
    difficulty_tier: Optional[str] = None,
    query: Optional[str] = None,
) -> List[Problem]:
    """Return problems filtered by category / algorithm / tier / id-substring."""
    out: List[Problem] = []
    for p in iter_problems(root):
        if category and p.category != category:
            continue
        if algorithm and p.algorithm != algorithm:
            continue
        if difficulty_tier and p.difficulty_tier != difficulty_tier:
            continue
        if query and query.lower() not in p.id.lower():
            continue
        out.append(p)
    return out


def resolve(path_or_id: str, root: Optional[Path] = None) -> List[Problem]:
    """Resolve a filesystem path or an id-substring to matching problems."""
    root = root or workspace_root()
    p = Path(path_or_id)
    if p.exists():
        target = p.resolve()
        # A path to a file (e.g. the solution.py itself) resolves to its problem
        # directory, so `dsa submit .../problem-.../solution.py` works too.
        if target.is_file():
            target = target.parent
        # A specific problem dir, or a parent dir containing several.
        matches = []
        for prob in iter_problems(root):
            if prob.path == target or target in prob.path.parents:
                matches.append(prob)
        if matches:
            return matches
    return find_problems(root, query=path_or_id)
