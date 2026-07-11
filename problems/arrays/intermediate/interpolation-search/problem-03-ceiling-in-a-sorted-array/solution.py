"""Ceiling in a Sorted Array.

Return the index of the smallest element that is >= x in a sorted array of
distinct integers, or -1 if no such element exists.
"""
from typing import List


def find_ceiling(arr: List[int], x: int) -> int:
    """Return the index of the ceiling of ``x`` in ``arr``.

    The ceiling is the smallest element ``>= x``.

    Args:
        arr: A list of distinct integers sorted in strictly increasing order.
        x: The value whose ceiling is sought.

    Returns:
        The index of the smallest element ``arr[i] >= x``; or ``-1`` if ``x`` is
        greater than every element in ``arr``.

    Example:
        >>> find_ceiling([1, 2, 8, 10, 12, 19], 5)
        2
        >>> find_ceiling([1, 2, 8, 10, 12, 19], 20)
        -1
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # Expected: 2
    print(find_ceiling([1, 2, 8, 10, 12, 19], 5))
    # Expected: -1
    print(find_ceiling([1, 2, 8, 10, 12, 19], 20))
    # Expected: 2
    print(find_ceiling([1, 2, 8, 10, 12, 19], 8))
