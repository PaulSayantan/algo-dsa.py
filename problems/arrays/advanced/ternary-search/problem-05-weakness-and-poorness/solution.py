"""Weakness and Poorness (Codeforces 578C) via Ternary Search on a real parameter.

Fill in `min_weakness` to return the minimum over real x of the weakness of the
sequence, where weakness(x) is the maximum absolute contiguous-subarray sum of
(a_i - x).
"""

from typing import List


def min_weakness(a: List[int]) -> float:
    """Minimize weakness(x) = max_subarray | sum(a_i - x) | over real x.

    For a fixed x, weakness(x) is computable in O(n) via Kadane's algorithm
    (max subarray sum and min subarray sum of b_i = a_i - x). As a function of
    x it is the pointwise max of convex functions, hence convex/unimodal, so
    ternary-search x on a real interval.

    Args:
        a: The input array of numbers.

    Returns:
        The minimum achievable weakness over all real x, accurate to ~1e-6.

    Example:
        >>> round(min_weakness([1, 2, 3]), 6)
        1.0
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(round(min_weakness([1, 2, 3]), 6))                              # Expected: 1.0
    print(round(min_weakness([1, 2, 3, 4]), 6))                           # Expected: 2.0
    print(round(min_weakness([1, 10, 2, 9, 3, 8, 4, 7, 5, 6]), 6))        # Expected: 4.5
