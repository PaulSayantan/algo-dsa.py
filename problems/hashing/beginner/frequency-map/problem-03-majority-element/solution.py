"""Majority Element — LeetCode 169."""
from typing import List  # noqa: F401


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TODO: return the element that appears more than n/2 times
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))  # expected: 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # expected: 2
    print(sol.majorityElement([1]))  # expected: 1
    print(sol.majorityElement([6, 6, 6, 7, 7]))  # expected: 6
