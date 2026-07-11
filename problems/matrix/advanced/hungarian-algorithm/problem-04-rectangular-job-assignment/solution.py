"""Rectangular Job Assignment (n workers, m jobs, n <= m) — empty template.

Pad the rectangular cost matrix to a square with dummy zero-cost worker rows
(or use an n<=m Hungarian variant), then run the Hungarian Algorithm to
minimize total cost. Do NOT hard-code answers.
"""

from typing import List


def min_rectangular_assignment(cost: List[List[int]]) -> int:
    """Return the minimum total cost of assigning each worker a distinct job.

    Args:
        cost: An ``n x m`` matrix (``n <= m``) where ``cost[i][j]`` is the cost
            of assigning worker ``i`` to job ``j``. Every worker must receive a
            distinct job; leftover jobs (when ``m > n``) are unassigned and free.

    Returns:
        The minimum achievable sum of costs over all valid assignments of the
        ``n`` workers to distinct jobs.

    Example:
        >>> min_rectangular_assignment([[9, 2, 7], [6, 4, 3]])
        5
    """
    # TODO: implement.
    #   - pad to a square m x m matrix with dummy zero rows, or
    #   - run an n<=m Hungarian variant directly.
    pass


if __name__ == "__main__":
    print(min_rectangular_assignment([[9, 2, 7],
                                       [6, 4, 3]]))  # Expected: 5

    print(min_rectangular_assignment([[8, 4, 7, 1],
                                      [5, 2, 3, 9]]))  # Expected: 3
