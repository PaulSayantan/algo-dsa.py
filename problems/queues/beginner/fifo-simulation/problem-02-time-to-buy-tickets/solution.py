"""Time Needed to Buy Tickets — LeetCode 2073."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # TODO: simulate a FIFO line; each second the front buys one ticket (1s) and
        # rejoins the back if it still needs more. Stop when person k finishes.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.timeRequiredToBuy([2, 3, 2], 2))  # expected: 6
    print(sol.timeRequiredToBuy([5, 1, 1, 1], 0))  # expected: 8
    print(sol.timeRequiredToBuy([1, 1, 1, 1], 3))  # expected: 4
