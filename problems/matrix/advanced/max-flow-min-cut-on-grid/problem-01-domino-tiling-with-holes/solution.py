"""Domino Tiling with Holes — maximum bipartite matching on a grid.

Fill in `max_dominoes` using a Max-Flow / Min-Cut on Grid model:
color the board like a chessboard, then find a maximum matching between the
black empty cells and their adjacent white empty cells.
"""

from typing import List


class Solution:
    def max_dominoes(self, grid: List[str]) -> int:
        """Return the maximum number of 1x2 dominoes that fit on the grid.

        A domino covers two orthogonally adjacent empty ('.') cells and may not
        overlap another domino or cover a blocked ('#') cell.

        Args:
            grid: A list of R strings, each of length C, using '.' for an empty
                cell and '#' for a blocked cell.

        Returns:
            The maximum number of non-overlapping dominoes that can be placed.

        Example:
            >>> Solution().max_dominoes(["...", "..."])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_dominoes(["...", "..."]))       # expected: 3
    print(sol.max_dominoes([".#", ".."]))         # expected: 1
    print(sol.max_dominoes(["...", "...", "..."]))  # expected: 4
