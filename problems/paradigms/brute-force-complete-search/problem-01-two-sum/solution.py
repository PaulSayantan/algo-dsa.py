"""Two Sum — Brute Force / Complete Search practice template.

Fill in the body of `two_sum`. Do NOT look at SOLUTION.md until you have tried.
"""
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """Return the indices of the two numbers that add up to `target`.

        Args:
            nums: List of integers (length >= 2). Exactly one valid pair exists.
            target: The desired sum of the two chosen numbers.

        Returns:
            A list ``[i, j]`` with ``i < j`` such that
            ``nums[i] + nums[j] == target``.

        Example:
            >>> Solution().two_sum([2, 7, 11, 15], 9)
            [0, 1]
        """
        # TODO: implement using Brute Force / Complete Search
        # (examine every pair of indices i < j).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]
    print(sol.two_sum([3, 2, 4], 6))       # expected: [1, 2]
    print(sol.two_sum([3, 3], 6))          # expected: [0, 1]
