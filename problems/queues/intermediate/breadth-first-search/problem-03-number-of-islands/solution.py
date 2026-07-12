"""Count 4-directionally connected islands in a grid via BFS."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # TODO: BFS-flood each unvisited '1' component, counting components
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))  # expected: 1
    print(sol.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))  # expected: 3
    print(sol.numIslands([]))  # expected: 0
    print(sol.numIslands([["0"]]))  # expected: 0
    print(sol.numIslands([["1"]]))  # expected: 1
