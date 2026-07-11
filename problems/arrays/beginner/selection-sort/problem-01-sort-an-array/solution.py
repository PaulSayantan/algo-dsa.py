"""Sort an Array — Selection Sort (LeetCode 912).

Implement Selection Sort to return `nums` in ascending order.
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort an integer array in ascending order using Selection Sort.

        Args:
            nums: The list of integers to sort. May contain duplicates and
                negative values.

        Returns:
            The list sorted in non-decreasing (ascending) order. Sorting in
            place and returning `nums` is acceptable.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray([5, 2, 3, 1]))          # expected: [1, 2, 3, 5]
    print(sol.sortArray([5, 1, 1, 2, 0, 0]))    # expected: [0, 0, 1, 1, 2, 5]
    print(sol.sortArray([-3, 0, -3, 7]))        # expected: [-3, -3, 0, 7]
