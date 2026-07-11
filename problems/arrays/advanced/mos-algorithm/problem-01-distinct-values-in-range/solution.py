"""Distinct Values in a Range (SPOJ DQUERY) — the canonical Mo's Algorithm problem.

Given a static array and many offline (l, r) range queries, return the number of
distinct values in each subarray a[l..r].

Solve with Mo's Algorithm in O((n + q) * sqrt(n)):
  - sort queries by (l // block, r),
  - slide curL / curR while maintaining a frequency array and a running distinct count.

Fill in the function body. Do NOT answer each query with an independent O(n) scan
(that is the O(n*q) brute force).
"""
from typing import List, Tuple


def distinct_in_ranges(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Answer distinct-value-count queries over subarrays of a static array.

    Args:
        a: The static input array. Indexing convention used by `queries` must
            match this list (this template treats `queries` as 0-indexed,
            inclusive [l, r] into `a`).
        queries: A list of (l, r) pairs, 0-indexed and inclusive.

    Returns:
        A list `ans` where ans[k] is the number of distinct values in
        a[queries[k][0] .. queries[k][1]], in the original query order.

    Example:
        distinct_in_ranges([1, 1, 2, 1, 3], [(0, 4), (1, 3), (2, 4)])
        # -> [3, 2, 3]
    """
    # TODO: implement using Mo's Algorithm
    pass


if __name__ == "__main__":
    # 0-indexed, inclusive ranges (a[1..5] from PROBLEM.md becomes indices 0..4).
    print(distinct_in_ranges([1, 1, 2, 1, 3], [(0, 4), (1, 3), (2, 4)]))  # expected: [3, 2, 3]
    print(distinct_in_ranges([4, 4, 4, 4], [(0, 3), (1, 1)]))              # expected: [1, 1]
