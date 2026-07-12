"""Relative Sort Array — LeetCode 1122. Order arr1 by each value's index in arr2."""
from typing import List  # noqa: F401


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # TODO: build value -> rank map from arr2; sort by (rank, value)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))  # expected: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    print(sol.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))  # expected: [22, 28, 8, 6, 17, 44]
    print(sol.relativeSortArray([1, 2, 3], []))  # expected: [1, 2, 3]
    print(sol.relativeSortArray([5, 3, 1, 2, 4], [4, 2]))  # expected: [4, 2, 1, 3, 5]
