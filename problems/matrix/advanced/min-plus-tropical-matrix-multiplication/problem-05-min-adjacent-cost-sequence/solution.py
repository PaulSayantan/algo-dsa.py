"""Minimum-Cost Cyclic Schedule of Exactly L Operations.

Empty solution template. Fill in the body yourself.
"""

from typing import List

INF = float("inf")


def min_cost_cycle(
    c: int,
    cost: List[List[float]],
    L: int,
) -> int:
    """Return the min-cost cyclic schedule of exactly ``L`` operations.

    The DP transition "extend the schedule by one operation" is a min-plus /
    tropical matrix product of the cost matrix ``C``:
    ``(A ⊙ B)[i][j] = min_t (A[i][t] + B[t][j])``. A cyclic (closed) schedule of
    length ``L`` starting and ending in the same mode is captured by the
    **diagonal** of ``C^{⊙L}``, so the answer is
    ``min over i of (C^{⊙L})[i][i]``. Because ``L`` may be as large as
    ``10**18``, compute the tropical power by fast exponentiation (seed with the
    tropical identity: ``0`` diagonal, ``INF`` elsewhere). Return ``-1`` if every
    diagonal entry is ``INF``.

    Args:
        c: Number of machine modes, labeled ``0 .. c-1``.
        cost: ``c x c`` reconfiguration-cost matrix; ``cost[i][j]`` is the cost of
            changing mode ``i -> j`` or ``INF`` if impossible. Diagonal is ``INF``
            (no-op operations are disallowed).
        L: Exact number of operations in the cycle (``1 <= L <= 10**18``).

    Returns:
        Minimum total reconfiguration cost of a valid exactly-``L``-operation
        cycle, or ``-1`` if none exists.

    Example:
        >>> min_cost_cycle(3, [[INF, 4, 1], [2, INF, 3], [5, 1, INF]], 2)
        4
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    m = [[INF, 4, 1], [2, INF, 3], [5, 1, INF]]
    print(min_cost_cycle(3, m, 2))  # expected: 4
    print(min_cost_cycle(3, m, 3))  # expected: 4
    print(min_cost_cycle(3, m, 6))  # expected: 8
