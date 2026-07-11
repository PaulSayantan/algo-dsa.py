"""LeetCode 289 — Game of Life.

Fill in the body of `gameOfLife`. Aim for the O(1) extra-space approach that
encodes both the old and the new state of each cell in a single integer.
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Advance the board one generation, in place.

        All cells transition simultaneously, so a cell's new value must not be
        written in a way that hides its old value from neighbors that still need
        it. Target solution packs both states into one cell (e.g. bit 0 = old
        state, bit 1 = next state, or the encoding ``next * 2 + old``), counts
        neighbors from the old bit, then extracts the new state in a final pass.

        Args:
            board: An ``m x n`` grid where each cell is ``0`` (dead) or ``1``
                   (live). Modified in place.

        Returns:
            None. ``board`` holds the next generation after the call.

        Example:
            >>> b = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
            >>> Solution().gameOfLife(b)
            >>> b
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    b1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(b1)
    print(b1)  # expected: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    b2 = [[1, 1], [1, 0]]
    sol.gameOfLife(b2)
    print(b2)  # expected: [[1, 1], [1, 1]]

    b3 = [[0]]
    sol.gameOfLife(b3)
    print(b3)  # expected: [[0]]
