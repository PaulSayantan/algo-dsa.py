"""K Closest Points to Origin — LeetCode 973.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the k points closest to the origin (0, 0).

        Distance is Euclidean; comparing squared distances is sufficient and
        avoids floating-point square roots. The answer may be in any order.

        Args:
            points: List of [x, y] coordinate pairs.
            k: Number of closest points to return (1 <= k <= len(points)).

        Returns:
            A list of the k points nearest the origin, in any order.

        Example:
            >>> Solution().kClosest([[1, 3], [-2, 2]], 1)
            [[-2, 2]]
            >>> sorted(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
            [[-2, 4], [3, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))            # expected: [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))   # expected (any order): [[3, 3], [-2, 4]]
