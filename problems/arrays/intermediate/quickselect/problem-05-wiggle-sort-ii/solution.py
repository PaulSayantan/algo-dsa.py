"""Wiggle Sort II (LeetCode 324).

Reorder `nums` in place so that
    nums[0] < nums[1] > nums[2] < nums[3] > ...
with STRICT inequalities. Fill in the body using Quickselect to find the median.
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """Reorder `nums` in place into a strict wiggle pattern.

        Do not return anything; modify `nums` in place instead.

        Args:
            nums: The list of integers to reorder. A valid arrangement is
                guaranteed to exist.

        Returns:
            None. After the call, `nums` satisfies
            nums[0] < nums[1] > nums[2] < nums[3] > ... (strict).

        Example:
            >>> nums = [1, 5, 1, 1, 6, 4]
            >>> Solution().wiggleSort(nums)
            >>> # nums is now a valid strict wiggle, e.g. [1, 6, 1, 5, 1, 4]
        """
        # TODO: implement using Quickselect to locate the median, then
        #       interleave larger-than-median values onto odd indices and
        #       smaller-than-median values onto even indices.
        pass


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 5, 1, 1, 6, 4]
    sol.wiggleSort(nums1)
    print(nums1)  # expected: a strict wiggle, e.g. [1, 6, 1, 5, 1, 4]

    nums2 = [1, 3, 2, 2, 3, 1]
    sol.wiggleSort(nums2)
    print(nums2)  # expected: a strict wiggle, e.g. [2, 3, 1, 3, 1, 2]
