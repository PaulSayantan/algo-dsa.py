"""Minimum Width of a Convex Polygon (narrowest slab containing all points).

Intended technique: build the convex hull, then rotate calipers so that one line is
flush with each hull edge while a single antipodal pointer tracks the farthest vertex;
the minimum perpendicular distance over all edges is the width. Overall O(n log n).
"""
from typing import List, Tuple

Point = Tuple[float, float]


def minimum_width(points: List[Point]) -> float:
    """Return the minimum width (thinnest enclosing slab) of the point set.

    Args:
        points: List of (x, y) coordinates, length n >= 3, not all collinear.

    Returns:
        The smallest distance between two parallel lines that enclose every point,
        minimized over all orientations, as a float.

    Example:
        >>> round(minimum_width([(0, 0), (4, 0), (4, 2), (0, 2)]), 6)
        2.0
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(minimum_width([(0, 0), (4, 0), (4, 2), (0, 2)]))  # expected: 2.0
    print(minimum_width([(0, 0), (4, 0), (0, 3)]))          # expected: 2.4
