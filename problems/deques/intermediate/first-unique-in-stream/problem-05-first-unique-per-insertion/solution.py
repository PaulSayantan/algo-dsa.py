"""First Unique Stream Tracker — design (add / first / numUnique)."""
from collections import deque  # noqa: F401
from typing import Optional  # noqa: F401


class FirstUniqueStream:
    def __init__(self) -> None:
        # TODO: counts + a deque of candidate values + a running unique counter
        pass

    def add(self, value: int) -> None:
        # TODO: bump the count; enqueue on first sight, adjust the unique counter
        pass

    def first(self) -> Optional[int]:
        # TODO: drop stale fronts, then return the front (or None)
        pass

    def numUnique(self) -> int:
        # TODO: return the running count of currently-unique values
        pass


if __name__ == "__main__":
    s = FirstUniqueStream()
    print(s.first())  # expected: None
    s.add(4)
    s.add(7)
    print(s.first())  # expected: 4
    print(s.numUnique())  # expected: 2
    s.add(4)
    print(s.first())  # expected: 7
    print(s.numUnique())  # expected: 1
    s.add(7)
    print(s.first())  # expected: None
    print(s.numUnique())  # expected: 0
    s.add(9)
    print(s.first())  # expected: 9
    print(s.numUnique())  # expected: 1
