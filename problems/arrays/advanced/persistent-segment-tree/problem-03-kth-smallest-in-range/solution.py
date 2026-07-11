"""K-th Smallest Number in Range (SPOJ MKTHNUM).

For each query (l, r, k), return the k-th smallest value (1-indexed) of the
subarray nums[l..r].

Fill in the body of `kth_smallest_in_range`. The intended approach is a
persistent segment tree over the value domain with one version per prefix,
walking two versions together to descend by count.
"""

from typing import List, Tuple


def kth_smallest_in_range(
    nums: List[int],
    queries: List[Tuple[int, int, int]],
) -> List[int]:
    """Answer range k-th-smallest (order statistic) queries.

    Args:
        nums: The input array.
        queries: A list of ``(l, r, k)`` triples. Each asks for the k-th
            smallest element (``k`` is 1-indexed) of the inclusive subarray
            ``nums[l..r]``. It is guaranteed ``1 <= k <= r - l + 1``.

    Returns:
        A list of integers, one answer per query, in the same order as
        ``queries``.

    Example:
        >>> kth_smallest_in_range(
        ...     [1, 5, 2, 6, 3, 7, 4],
        ...     [(1, 5, 3), (0, 6, 1), (2, 4, 2)],
        ... )
        [5, 1, 3]
    """
    # TODO: implement with a persistent segment tree over the compressed value
    #       domain: one version per prefix, then descend root[r]/root[l-1] by
    #       comparing k against the left-subtree window count.
    pass


if __name__ == "__main__":
    # Expected output: [5, 1, 3]
    print(
        kth_smallest_in_range(
            [1, 5, 2, 6, 3, 7, 4],
            [(1, 5, 3), (0, 6, 1), (2, 4, 2)],
        )
    )

    # Expected output: [4, 1, 4]
    print(
        kth_smallest_in_range(
            [4, 4, 4, 1, 2],
            [(0, 2, 2), (0, 4, 1), (0, 4, 5)],
        )
    )
