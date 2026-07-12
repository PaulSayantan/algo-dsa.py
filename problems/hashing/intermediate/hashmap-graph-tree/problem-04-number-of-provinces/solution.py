"""Number of Provinces — LeetCode 547."""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # TODO: count connected components via a visited set + DFS
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # expected: 2
    print(sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # expected: 3
    print(sol.findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # expected: 1
