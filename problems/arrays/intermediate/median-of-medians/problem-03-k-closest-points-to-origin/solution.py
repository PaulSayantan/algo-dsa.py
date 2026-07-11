"""K Closest Points to Origin (LeetCode 973).

Return the k points closest to the origin in worst-case O(n) time by selecting
the k-th smallest squared distance with the Median of Medians algorithm.
"""
from typing import List


class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the ``k`` points nearest to the origin (0, 0).

        Points are ranked by squared Euclidean distance ``x*x + y*y``. The
        returned points may be in any order; any valid set of k closest points
        is accepted.

        Args:
            points: List of ``[x, y]`` integer coordinate pairs.
            k: Number of closest points to return (1 <= k <= len(points)).

        Returns:
            A list of ``k`` points closest to the origin, in any order.

        Example:
            >>> Solution().k_closest([[3, 3], [5, -1], [-2, 4]], 2)
            [[3, 3], [-2, 4]]
        """
        # TODO: implement using Median of Medians selection on squared distances
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.k_closest([[1, 3], [-2, 2]], 1))              # expected: [[-2, 2]]
    print(sol.k_closest([[3, 3], [5, -1], [-2, 4]], 2))     # expected (any order): [[3, 3], [-2, 4]]
