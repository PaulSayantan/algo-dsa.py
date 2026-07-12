"""Return the sum of the longest consecutive run (smallest start on ties)."""
from typing import List  # noqa: F401


class Solution:
    def sumOfLongestRun(self, nums: List[int]) -> int:
        # TODO: find the longest run, then sum its consecutive values
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfLongestRun([100, 4, 200, 1, 3, 2]))  # expected: 10
    print(sol.sumOfLongestRun([]))  # expected: 0
    print(sol.sumOfLongestRun([10, 11, 12, 100]))  # expected: 33
    print(sol.sumOfLongestRun([5, 6, 1, 2, 3]))  # expected: 6
