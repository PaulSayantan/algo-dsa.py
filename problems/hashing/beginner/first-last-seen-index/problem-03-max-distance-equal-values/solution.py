"""Maximum Distance Between Equal Values. Largest j - i with nums[i] == nums[j]."""
from typing import List  # noqa: F401


class Solution:
    def maxEqualDistance(self, nums: List[int]) -> int:
        # TODO: record each value's FIRST index; the farthest later match wins
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEqualDistance([1, 2, 3, 1, 2, 3]))  # expected: 3
    print(sol.maxEqualDistance([1, 1, 1, 1]))  # expected: 3
    print(sol.maxEqualDistance([1, 2, 3, 4]))  # expected: 0
    print(sol.maxEqualDistance([5]))  # expected: 0
    print(sol.maxEqualDistance([3, 1, 3, 1, 3]))  # expected: 4
