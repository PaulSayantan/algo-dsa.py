"""Median of an Unsorted Array (expected linear time via Quickselect).

Fill in the body of `find_median` using Quickselect.
"""
from typing import List


def find_median(nums: List[int]) -> float:
    """Return the median of `nums` in expected O(n) time.

    Args:
        nums: A non-empty list of numbers, in arbitrary order.

    Returns:
        The median. For odd-length input this is the middle sorted element;
        for even-length input it is the average of the two middle elements
        (which may be a non-integer float).

    Example:
        >>> find_median([3, 1, 2])
        2
        >>> find_median([4, 1, 3, 2])
        2.5
    """
    # TODO: implement using Quickselect
    pass


if __name__ == "__main__":
    print(find_median([3, 1, 2]))        # expected: 2
    print(find_median([4, 1, 3, 2]))     # expected: 2.5
    print(find_median([7]))              # expected: 7
