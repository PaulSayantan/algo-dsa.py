"""Counting Bloom Filter: counters instead of bits so deletion is supported."""
from typing import List  # noqa: F401


class CountingBloomFilter:
    def __init__(self, size: int = 100, num_hashes: int = 3) -> None:
        # TODO: size-m counter array + k
        pass

    def add(self, x: int) -> None:
        # TODO: increment the k hashed counters
        pass

    def remove(self, x: int) -> None:
        # TODO: only if present, decrement the k hashed counters
        pass

    def contains(self, x: int) -> bool:
        # TODO: True iff all k hashed counters are > 0
        pass


if __name__ == "__main__":
    cbf = CountingBloomFilter(100, 3)
    cbf.add(5)
    cbf.add(7)
    print(cbf.contains(5))  # expected: True
    print(cbf.contains(7))  # expected: True
    cbf.remove(5)
    print(cbf.contains(5))  # expected: False
    print(cbf.contains(7))  # expected: True
    print(cbf.contains(25))  # expected: False
