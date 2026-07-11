"""Kth Largest Element — partial Selection Sort (LeetCode 215).

Return the k-th largest value using only k selection passes.
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element using a partial Selection Sort.

        Args:
            nums: The list of integers (may contain duplicates).
            k: 1-based rank counted from the largest element; 1 <= k <= len(nums).

        Returns:
            The value that would sit at position k when nums is sorted in
            descending order (duplicates counted).

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))              # expected: 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # expected: 4
    print(sol.findKthLargest([1], 1))                             # expected: 1
