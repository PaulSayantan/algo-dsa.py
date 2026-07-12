"""Subarray Sums Divisible by K — LeetCode 974."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # TODO: frequency map over prefix remainders ((cur+x)%k, kept in [0,k))
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # expected: 7
    print(sol.subarraysDivByK([5], 9))  # expected: 0
    print(sol.subarraysDivByK([2, -2, 2, -4], 6))  # expected: 2
