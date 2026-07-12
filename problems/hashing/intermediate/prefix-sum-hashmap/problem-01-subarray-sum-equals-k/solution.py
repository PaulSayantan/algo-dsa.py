"""Subarray Sum Equals K — LeetCode 560."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: prefix-sum frequency map; count += freq[cur - k]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))  # expected: 2
    print(sol.subarraySum([1, 2, 3], 3))  # expected: 2
    print(sol.subarraySum([1, -1, 0], 0))  # expected: 3
    print(sol.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # expected: 4
