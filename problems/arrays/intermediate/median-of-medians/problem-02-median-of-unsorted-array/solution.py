"""Median of an Unsorted Array.

Return the lower median (the element at sorted index (n - 1) // 2) in
worst-case O(n) time using the Median of Medians selection algorithm.
"""
from typing import List


def find_median(nums: List[int]) -> int:
    """Return the lower median of ``nums`` in worst-case linear time.

    The lower median is the element at 0-indexed position ``(n - 1) // 2`` of
    the sorted array, i.e. the ``ceil(n / 2)``-th smallest element (1-indexed).

    Args:
        nums: A non-empty array of integers (may contain duplicates).

    Returns:
        The lower-median value of ``nums``.

    Example:
        >>> find_median([7, 10, 4, 3, 20, 15])
        7
    """
    # TODO: implement using Median of Medians selection
    pass


if __name__ == "__main__":
    print(find_median([3, 1, 2]))                  # expected: 2
    print(find_median([7, 10, 4, 3, 20, 15]))      # expected: 7
    print(find_median([5]))                        # expected: 5
