"""Count the number of maximal consecutive runs in a set of integers."""
from typing import List  # noqa: F401


class Solution:
    def countConsecutiveRuns(self, nums: List[int]) -> int:
        # TODO: each run-start is a value x with x-1 absent; count them
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countConsecutiveRuns([1, 2, 3, 10, 11, 20]))  # expected: 3
    print(sol.countConsecutiveRuns([1, 2, 3, 4]))  # expected: 1
    print(sol.countConsecutiveRuns([]))  # expected: 0
    print(sol.countConsecutiveRuns([5, 7, 9]))  # expected: 3
    print(sol.countConsecutiveRuns([1, 1, 2]))  # expected: 1
