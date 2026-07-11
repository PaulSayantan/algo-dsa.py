"""Minimum-Area Bounding Rectangle (smallest possibly-rotated enclosing rectangle).

Intended technique: build the convex hull, then rotate four calipers around it. For
each hull edge, project all hull vertices onto the edge direction and its normal to get
the rectangle width and height for that orientation; take the minimum area. With
monotone caliper pointers this is O(n log n).
"""
from typing import List, Tuple

Point = Tuple[float, float]


def minimum_area_rectangle(points: List[Point]) -> float:
    """Return the area of the smallest (possibly rotated) rectangle enclosing all points.

    Args:
        points: List of (x, y) coordinates, length n >= 1.

    Returns:
        The minimum enclosing-rectangle area as a float. Returns 0.0 when the points
        are collinear or there are fewer than 3 distinct points.

    Example:
        >>> round(minimum_area_rectangle([(0, 0), (4, 0), (4, 2), (0, 2)]), 6)
        8.0
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(minimum_area_rectangle([(1, 0), (0, 1), (-1, 0), (0, -1)]))   # expected: 2.0
    print(minimum_area_rectangle([(0, 0), (4, 0), (4, 2), (0, 2)]))     # expected: 8.0
