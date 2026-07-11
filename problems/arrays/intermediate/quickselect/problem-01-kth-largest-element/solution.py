"""Kth Largest Element in an Array (LeetCode 215).

Fill in the body of `findKthLargest` using Quickselect.
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element of `nums`.

        Args:
            nums: An unsorted list of integers.
            k: 1-indexed rank counting from the largest element
                (k = 1 -> the maximum).

        Returns:
            The value that would occupy position k when `nums` is sorted in
            non-increasing order (equivalently, the element at index len(nums) - k
            when sorted ascending).

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
        """
        # TODO: implement using Quickselect
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))          # expected: 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)) # expected: 4
    print(sol.findKthLargest([1], 1))                          # expected: 1
