"""Stamping the Grid (LeetCode 2132).

Decide whether stampHeight x stampWidth stamps can cover every empty cell
without covering any occupied cell or leaving the grid. Solve with a 2D prefix
sum (to test valid placements) plus a 2D difference array (to accumulate stamp
coverage).
"""

from typing import List


class Solution:
    def possibleToStamp(
        self,
        grid: List[List[int]],
        stampHeight: int,
        stampWidth: int,
    ) -> bool:
        """Return whether stamps can cover all empty cells legally.

        Args:
            grid: m x n binary matrix; 0 is an empty cell, 1 is occupied.
            stampHeight: Number of rows each stamp occupies (no rotation).
            stampWidth: Number of columns each stamp occupies (no rotation).

        Returns:
            True if stamps of the given size can cover every empty cell without
            covering any occupied cell and without extending outside the grid;
            False otherwise. Stamps may overlap and any number may be used.

        Example:
            >>> Solution().possibleToStamp(
            ...     [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]],
            ...     2, 2,
            ... )
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.possibleToStamp(
            [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]],
            2, 2,
        )
    )
    # Expected: True

    print(sol.possibleToStamp([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1, 2))
    # Expected: False
