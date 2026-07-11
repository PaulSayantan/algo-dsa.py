"""Kth Largest Element in an Array — LeetCode 215.

Empty solution template. Solve it with quickselect (Divide and Conquer);
avoid fully sorting the array.
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element (duplicates counted) in nums.

        Use quickselect: partition around a pivot and recurse into only the
        side that must contain the k-th largest element.

        Args:
            nums: List of integers.
            k: 1-based rank from the largest end (1 == the maximum).

        Returns:
            The k-th largest element in sorted order.

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
            >>> Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))              # expected: 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))    # expected: 4
    print(sol.findKthLargest([1], 1))                            # expected: 1
