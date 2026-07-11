"""Longest Increasing Subsequence (LeetCode 300).

Return the length of the longest strictly increasing subsequence of nums.
The target complexity is O(n log n), achieved with patience sorting plus a
lower-bound binary search over a `tails` array.
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Return the length of the longest strictly increasing subsequence.

        Args:
            nums: A non-empty list of integers.

        Returns:
            The length of the longest strictly increasing subsequence of nums.

        Example:
            >>> Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # expected: 4
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # expected: 4
    print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))         # expected: 1
