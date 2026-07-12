"""Josephus circle of names: return the surviving name via circular-queue simulation."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def survivor(self, names: List[str], k: int) -> str:
        # TODO: seed a queue with the names in order; rotate k-1 to the back and
        # remove the k-th until one name remains — that is the survivor
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.survivor(["Alice", "Bob", "Carol", "Dan"], 2))  # expected: 'Alice'
    print(sol.survivor(["a", "b", "c", "d", "e"], 3))  # expected: 'd'
    print(sol.survivor(["x"], 7))  # expected: 'x'
    print(sol.survivor(["p", "q"], 3))  # expected: 'q'
