"""Maximum Distance Between Two Convex Polygons.

Given two convex polygons (vertices CCW), find the largest distance between a vertex of
one and a vertex of the other.

Intended technique: rotating calipers with a pair of parallel supporting lines placed on
opposite sides of the two polygons; walk both pointers once around -> O(|P| + |Q|).
"""
from typing import List, Tuple

Point = Tuple[float, float]


def max_distance_between_polygons(P: List[Point], Q: List[Point]) -> float:
    """Return the maximum distance between any vertex of P and any vertex of Q.

    Args:
        P: Vertices of the first convex polygon in counter-clockwise order.
        Q: Vertices of the second convex polygon in counter-clockwise order.

    Returns:
        The maximum Euclidean distance between a point of P and a point of Q, as a float.

    Example:
        >>> round(max_distance_between_polygons(
        ...     [(0, 0), (1, 0), (1, 1), (0, 1)],
        ...     [(3, 0), (4, 0), (4, 1), (3, 1)]), 4)
        4.1231
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    p = [(0, 0), (1, 0), (1, 1), (0, 1)]
    q1 = [(3, 0), (4, 0), (4, 1), (3, 1)]
    q2 = [(5, 5), (6, 5), (6, 6), (5, 6)]
    print(max_distance_between_polygons(p, q1))  # expected: sqrt(17) ~= 4.123105625617661
    print(max_distance_between_polygons(p, q2))  # expected: sqrt(72) ~= 8.48528137423857
