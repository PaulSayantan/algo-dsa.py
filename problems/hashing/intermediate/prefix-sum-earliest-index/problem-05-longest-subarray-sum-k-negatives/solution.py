"""Longest subarray with sum exactly k (negatives allowed) — return length."""
from typing import List


class Solution:
    def longestSubarraySumK(self, nums: List[int], k: int) -> int:
        # TODO: earliest-index prefix map; best = i - first[cur - k]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarraySumK([10, 5, 2, 7, 1, 9], 15))  # expected: 4
    print(sol.longestSubarraySumK([-5, 8, -14, 2, 4, 12], -5))  # expected: 5
    print(sol.longestSubarraySumK([1, -1, 1, -1, 1], 0))  # expected: 4
