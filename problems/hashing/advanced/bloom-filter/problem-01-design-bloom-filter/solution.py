"""Design a Bloom Filter (bit array + k arithmetic hash functions)."""
from typing import List  # noqa: F401


class BloomFilter:
    def __init__(self, size: int = 100, num_hashes: int = 3) -> None:
        # TODO: keep a size-m bit array and remember k
        pass

    def add(self, x: int) -> None:
        # TODO: set the k hashed bit positions to 1
        pass

    def contains(self, x: int) -> bool:
        # TODO: True iff all k hashed bits are set (no false negatives)
        pass


if __name__ == "__main__":
    bf = BloomFilter(100, 3)
    bf.add(10)
    bf.add(20)
    bf.add(30)
    print(bf.contains(10))  # expected: True
    print(bf.contains(20))  # expected: True
    print(bf.contains(30))  # expected: True
    print(bf.contains(40))  # expected: False
    print(bf.contains(15))  # expected: False
    print(bf.contains(110))  # expected: True
