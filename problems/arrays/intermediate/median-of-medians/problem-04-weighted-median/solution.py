"""Weighted Median (CLRS Problem 9-2).

Return the lower weighted median in worst-case O(n) time using Median of
Medians selection to pick partition pivots.
"""
from typing import List, Union

Number = Union[int, float]


def weighted_median(nums: List[int], weights: List[Number]) -> int:
    """Return the lower weighted median value of ``nums``.

    The lower weighted median is the value ``x`` for which the total weight of
    all values strictly less than ``x`` is ``< W / 2`` and the total weight of
    all values strictly greater than ``x`` is ``<= W / 2``, where
    ``W = sum(weights)``.

    Args:
        nums: List of ``n`` distinct values.
        weights: List of ``n`` positive weights aligned with ``nums``.

    Returns:
        The value at the lower weighted median position.

    Example:
        >>> weighted_median([10, 35, 5, 20, 60], [10, 35, 5, 20, 30])
        35
    """
    # TODO: implement using Median of Medians selection / partitioning
    pass


if __name__ == "__main__":
    print(weighted_median([1, 2, 3, 4, 5], [0.2, 0.2, 0.2, 0.2, 0.2]))   # expected: 3
    print(weighted_median([10, 35, 5, 20, 60], [10, 35, 5, 20, 30]))     # expected: 35
    print(weighted_median([1, 2, 3], [0.1, 0.1, 0.8]))                   # expected: 3
