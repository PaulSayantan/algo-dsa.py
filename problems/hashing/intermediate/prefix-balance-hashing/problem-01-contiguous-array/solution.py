"""Contiguous Array — LeetCode 525."""
from typing import List  # noqa: F401


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # TODO: map 0 -> -1, 1 -> +1; a balanced window has equal running balance
        #       at its ends. Store the earliest index of each balance (seed {0: -1}).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0, 1]))  # expected: 2
    print(sol.findMaxLength([0, 1, 0]))  # expected: 2
    print(sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))  # expected: 6
    print(sol.findMaxLength([1, 1, 1]))  # expected: 0
    print(sol.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))  # expected: 4
