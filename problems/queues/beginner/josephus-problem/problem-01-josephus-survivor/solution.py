"""Josephus survivor via circular-queue simulation; return the 1-indexed survivor."""
from collections import deque  # noqa: F401


class Solution:
    def josephus(self, n: int, k: int) -> int:
        # TODO: seat 1..n in a queue; repeatedly rotate k-1 people to the back and
        # remove the k-th, until one remains — that is the survivor
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.josephus(7, 3))  # expected: 4
    print(sol.josephus(5, 2))  # expected: 3
    print(sol.josephus(6, 2))  # expected: 5
    print(sol.josephus(1, 5))  # expected: 1
