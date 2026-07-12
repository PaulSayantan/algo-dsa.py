"""Tests for the git-backed ``submit`` / ``revise`` / ``revisit`` commands.

Everything here runs against a *throwaway* git repository built in ``tmp_path``
with a single fake problem, so no test can commit to or mutate the real corpus.
The workspace-root lookup (anchored to the ``dsa`` package location) is
monkeypatched in every module that captured it, redirecting the whole CLI at the
temp workspace.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from dsa import cli, revision, vcs

# --- fixtures ---------------------------------------------------------------

_STUB = '''\
def add(a, b):
    """Return a + b."""
    # TODO: implement
    pass


if __name__ == "__main__":
    print(add(1, 2))  # expected: 3
    print(add(5, 7))  # expected: 12
'''

_CORRECT = _STUB.replace("    # TODO: implement\n    pass", "    return a + b")
_WRONG = _STUB.replace("    # TODO: implement\n    pass", "    return 0")

# An implemented solution whose only cases are non-deterministic (prose "# e.g."
# comments, no `# expected:` marker) — grades as ok=True with 0 verifiable cases.
_NONDET = '''\
import random


def pick(n):
    """Return a random int in [0, n)."""
    return random.randrange(n)


if __name__ == "__main__":
    print(pick(10))  # e.g. some int in [0, 10)
    print(pick(5))  # e.g. some int in [0, 5)
'''

_PROBLEM_ID = "arrays/beginner/toy-add/problem-01-add"
# Path of the solution.py relative to the git top level (includes ``problems/``).
_SOLUTION_REL = f"problems/{_PROBLEM_ID}/solution.py"


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True)


@pytest.fixture()
def workspace(tmp_path, monkeypatch):
    """A temp git repo containing one fake problem whose solution.py is a stub.

    Yields ``(root, solution_py)``. The stub is committed (its first-add blob is
    thus the pristine template), and every module's ``workspace_root`` is pointed
    here so ``cli.main([...])`` operates entirely inside the temp repo.
    """
    root = tmp_path.resolve()
    prob_dir = root / "problems" / "arrays" / "beginner" / "toy-add" / "problem-01-add"
    prob_dir.mkdir(parents=True)
    solution_py = prob_dir / "solution.py"
    solution_py.write_text(_STUB, encoding="utf-8")
    (prob_dir / "PROBLEM.md").write_text("# Add\n\nAdd two numbers.\n", encoding="utf-8")
    (prob_dir / "SOLUTION.md").write_text("## Optimal\n\n```python\ndef add(a, b):\n    return a + b\n```\n", encoding="utf-8")

    _git(root, "init", "-q")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "user.name", "Test")
    _git(root, "config", "commit.gpgsign", "false")
    _git(root, "add", "-A")
    _git(root, "commit", "-qm", "seed corpus")

    for mod in (cli, revision, __import__("dsa.discovery", fromlist=["x"])):
        monkeypatch.setattr(mod, "workspace_root", lambda *a, **k: root, raising=False)

    return root, solution_py


def _run(argv):
    return cli.main(argv)


def _head_message(root: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(root), "log", "-1", "--format=%B"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def _tracked_content(root: Path, rel: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), "show", f"HEAD:{rel}"],
        capture_output=True, text=True, check=True,
    ).stdout


# --- vcs --------------------------------------------------------------------


def test_first_add_blob_returns_pristine_stub(workspace):
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")  # learner edits it
    blob = vcs.first_add_blob(root, solution_py)
    assert blob == _STUB  # the *first* committed content, not the working tree


def test_path_differs_from_head_detects_edits(workspace):
    root, solution_py = workspace
    assert not vcs.path_differs_from_head(root, solution_py)
    solution_py.write_text(_CORRECT, encoding="utf-8")
    assert vcs.path_differs_from_head(root, solution_py)


def test_vcs_helpers_work_when_root_is_subdir_of_repo(tmp_path):
    # Reference-frame regression: the corpus/workspace root is a *subdirectory* of
    # a larger git repo (root != git toplevel). All pathspec-bearing git commands
    # must anchor at the toplevel so blob/status/commit stay consistent.
    repo = tmp_path.resolve()
    ws = repo / "corpus"  # workspace root nested one level down
    prob_dir = ws / "problems" / "arrays" / "beginner" / "toy-add" / "problem-01-add"
    prob_dir.mkdir(parents=True)
    solution_py = prob_dir / "solution.py"
    solution_py.write_text(_STUB, encoding="utf-8")

    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "user.name", "Test")
    _git(repo, "config", "commit.gpgsign", "false")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-qm", "seed")

    # first_add_blob recovers the pristine stub even after an edit.
    solution_py.write_text(_CORRECT, encoding="utf-8")
    assert vcs.first_add_blob(ws, solution_py) == _STUB
    assert vcs.path_differs_from_head(ws, solution_py)

    # commit_path records the nested path correctly and only that file.
    sha = vcs.commit_path(ws, solution_py, "solve nested")
    assert sha
    changed = subprocess.run(
        ["git", "-C", str(repo), "show", "--name-only", "--format=", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    assert changed == ["corpus/problems/arrays/beginner/toy-add/problem-01-add/solution.py"]


def test_commit_path_commits_only_target(workspace):
    root, solution_py = workspace
    # Two dirty files; commit_path must record only the solution.py.
    other = root / "problems" / "arrays" / "beginner" / "toy-add" / "problem-01-add" / "PROBLEM.md"
    other.write_text("# Add (edited)\n", encoding="utf-8")
    solution_py.write_text(_CORRECT, encoding="utf-8")

    sha = vcs.commit_path(root, solution_py, "solve it")
    assert sha
    changed = subprocess.run(
        ["git", "-C", str(root), "show", "--name-only", "--format=", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    assert changed == [_SOLUTION_REL]
    # PROBLEM.md edit is still pending, not swept into the commit.
    assert vcs.path_differs_from_head(root, other)


def test_commit_path_noop_when_unchanged(workspace):
    root, solution_py = workspace
    assert vcs.commit_path(root, solution_py, "noop") is None


def test_path_differs_raises_on_failed_status(workspace):
    # A failed `git status` (e.g. corrupt index) must raise GitError, not return
    # False ("no difference") — which would make commit_path silently skip the commit
    # and cmd_submit report a false "already committed".
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")  # a genuine, uncommitted change
    (root / ".git" / "index").write_bytes(b"\x00corrupt-index")
    with pytest.raises(vcs.GitError):
        vcs.path_differs_from_head(root, solution_py)


# --- revision store ---------------------------------------------------------


def test_store_roundtrip_and_gitignored_location(workspace):
    root, _ = workspace
    revision.mark(_PROBLEM_ID, reason="manual", root=root)
    assert revision.is_marked(_PROBLEM_ID, root)
    assert revision.store_path(root) == root / ".dsa" / "revision.json"
    assert list(revision.list_marked(root)) == [_PROBLEM_ID]
    assert revision.unmark(_PROBLEM_ID, root)
    assert not revision.is_marked(_PROBLEM_ID, root)


def test_mark_zeroes_attempts(workspace):
    # Marking always coincides with a reset (fresh start), so the failed-attempt
    # counter is zeroed — this is what restarts the two-strike grace and prevents
    # a monotonic counter from re-resetting on every later single failure.
    root, _ = workspace
    revision.record_failed_attempt(_PROBLEM_ID, root=root)
    entry = revision.mark(_PROBLEM_ID, reason="manual", root=root)
    assert entry["attempts"] == 0


def test_reset_solution_restores_template(workspace):
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")
    revision.reset_solution(solution_py, root)
    assert solution_py.read_text(encoding="utf-8") == _STUB


def test_corrupt_store_recovers_gracefully(workspace):
    root, _ = workspace
    (root / ".dsa").mkdir()
    (root / ".dsa" / "revision.json").write_text("{not json", encoding="utf-8")
    assert revision.load(root)["problems"] == {}


# --- submit -----------------------------------------------------------------


def test_submit_stub_refuses(workspace, capsys):
    root, solution_py = workspace
    rc = _run(["submit", "-k", "toy-add"])
    assert rc == 2
    assert "STUB" in capsys.readouterr().out
    assert _head_message(root) == "seed corpus"  # nothing committed


def test_submit_pass_commits_with_timestamp(workspace, capsys):
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")
    rc = _run(["submit", "-k", "toy-add"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "PASS" in out and "committed" in out
    msg = _head_message(root)
    assert _PROBLEM_ID in msg and "Submitted" in msg
    # The committed blob is the correct solution.
    assert _tracked_content(root, _SOLUTION_REL) == _CORRECT


def test_submit_fail_once_records_attempt_no_reset(workspace, capsys):
    root, solution_py = workspace
    solution_py.write_text(_WRONG, encoding="utf-8")
    rc = _run(["submit", "-k", "toy-add"])
    assert rc == 1
    assert "FAIL" in capsys.readouterr().out
    # First failure: solution left intact, not yet marked for revision.
    assert solution_py.read_text(encoding="utf-8") == _WRONG
    assert not any(
        e.get("reason") != "pending"
        for e in revision.list_marked(root).values()
    )


def test_submit_fail_twice_marks_and_resets(workspace, capsys):
    root, solution_py = workspace
    solution_py.write_text(_WRONG, encoding="utf-8")
    assert _run(["submit", "-k", "toy-add"]) == 1
    solution_py.write_text(_WRONG, encoding="utf-8")  # fails again
    assert _run(["submit", "-k", "toy-add"]) == 1
    out = capsys.readouterr().out
    assert "marked for revision" in out
    # Reset to pristine template, and nothing committed.
    assert solution_py.read_text(encoding="utf-8") == _STUB
    assert revision.is_marked(_PROBLEM_ID, root)
    assert revision.list_marked(root)[_PROBLEM_ID]["reason"] == "failed-submit"
    assert _head_message(root) == "seed corpus"


def test_submit_pass_clears_pending_attempt(workspace):
    root, solution_py = workspace
    solution_py.write_text(_WRONG, encoding="utf-8")
    _run(["submit", "-k", "toy-add"])  # one failure -> pending counter
    solution_py.write_text(_CORRECT, encoding="utf-8")
    _run(["submit", "-k", "toy-add"])  # pass -> should clear pending entry
    assert not revision.is_marked(_PROBLEM_ID, root)


def test_submit_pass_graduates_marked_problem(workspace, capsys):
    # A problem manually marked for revision, then solved+submitted, should leave
    # the revision set (it's committed now) so `dsa revise` won't resurface it.
    root, solution_py = workspace
    revision.mark(_PROBLEM_ID, reason="manual", root=root)
    solution_py.write_text(_CORRECT, encoding="utf-8")
    assert _run(["submit", "-k", "toy-add"]) == 0
    assert "cleared from the revision set" in capsys.readouterr().out
    assert not revision.is_marked(_PROBLEM_ID, root)


def test_reset_zeroes_attempt_counter_restoring_grace(workspace):
    # Regression: after a fails-twice auto-reset, a single subsequent failure must
    # NOT immediately re-reset. The two-strike grace restarts because marking
    # (which always accompanies a reset) zeroes the attempts counter.
    root, solution_py = workspace

    # Two failures -> marked + reset to stub.
    solution_py.write_text(_WRONG, encoding="utf-8")
    _run(["submit", "-k", "toy-add"])
    solution_py.write_text(_WRONG, encoding="utf-8")
    _run(["submit", "-k", "toy-add"])
    assert solution_py.read_text(encoding="utf-8") == _STUB
    assert revision.list_marked(root)[_PROBLEM_ID]["attempts"] == 0

    # Learner reworks but fails ONCE more: counter is back to 1, no reset yet.
    solution_py.write_text(_WRONG, encoding="utf-8")
    assert _run(["submit", "-k", "toy-add"]) == 1
    assert revision.list_marked(root)[_PROBLEM_ID]["attempts"] == 1
    # Crucially, the learner's (wrong) work is preserved — NOT wiped to the stub.
    assert solution_py.read_text(encoding="utf-8") == _WRONG


def test_submit_ambiguous_target_errors(workspace, monkeypatch, capsys):
    root, solution_py = workspace
    # Add a second problem so an id substring matches two.
    d2 = root / "problems" / "arrays" / "beginner" / "toy-add" / "problem-02-add-again"
    d2.mkdir()
    (d2 / "solution.py").write_text(_CORRECT, encoding="utf-8")
    (d2 / "PROBLEM.md").write_text("# Add again\n", encoding="utf-8")
    (d2 / "SOLUTION.md").write_text("## Optimal\n```python\ndef add(a,b): return a+b\n```\n", encoding="utf-8")
    rc = _run(["submit", "-k", "add"])
    assert rc == 2
    assert "matches 2 problems" in capsys.readouterr().err


# --- revise / revisit ----------------------------------------------------


def test_revise_add_marks_and_resets(workspace, capsys):
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")
    rc = _run(["revisit", "-k", "toy-add"])
    assert rc == 0
    assert revision.is_marked(_PROBLEM_ID, root)
    assert revision.list_marked(root)[_PROBLEM_ID]["reason"] == "manual"
    assert solution_py.read_text(encoding="utf-8") == _STUB  # reset


def test_revise_lists_random_marked_in_category(workspace, capsys):
    root, _ = workspace
    revision.mark(_PROBLEM_ID, reason="manual", root=root)
    rc = _run(["revise", "arrays"])
    assert rc == 0
    out = capsys.readouterr().out
    assert _PROBLEM_ID in out


def test_revise_empty_category_is_clean(workspace, capsys):
    root, _ = workspace
    rc = _run(["revise", "strings"])
    assert rc == 0
    assert "no problems marked" in capsys.readouterr().out


def test_revise_singular_alias(workspace, capsys):
    root, _ = workspace
    revision.mark(_PROBLEM_ID, reason="manual", root=root)
    assert _run(["revise", "array"]) == 0  # singular alias -> arrays
    assert _PROBLEM_ID in capsys.readouterr().out


def test_revise_unknown_category_errors(workspace, capsys):
    root, _ = workspace
    assert _run(["revise", "bogus"]) == 2
    assert "unknown category" in capsys.readouterr().err


def test_revise_ignores_pending_only_entries(workspace, capsys):
    root, solution_py = workspace
    # A single failed submit creates a 'pending' entry that must NOT show up.
    solution_py.write_text(_WRONG, encoding="utf-8")
    _run(["submit", "-k", "toy-add"])
    assert _run(["revise", "arrays"]) == 0
    assert "no problems marked" in capsys.readouterr().out


# --- hardening: findings surfaced by the adversarial review -----------------


def test_submit_unverified_solution_not_committed_by_default(workspace, capsys):
    # An implemented solution with only non-deterministic cases passes 0 verifiable
    # cases (ok=True, passed=0). It must NOT commit silently as "passing".
    root, solution_py = workspace
    solution_py.write_text(_NONDET, encoding="utf-8")
    rc = _run(["submit", "-k", "toy-add"])
    assert rc == 2
    assert "UNVERIFIED" in capsys.readouterr().out
    assert _head_message(root) == "seed corpus"  # nothing committed


def test_submit_unverified_with_flag_commits(workspace, capsys):
    root, solution_py = workspace
    solution_py.write_text(_NONDET, encoding="utf-8")
    rc = _run(["submit", "-k", "toy-add", "--allow-unverified"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "PASS (unverified)" in out and "committed" in out
    assert "unverified" in _head_message(root)


def test_submit_infinite_loop_times_out_not_hangs(workspace, capsys):
    # A solution with an infinite loop must be graded in a bounded subprocess: it
    # surfaces as an ERROR (timeout) and nothing is committed, rather than hanging the
    # CLI forever. A short --timeout keeps the test fast.
    root, solution_py = workspace
    looping = _STUB.replace(
        "    # TODO: implement\n    pass", "    while True:\n        pass"
    )
    solution_py.write_text(looping, encoding="utf-8")
    rc = _run(["submit", "-k", "toy-add", "--timeout", "3"])
    assert rc == 1
    out = capsys.readouterr().out
    assert "ERROR" in out and "timeout" in out
    assert _head_message(root) == "seed corpus"  # nothing committed


def test_submit_category_alias_matches(workspace, capsys):
    # `--category array` (singular alias) must resolve like `revise array`, not
    # silently match zero problems.
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")
    rc = _run(["submit", "--category", "array", "-k", "toy-add"])
    assert rc == 0
    assert "PASS" in capsys.readouterr().out


def test_submit_resolves_path_to_solution_file(workspace, capsys):
    # A path pointing at the solution.py file itself (not the dir) resolves.
    root, solution_py = workspace
    solution_py.write_text(_CORRECT, encoding="utf-8")
    rc = _run(["submit", str(solution_py)])
    assert rc == 0
    assert "PASS" in capsys.readouterr().out


def test_revise_tolerates_non_dict_entry(workspace, capsys):
    # A hand-corrupted store whose entry value is not a dict must not crash
    # cmd_revise; load() sanitizes it away.
    root, _ = workspace
    (root / ".dsa").mkdir()
    (root / ".dsa" / "revision.json").write_text(
        '{"version": 1, "problems": {"arrays/x": "oops-not-a-dict"}}',
        encoding="utf-8",
    )
    assert revision.load(root)["problems"] == {}
    assert _run(["revise", "arrays"]) == 0
    assert "no problems marked" in capsys.readouterr().out
