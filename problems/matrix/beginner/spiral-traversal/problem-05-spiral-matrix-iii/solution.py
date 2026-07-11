"""LeetCode 885 - Spiral Matrix III.

Walk an outward-growing clockwise spiral from a start cell and return the
coordinates of every grid cell in visit order.
"""

from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        """Return grid coordinates in outward clockwise spiral visit order.

        Starting at ``(rStart, cStart)`` facing east, follow a clockwise
        spiral with step lengths 1, 1, 2, 2, 3, 3, ... cycling through the
        directions east, south, west, north. Out-of-bounds positions are
        walked over but not recorded. Stop once all ``rows * cols`` cells
        have been collected.

        Args:
            rows: Number of rows in the grid (>= 1).
            cols: Number of columns in the grid (>= 1).
            rStart: Starting row index (0 <= rStart < rows).
            cStart: Starting column index (0 <= cStart < cols).

        Returns:
            A list of ``[r, c]`` pairs — every cell of the grid, in the
            order the spiral visits them.

        Example:
            >>> Solution().spiralMatrixIII(1, 4, 0, 0)
            [[0, 0], [0, 1], [0, 2], [0, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().spiralMatrixIII(1, 4, 0, 0))
    # Expected: [[0, 0], [0, 1], [0, 2], [0, 3]]
