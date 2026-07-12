"""Find the Difference of Two Arrays — LeetCode 2215."""
from typing import List  # noqa: F401


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # TODO: return [distinct in nums1 not nums2, distinct in nums2 not nums1]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDifference([1, 2, 3], [2, 4, 6]))  # expected: [[1, 3], [4, 6]]
    print(sol.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # expected: [[3], []]
