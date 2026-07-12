"""Zobrist hashing for board state (incremental, repetition detection)."""
from typing import List  # noqa: F401


class ZobristHasher:
    def __init__(self) -> None:
        # TODO: seed the RNG with a FIXED int and build a table[square][piece] of
        # random 64-bit keys (9 squares, 2 piece types)
        pass

    def full_hash(self, board) -> int:
        # TODO: XOR the key for each occupied square/piece
        pass

    def num_distinct(self, boards) -> int:
        # TODO: number of distinct board hashes
        pass

    def has_repeat(self, boards) -> bool:
        # TODO: True iff any board position (by hash) repeats
        pass

    def verify_incremental(self, moves) -> bool:
        # TODO: maintain the hash by XOR-ing keys in/out and confirm it equals a
        # full recompute of the final board
        pass

    def returns_to_zero(self, moves) -> bool:
        # TODO: True iff XOR-ing all move keys cancels back to 0
        pass


if __name__ == "__main__":
    z = ZobristHasher()
    print(z.verify_incremental([("place", 0, 1), ("place", 4, 2), ("place", 8, 1), ("remove", 4, 2)]))  # expected: True
    print(z.returns_to_zero([("place", 3, 1), ("remove", 3, 1)]))  # expected: True
    print(z.returns_to_zero([("place", 3, 1), ("place", 5, 2)]))  # expected: False
