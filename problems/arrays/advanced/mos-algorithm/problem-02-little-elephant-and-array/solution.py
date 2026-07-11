"""Little Elephant and Array (Codeforces 220B).

For each offline range query (l, r), count how many values x appear in a[l..r]
exactly x times.

Solve with Mo's Algorithm in O((n + q) * sqrt(n)). Key trick: when you add or remove
one occurrence of a value v, the running answer changes by at most 1, because only v
can cross the "cnt[v] == v" boundary.

Fill in the function body. Do NOT recount frequencies from scratch per query
(that is the O(n*q) brute force).
"""
from typing import List, Tuple


def count_values_equal_frequency(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Count, per query, how many values occur exactly as many times as their value.

    Args:
        a: The static input array of positive integers.
        queries: A list of (l, r) pairs, 0-indexed and inclusive into `a`.

    Returns:
        A list `ans` where ans[k] is the number of values x such that x appears
        exactly x times in a[queries[k][0] .. queries[k][1]], in original order.

    Example:
        count_values_equal_frequency([3, 1, 2, 2, 3, 3, 7], [(0, 6)])
        # -> [3]
    """
    # TODO: implement using Mo's Algorithm
    pass


if __name__ == "__main__":
    # 0-indexed, inclusive ranges.
    print(count_values_equal_frequency([3, 1, 2, 2, 3, 3, 7], [(0, 6)]))          # expected: [3]
    print(count_values_equal_frequency([1, 1, 3, 3, 3], [(0, 1), (0, 4)]))        # expected: [0, 1]
