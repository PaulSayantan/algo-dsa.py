"""K Closest Points to Origin (LeetCode 973).

Return the k points closest to (0, 0) in any order. Recommended: a size-k max-heap keyed
on SQUARED distance (no sqrt needed), giving O(n log k).
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the k points nearest to the origin (order does not matter).

        Args:
            points: A list of [x, y] coordinate pairs.
            k: How many nearest points to return.

        Returns:
            A list of the k points with the smallest Euclidean distance to (0, 0).

        Example:
            kClosest([[3, 3], [5, -1], [-2, 4]], 2) -> [[3, 3], [-2, 4]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))              # expected: [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))     # expected (any order): [[3, 3], [-2, 4]]
