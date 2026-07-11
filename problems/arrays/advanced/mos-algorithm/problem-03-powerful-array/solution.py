"""Powerful Array (Codeforces 86D).

For each offline range query (l, r), compute the "power"
    power(l, r) = sum over distinct x of  cnt[x]^2 * x
where cnt[x] is the frequency of value x in a[l..r].

Solve with Mo's Algorithm in O((n + q) * sqrt(n)). Maintain the running power with an
incremental delta: adding an occurrence of x moves its term by x*(2*cnt + 1).

Fill in the function body. Do NOT recompute the full sum per query
(that is the O(n*q) brute force).
"""
from typing import List, Tuple


def powerful_array(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Answer power(l, r) = sum_x cnt[x]^2 * x for each offline range query.

    Args:
        a: The static input array of positive integers.
        queries: A list of (l, r) pairs, 0-indexed and inclusive into `a`.

    Returns:
        A list `ans` where ans[k] is power(l, r) for the k-th query, in original
        input order.

    Example:
        powerful_array([1, 2, 1], [(0, 1), (0, 2), (1, 2)])
        # -> [3, 6, 3]
    """
    # TODO: implement using Mo's Algorithm
    pass


if __name__ == "__main__":
    # 0-indexed, inclusive ranges.
    print(powerful_array([1, 2, 1], [(0, 1), (0, 2), (1, 2)]))  # expected: [3, 6, 3]
    print(powerful_array([1, 1, 1], [(0, 2), (0, 0)]))          # expected: [9, 1]
