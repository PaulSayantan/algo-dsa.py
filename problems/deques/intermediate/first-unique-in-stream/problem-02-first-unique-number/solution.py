"""First Unique Number — LeetCode 1429 (design)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class FirstUnique:
    def __init__(self, nums: List[int]) -> None:
        # TODO: counts + a deque of candidate values (oldest first)
        pass

    def showFirstUnique(self) -> int:
        # TODO: drop stale fronts, then return the front (or -1)
        pass

    def add(self, value: int) -> None:
        # TODO: bump the count; enqueue when first seen
        pass


if __name__ == "__main__":
    fu = FirstUnique([2, 3, 5])
    print(fu.showFirstUnique())  # expected: 2
    fu.add(5)
    print(fu.showFirstUnique())  # expected: 2
    fu.add(2)
    print(fu.showFirstUnique())  # expected: 3
    fu.add(3)
    print(fu.showFirstUnique())  # expected: -1
