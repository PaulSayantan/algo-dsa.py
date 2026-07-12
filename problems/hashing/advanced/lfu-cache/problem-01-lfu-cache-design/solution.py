"""LFU Cache — LeetCode 460. O(1) get/put; evict least-frequently-used (LRU tie-break)."""
from collections import defaultdict, OrderedDict  # noqa: F401


class LFUCache:
    def __init__(self, capacity: int) -> None:
        # TODO: value map, freq map, freq->keys buckets, and a min-frequency tracker
        pass

    def get(self, key: int) -> int:
        # TODO: return value and bump its frequency, else -1
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: insert/update; on overflow evict the LFU key (LRU among ties)
        pass


if __name__ == "__main__":
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    print(c.get(1))  # expected: 1
    c.put(3, 3)
    print(c.get(2))  # expected: -1
    print(c.get(3))  # expected: 3
    c.put(4, 4)
    print(c.get(1))  # expected: -1
    print(c.get(3))  # expected: 3
    print(c.get(4))  # expected: 4
