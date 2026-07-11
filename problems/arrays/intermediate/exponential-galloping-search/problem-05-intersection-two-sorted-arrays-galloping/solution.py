"""Intersection of Two Sorted Arrays via Galloping (classic algorithm).

Fill in `intersect_sorted` using the Exponential (Galloping) Search technique:
iterate over the smaller array and gallop forward through the larger one to test
membership, keeping a cursor so each search resumes where the last ended.
"""
from typing import List


def intersect_sorted(a: List[int], b: List[int]) -> List[int]:
    """Return the ascending intersection of two sorted, distinct-valued arrays.

    Args:
        a: A list of distinct integers sorted in ascending order.
        b: A list of distinct integers sorted in ascending order. `a` and `b`
            may differ greatly in length.

    Returns:
        The values present in both `a` and `b`, sorted ascending, each once.

    Example:
        >>> intersect_sorted([1, 4, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        [1, 4, 9]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(intersect_sorted([1, 4, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # expected: [1, 4, 9]
    print(intersect_sorted([2, 5, 100], [1, 2, 3, 4, 5, 6]))                # expected: [2, 5]
    print(intersect_sorted([10, 20, 30], [1, 2, 3]))                        # expected: []
