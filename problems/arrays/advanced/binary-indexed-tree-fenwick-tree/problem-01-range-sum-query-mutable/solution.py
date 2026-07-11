"""LeetCode 307 - Range Sum Query - Mutable.

Fill in the body using a Binary Indexed Tree (Fenwick Tree). Do NOT rebuild
prefix sums from scratch on every query.
"""

from typing import List


class NumArray:
    """Supports point updates and range-sum queries over a mutable array.

    Args:
        nums: The initial integer array.

    Example:
        >>> na = NumArray([1, 3, 5])
        >>> na.sumRange(0, 2)
        9
        >>> na.update(1, 2)
        >>> na.sumRange(0, 2)
        8
    """

    def __init__(self, nums: List[int]) -> None:
        # TODO: implement (initialize the Fenwick Tree and store base values)
        pass

    def update(self, index: int, val: int) -> None:
        """Set nums[index] = val in O(log n).

        Args:
            index: 0-based position to update.
            val: New value to store at that position.
        """
        # TODO: implement
        pass

    def sumRange(self, left: int, right: int) -> int:
        """Return the inclusive sum nums[left..right] in O(log n).

        Args:
            left: 0-based inclusive left bound.
            right: 0-based inclusive right bound (right >= left).

        Returns:
            The sum of nums[left] + ... + nums[right].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    na = NumArray([2, 4, 1, 7])
    print(na.sumRange(1, 3))  # expected: 12
    na.update(2, 10)
    print(na.sumRange(1, 3))  # expected: 21
    print(na.sumRange(0, 0))  # expected: 2
