"""Range Sum Query - Mutable (LeetCode 307).

Implement a data structure supporting point updates and range-sum queries, both
in O(log n), using a Segment Tree.

Fill in the method bodies. Do NOT keep the naive O(n)-per-query approach.
"""
from typing import List


class NumArray:
    """Segment-tree backed mutable range-sum structure.

    Example:
        arr = NumArray([1, 3, 5])
        arr.sumRange(0, 2)  # -> 9
        arr.update(1, 2)
        arr.sumRange(0, 2)  # -> 8
    """

    def __init__(self, nums: List[int]) -> None:
        """Build the segment tree over `nums`.

        Args:
            nums: The initial integer array.
        """
        # TODO: implement
        pass

    def update(self, index: int, val: int) -> None:
        """Set nums[index] = val and repair the affected tree nodes.

        Args:
            index: 0-based position to overwrite.
            val: New value to store at `index`.
        """
        # TODO: implement
        pass

    def sumRange(self, left: int, right: int) -> int:
        """Return the inclusive sum nums[left] + ... + nums[right].

        Args:
            left: Inclusive left index of the query range.
            right: Inclusive right index of the query range.

        Returns:
            The sum of the elements in [left, right].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    arr = NumArray([1, 3, 5])
    print(arr.sumRange(0, 2))  # expected: 9
    arr.update(1, 2)
    print(arr.sumRange(0, 2))  # expected: 8
