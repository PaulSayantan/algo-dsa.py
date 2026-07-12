"""Next Greater Element I — LeetCode 496."""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TODO: monotonic decreasing stack over nums2, then map nums1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # expected: [-1, 3, -1]
    print(sol.nextGreaterElement([2, 4], [1, 2, 3, 4]))  # expected: [3, -1]
