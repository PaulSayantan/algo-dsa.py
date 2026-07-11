"""Word Search (LeetCode 79).

Empty solution template — fill in the backtracking logic yourself.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Return True if `word` can be traced through adjacent board cells.

        Adjacent means horizontally or vertically neighboring. A cell may not
        be reused within a single word.

        Args:
            board: An m x n grid of single-character strings.
            word: The target string to search for.

        Returns:
            True if the word exists in the grid, otherwise False.

        Example:
            >>> Solution().exist(
            ...     [["A", "B", "C", "E"],
            ...      ["S", "F", "C", "S"],
            ...      ["A", "D", "E", "E"]],
            ...     "ABCCED",
            ... )
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print(Solution().exist(board, "ABCCED"))  # Expected: True
    print(Solution().exist(board, "ABCB"))    # Expected: False
    print(Solution().exist([["a"]], "a"))     # Expected: True
