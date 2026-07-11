"""Classic Assignment Problem — empty solution template.

Fill in `min_assignment_cost` using the Hungarian Algorithm (Kuhn-Munkres).
Do NOT hard-code answers; implement the general O(n^3) algorithm.
"""

from typing import List


def min_assignment_cost(cost: List[List[int]]) -> int:
    """Return the minimum total cost of a perfect worker-to-job assignment.

    Args:
        cost: An ``n x n`` matrix where ``cost[i][j]`` is the cost of assigning
            worker ``i`` to job ``j``. Every worker is matched to exactly one
            job and every job to exactly one worker.

    Returns:
        The minimum achievable sum of costs over all valid one-to-one
        assignments.

    Example:
        >>> min_assignment_cost([[3, 1, 2], [2, 3, 1], [1, 2, 3]])
        3
    """
    # TODO: implement using the Hungarian Algorithm (O(n^3)).
    pass


if __name__ == "__main__":
    sample = [[3, 1, 2],
              [2, 3, 1],
              [1, 2, 3]]
    print(min_assignment_cost(sample))  # Expected: 3

    sample2 = [[9, 11, 14],
               [6, 15, 13],
               [12, 13, 6]]
    print(min_assignment_cost(sample2))  # Expected: 23
