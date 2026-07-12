"""Return the binary strings for the integers low..high (inclusive) using a queue."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def binaryRange(self, low: int, high: int) -> List[str]:
        # TODO: run the queue BFS high times; keep only dequeues at positions low..high (1-indexed)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.binaryRange(3, 6))  # expected: ['11', '100', '101', '110']
    print(sol.binaryRange(1, 3))  # expected: ['1', '10', '11']
    print(sol.binaryRange(5, 5))  # expected: ['101']
    print(sol.binaryRange(1, 1))  # expected: ['1']
