"""Commando (APIO 2010).

Partition an array into consecutive squads maximizing the sum of
a*(squad_sum)^2 + b*(squad_sum) + c, with a < 0.
Solve with the maximization (upper-hull) Convex Hull Trick.
This is an EMPTY TEMPLATE: fill in the body yourself.
"""
from typing import List


def max_effectiveness(w: List[int], a: int, b: int, c: int) -> int:
    """Return the maximum total effectiveness over all consecutive partitions.

    A squad whose strengths sum to x contributes a*x*x + b*x + c. Partition all
    soldiers into consecutive squads to maximize the total. a is strictly negative.

    Args:
        w: Positive per-soldier strengths, length N (1 <= N <= 1e6).
        a: Quadratic coefficient, strictly negative (-5 <= a <= -1).
        b: Linear coefficient (|b| <= 1e7).
        c: Constant term (|c| <= 1e7).

    Returns:
        dp[N], the maximum total effectiveness.

    Example:
        >>> max_effectiveness([2, 2, 3, 4], -1, 10, -20)
        9
    """
    # TODO: implement using the Convex Hull Trick / Li Chao Tree
    pass


if __name__ == "__main__":
    # Expected output: 9
    print(max_effectiveness([2, 2, 3, 4], -1, 10, -20))
    # Expected output: 1
    print(max_effectiveness([1, 7, 6, 2, 1], -1, 10, -20))
