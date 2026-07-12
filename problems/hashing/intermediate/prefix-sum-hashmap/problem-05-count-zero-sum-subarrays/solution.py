"""Count subarrays summing to zero (a prefix-sum repeats)."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def countZeroSum(self, nums: List[int]) -> int:
        # TODO: a zero-sum subarray ends wherever a prefix sum repeats
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countZeroSum([1, -1, 1, -1]))  # expected: 4
    print(sol.countZeroSum([0, 0, 0]))  # expected: 6
    print(sol.countZeroSum([3, -3, 3]))  # expected: 2
    print(sol.countZeroSum([1, 2, 3]))  # expected: 0
