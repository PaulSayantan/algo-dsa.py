"""Asteroids — Minimum Beam Shots (minimum vertex cover via König's theorem).

Fill in `min_shots` using a Max-Flow / Min-Cut on Grid model: build a bipartite
graph of rows vs columns with one edge per asteroid, then return the maximum
matching size (= minimum vertex cover = minimum number of shots).
"""

from typing import List


class Solution:
    def min_shots(self, n: int, asteroids: List[List[int]]) -> int:
        """Return the minimum number of row/column beam shots to clear all asteroids.

        Each shot destroys every asteroid in one full row or one full column.

        Args:
            n: The grid is n x n, with rows and columns indexed 0..n-1.
            asteroids: A list of [r, c] coordinates, one per asteroid (no duplicates).

        Returns:
            The minimum number of shots needed to destroy every asteroid.

        Example:
            >>> Solution().min_shots(3, [[0,1],[1,0],[1,1],[1,2],[2,1]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.min_shots(3, [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]))  # expected: 2
    print(sol.min_shots(3, [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))  # expected: 3
    print(sol.min_shots(2, []))                                        # expected: 0
