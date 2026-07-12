"""Intersection of Two Arrays — LeetCode 349."""
from typing import List  # noqa: F401


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TODO: build two sets and take their intersection
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1, 2, 2, 1], [2, 2]))  # expected: [2]
    print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # expected: [4, 9]
    print(sol.intersection([1, 2, 3], [4, 5, 6]))  # expected: []
