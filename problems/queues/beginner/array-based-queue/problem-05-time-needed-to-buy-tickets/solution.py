"""Simulate a ticket line as an array-backed FIFO queue and time person k."""
from typing import List  # noqa: F401


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # TODO: build a queue of [index, remaining]; dequeue the front, spend
        # 1 second, re-enqueue at the rear if tickets remain, and return the
        # elapsed time when person k hits 0
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.timeRequiredToBuy([2, 3, 2], 2))  # expected: 6
    print(sol.timeRequiredToBuy([5, 1, 1, 1], 0))  # expected: 8
    print(sol.timeRequiredToBuy([1], 0))  # expected: 1
    print(sol.timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3))  # expected: 154
