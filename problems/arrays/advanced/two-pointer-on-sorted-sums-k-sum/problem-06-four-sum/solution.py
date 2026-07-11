"""4Sum (LeetCode 18).

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Return all unique quadruplets that sum to target.

        Args:
            nums: List of integers (unsorted; you may sort in place).
            target: The required sum of the four chosen values.

        Returns:
            A list of quadruplets ``[a, b, c, d]`` drawn from four distinct indices
            with ``a + b + c + d == target``. The result must contain no duplicate
            quadruplets (same multiset of values). Any order is accepted.

        Example:
            >>> Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(sol.fourSum([2, 2, 2, 2, 2], 8))                        # expected: [[2, 2, 2, 2]]
    print(sol.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))         # expected: [[-5, -4, -3, 1]]
