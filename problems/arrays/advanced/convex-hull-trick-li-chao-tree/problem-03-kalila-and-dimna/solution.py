"""Kalila and Dimna in the Forest (Codeforces 319C).

Minimize dp[i] = min_{j<i} dp[j] + b[j]*a[i], with dp[0] = 0, answer dp[N-1].
Solve with the monotonic Convex Hull Trick.
This is an EMPTY TEMPLATE: fill in the body yourself.
"""
from typing import List


def min_total_cost(a: List[int], b: List[int]) -> int:
    """Return the minimum total cost dp[N-1].

    Uses the recurrence dp[0] = 0 and, for i >= 1,
        dp[i] = min over 0 <= j < i of ( dp[j] + b[j] * a[i] ).
    Heights a are strictly increasing; costs b are non-increasing with b[-1] == 0.

    Args:
        a: Strictly increasing tree heights, length N (1 <= N <= 1e5), a[0] == 1.
        b: Non-increasing recharge costs, length N, b[-1] == 0.

    Returns:
        dp[N-1], the minimum total cost to cut all trees.

    Example:
        >>> min_total_cost([1, 2, 3, 4, 5], [5, 4, 3, 2, 0])
        25
    """
    # TODO: implement using the Convex Hull Trick / Li Chao Tree
    pass


if __name__ == "__main__":
    # Expected output: 25
    print(min_total_cost([1, 2, 3, 4, 5], [5, 4, 3, 2, 0]))
    # Expected output: 138
    print(min_total_cost([1, 2, 3, 10, 20, 30], [6, 5, 4, 3, 2, 0]))
