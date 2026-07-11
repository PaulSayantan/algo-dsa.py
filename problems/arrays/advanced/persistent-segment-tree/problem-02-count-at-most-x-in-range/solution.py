"""Count Elements <= X in a Subarray.

For each query (l, r, x), report how many indices i in [l, r] have nums[i] <= x.

Fill in the body of `count_at_most`. The intended approach builds one persistent
segment tree version per prefix over the value domain and subtracts two versions.
"""

from typing import List, Tuple


def count_at_most(
    nums: List[int],
    queries: List[Tuple[int, int, int]],
) -> List[int]:
    """Answer range "count of values <= x" queries.

    Args:
        nums: The input array.
        queries: A list of ``(l, r, x)`` triples. Each asks for the number of
            indices ``i`` with ``l <= i <= r`` and ``nums[i] <= x``. Indices are
            0-based and both endpoints are inclusive.

    Returns:
        A list of integers, one answer per query, in the same order as
        ``queries``.

    Example:
        >>> count_at_most([1, 3, 2, 4, 2], [(0, 4, 2), (1, 3, 3), (0, 4, 0)])
        [3, 2, 0]
    """
    # TODO: implement using per-prefix persistent segment tree versions over
    #       the compressed value domain, then countLE(root[r]) - countLE(root[l-1]).
    pass


if __name__ == "__main__":
    # Expected output: [3, 2, 0]
    print(count_at_most([1, 3, 2, 4, 2], [(0, 4, 2), (1, 3, 3), (0, 4, 0)]))

    # Expected output: [4, 0, 1]
    print(count_at_most([5, 5, 5, 5], [(0, 3, 5), (0, 3, 4), (2, 2, 5)]))
