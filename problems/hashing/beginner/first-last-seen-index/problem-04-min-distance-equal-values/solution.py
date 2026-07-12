"""Minimum Distance Between Equal Values. Smallest j - i with nums[i] == nums[j], else -1."""
from typing import List  # noqa: F401


class Solution:
    def minEqualDistance(self, nums: List[int]) -> int:
        # TODO: record each value's MOST RECENT index; closest repeat wins
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEqualDistance([1, 2, 3, 1, 2, 3]))  # expected: 3
    print(sol.minEqualDistance([1, 2, 1, 3, 1]))  # expected: 2
    print(sol.minEqualDistance([1, 2, 3, 4]))  # expected: -1
    print(sol.minEqualDistance([7, 7, 7]))  # expected: 1
    print(sol.minEqualDistance([4, 1, 2, 1, 4]))  # expected: 2
