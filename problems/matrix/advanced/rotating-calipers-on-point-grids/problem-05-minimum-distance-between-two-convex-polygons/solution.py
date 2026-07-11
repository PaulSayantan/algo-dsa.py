"""Minimum Distance Between Two Convex Polygons.

Given two disjoint convex polygons (vertices CCW), find the closest distance between
them (the closest pair may involve edge interiors, so measure segment-to-segment).

Intended technique: rotating calipers with co-parallel supporting lines walked once
around both hulls, taking segment-to-segment distances -> O(|P| + |Q|).
"""
from typing import List, Tuple

Point = Tuple[float, float]


def min_distance_between_polygons(P: List[Point], Q: List[Point]) -> float:
    """Return the minimum distance between two disjoint convex polygons.

    Args:
        P: Vertices of the first convex polygon in counter-clockwise order.
        Q: Vertices of the second convex polygon in counter-clockwise order.

    Returns:
        The smallest Euclidean distance between any point of P and any point of Q,
        as a float. (0.0 if the polygons touch or overlap.)

    Example:
        >>> round(min_distance_between_polygons(
        ...     [(0, 0), (1, 0), (1, 1), (0, 1)],
        ...     [(3, 0), (4, 0), (4, 1), (3, 1)]), 6)
        2.0
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    p = [(0, 0), (1, 0), (1, 1), (0, 1)]
    q1 = [(3, 0), (4, 0), (4, 1), (3, 1)]
    q2 = [(5, 5), (6, 5), (6, 6), (5, 6)]
    print(min_distance_between_polygons(p, q1))  # expected: 2.0
    print(min_distance_between_polygons(p, q2))  # expected: sqrt(32) ~= 5.656854249492381
