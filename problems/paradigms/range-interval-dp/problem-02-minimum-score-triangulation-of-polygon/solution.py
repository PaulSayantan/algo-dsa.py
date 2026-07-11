"""Minimum Score Triangulation of Polygon (LeetCode 1039).

Fill in the body of `minScoreTriangulation` using Range / Interval DP.
"""

from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """Return the minimum total score over all triangulations.

        Args:
            values: Vertex values of a convex polygon in order; length n (3..50).

        Returns:
            The smallest achievable sum of (product of the 3 vertices) over the
            n - 2 triangles of a triangulation.

        Example:
            >>> Solution().minScoreTriangulation([3, 7, 4, 5])
            144
        """
        # TODO: implement using interval DP over dp[i][j] with an apex vertex k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minScoreTriangulation([1, 2, 3]))           # expected: 6
    print(sol.minScoreTriangulation([3, 7, 4, 5]))        # expected: 144
    print(sol.minScoreTriangulation([1, 3, 1, 4, 1, 5]))  # expected: 13
