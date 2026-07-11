"""N-Queens (LeetCode 51).

Empty solution template — fill in the backtracking logic yourself.
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Return all distinct placements of n non-attacking queens on an
        n x n board.

        Each solution is a list of n strings of length n, using 'Q' for a
        queen and '.' for an empty square.

        Args:
            n: The board size and number of queens to place.

        Returns:
            A list of all valid board configurations (each a list of strings).

        Example:
            >>> sols = Solution().solveNQueens(4)
            >>> len(sols)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().solveNQueens(4))  # Expected: 2 distinct boards
    print(Solution().solveNQueens(1))  # Expected: [["Q"]]
    print(Solution().solveNQueens(3))  # Expected: []
