"""Range Sum Query - Immutable — LeetCode 303.

Fill in the body of the `NumArray` methods. Do not change the signatures.
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        """Initialize the structure with an immutable integer array.

        Args:
            nums: The integer array. It will not be modified after construction.
        """
        # TODO: implement (precompute whatever you need here)
        pass

    def sumRange(self, left: int, right: int) -> int:
        """Return the inclusive sum ``nums[left] + ... + nums[right]``.

        Args:
            left: Start index (0-based, inclusive), with ``0 <= left <= right``.
            right: End index (0-based, inclusive), with ``right < len(nums)``.

        Returns:
            The sum of the elements in the inclusive range ``[left, right]``.

        Example:
            >>> obj = NumArray([-2, 0, 3, -5, 2, -1])
            >>> obj.sumRange(0, 2)
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))   # expected: 1
    print(obj.sumRange(2, 5))   # expected: -1
    print(obj.sumRange(0, 5))   # expected: -3

    obj2 = NumArray([1, 2, 3, 4, 5])
    print(obj2.sumRange(1, 3))  # expected: 9
    print(obj2.sumRange(0, 4))  # expected: 15
