"""Interpolation Search Basics.

Find the index of a target value in a sorted, uniformly distributed array of
distinct integers using interpolation search.
"""
from typing import List


def interpolation_search(arr: List[int], x: int) -> int:
    """Return the index of ``x`` in the sorted array ``arr``, or -1 if absent.

    Args:
        arr: A list of distinct integers sorted in strictly increasing order.
        x: The target value to locate.

    Returns:
        The index ``i`` such that ``arr[i] == x``, or ``-1`` if ``x`` is not
        present in ``arr``.

    Example:
        >>> interpolation_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 70)
        6
        >>> interpolation_search([1, 2, 4, 8, 16, 32, 64], 5)
        -1
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # Expected: 6
    print(interpolation_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 70))
    # Expected: -1
    print(interpolation_search([1, 2, 4, 8, 16, 32, 64], 5))
    # Expected: 0
    print(interpolation_search([7], 7))
