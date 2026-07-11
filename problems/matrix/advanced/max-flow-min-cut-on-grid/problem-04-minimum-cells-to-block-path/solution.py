"""Minimum Cells to Block a Path — minimum vertex cut via Menger's theorem.

Fill in `min_cells_to_block` using a Max-Flow / Min-Cut on Grid model: split each
removable cell into in/out nodes joined by a capacity-1 edge, give the
non-removable source and sink capacity infinity, and return the max flow (which
equals the minimum vertex cut). Return -1 when disconnection is impossible.
"""

from typing import List


class Solution:
    def min_cells_to_block(self, grid: List[str]) -> int:
        """Return the minimum number of open cells to wall off to disconnect S from T.

        Source is (0,0) and sink is (R-1, C-1); both are open and cannot be removed.
        Movement is between orthogonally adjacent open cells.

        Args:
            grid: A list of R strings of length C, each character '.' (open) or
                '#' (wall). grid[0][0] and grid[R-1][C-1] are both '.'.

        Returns:
            The minimum number of cells (excluding source and sink) to convert into
            walls so that no path connects source to sink, or -1 if that is impossible.

        Example:
            >>> Solution().min_cells_to_block(["..", ".."])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.min_cells_to_block(["..", ".."]))   # expected: 2
    print(sol.min_cells_to_block(["..."]))        # expected: 1
    print(sol.min_cells_to_block([".#", "#."]))   # expected: 0
