"""Building Bridges (CSES).

dp[i] = min_{j<i} dp[j] + (h[i]-h[j])^2 + (W[i-1]-W[j]), keep pillars 1 and N.
Heights are NOT sorted, so slopes are non-monotone: use a Li Chao Tree.
This is an EMPTY TEMPLATE: fill in the body yourself.
"""
from typing import List


def min_bridge_cost(h: List[int], c: List[int]) -> int:
    """Return the minimum total cost of bridges plus demolitions.

    Pillar i has height h[i] and demolition cost c[i]. Pillars 0 and N-1 are always
    kept; each other pillar is kept or demolished. Consecutive kept pillars are joined
    by a bridge of cost (h[i]-h[j])**2; demolished pillars cost their c value.

    Args:
        h: Pillar heights, length N (1 <= N <= 1e5). NOT necessarily sorted.
        c: Positive demolition costs, length N.

    Returns:
        dp[N-1], the minimum total cost to reach the last pillar.

    Example:
        >>> min_bridge_cost([1, 3, 12, 6, 10], [4, 5, 3, 6, 1])
        32
    """
    # TODO: implement using the Convex Hull Trick / Li Chao Tree
    pass


if __name__ == "__main__":
    # Expected output: 32
    print(min_bridge_cost([1, 3, 12, 6, 10], [4, 5, 3, 6, 1]))
    # Expected output: 3
    print(min_bridge_cost([3, 5, 3, 2, 4], [1, 1, 1, 1, 1]))
