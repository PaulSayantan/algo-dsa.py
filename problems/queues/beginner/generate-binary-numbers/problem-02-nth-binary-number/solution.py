"""Return the n-th binary number (1-indexed) produced by the queue generation."""
from collections import deque  # noqa: F401


class Solution:
    def nthBinary(self, n: int) -> str:
        # TODO: run the same queue BFS n times; the last dequeued string is the answer
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nthBinary(1))  # expected: '1'
    print(sol.nthBinary(5))  # expected: '101'
    print(sol.nthBinary(10))  # expected: '1010'
