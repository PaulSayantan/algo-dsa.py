"""Jump Game VI — maximum score to reach the last index (LeetCode 1696)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # TODO: dp[i] = nums[i] + windowed max of dp[i-k..i-1] via a decreasing deque
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxResult([1, -1, -2, 4, -7, 3], 2))  # expected: 7
    print(sol.maxResult([10, -5, -2, 4, 0, 3], 3))  # expected: 17
    print(sol.maxResult([1, 2, 3], 1))  # expected: 6
    print(sol.maxResult([5], 1))  # expected: 5
