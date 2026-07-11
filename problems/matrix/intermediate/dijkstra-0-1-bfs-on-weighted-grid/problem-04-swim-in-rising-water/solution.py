"""Swim in Rising Water (LeetCode 778).

Fill in the body using Dijkstra with a minimax ("max" instead of "+")
relaxation over cell elevations. Do not modify the signature.
"""
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Return the least time to swim from (0, 0) to (n-1, n-1).

        At time t the water depth is t everywhere, and you may occupy a cell
        only when its elevation is at most t. Equivalently, return the minimum
        over all paths of the maximum cell elevation on the path.

        Args:
            grid: An n x n matrix; grid[i][j] is the elevation, a permutation of
                  0 .. n*n - 1.

        Returns:
            The earliest time (an integer) at which (n-1, n-1) is reachable.

        Example:
            >>> Solution().swimInWater([[0, 2],
            ...                         [1, 3]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.swimInWater([[0, 2],
                           [1, 3]]))                       # expected: 3
    print(sol.swimInWater([[0, 1, 2, 3, 4],
                           [24, 23, 22, 21, 5],
                           [12, 13, 14, 15, 16],
                           [11, 17, 18, 19, 20],
                           [10, 9, 8, 7, 6]]))             # expected: 16
