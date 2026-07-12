"""Perfect Squares via state-space BFS — LeetCode 279."""
from collections import deque  # noqa: F401


class Solution:
    def numSquares(self, n: int) -> int:
        # TODO: BFS over remaining amounts; each edge subtracts a perfect square
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSquares(12))  # expected: 3
    print(sol.numSquares(13))  # expected: 2
    print(sol.numSquares(1))  # expected: 1
    print(sol.numSquares(7))  # expected: 4
    print(sol.numSquares(48))  # expected: 3
