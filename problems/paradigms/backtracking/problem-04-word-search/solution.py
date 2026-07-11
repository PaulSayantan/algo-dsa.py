"""LeetCode 79 - Word Search.

Fill in the body of `exist` using backtracking (DFS with visited marking and
undo). Do not hard-code answers.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Return whether `word` can be traced through adjacent grid cells.

        Cells are adjacent horizontally or vertically. A single cell may not be
        reused within one traced path.

        Args:
            board: An m x n grid of single-character strings.
            word: The target string to spell out along a connected path.

        Returns:
            True if such a path exists, False otherwise.

        Example:
            >>> b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            >>> Solution().exist(b, "ABCCED")
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    print(sol.exist(board, "ABCCED"))  # Expected: True
    print(sol.exist(board, "SEE"))     # Expected: True
    print(sol.exist(board, "ABCB"))    # Expected: False
