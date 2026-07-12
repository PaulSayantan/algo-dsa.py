"""Find K Pairs with Smallest Sums — LeetCode 373."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # TODO: min-heap over candidate pairs
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))  # expected: [[1, 2], [1, 4], [1, 6]]
    print(sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))  # expected: [[1, 1], [1, 1]]
    print(sol.kSmallestPairs([1, 2], [3], 3))  # expected: [[1, 3], [2, 3]]
