from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Return the length of the shortest 8-directional clear path.

        A clear path goes from (0,0) to (n-1,n-1) stepping only on cells valued
        0, moving to any of the 8 neighboring cells. Path length is the number
        of cells visited, inclusive of both endpoints.

        Args:
            grid: An n x n binary matrix of 0s (open) and 1s (blocked).

        Returns:
            The shortest clear-path length, or -1 if no such path exists.

        Example:
            >>> Solution().shortestPathBinaryMatrix([[0,0,0],
            ...                                      [1,1,0],
            ...                                      [1,1,0]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    # Expected: 2
    print(sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # Expected: 4
    print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # Expected: -1
