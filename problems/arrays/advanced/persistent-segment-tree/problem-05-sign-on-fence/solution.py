"""Sign on Fence (Codeforces 484E).

For each query (l, r, w), return
    max over i in [l, r-w+1] of min(heights[i .. i+w-1]).

Fill in the body of `max_sign_height`. The intended approach builds persistent
segment tree versions by inserting planks tallest-first (version k = k tallest
planks), where each node tracks the longest run of consecutive inserted planks;
each query binary searches over the versions.
"""

from typing import List, Tuple


def max_sign_height(
    heights: List[int],
    queries: List[Tuple[int, int, int]],
) -> List[int]:
    """Answer max-of-window-minimums queries with a fixed window width.

    Args:
        heights: Plank heights, length ``n``.
        queries: A list of ``(l, r, w)`` triples. Each asks for the maximum,
            over all width-``w`` blocks of consecutive planks lying inside
            ``[l, r]``, of that block's minimum height. It is guaranteed that
            ``1 <= w <= r - l + 1``.

    Returns:
        A list of integers, one answer per query, in the same order as
        ``queries``.

    Example:
        >>> max_sign_height([2, 6, 4, 3, 5, 7, 1, 8], [(1, 4, 2), (0, 7, 3)])
        [4, 3]
    """
    # TODO: implement with a persistent segment tree over positions that tracks
    #       the longest consecutive run of inserted planks (store, per node:
    #       prefix run, suffix run, best run, and segment length). Insert planks
    #       tallest-first to create versions, then binary search the version /
    #       threshold height for which the best run inside [l, r] reaches w.
    pass


if __name__ == "__main__":
    # Expected output: [4, 3]
    print(max_sign_height([2, 6, 4, 3, 5, 7, 1, 8], [(1, 4, 2), (0, 7, 3)]))

    # Expected output: [8, 3, 6]
    print(max_sign_height([5, 3, 8, 6], [(0, 3, 1), (0, 3, 4), (2, 3, 2)]))
