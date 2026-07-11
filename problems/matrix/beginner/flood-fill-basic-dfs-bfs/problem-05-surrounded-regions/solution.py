"""Surrounded Regions — LeetCode 130.

Fill in the body of `solve`. Do not hard-code answers; implement the traversal
so it works for any valid input. The board must be modified in place.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Capture every 'O' region not connected to the border, in place.

        A region of 'O' cells is captured (flipped to 'X') iff none of its
        cells touch the border. 'O' regions connected 4-directionally to a
        border 'O' are safe and left unchanged.

        Args:
            board: An m x n grid of 'X' and 'O' characters. Mutated in place.

        Returns:
            None. The transformation is applied directly to `board`.

        Example:
            board = [["X","X","X"],
                     ["X","O","X"],
                     ["X","X","X"]]
            # after solve -> [["X","X","X"],
            #                 ["X","X","X"],
            #                 ["X","X","X"]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    b = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    sol.solve(b)
    print(b)
    # Expected: [["X","X","X","X"],
    #            ["X","X","X","X"],
    #            ["X","X","X","X"],
    #            ["X","O","X","X"]]
