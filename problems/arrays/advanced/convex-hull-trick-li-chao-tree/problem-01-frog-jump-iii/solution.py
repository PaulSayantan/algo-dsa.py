"""Frog Jump III (AtCoder EDPC-Z).

Solve with the monotonic Convex Hull Trick.
This is an EMPTY TEMPLATE: fill in the body yourself.
"""
from typing import List


def min_total_cost(heights: List[int], c: int) -> int:
    """Return the minimum total cost for the frog to reach the last stone.

    The frog starts on stone 0 and may jump from stone i to any stone j > i,
    paying (heights[i] - heights[j])**2 + c. Heights are strictly increasing.

    Args:
        heights: Strictly increasing list of stone heights, length N (2 <= N <= 2e5).
        c: Non-negative per-jump constant (1 <= c <= 1e12).

    Returns:
        The minimum total cost to travel from stone 0 to stone N-1.

    Example:
        >>> min_total_cost([1, 2, 4, 5, 7], 6)
        30
    """
    # TODO: implement using the Convex Hull Trick / Li Chao Tree
    pass


if __name__ == "__main__":
    # Expected output: 30
    print(min_total_cost([1, 2, 4, 5, 7], 6))
    # Expected output: 1250000000000
    print(min_total_cost([500000, 1000000], 10**12))
    # Expected output: 62
    print(min_total_cost([1, 3, 4, 5, 10, 11, 12, 13], 5))
