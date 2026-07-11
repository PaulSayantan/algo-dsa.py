"""LeetCode 912 - Sort an Array.

Implement Quick Sort from scratch (no built-in sort).
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort the array in ascending order using Quick Sort.

        Args:
            nums: List of integers to sort. May contain duplicates and
                negative values.

        Returns:
            The same list sorted in non-decreasing (ascending) order.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        # TODO: implement
        # Hint: write a partition(lo, hi) helper that places a (ideally random)
        # pivot in its final position, then recursively quicksort(lo, p - 1)
        # and quicksort(p + 1, hi).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray([5, 2, 3, 1]))          # expected: [1, 2, 3, 5]
    print(sol.sortArray([5, 1, 1, 2, 0, 0]))    # expected: [0, 0, 1, 1, 2, 5]
    print(sol.sortArray([3]))                    # expected: [3]
