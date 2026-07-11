"""Number of Enclaves — LeetCode 1020.

Fill in the body of `numEnclaves`. Do not hard-code answers; implement the
traversal so it works for any valid input.
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """Count land cells that cannot reach any border of the grid.

        Args:
            grid: An m x n binary matrix where 1 is land and 0 is sea.
                Land connects 4-directionally.

        Returns:
            The number of land cells from which it is impossible to walk off
            the boundary via a path of 4-connected land cells.

        Example:
            grid = [[0,0,0,0],
                    [1,0,1,0],
                    [0,1,1,0],
                    [0,0,0,0]]
            -> 3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    g = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    print(sol.numEnclaves(g))
    # Expected: 3
