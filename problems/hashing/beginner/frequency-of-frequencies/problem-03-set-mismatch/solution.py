"""Set Mismatch — LeetCode 645."""
from collections import Counter  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # TODO: count 1..n; the value seen twice and the value seen zero times
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findErrorNums([1, 2, 2, 4]))  # expected: [2, 3]
    print(sol.findErrorNums([1, 1]))  # expected: [1, 2]
    print(sol.findErrorNums([3, 2, 3, 4, 6, 5]))  # expected: [3, 1]
