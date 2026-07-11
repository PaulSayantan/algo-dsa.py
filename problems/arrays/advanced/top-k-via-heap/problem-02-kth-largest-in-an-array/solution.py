"""Kth Largest Element in an Array (LeetCode 215).

Return the k-th largest element WITHOUT fully sorting. Recommended: a size-k min-heap
(O(n log k)) or Quickselect (O(n) average).
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element of nums (1-indexed, duplicates counted).

        Args:
            nums: The array of integers to search.
            k: The rank of the largest element to return (1 = maximum).

        Returns:
            The value that is the k-th largest in sorted (descending) order.

        Example:
            findKthLargest([3, 2, 1, 5, 6, 4], 2) -> 5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))            # expected: 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))   # expected: 4
    print(sol.findKthLargest([1], 1))                           # expected: 1
