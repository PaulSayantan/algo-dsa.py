"""Jump Game VI — LeetCode 1696."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # TODO: dp[i] = nums[i] + max(dp[i-k..i-1]); window max via decreasing deque
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxResult([1, -1, -2, 4, -7, 3], 2))  # expected: 7
    print(sol.maxResult([10, -5, -2, 4, 0, 3], 3))  # expected: 17
    print(sol.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))  # expected: 0
    print(sol.maxResult([5], 1))  # expected: 5
    print(sol.maxResult([0, -1, -2, -3, -4], 1))  # expected: -10
