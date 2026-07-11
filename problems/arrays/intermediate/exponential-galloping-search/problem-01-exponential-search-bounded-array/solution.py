"""Exponential Search in a Sorted Array (classic algorithm).

Fill in `exponential_search` using the Exponential (Galloping) Search technique:
double a probe index until it reaches or overshoots the target, then binary
search the located window.
"""
from typing import List


def exponential_search(nums: List[int], target: int) -> int:
    """Return an index of `target` in the sorted array `nums`, or -1.

    Args:
        nums: A list of integers sorted in non-decreasing order.
        target: The value to locate.

    Returns:
        An index `i` such that `nums[i] == target`, or -1 if `target` is absent.
        If `target` appears multiple times, any matching index is acceptable.

    Example:
        >>> exponential_search([2, 3, 4, 10, 40], 10)
        3
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(exponential_search([2, 3, 4, 10, 40], 10))  # expected: 3
    print(exponential_search([2, 3, 4, 10, 40], 5))   # expected: -1
    print(exponential_search([1], 1))                 # expected: 0
    print(exponential_search([], 7))                  # expected: -1
