"""Range Sum Query - Mutable — LeetCode 307.

Empty solution template. Fill in the body yourself using Square Root
Decomposition (block sums).
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        """Initialize the structure over ``nums``.

        Args:
            nums: The initial integer array.

        Example:
            >>> na = NumArray([1, 3, 5])
            >>> na.sumRange(0, 2)
            9
        """
        # TODO: implement — precompute block size ~ sqrt(n) and per-block sums
        pass

    def update(self, index: int, val: int) -> None:
        """Set ``nums[index] = val`` and keep block sums consistent.

        Args:
            index: The position to overwrite (0-indexed).
            val: The new value stored at ``index``.

        Returns:
            None. Mutates internal state in place.
        """
        # TODO: implement — adjust the containing block's stored sum
        pass

    def sumRange(self, left: int, right: int) -> int:
        """Return the inclusive sum of ``nums[left .. right]``.

        Args:
            left: Left endpoint of the range (0-indexed, inclusive).
            right: Right endpoint of the range (0-indexed, inclusive).

        Returns:
            The sum ``nums[left] + ... + nums[right]``.
        """
        # TODO: implement — add partial ends elementwise, whole blocks by sum
        pass


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print(na.sumRange(0, 2))  # expected: 9
    na.update(1, 2)
    print(na.sumRange(0, 2))  # expected: 8

    na2 = NumArray([-1, 3, 5])
    print(na2.sumRange(0, 2))  # expected: 7
    na2.update(0, 2)
    print(na2.sumRange(0, 2))  # expected: 10
    print(na2.sumRange(1, 1))  # expected: 3
