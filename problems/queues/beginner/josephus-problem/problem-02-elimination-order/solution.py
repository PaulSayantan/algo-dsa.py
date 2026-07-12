"""Josephus elimination order: the people removed, in the order they are removed."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def eliminationOrder(self, n: int, k: int) -> List[int]:
        # TODO: same rotate-k-1-then-remove loop, but record each removed person;
        # the single survivor is NOT included in the returned list
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.eliminationOrder(7, 3))  # expected: [3, 6, 2, 7, 5, 1]
    print(sol.eliminationOrder(5, 2))  # expected: [2, 4, 1, 5]
    print(sol.eliminationOrder(4, 2))  # expected: [2, 4, 3]
