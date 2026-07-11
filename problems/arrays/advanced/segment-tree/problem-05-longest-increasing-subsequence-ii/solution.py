"""Longest Increasing Subsequence II (LeetCode 2407).

Length of the longest strictly-increasing subsequence whose adjacent elements
differ by at most k. Solve in O(n log n) with a Segment Tree over the value domain
that supports range-max query + point update, accelerating a value-indexed DP.

Fill in the method body. Do NOT use the O(n^2) pairwise DP.
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        """Return the length of the longest valid subsequence.

        A valid subsequence is strictly increasing and every pair of adjacent
        chosen elements differs by at most k.

        Args:
            nums: The input integer array (all values >= 1).
            k: Maximum allowed gap between adjacent chosen elements.

        Returns:
            The length of the longest strictly-increasing subsequence with
            adjacent differences at most k.

        Example:
            Solution().lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3)  # -> 5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3))  # expected: 5
    print(Solution().lengthOfLIS([7, 4, 5, 1, 8, 12, 4, 7], 5))     # expected: 4
    print(Solution().lengthOfLIS([1, 5], 1))                         # expected: 1
