"""Intersection of Three Sorted Arrays — LeetCode 1213."""
from typing import List  # noqa: F401


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # TODO: intersect the three sets (or 3-pointer merge)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.arraysIntersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))  # expected: [1, 5]
    print(sol.arraysIntersection([197, 418, 523, 876, 1356], [501, 880, 1593, 1710, 1870], [521, 682, 1337, 1395, 1764]))  # expected: []
