"""Distinct Elements in Range — empty solution template.

Fill in the body using Mo's algorithm (offline sqrt decomposition on queries).
Do NOT change the function signature.
"""
from typing import List, Tuple


def distinct_in_ranges(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Answer, for each query (l, r), the number of distinct values in a[l..r].

    Args:
        a: The static input array of integers.
        queries: A list of (l, r) pairs, each 0-indexed and inclusive
            (0 <= l <= r <= len(a) - 1).

    Returns:
        A list of integers, one per query in the ORIGINAL query order, where the
        i-th entry is the count of distinct values in a[queries[i][0] .. queries[i][1]].

    Example:
        >>> distinct_in_ranges([1, 1, 2, 1, 3], [(0, 4), (1, 2), (3, 4)])
        [3, 2, 2]
    """
    # TODO: implement using Mo's algorithm:
    #   1. Choose block size B ~ sqrt(n).
    #   2. Sort a list of query indices by (l // B, r) (optionally alternating r
    #      direction per block).
    #   3. Maintain curL, curR, a frequency table, and a running distinct count;
    #      define add(i) and remove(i) that update the count in O(1).
    #   4. Move the pointers to each query's [l, r] and record the answer at the
    #      query's original position.
    pass


if __name__ == "__main__":
    sample_a = [1, 1, 2, 1, 3]
    sample_queries = [(0, 4), (1, 2), (3, 4)]
    print(distinct_in_ranges(sample_a, sample_queries))
    # Expected: [3, 2, 2]
