"""Farthest Pair of Points (Diameter of a Point Set).

Return the maximum SQUARED Euclidean distance between any two of the given points.

Intended technique: build the convex hull, then use rotating calipers to enumerate
antipodal pairs in linear time -> overall O(n log n).
"""
from typing import List, Tuple

Point = Tuple[int, int]


def farthest_pair_sq(points: List[Point]) -> int:
    """Return the largest squared distance between any two points.

    Args:
        points: List of (x, y) integer coordinates, length n >= 2, all distinct.

    Returns:
        The maximum value of (x_i - x_j)^2 + (y_i - y_j)^2 over all pairs i != j.

    Example:
        >>> farthest_pair_sq([(0, 0), (0, 1), (1, 0), (1, 1)])
        2
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(farthest_pair_sq([(0, 0), (0, 1), (1, 0), (1, 1)]))  # expected: 2
    print(farthest_pair_sq([(0, 0), (4, 0), (2, 3), (1, 1)]))  # expected: 16
