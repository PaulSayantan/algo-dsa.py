"""Rotting Oranges (LeetCode 994).

Fill in the body using the multi-source, level-by-level Lee Algorithm (BFS). Do
not modify the signature.
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Return the minutes until no fresh orange remains, or -1 if impossible.

        Each minute, every fresh orange (1) that is 4-directionally adjacent to
        a rotten orange (2) becomes rotten. Empty cells are 0.

        Args:
            grid: An m x n grid of values 0 (empty), 1 (fresh), 2 (rotten).

        Returns:
            The minimum number of minutes until all reachable fresh oranges rot,
            or -1 if at least one fresh orange can never rot.

        Example:
            >>> Solution().orangesRotting([[2, 1, 1],
            ...                            [1, 1, 0],
            ...                            [0, 1, 1]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1],
                              [1, 1, 0],
                              [0, 1, 1]]))   # expected: 4
    print(sol.orangesRotting([[2, 1, 1],
                              [0, 1, 1],
                              [1, 0, 1]]))   # expected: -1
    print(sol.orangesRotting([[0, 2]]))     # expected: 0
