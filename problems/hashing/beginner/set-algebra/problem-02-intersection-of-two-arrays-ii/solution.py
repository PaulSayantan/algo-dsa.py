"""Intersection of Two Arrays II — LeetCode 350 (keep multiplicities)."""
from collections import Counter  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TODO: count one array, then consume matches from the other
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1, 2, 2, 1], [2, 2]))  # expected: [2, 2]
    print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # expected: [4, 9]
    print(sol.intersect([1, 2, 2, 1], [1, 1, 1]))  # expected: [1, 1]
