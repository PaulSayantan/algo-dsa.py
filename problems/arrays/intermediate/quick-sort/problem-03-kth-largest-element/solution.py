"""LeetCode 215 - Kth Largest Element in an Array.

Find the k-th largest element using Quickselect (a Quick Sort variant).
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element in nums.

        Args:
            nums: List of integers (may contain duplicates).
            k: 1-based rank counted from the largest element
                (k = 1 -> the maximum).

        Returns:
            The value that would sit at position (len(nums) - k) if nums were
            sorted in ascending order.

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
        """
        # TODO: implement
        # Hint: the k-th largest sits at ascending index target = len(nums) - k.
        # Partition around a random pivot; if the pivot's final index == target
        # you are done, otherwise recurse into the single side containing target.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))               # expected: 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))      # expected: 4
    print(sol.findKthLargest([1], 1))                              # expected: 1
