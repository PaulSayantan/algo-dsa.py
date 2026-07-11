"""Squares of a Sorted Array — LeetCode 977.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Return the squares of `nums` in non-decreasing order.

        Args:
            nums: A list of integers sorted in non-decreasing order (may include
                negatives).

        Returns:
            A new list containing the square of every element, sorted in
            non-decreasing order.

        Example:
            >>> Solution().sortedSquares([-4, -1, 0, 3, 10])
            [0, 1, 9, 16, 100]
        """
        # TODO: implement using two pointers (opposite ends)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))  # expected: [0, 1, 9, 16, 100]
    print(sol.sortedSquares([-7, -3, 2, 3, 11]))  # expected: [4, 9, 9, 49, 121]
    print(sol.sortedSquares([-5, -3, -2]))        # expected: [4, 9, 25]
