"""LeetCode 778 - Swim in Rising Water.

Solve as a percolation sweep with Union-Find on Grid: process cells in
increasing elevation, activating each and unioning it with already-active
neighbors. The answer is the elevation at which (0,0) and (n-1,n-1) first join
the same set.
"""
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Return the least time t at which (0,0) can reach (n-1,n-1).

        At time t you may occupy any cell with elevation <= t and move freely
        between such adjacent cells.

        Args:
            grid: An n x n matrix whose entries are a permutation of
                0 .. n*n-1, giving the elevation of each cell.

        Returns:
            The minimum time (water level) at which the top-left and
            bottom-right cells become connected.

        Example:
            >>> Solution().swimInWater([[0, 2], [1, 3]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().swimInWater([[0, 2], [1, 3]]))  # expected: 3
    grid = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    print(Solution().swimInWater(grid))  # expected: 16
