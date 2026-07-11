"""Cyclic Sort — sort an array containing 1..n in place.

Fill in the body yourself. Do not add a working implementation elsewhere.
"""

from typing import List


def cyclic_sort(nums: List[int]) -> List[int]:
    """Sort an array containing every integer from 1..n exactly once, in place.

    Args:
        nums: A list of length n holding each integer in [1, n] exactly once,
            in arbitrary order. The list is mutated in place.

    Returns:
        The same list, sorted in ascending order.

    Example:
        >>> cyclic_sort([3, 1, 5, 4, 2])
        [1, 2, 3, 4, 5]
    """
    # TODO: implement using the cyclic sort pattern (swap value v to index v - 1)
    pass


if __name__ == "__main__":
    print(cyclic_sort([3, 1, 5, 4, 2]))     # expected: [1, 2, 3, 4, 5]
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))  # expected: [1, 2, 3, 4, 5, 6]
    print(cyclic_sort([1]))                 # expected: [1]
