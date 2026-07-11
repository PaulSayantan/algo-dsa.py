"""Distinct Elements in Range (SPOJ DQUERY), online.

For each query (l, r), report the number of distinct values in nums[l..r].

Fill in the body of `distinct_in_range`. The intended approach is a persistent
segment tree over positions, one version per prefix, marking only the last
occurrence of each value with a 1.
"""

from typing import List, Tuple


def distinct_in_range(
    nums: List[int],
    queries: List[Tuple[int, int]],
) -> List[int]:
    """Answer online range-distinct-count queries.

    Args:
        nums: The input array.
        queries: A list of ``(l, r)`` pairs. Each asks for the number of
            distinct values in the inclusive subarray ``nums[l..r]`` (0-based).

    Returns:
        A list of integers, one answer per query, in the same order as
        ``queries``.

    Example:
        >>> distinct_in_range([1, 1, 2, 1, 3], [(0, 4), (0, 2), (1, 3)])
        [3, 2, 2]
    """
    # TODO: implement using a persistent segment tree over positions. Version i
    #       keeps a 1 only at the last occurrence of each value seen in [0..i];
    #       answer (l, r) = range-sum over positions [l, r] in version r.
    pass


if __name__ == "__main__":
    # Expected output: [3, 2, 2]
    print(distinct_in_range([1, 1, 2, 1, 3], [(0, 4), (0, 2), (1, 3)]))

    # Expected output: [5, 3, 1]
    print(distinct_in_range([1, 2, 3, 4, 5], [(0, 4), (2, 4), (1, 1)]))
