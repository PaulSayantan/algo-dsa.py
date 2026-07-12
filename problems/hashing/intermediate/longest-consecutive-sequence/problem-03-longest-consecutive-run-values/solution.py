"""Return the longest consecutive run itself (smallest start on ties)."""
from typing import List  # noqa: F401


class Solution:
    def longestConsecutiveRun(self, nums: List[int]) -> List[int]:
        # TODO: expand from each run-start; return the values of the longest run as a list
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutiveRun([100, 4, 200, 1, 3, 2]))  # expected: [1, 2, 3, 4]
    print(sol.longestConsecutiveRun([]))  # expected: []
    print(sol.longestConsecutiveRun([5, 5, 6, 6, 7]))  # expected: [5, 6, 7]
    print(sol.longestConsecutiveRun([3, 1, 2, 8, 9]))  # expected: [1, 2, 3]
    print(sol.longestConsecutiveRun([10, 20, 30]))  # expected: [10]
