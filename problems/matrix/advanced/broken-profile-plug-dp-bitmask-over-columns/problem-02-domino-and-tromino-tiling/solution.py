"""LeetCode 790 -- Domino and Tromino Tiling.

Broken-profile / plug DP template. Fill in `numTilings` by sweeping the 2-row
board column by column while carrying a bitmask of which cells of the next
column are already filled by a piece that started in the current column.
"""

from __future__ import annotations


class Solution:
    def numTilings(self, n: int) -> int:
        """Count tilings of a 2 x n board using 2x1 dominoes and L-trominoes.

        Args:
            n: Number of columns of the board (the board has exactly 2 rows).
               1 <= n <= 1000.

        Returns:
            The number of distinct full tilings, taken modulo 1_000_000_007.

        Example:
            >>> Solution().numTilings(3)
            5
        """
        # TODO: implement using broken-profile / plug DP (bitmask over columns).
        # Enumerate, per column, the ways to cover its cells with dominoes and
        # the four L-tromino orientations; a piece may pre-fill one cell of the
        # next column, which the profile bitmask must record.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTilings(1))  # expected: 1
    print(sol.numTilings(2))  # expected: 2
    print(sol.numTilings(3))  # expected: 5
    print(sol.numTilings(4))  # expected: 11
    print(sol.numTilings(5))  # expected: 24
