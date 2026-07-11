"""Maximal Square (LeetCode 221).

Return the area of the largest all-'1' square. Empty solution template —
fill in the logic yourself.
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Return the area of the largest square of '1's in ``matrix``.

        Args:
            matrix: An m x n grid of the characters '0' and '1'.

        Returns:
            The area (side * side) of the largest all-'1' square, or 0 if
            there are no '1's.

        Example:
            >>> Solution().maximalSquare([["1","0"], ["1","1"]])
            1
        """
        # TODO: implement.
        # Hint: per-row heights of consecutive '1's, then for each row find the
        # largest square in that histogram (side capped to min(height, width)),
        # OR use the classic dp[i][j] = 1 + min(up, left, up-left) recurrence.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalSquare([["1", "0", "1", "0", "0"],
                             ["1", "0", "1", "1", "1"],
                             ["1", "1", "1", "1", "1"],
                             ["1", "0", "0", "1", "0"]]))  # expected: 4
    print(sol.maximalSquare([["0", "1"],
                             ["1", "0"]]))                  # expected: 1
    print(sol.maximalSquare([["0"]]))                       # expected: 0
