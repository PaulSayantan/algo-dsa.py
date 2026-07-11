"""Relative Sort Array — LeetCode 1122.

Sort arr1 so that elements follow the relative order given in arr2, with any
leftover values appended in ascending order.
"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Reorder arr1 according to arr2's priority ordering.

        Args:
            arr1: Values to sort. Each value is an integer in [0, 1000].
            arr2: Distinct values defining the desired relative order. Every
                element of arr2 also occurs in arr1.

        Returns:
            A list containing all elements of arr1, with values present in arr2
            appearing first in arr2's order, followed by the remaining values in
            ascending order.

        Example:
            >>> Solution().relativeSortArray(
            ...     [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
            [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
        """
        # TODO: implement using Counting Sort (values bounded by 1000).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.relativeSortArray(
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
    # expected: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    print(sol.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
    # expected: [22, 28, 8, 6, 17, 44]
