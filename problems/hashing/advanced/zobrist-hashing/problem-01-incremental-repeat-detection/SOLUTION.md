# Detect Repeated Board Positions — Solution

## Optimal Approach

One XOR-fold per board turns each position into a 64-bit key; set membership then answers distinctness and repetition in O(1) per board.

### Reference implementation

```python
class ZobristHasher:
    """Zobrist hashing over a 3x3 board (2 piece types) with a FIXED key table."""

    def __init__(self):
        random.seed(12345)     # fixed seed => reproducible random key table
        self._table = [[random.getrandbits(64) for _ in range(2)] for _ in range(9)]

    def full_hash(self, board):
        # board: length-9 iterable; 0 = empty, 1 or 2 = piece type at that square.
        h = 0
        for sq in range(9):
            if board[sq]:
                h ^= self._table[sq][board[sq] - 1]
        return h

    def num_distinct(self, boards):
        return len({self.full_hash(b) for b in boards})

    def has_repeat(self, boards):
        seen = set()
        for b in boards:
            h = self.full_hash(b)
            if h in seen:
                return True
            seen.add(h)
        return False

    def verify_incremental(self, moves):
        # moves: (op, square, piece); "place" adds, "remove" clears (XOR is its own
        # inverse). Confirm the incrementally-maintained hash matches a full recompute.
        h = 0
        board = [0] * 9
        for op, sq, piece in moves:
            h ^= self._table[sq][piece - 1]
            board[sq] = piece if op == "place" else 0
        return h == self.full_hash(board)

    def returns_to_zero(self, moves):
        h = 0
        for op, sq, piece in moves:
            h ^= self._table[sq][piece - 1]
        return h == 0
```

### Complexity

O(#boards * squares) to hash; O(1) set ops.

## Key Insights & Edge Cases

The three boards b1, b2, b3 are distinct, so among [b1,b2,b3,b1,b2] there are exactly 3 distinct hashes. has_repeat is True when a position recurs (b1 appears twice) and False when all are unique. With 64-bit keys the chance of a false collision is negligible, which is why engines trust the hash to stand in for the full position.
