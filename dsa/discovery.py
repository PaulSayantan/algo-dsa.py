"""Discover problem folders under ``problems/`` and build :class:`Problem`s."""

from __future__ import annotations

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
    category = parts[0]
    if category == "paradigms":
        difficulty_tier = ""
        algorithm = parts[1]
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
    """Yield every problem folder (one containing a ``solution.py``)."""
    root = root or workspace_root()
    problems_dir = root / "problems"
    for sol in sorted(problems_dir.rglob("solution.py")):
        yield _problem_from_dir(root, sol.parent)


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
        # A specific problem dir, or a parent dir containing several.
        matches = []
        for prob in iter_problems(root):
            if prob.path == target or target in prob.path.parents or prob.path == target:
                matches.append(prob)
        if matches:
            return matches
    return find_problems(root, query=path_or_id)
