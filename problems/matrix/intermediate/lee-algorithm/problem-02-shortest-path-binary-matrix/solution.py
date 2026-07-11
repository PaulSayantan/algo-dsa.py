"""Shortest Path in Binary Matrix (LeetCode 1091).

Fill in the body using the Lee Algorithm (8-directional BFS). Do not modify the
signature.
"""
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Return the length (in cells) of the shortest 8-connected clear path.

        A clear path runs from (0, 0) to (n-1, n-1), visiting only cells equal
        to 0, moving to any of the 8 neighbours. The length counts the number
        of visited cells including both endpoints.

        Args:
            grid: An n x n binary matrix where 0 is walkable and 1 is blocked.

        Returns:
            The number of cells on the shortest clear path, or -1 if none
            exists (including when the start or end cell is blocked).

        Example:
            >>> Solution().shortestPathBinaryMatrix([[0, 0, 0],
            ...                                      [1, 1, 0],
            ...                                      [1, 1, 0]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))            # expected: 2
    print(sol.shortestPathBinaryMatrix([[0, 0, 0],
                                        [1, 1, 0],
                                        [1, 1, 0]]))                 # expected: 4
    print(sol.shortestPathBinaryMatrix([[1, 0, 0],
                                        [1, 1, 0],
                                        [1, 1, 0]]))                 # expected: -1
