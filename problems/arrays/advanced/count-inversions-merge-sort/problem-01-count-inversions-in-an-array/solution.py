"""Count Inversions in an Array.

Fill in `count_inversions` using the merge-sort inversion-counting technique.
"""
from typing import List


def count_inversions(a: List[int]) -> int:
    """Count the number of pairs (i, j) with i < j and a[i] > a[j].

    Args:
        a: A list of integers (may contain duplicates), length 0 <= n <= 1e5.

    Returns:
        The total number of inversions as an integer. Equal elements do not
        count as an inversion.

    Example:
        >>> count_inversions([2, 4, 1, 3, 5])
        3
    """
    # TODO: implement using Count Inversions (merge sort)
    pass


if __name__ == "__main__":
    print(count_inversions([2, 4, 1, 3, 5]))  # expected: 3
    print(count_inversions([5, 4, 3, 2, 1]))  # expected: 10
    print(count_inversions([1, 2, 3, 4]))     # expected: 0
