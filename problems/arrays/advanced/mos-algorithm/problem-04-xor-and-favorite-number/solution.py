"""XOR and Favorite Number (Codeforces 617E).

For each offline range query (l, r), count pairs (i, j) with l <= i <= j <= r such
that a[i] XOR ... XOR a[j] == k.

Key reduction: with prefix XOR P (P[0] = 0, P[t] = a[0]^...^a[t-1]), a subarray
a[i..j] has XOR k  iff  P[i] XOR P[j+1] == k. Counting such subarrays inside a[l..r]
(0-indexed inclusive) is counting pairs of equal-XOR-partner prefix values among the
prefix indices l, l+1, ..., r+1. Run Mo's Algorithm over that prefix window in
O((n + q) * sqrt(n)).

Fill in the function body. Do NOT count pairs by an O(len^2) scan per query.
"""
from typing import List, Tuple


def xor_favorite_number(a: List[int], k: int, queries: List[Tuple[int, int]]) -> List[int]:
    """Count subarrays with XOR == k inside each offline range query.

    Args:
        a: The static input array of non-negative integers.
        k: The favorite number to match against subarray XORs.
        queries: A list of (l, r) pairs, 0-indexed and inclusive into `a`.

    Returns:
        A list `ans` where ans[m] is the number of pairs (i, j),
        queries[m][0] <= i <= j <= queries[m][1], with a[i]^...^a[j] == k, in
        original query order.

    Example:
        xor_favorite_number([1, 2, 1, 1, 0, 3], 3, [(0, 5), (2, 4)])
        # -> [7, 0]
    """
    # TODO: implement using Mo's Algorithm over prefix-XOR indices
    pass


if __name__ == "__main__":
    # 0-indexed, inclusive ranges.
    print(xor_favorite_number([1, 2, 1, 1, 0, 3], 3, [(0, 5), (2, 4)]))  # expected: [7, 0]
    print(xor_favorite_number([1, 1, 1], 0, [(0, 2), (1, 2)]))            # expected: [2, 1]
