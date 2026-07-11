"""Random Pick Index (LeetCode 398).

Fill in `Solution.pick` using Reservoir Sampling (k = 1) over the indices that
match `target`, so each matching index is returned with equal probability.
"""
from typing import List


class Solution:
    def __init__(self, nums: List[int]) -> None:
        """Initialize the object with the array `nums`.

        Args:
            nums: The integer array, possibly containing duplicates.
        """
        # TODO: store nums (O(n) space for the input is expected;
        #       the follow-up asks for O(1) *extra* space beyond this).
        pass

    def pick(self, target: int) -> int:
        """Return a uniformly random index i such that nums[i] == target.

        Args:
            target: A value guaranteed to appear in `nums`.

        Returns:
            An index i with nums[i] == target, chosen uniformly among all such
            indices.

        Example:
            >>> s = Solution([1, 2, 3, 3, 3])
            >>> s.pick(3) in (2, 3, 4)
            True
            >>> s.pick(1)
            0
        """
        # TODO: implement using Reservoir Sampling with k = 1 over matches
        pass


if __name__ == "__main__":
    s = Solution([1, 2, 3, 3, 3])
    print(s.pick(3))  # expected: one of 2, 3, 4 (uniformly at random)
    print(s.pick(1))  # expected: 0 (only index whose value is 1)
