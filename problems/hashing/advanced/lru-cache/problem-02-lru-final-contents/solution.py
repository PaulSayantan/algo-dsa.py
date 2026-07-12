"""LRU cache that can also report its current keys (sorted) after a sequence of ops."""
from collections import OrderedDict  # noqa: F401
from typing import List  # noqa: F401


class LRUCacheKeys:
    def __init__(self, capacity: int) -> None:
        # TODO
        pass

    def get(self, key: int) -> int:
        # TODO: return value + mark MRU, else -1
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: insert/update + evict LRU if over capacity
        pass

    def keys_sorted(self) -> List[int]:
        # TODO: the keys currently resident, sorted ascending
        pass


if __name__ == "__main__":
    c = LRUCacheKeys(3)
    c.put(1, 10)
    c.put(2, 20)
    c.put(3, 30)
    print(c.keys_sorted())  # expected: [1, 2, 3]
    c.put(4, 40)
    print(c.keys_sorted())  # expected: [2, 3, 4]
    print(c.get(2))  # expected: 20
    c.put(5, 50)
    print(c.keys_sorted())  # expected: [2, 4, 5]
