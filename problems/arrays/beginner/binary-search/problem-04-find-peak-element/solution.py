"""LeetCode 162 - Find Peak Element.

Return the index of any peak element (strictly greater than its neighbors) in
O(log n) time.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Return the index of any peak element in `nums`.

        A peak is strictly greater than both neighbors; out-of-bounds neighbors
        are treated as negative infinity.

        Args:
            nums: A list of integers where no two adjacent values are equal.

        Returns:
            The index of any element that is a peak.

        Example:
            >>> Solution().findPeakElement([1, 2, 3, 1])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))           # expected: 2
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # expected: 5 (or 1)
    print(sol.findPeakElement([1]))                     # expected: 0
