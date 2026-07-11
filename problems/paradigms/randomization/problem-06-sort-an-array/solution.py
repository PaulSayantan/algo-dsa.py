"""LeetCode 912 - Sort an Array.

Sort the array in ascending order without built-in sort functions, in O(n log n) expected
time. Use randomized quicksort (random pivot); three-way partitioning handles many
duplicates gracefully.
"""

from __future__ import annotations

from typing import List


class Solution:
    """Sort an integer array using randomized quicksort."""

    def sortArray(self, nums: List[int]) -> List[int]:
        """Return nums sorted in ascending order.

        Do not use built-in sorting functions. Target O(n log n) expected time
        with a randomly chosen pivot so adversarial inputs cannot force O(n^2).

        Args:
            nums: The array of integers to sort (may contain duplicates).

        Returns:
            The same elements arranged in non-decreasing order.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
            >>> Solution().sortArray([5, 1, 1, 2, 0, 0])
            [0, 0, 1, 1, 2, 5]
        """
        # TODO: implement (randomized quicksort with a random pivot)
        pass


if __name__ == "__main__":
    print(Solution().sortArray([5, 2, 3, 1]))          # expected: [1, 2, 3, 5]
    print(Solution().sortArray([5, 1, 1, 2, 0, 0]))    # expected: [0, 0, 1, 1, 2, 5]
    print(Solution().sortArray([3, 3, 3]))             # expected: [3, 3, 3]
