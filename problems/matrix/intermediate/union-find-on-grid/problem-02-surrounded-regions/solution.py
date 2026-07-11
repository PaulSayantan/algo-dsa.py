"""LeetCode 130 - Surrounded Regions.

Solve with Union-Find on Grid plus one virtual "border" node. Union every
border 'O' to that virtual node, union adjacent 'O's, then flip any 'O' whose
root differs from the virtual node's root.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Capture all regions of 'O' that are fully surrounded by 'X'.

        The board is modified in place; there is no return value.

        Args:
            board: An m x n grid of 'X' and 'O' characters. Mutated in place so
                that every enclosed 'O' becomes 'X' and every border-connected
                'O' is left unchanged.

        Returns:
            None. The transformation is applied in place to ``board``.

        Example:
            >>> b = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
            >>> Solution().solve(b)
            >>> b
            [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board)
    print(board)
    # expected:
    # [["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","X","X","X"],
    #  ["X","O","X","X"]]
