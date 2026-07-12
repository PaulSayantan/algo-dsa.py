"""Minimal perfect hashing via displacement (CHD-lite)."""
from typing import List  # noqa: F401


class MinimalPerfectHash:
    def __init__(self, keys: List[int]) -> None:
        # TODO: seed the RNG with a FIXED int; split keys into buckets by one
        # universal hash, then greedily assign each bucket a displacement d so a
        # second hash + d lands every key in a distinct free slot in [0, n)
        pass

    def hash(self, key: int) -> int:
        # TODO: (h(key) + g[bucket_of(key)]) mod n
        pass

    def all_hashes(self) -> List[int]:
        # TODO: hash of every stored key, in insertion order
        pass

    def is_minimal_perfect(self) -> bool:
        # TODO: True iff the n keys map bijectively onto 0..n-1
        pass


if __name__ == "__main__":
    keys = [11, 22, 33, 44, 55, 66]
    mph = MinimalPerfectHash(keys)
    print(mph.is_minimal_perfect())  # expected: True
    print(mph.all_hashes())  # expected: [0, 1, 2, 3, 4, 5]
