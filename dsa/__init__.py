"""dsa — toolkit for the DSA practice workspace.

Parses the workspace's existing 3-file contract (PROBLEM.md / solution.py /
SOLUTION.md), turns the `# expected:` oracle in each ``__main__`` block into
runnable test cases, grades a learner's solution against it, and self-verifies
the corpus by running the reference implementations extracted from SOLUTION.md.

Public entry points live in :mod:`dsa.cli`.
"""

from __future__ import annotations

__version__ = "0.1.0"
