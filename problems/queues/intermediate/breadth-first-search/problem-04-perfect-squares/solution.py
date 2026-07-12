"""Least count of perfect squares summing to n, via layered BFS."""
from typing import List  # noqa: F401
from collections import deque  # noqa: F401
import math  # noqa: F401


class Solution:
    def numSquares(self, n: int) -> int:
        # TODO: BFS over running-sum states, one square added per layer
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSquares(12))  # expected: 3
    print(sol.numSquares(13))  # expected: 2
    print(sol.numSquares(1))  # expected: 1
    print(sol.numSquares(4))  # expected: 1
    print(sol.numSquares(43))  # expected: 3
    print(sol.numSquares(0))  # expected: 0
