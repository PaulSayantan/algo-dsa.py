"""Wiggle Sort II (LeetCode 324).

Reorder nums in place so that nums[0] < nums[1] > nums[2] < nums[3] > ...
Find the median in worst-case O(n) with Median of Medians, then interleave the
low and high halves using a virtual index mapping.
"""
from typing import List


class Solution:
    def wiggle_sort(self, nums: List[int]) -> None:
        """Reorder ``nums`` in place into a wiggle pattern.

        After the call, ``nums`` satisfies
        ``nums[0] < nums[1] > nums[2] < nums[3] > ...``. Modifies ``nums`` in
        place and returns ``None`` (LeetCode 324 signature).

        Args:
            nums: Integer array; guaranteed to admit a valid wiggle ordering.

        Returns:
            None. The reordering is performed in place on ``nums``.

        Example:
            >>> nums = [1, 5, 1, 1, 6, 4]
            >>> Solution().wiggle_sort(nums)
            >>> nums  # e.g. [1, 6, 1, 5, 1, 4] (any valid wiggle is accepted)
        """
        # TODO: implement using Median of Medians to find the median,
        #       then a virtual-index three-way partition to interleave halves
        pass


if __name__ == "__main__":
    sol = Solution()

    a = [1, 5, 1, 1, 6, 4]
    sol.wiggle_sort(a)
    print(a)  # expected: a valid wiggle, e.g. [1, 6, 1, 5, 1, 4]

    b = [1, 3, 2, 2, 3, 1]
    sol.wiggle_sort(b)
    print(b)  # expected: a valid wiggle, e.g. [2, 3, 1, 3, 1, 2]
