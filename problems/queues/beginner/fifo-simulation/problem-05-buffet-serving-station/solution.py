"""Buffet Serving Station: count guests left unsatisfied when servings run out."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def unservedGuests(self, hunger: List[int], servings: int) -> int:
        # TODO: FIFO queue of remaining portions per guest; each step serve one
        # portion to the front guest (spend one serving) and re-enqueue if they
        # still want more. Stop when servings hit 0 and return how many remain.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.unservedGuests([1, 2, 1], 3))  # expected: 1
    print(sol.unservedGuests([2, 3, 2], 4))  # expected: 2
    print(sol.unservedGuests([2, 2], 10))  # expected: 0
    print(sol.unservedGuests([3, 1], 2))  # expected: 1
    print(sol.unservedGuests([1, 1, 1], 0))  # expected: 3
