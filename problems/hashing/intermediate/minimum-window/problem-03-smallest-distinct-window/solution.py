"""Smallest subarray containing all distinct elements of the array."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def smallestDistinctWindow(self, arr: List[int]) -> int:
        # TODO: total = number of distinct values; shrink each covering window; keep the min length
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestDistinctWindow([1, 2, 2, 3, 1]))  # expected: 3
    print(sol.smallestDistinctWindow([1, 1, 1]))  # expected: 1
    print(sol.smallestDistinctWindow([1, 2, 3, 4]))  # expected: 4
    print(sol.smallestDistinctWindow([4, 3, 2, 1, 2, 3, 4]))  # expected: 4
