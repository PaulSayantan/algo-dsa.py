"""Closest approach of two points moving at constant velocity, via Ternary Search.

Fill in `closest_approach` to return the minimum Euclidean distance between the
two points over the time window [0, T].
"""

from typing import Tuple

Point = Tuple[float, float]


def closest_approach(
    a: Point, va: Point, b: Point, vb: Point, T: float
) -> float:
    """Minimum distance between two constant-velocity points over [0, T].

    Positions at time t are A(t) = a + va*t and B(t) = b + vb*t. The squared
    distance d(t)^2 is a convex quadratic in t, so d(t) is unimodal on [0, T].
    Ternary-search the time interval for the minimizer.

    Args:
        a: Start position of point A, (ax, ay).
        va: Velocity of point A, (vax, vay).
        b: Start position of point B, (bx, by).
        vb: Velocity of point B, (vbx, vby).
        T: End of the time window (t ranges over [0, T]).

    Returns:
        The minimum Euclidean distance |A(t) - B(t)| over t in [0, T],
        accurate to ~1e-6.

    Example:
        >>> round(closest_approach((0, 0), (1, 0), (0, 10), (0, -1), 10), 6)
        7.071068
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(round(closest_approach((0, 0), (1, 0), (10, 0), (-1, 0), 10), 6))  # Expected: 0.0
    print(round(closest_approach((0, 0), (0, 1), (5, 0), (0, 1), 10), 6))    # Expected: 5.0
    print(round(closest_approach((0, 0), (1, 0), (0, 10), (0, -1), 10), 6))  # Expected: 7.071068
