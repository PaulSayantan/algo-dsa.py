"""LeetCode 973 - K Closest Points to Origin.

Return the k closest points using Quickselect on squared distance.
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the k points closest to the origin (0, 0).

        Args:
            points: List of [x, y] coordinate pairs.
            k: Number of closest points to return (1 <= k <= len(points)).

        Returns:
            A list of the k closest points, in any order.

        Example:
            >>> Solution().kClosest([[1, 3], [-2, 2]], 1)
            [[-2, 2]]
        """
        # TODO: implement
        # Hint: use squared distance x*x + y*y as the key (no sqrt needed).
        # Quickselect to place the k smallest-distance points in points[:k],
        # then return points[:k].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))              # expected: [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))     # expected (any order): [[3, 3], [-2, 4]]
    print(sol.kClosest([[0, 1], [1, 0]], 2))               # expected (any order): [[0, 1], [1, 0]]
