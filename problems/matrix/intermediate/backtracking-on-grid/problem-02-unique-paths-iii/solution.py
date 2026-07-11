"""Unique Paths III (LeetCode 980).

Empty solution template — fill in the backtracking logic yourself.
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """Count 4-directional walks from start (1) to end (2) that cover
        every non-obstacle square exactly once.

        Cell values: 1 = start, 2 = end, 0 = empty (walkable), -1 = obstacle.

        Args:
            grid: An m x n integer grid using the encoding above.

        Returns:
            The number of valid walks that visit every non-obstacle square
            exactly once and terminate on the end square.

        Example:
            >>> Solution().uniquePathsIII(
            ...     [[1, 0, 0, 0],
            ...      [0, 0, 0, 0],
            ...      [0, 0, 2, -1]],
            ... )
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().uniquePathsIII([[1, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 2, -1]]))  # Expected: 2
    print(Solution().uniquePathsIII([[1, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 2]]))    # Expected: 4
    print(Solution().uniquePathsIII([[0, 1],
                                     [2, 0]]))          # Expected: 0
