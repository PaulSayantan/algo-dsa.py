"""Constrained Subsequence Sum — LeetCode 1425.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """Return the maximum sum of a subsequence with bounded index gaps.

        Any two elements that are adjacent in the chosen subsequence must have
        original indices differing by at most ``k``.

        Args:
            nums: The input array of integers (may contain negatives).
            k: The maximum allowed gap between original indices of consecutive
                chosen elements, with ``1 <= k <= len(nums)``.

        Returns:
            The maximum achievable sum over all non-empty valid subsequences.

        Example:
            >>> Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2)
            37
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.constrainedSubsetSum([10, 2, -10, 5, 20], 2))  # expected: 37
    print(sol.constrainedSubsetSum([-1, -2, -3], 1))  # expected: -1
    print(sol.constrainedSubsetSum([10, -2, -10, -5, 20], 2))  # expected: 23
