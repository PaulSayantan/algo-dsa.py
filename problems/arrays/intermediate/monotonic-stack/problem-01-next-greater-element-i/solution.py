"""Next Greater Element I — LeetCode 496.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Find the next greater element of each nums1 value within nums2.

        For every value ``nums1[i]``, locate it in ``nums2`` and return the first
        element strictly greater than it that appears to its right in ``nums2``,
        or ``-1`` if none exists.

        Args:
            nums1: A list of distinct integers, each of which appears in nums2.
            nums2: A list of distinct integers containing all of nums1's values.

        Returns:
            A list ``ans`` where ``ans[i]`` is the next greater element of
            ``nums1[i]`` in ``nums2``, or ``-1`` when there is none.

        Example:
            >>> Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
            [-1, 3, -1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # expected: [-1, 3, -1]
    print(sol.nextGreaterElement([2, 4], [1, 2, 3, 4]))      # expected: [3, -1]
