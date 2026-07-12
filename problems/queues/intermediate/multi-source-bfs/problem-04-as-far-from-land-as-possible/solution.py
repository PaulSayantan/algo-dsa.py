"""As Far from Land as Possible — LeetCode 1162."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # TODO: multi-source BFS from every land cell; answer is the last wave
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))  # expected: 2
    print(sol.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))  # expected: 4
    print(sol.maxDistance([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # expected: -1
