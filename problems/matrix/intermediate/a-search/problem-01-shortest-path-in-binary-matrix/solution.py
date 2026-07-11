"""Shortest Path in Binary Matrix — LeetCode 1091.

Empty solution template. Fill in `shortestPathBinaryMatrix`.
"""

from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Return the length (number of cells) of the shortest 8-directional clear path
        from the top-left corner to the bottom-right corner, or -1 if none exists.

        A clear path only visits cells whose value is 0, and consecutive cells must be
        8-directionally adjacent (sharing an edge or a corner).

        Args:
            grid: An n x n binary matrix; 0 means passable, 1 means blocked.

        Returns:
            The number of cells on the shortest clear path from (0, 0) to (n-1, n-1),
            or -1 if the corner is unreachable.

        Example:
            >>> Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
            4
        """
        # TODO: implement using A* Search with a Chebyshev-distance heuristic.
        pass


if __name__ == "__main__":
    print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    # Expected: 2
    print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # Expected: 4
    print(Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # Expected: -1
