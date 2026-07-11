"""Minimum Cost to Make at Least One Valid Path in a Grid (LeetCode 1368).

Fill in the body using 0-1 BFS (a deque). Do not modify the signature.
"""
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """Return the minimum number of sign changes needed so that at least one
        path following the signs leads from (0, 0) to (m-1, n-1).

        Signs: 1=right, 2=left, 3=down, 4=up. Moving in the direction the
        current cell already points is free; any other move costs 1 (one sign
        change), and each cell's sign may be changed at most once.

        Args:
            grid: An m x n matrix of sign values in {1, 2, 3, 4}.

        Returns:
            The minimum total cost (number of sign changes).

        Example:
            >>> Solution().minCost([[1, 1, 1, 1],
            ...                     [2, 2, 2, 2],
            ...                     [1, 1, 1, 1],
            ...                     [2, 2, 2, 2]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCost([[1, 1, 1, 1],
                       [2, 2, 2, 2],
                       [1, 1, 1, 1],
                       [2, 2, 2, 2]]))          # expected: 3
    print(sol.minCost([[1, 1, 3],
                       [3, 2, 2],
                       [1, 1, 4]]))             # expected: 0
    print(sol.minCost([[1, 2],
                       [4, 3]]))                # expected: 1
