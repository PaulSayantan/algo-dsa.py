"""A deque used BOTH as a stack (LIFO, one end) and as a queue (FIFO, two ends)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def asStack(self, values: List[int]) -> List[int]:
        # TODO: append all, then pop from the SAME end -> LIFO (reversed)
        pass

    def asQueue(self, values: List[int]) -> List[int]:
        # TODO: append all, then popleft from the OPPOSITE end -> FIFO (same order)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.asStack([1, 2, 3, 4]))  # expected: [4, 3, 2, 1]
    print(sol.asQueue([1, 2, 3, 4]))  # expected: [1, 2, 3, 4]
    print(sol.asStack([]))  # expected: []
    print(sol.asQueue([9]))  # expected: [9]
