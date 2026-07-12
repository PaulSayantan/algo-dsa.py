"""FKS two-level perfect hashing for a static integer set."""
from typing import List  # noqa: F401


class FKSPerfectHash:
    def __init__(self, keys: List[int]) -> None:
        # TODO: seed the RNG with a FIXED int, pick a first-level universal hash
        # (a*k+b) mod p mod n, then for each bucket retry a second-level hash into
        # len(bucket)**2 slots until it is collision-free
        pass

    def lookup(self, key: int) -> bool:
        # TODO: route through both levels; True iff the slot holds exactly `key`
        pass

    def verify_all(self, keys: List[int]) -> bool:
        # TODO: True iff every original key resolves to itself
        pass

    def total_slots(self) -> int:
        # TODO: total second-level slots allocated
        pass


if __name__ == "__main__":
    keys = [5, 12, 19, 26, 33, 40, 47]
    fks = FKSPerfectHash(keys)
    print(fks.verify_all(keys))  # expected: True
    print(fks.lookup(100))  # expected: False
    print(fks.total_slots())  # expected: 11
