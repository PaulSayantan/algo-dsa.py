"""LeetCode 977 - Squares of a Sorted Array.

Return the sorted squares in O(n) using the Two-Pointer Merge technique
(two pointers walking inward from both ends). Fill in `sortedSquares`.
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Return the squares of nums, sorted in non-decreasing order.

        Args:
            nums: A list of integers sorted in non-decreasing order (may contain
                negatives).

        Returns:
            A new list containing each element squared, sorted non-decreasing.

        Example:
            >>> Solution().sortedSquares([-4, -1, 0, 3, 10])
            [0, 1, 9, 16, 100]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.sortedSquares([-4, -1, 0, 3, 10]))  # expected: [0, 1, 9, 16, 100]
    print(s.sortedSquares([-7, -3, 2, 3, 11]))  # expected: [4, 9, 9, 49, 121]
    print(s.sortedSquares([-5, -3, -2, -1]))    # expected: [1, 4, 9, 25]
