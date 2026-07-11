"""Minimum Knight Moves — LeetCode 1197.

Empty solution template. Fill in `minKnightMoves`.
"""


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """Return the minimum number of knight moves from (0, 0) to (x, y) on an
        infinite chessboard.

        A knight moves in an L shape: two squares along one axis and one square along
        the perpendicular axis (8 possible moves).

        Args:
            x: Target column coordinate (may be negative).
            y: Target row coordinate (may be negative).

        Returns:
            The fewest knight moves needed to land exactly on (x, y).

        Example:
            >>> Solution().minKnightMoves(5, 5)
            4
        """
        # TODO: implement using A* Search with an admissible knight-distance heuristic.
        pass


if __name__ == "__main__":
    print(Solution().minKnightMoves(2, 1))
    # Expected: 1
    print(Solution().minKnightMoves(5, 5))
    # Expected: 4
    print(Solution().minKnightMoves(0, 0))
    # Expected: 0
