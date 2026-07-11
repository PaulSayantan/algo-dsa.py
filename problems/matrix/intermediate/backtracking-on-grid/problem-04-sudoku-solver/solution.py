"""Sudoku Solver (LeetCode 37).

Empty solution template — fill in the backtracking logic yourself.
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Solve the Sudoku puzzle in place.

        Fill every '.' cell so each row, column, and 3x3 box contains the
        digits '1'-'9' exactly once. Modifies `board` directly and returns
        None. The puzzle is guaranteed to have a unique solution.

        Args:
            board: A 9x9 grid of single-character strings ('1'-'9' or '.').

        Returns:
            None. The solution is written into `board`.

        Example:
            >>> b = [["5","3",".",".","7",".",".",".","."],
            ...      ["6",".",".","1","9","5",".",".","."],
            ...      [".","9","8",".",".",".",".","6","."],
            ...      ["8",".",".",".","6",".",".",".","3"],
            ...      ["4",".",".","8",".","3",".",".","1"],
            ...      ["7",".",".",".","2",".",".",".","6"],
            ...      [".","6",".",".",".",".","2","8","."],
            ...      [".",".",".","4","1","9",".",".","5"],
            ...      [".",".",".",".","8",".",".","7","9"]]
            >>> Solution().solveSudoku(b)
            >>> b[0][2]
            '4'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    Solution().solveSudoku(board)
    # Expected: board fully filled; e.g. board[0] == ['5','3','4','6','7','8','9','1','2']
    for row in board:
        print(row)
