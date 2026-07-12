"""Max Value of Equation — LeetCode 1499."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # TODO: monotonic deque of (y - x) within the x-window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))  # expected: 4
    print(sol.findMaxValueOfEquation([[0, 0], [3, 0], [9, 2]], 3))  # expected: 3
    print(sol.findMaxValueOfEquation([[-19, 9], [-15, -19], [-5, -8]], 10))  # expected: -6
