"""Minimum Cost Path on a weighted grid (4-directional).

Fill in the body using Dijkstra's algorithm with a min-heap. Do not modify the
signature.
"""
from typing import List


def min_cost_path(grid: List[List[int]]) -> int:
    """Return the minimum sum-of-cells cost of a path from top-left to
    bottom-right, moving in the 4 orthogonal directions.

    The cost of a path is the sum of every visited cell's value, counting both
    the start cell (0, 0) and the destination cell (m-1, n-1).

    Args:
        grid: An m x n matrix of non-negative integer cell costs.

    Returns:
        The minimum achievable total path cost.

    Example:
        >>> min_cost_path([[1, 3, 1],
        ...                 [1, 5, 1],
        ...                 [4, 2, 1]])
        7
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(min_cost_path([[1, 3, 1],
                         [1, 5, 1],
                         [4, 2, 1]]))          # expected: 7
    print(min_cost_path([[1, 1, 1],
                         [9, 9, 1],
                         [1, 1, 1],
                         [1, 9, 9],
                         [1, 1, 1]]))          # expected: 11
    print(min_cost_path([[5]]))                # expected: 5
