"""Subarrays with K Different Integers — LeetCode 992."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # TODO: exactly K = atMost(K) - atMost(K-1); each atMost is a sliding-window count
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))  # expected: 7
    print(sol.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))  # expected: 3
    print(sol.subarraysWithKDistinct([1, 1, 1, 1], 1))  # expected: 10
    print(sol.subarraysWithKDistinct([1, 2], 2))  # expected: 1
