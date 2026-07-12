"""Jump Game VI — LeetCode 1696."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # TODO: windowed-max DP with a monotonic deque
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxResult([1, -1, -2, 4, -7, 3], 2))  # expected: 7
    print(sol.maxResult([10, -5, -2, 4, 0, 3], 3))  # expected: 17
    print(sol.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))  # expected: 0
