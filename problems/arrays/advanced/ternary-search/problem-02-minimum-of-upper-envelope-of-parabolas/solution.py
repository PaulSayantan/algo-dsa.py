"""Minimum of the upper envelope of parabolas via continuous Ternary Search.

Fill in `min_of_upper_envelope` to return min_{x in [lo, hi]} max_i f_i(x),
where each f_i(x) = a_i * x^2 + b_i * x + c_i is convex.
"""

from typing import List


def min_of_upper_envelope(
    parabolas: List[List[float]], lo: float, hi: float
) -> float:
    """Minimize the convex upper envelope of parabolas over [lo, hi].

    g(x) = max_i (a_i * x^2 + b_i * x + c_i) is convex (max of convex functions),
    hence unimodal. Use ternary search on the real interval [lo, hi] to find the
    x that minimizes g, then return g at that x.

    Args:
        parabolas: List of [a_i, b_i, c_i] with a_i > 0.
        lo: Left end of the search interval (inclusive).
        hi: Right end of the search interval (inclusive), lo < hi.

    Returns:
        The minimum value of g(x) over x in [lo, hi], accurate to ~1e-6.

    Example:
        >>> round(min_of_upper_envelope([[1, -2, 1], [1, 2, 1]], -5, 5), 6)
        1.0
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(round(min_of_upper_envelope([[1, 0, 0]], -10, 10), 6))          # Expected: 0.0
    print(round(min_of_upper_envelope([[1, -2, 1], [1, 2, 1]], -5, 5), 6))  # Expected: 1.0
    print(round(min_of_upper_envelope([[1, 0, 0], [1, -8, 16]], 0, 4), 6))  # Expected: 4.0
