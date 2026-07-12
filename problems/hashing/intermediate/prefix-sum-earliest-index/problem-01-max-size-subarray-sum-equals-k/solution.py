"""Maximum Size Subarray Sum Equals k — LeetCode 325."""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # TODO: store the EARLIEST index of each prefix sum; longest range
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))  # expected: 4
    print(sol.maxSubArrayLen([-2, -1, 2, 1], 1))  # expected: 2
    print(sol.maxSubArrayLen([1, 2, 3], 100))  # expected: 0
