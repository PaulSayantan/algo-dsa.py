"""LFU cache that can also report its current keys (sorted) after a sequence of ops."""
from collections import defaultdict, OrderedDict  # noqa: F401
from typing import List  # noqa: F401


class LFUCacheKeys:
    def __init__(self, capacity: int) -> None:
        # TODO
        pass

    def get(self, key: int) -> int:
        # TODO: return value + bump frequency, else -1
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: insert/update + evict LFU (LRU tie-break) on overflow
        pass

    def keys_sorted(self) -> List[int]:
        # TODO: the keys currently resident, sorted ascending
        pass


if __name__ == "__main__":
    c = LFUCacheKeys(2)
    c.put(1, 1)
    c.put(2, 2)
    print(c.get(1))  # expected: 1
    c.put(3, 3)
    print(c.keys_sorted())  # expected: [1, 3]
    print(c.get(3))  # expected: 3
    c.put(4, 4)
    print(c.keys_sorted())  # expected: [3, 4]
