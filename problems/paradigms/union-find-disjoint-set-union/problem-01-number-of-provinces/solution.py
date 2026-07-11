"""LeetCode 547 - Number of Provinces.

Fill in the body of `findCircleNum`. The intended technique is
Union-Find (Disjoint Set Union): union every directly connected pair of
cities, then count how many distinct roots remain.
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Return the number of provinces (connected components of cities).

        Args:
            isConnected: An n x n symmetric 0/1 matrix where
                isConnected[i][j] == 1 means city i and city j are directly
                connected. The diagonal is always 1.

        Returns:
            The number of provinces: maximal groups of directly or
            indirectly connected cities.

        Example:
            >>> Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
            2
        """
        # TODO: implement using Union-Find (Disjoint Set Union)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # expected: 2
    print(sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # expected: 3
    print(sol.findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # expected: 1
