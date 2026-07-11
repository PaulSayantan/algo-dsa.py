"""Surrounded Regions — LeetCode 130.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Capture all 'O' regions fully surrounded by 'X', in place.

        An 'O' survives only if it is connected (4-directionally) to an 'O'
        on the border of the board.

        Args:
            board: An ``m x n`` grid of the characters 'X' and 'O'. Modified
                in place; the function returns nothing.

        Returns:
            None. The ``board`` argument is mutated directly.

        Example:
            >>> b = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
            >>> Solution().solve(b)
            >>> b
            [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    sol.solve(board1)
    print(board1)
    # Expected: [["X","X","X","X"],
    #            ["X","X","X","X"],
    #            ["X","X","X","X"],
    #            ["X","O","X","X"]]

    board3 = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
    sol.solve(board3)
    print(board3)
    # Expected: unchanged — every 'O' touches the border
