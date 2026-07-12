"""Make Sum Divisible by P — LeetCode 1590."""
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # TODO: remove the shortest subarray whose sum % p == total % p
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubarray([3, 1, 4, 2], 6))  # expected: 1
    print(sol.minSubarray([6, 3, 5, 2], 9))  # expected: 2
    print(sol.minSubarray([1, 2, 3], 3))  # expected: 0
    print(sol.minSubarray([1, 2, 3], 7))  # expected: -1
