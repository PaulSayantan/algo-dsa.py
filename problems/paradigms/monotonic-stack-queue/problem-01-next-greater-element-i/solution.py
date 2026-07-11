"""Next Greater Element I — LeetCode 496.

Fill in the body of `nextGreaterElement`. Do not modify the signature.
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Return the next greater element in nums2 for each value in nums1.

        Args:
            nums1: A list of distinct integers, each of which also appears in nums2.
            nums2: A list of distinct integers to search within.

        Returns:
            A list `ans` of the same length as `nums1`, where `ans[i]` is the first
            element to the right of `nums1[i]` in `nums2` that is strictly greater
            than `nums1[i]`, or -1 if no such element exists.

        Example:
            >>> Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
            [-1, 3, -1]
        """
        # TODO: implement using a monotonic (decreasing) stack over nums2,
        # building a value -> next-greater map, then look up each nums1[i].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # expected: [-1, 3, -1]
    print(sol.nextGreaterElement([2, 4], [1, 2, 3, 4]))      # expected: [3, -1]
