"""Round-robin scheduling: return completion order."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def completionOrder(self, burst: List[int], quantum: int) -> List[int]:
        # TODO: FIFO queue of (id, remaining)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.completionOrder([5, 3, 8], 3))  # expected: [1, 0, 2]
    print(sol.completionOrder([4, 4, 4], 2))  # expected: [0, 1, 2]
    print(sol.completionOrder([10], 3))  # expected: [0]
