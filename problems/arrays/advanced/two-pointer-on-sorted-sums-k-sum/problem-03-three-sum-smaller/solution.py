"""3Sum Smaller (LeetCode 259).

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """Count index triplets (i, j, k) with i < j < k whose values sum below target.

        Args:
            nums: List of integers (unsorted; you may sort a copy or in place).
            target: Exclusive upper bound for the triplet sum.

        Returns:
            The number of triplets ``(i, j, k)`` with ``0 <= i < j < k < len(nums)``
            such that ``nums[i] + nums[j] + nums[k] < target``.

        Example:
            >>> Solution().threeSumSmaller([-2, 0, 1, 3], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumSmaller([-2, 0, 1, 3], 2))  # expected: 2
    print(sol.threeSumSmaller([], 0))             # expected: 0
    print(sol.threeSumSmaller([0, 0, 0], 1))      # expected: 1
