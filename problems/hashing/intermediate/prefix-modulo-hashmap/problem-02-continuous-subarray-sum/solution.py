"""Continuous Subarray Sum — LeetCode 523."""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # TODO: earliest index of each prefix remainder; need length >= 2
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))  # expected: True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))  # expected: True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))  # expected: False
    print(sol.checkSubarraySum([1, 0], 2))  # expected: False
