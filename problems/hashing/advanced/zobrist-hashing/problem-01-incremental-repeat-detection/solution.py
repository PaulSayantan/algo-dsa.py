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
    b1 = (1, 2, 0, 0, 1, 0, 0, 0, 2)
    b2 = (1, 2, 0, 0, 2, 0, 0, 0, 1)
    b3 = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    print(z.num_distinct([b1, b2, b3, b1, b2]))  # expected: 3
    print(z.has_repeat([b1, b2, b1]))  # expected: True
    print(z.has_repeat([b1, b2, b3]))  # expected: False
