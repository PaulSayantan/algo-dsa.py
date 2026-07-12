"""Grumpy Bookstore Owner — LeetCode 1052."""
from typing import List  # noqa: F401


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # TODO: base satisfied + max recoverable via a size-`minutes` sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))  # expected: 16
    print(sol.maxSatisfied([1], [0], 1))  # expected: 1
    print(sol.maxSatisfied([2, 6, 6, 9], [0, 0, 1, 1], 1))  # expected: 17
