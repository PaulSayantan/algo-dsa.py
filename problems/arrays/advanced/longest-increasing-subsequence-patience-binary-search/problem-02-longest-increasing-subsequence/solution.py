"""Longest Increasing Subsequence (LeetCode 300).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Return the length of the longest strictly increasing subsequence.

        Args:
            nums: The input integer array. Elements may repeat and may be
                negative; order defines valid subsequences.

        Returns:
            The length of the longest strictly increasing subsequence of nums.

        Example:
            >>> Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
            4
            >>> Solution().lengthOfLIS([7, 7, 7, 7, 7])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # expected: 4
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # expected: 4
    print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))         # expected: 1
