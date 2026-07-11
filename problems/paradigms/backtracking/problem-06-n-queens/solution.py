"""LeetCode 51 - N-Queens.

Fill in the body of `solveNQueens` using backtracking. Do not hard-code answers.
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Return all distinct placements of n non-attacking queens on n x n.

        No two queens may share a row, column, or diagonal. Each solution is a
        list of n strings of length n, using 'Q' for a queen and '.' for empty.

        Args:
            n: The board size and number of queens (1 <= n <= 9).

        Returns:
            A list of all valid board configurations. Any ordering is valid.

        Example:
            >>> len(Solution().solveNQueens(4))
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    for board in sol.solveNQueens(4):
        for row in board:
            print(row)
        print()
    # Expected: 2 distinct boards, e.g. columns (1,3,0,2) and (2,0,3,1).
    print(sol.solveNQueens(1))  # Expected: [["Q"]]
