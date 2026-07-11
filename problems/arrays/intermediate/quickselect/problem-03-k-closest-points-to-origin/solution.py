"""K Closest Points to Origin (LeetCode 973).

Fill in the body of `kClosest` using Quickselect on squared distances.
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the k points closest to the origin (0, 0).

        Args:
            points: A list of [x, y] coordinate pairs.
            k: How many of the nearest points to return (1 <= k <= len(points)).

        Returns:
            A list of the k points with the smallest Euclidean distance to the
            origin, in any order.

        Example:
            >>> Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)
            [[3, 3], [-2, 4]]
        """
        # TODO: implement using Quickselect (compare by squared distance x*x + y*y)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))            # expected: [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))   # expected (any order): [[3, 3], [-2, 4]]
