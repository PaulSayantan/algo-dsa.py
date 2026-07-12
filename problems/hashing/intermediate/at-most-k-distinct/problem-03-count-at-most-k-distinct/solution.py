"""Count subarrays with at most K distinct integers (classic subroutine)."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def atMostKDistinct(self, nums: List[int], k: int) -> int:
        # TODO: for each right, add (right - left + 1) valid subarrays ending at right
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.atMostKDistinct([1, 2, 1, 2, 3], 2))  # expected: 12
    print(sol.atMostKDistinct([1, 2, 1, 2, 3], 1))  # expected: 5
    print(sol.atMostKDistinct([1, 2, 3, 4], 2))  # expected: 7
    print(sol.atMostKDistinct([5, 5, 5], 1))  # expected: 6
