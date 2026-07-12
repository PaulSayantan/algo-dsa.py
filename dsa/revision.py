"""Track which problems are marked for revision, and reset their solutions.

State lives in ``.dsa/revision.json`` at the workspace root (``.dsa/`` is already
git-ignored, so revision tracking never pollutes the corpus history). Shape::

    {
      "version": 1,
      "problems": {
        "<problem-id>": {
          "added_at": "2026-07-12T10:30:00",
          "reason": "manual" | "failed-submit",
          "attempts": 2
        },
        ...
      }
    }

``added_at`` is an ISO-8601 local timestamp. ``attempts`` is the running count of
failed ``dsa submit`` runs for that problem, used to implement the "fails twice ->
auto-revise + reset" rule. ``reason`` records how it entered the revision set.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

from . import vcs
from .discovery import workspace_root

STORE_VERSION = 1
_STORE_RELPATH = Path(".dsa") / "revision.json"


def _atomic_write(path: Path, text: str) -> None:
    """Write ``text`` to ``path`` atomically (temp file + ``os.replace``).

    ``Path.write_text`` opens in ``"w"`` mode, truncating the target *before* writing;
    an interrupted write (SIGINT, disk-full, power-loss) therefore leaves a truncated
    file. Writing to a sibling temp file and atomically renaming means ``path`` is
    always either its full old contents or its full new contents — never a partial.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except OSError:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def store_path(root: Optional[Path] = None) -> Path:
    """Absolute path to the revision store for ``root`` (default: workspace root)."""
    return (root or workspace_root()) / _STORE_RELPATH


def load(root: Optional[Path] = None) -> Dict:
    """Load the revision store, returning a fresh empty structure if absent/corrupt."""
    path = store_path(root)
    if not path.exists():
        return {"version": STORE_VERSION, "problems": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        # The store is disposable (git-ignored progress metadata), so we degrade to an
        # empty set rather than crash — but warn, because silently discarding an
        # existing-but-corrupt store would erase all revision markers with no trace.
        print(
            f"warning: revision store at {path} is unreadable/corrupt ({type(e).__name__}); "
            "starting from an empty set",
            file=sys.stderr,
        )
        return {"version": STORE_VERSION, "problems": {}}
    if not isinstance(data, dict) or "problems" not in data:
        return {"version": STORE_VERSION, "problems": {}}
    data.setdefault("version", STORE_VERSION)
    problems = data.get("problems")
    if not isinstance(problems, dict):
        data["problems"] = {}
        return data
    # Drop any entry whose value isn't a dict, so downstream ``entry.get(...)``
    # calls can't raise on a hand-corrupted store (load() promises tolerance).
    data["problems"] = {k: v for k, v in problems.items() if isinstance(v, dict)}
    return data


def save(data: Dict, root: Optional[Path] = None) -> None:
    """Persist ``data`` to the store, creating ``.dsa/`` on first write.

    Written atomically so an interrupted write can never truncate revision.json into
    invalid JSON — which :func:`load` would then silently discard, wiping the entire
    revision set.
    """
    path = store_path(root)
    _atomic_write(path, json.dumps(data, indent=2, sort_keys=True) + "\n")


def is_marked(problem_id: str, root: Optional[Path] = None) -> bool:
    """True if ``problem_id`` is currently in the revision set."""
    return problem_id in load(root)["problems"]


def list_marked(root: Optional[Path] = None) -> Dict[str, Dict]:
    """Return the ``{problem_id: entry}`` map of all problems marked for revision."""
    return dict(load(root)["problems"])


def _now_iso(now: Optional[datetime] = None) -> str:
    return (now or datetime.now()).replace(microsecond=0).isoformat()


def mark(
    problem_id: str,
    *,
    reason: str = "manual",
    root: Optional[Path] = None,
    now: Optional[datetime] = None,
) -> Dict:
    """Add ``problem_id`` to the revision set (idempotent) and return its entry.

    Marking always coincides with resetting the solution to its template (both
    the auto ``fails-twice`` path and ``revisit`` reset right after marking),
    so the failed-attempt counter is zeroed: a freshly-reset problem starts a new
    two-strike cycle. Without this, the monotonic counter would stay at/above the
    threshold and every *single* later failure would immediately re-reset the
    solution, destroying the learner's work with no grace.
    """
    data = load(root)
    entry = data["problems"].get(problem_id, {})
    entry["added_at"] = _now_iso(now)
    entry["reason"] = reason
    entry["attempts"] = 0
    data["problems"][problem_id] = entry
    save(data, root)
    return entry


def unmark(problem_id: str, root: Optional[Path] = None) -> bool:
    """Remove ``problem_id`` from the revision set. Returns True if it was present."""
    data = load(root)
    existed = data["problems"].pop(problem_id, None) is not None
    if existed:
        save(data, root)
    return existed


def record_failed_attempt(
    problem_id: str, *, root: Optional[Path] = None
) -> int:
    """Increment and persist the failed-submit counter for ``problem_id``.

    The entry is created lazily if the problem isn't tracked yet, so the counter
    survives across separate ``dsa submit`` invocations. Returns the new count.
    """
    data = load(root)
    entry = data["problems"].get(problem_id)
    if entry is None:
        # Not yet in the revision set: track the attempt count out-of-band so the
        # "fails twice" rule spans separate CLI invocations. Keep it out of the
        # active revision listing by flagging it pending.
        entry = {"attempts": 0, "reason": "pending", "added_at": _now_iso()}
    entry["attempts"] = int(entry.get("attempts", 0)) + 1
    data["problems"][problem_id] = entry
    save(data, root)
    return entry["attempts"]


class ResetError(Exception):
    """Raised when a solution.py cannot be reset to its pristine template."""


def reset_solution(solution_py: Path, root: Optional[Path] = None) -> None:
    """Restore ``solution.py`` to the pristine stub it was first committed as.

    Uses the blob from the commit that first added the file (see
    :func:`dsa.vcs.first_add_blob`), which for this corpus is the unimplemented
    template — so helper classes and the ``__main__`` oracle are preserved while
    the learner's solution is discarded.
    """
    root = root or workspace_root()
    blob = vcs.first_add_blob(root, solution_py)
    if blob is None:
        raise ResetError(
            f"cannot recover a pristine template for {solution_py} "
            "(no add-commit found in git history)"
        )
    # Write atomically and convert any IO failure into ResetError. A bare
    # write_text would truncate solution.py to 0 bytes before writing, so a mid-write
    # failure (disk full / read-only) would leave it empty *and* escape both callers'
    # `except ResetError` handlers as a raw traceback.
    try:
        _atomic_write(solution_py, blob)
    except OSError as e:
        raise ResetError(f"could not write template to {solution_py}: {e}") from e
