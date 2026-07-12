"""LRU Cache — LeetCode 146. O(1) get/put with least-recently-used eviction."""
from collections import OrderedDict  # noqa: F401


class LRUCache:
    def __init__(self, capacity: int) -> None:
        # TODO: capacity + an ordering structure (OrderedDict or hashmap+DLL)
        pass

    def get(self, key: int) -> int:
        # TODO: return value and mark key most-recently-used, else -1
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: insert/update, mark MRU, evict LRU if over capacity
        pass


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    print(c.get(1))  # expected: 1
    c.put(3, 3)
    print(c.get(2))  # expected: -1
    c.put(4, 4)
    print(c.get(1))  # expected: -1
    print(c.get(3))  # expected: 3
    print(c.get(4))  # expected: 4
