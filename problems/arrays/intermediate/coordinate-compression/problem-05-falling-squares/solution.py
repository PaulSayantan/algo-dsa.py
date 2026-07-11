"""Falling Squares (LeetCode 699).

Fill in the body of `fallingSquares`. The intended approach compresses the square
edges and runs a segment tree (or an O(n^2) interval scan). Do NOT read SOLUTION.md
until you have attempted it.
"""

from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """Return the tallest stack height after each square is dropped.

        Args:
            positions: A list of [left, sideLength] pairs, one per square, in the
                order they are dropped.

        Returns:
            A list ``ans`` where ``ans[i]`` is the maximum height of any square after
            dropping the first ``i + 1`` squares.

        Example:
            >>> Solution().fallingSquares([[1, 2], [2, 3], [6, 1]])
            [2, 5, 5]
        """
        # TODO: implement
        # Hint: collect and compress all edges {left, left+side}. A square covering
        #       [left, right) rests on 1 + max-height over that half-open interval,
        #       then that interval is raised to the new top.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fallingSquares([[1, 2], [2, 3], [6, 1]]))  # expected: [2, 5, 5]
    print(sol.fallingSquares([[100, 100], [200, 100]]))  # expected: [100, 100]
