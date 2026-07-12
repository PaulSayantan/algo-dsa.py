"""Create Maximum Number — LeetCode 321."""
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # TODO: pick max length-t subsequence per array (drop-stack), then merge
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))  # expected: [9, 8, 6, 5, 3]
    print(sol.maxNumber([6, 7], [6, 0, 4], 5))  # expected: [6, 7, 6, 0, 4]
    print(sol.maxNumber([3, 9], [8, 9], 3))  # expected: [9, 8, 9]
