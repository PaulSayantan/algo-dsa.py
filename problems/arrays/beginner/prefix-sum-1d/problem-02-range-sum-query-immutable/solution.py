from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        """Initialize the structure with an immutable array.

        Args:
            nums: The integer array that range-sum queries will run against.
        """
        # TODO: implement (precompute a prefix-sum array here)
        pass

    def sumRange(self, left: int, right: int) -> int:
        """Return the inclusive sum nums[left] + ... + nums[right].

        Args:
            left: Left index of the range (0-based, inclusive).
            right: Right index of the range (0-based, inclusive), right >= left.

        Returns:
            The sum of all elements from index left through index right.

        Example:
            >>> na = NumArray([-2, 0, 3, -5, 2, -1])
            >>> na.sumRange(0, 2)
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Sample run — expected outputs shown as comments, not asserted.
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sumRange(0, 2))   # expected: 1
    print(na.sumRange(2, 5))   # expected: -1
    print(na.sumRange(0, 5))   # expected: -3

    na2 = NumArray([1, 2, 3, 4, 5])
    print(na2.sumRange(1, 3))  # expected: 9
    print(na2.sumRange(0, 4))  # expected: 15
