# XOR-In / XOR-Out Consistency — Solution

## Optimal Approach

Each move is a single XOR against the precomputed key. The final incremental hash provably equals a from-scratch recompute because XOR is associative and commutative.

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

O(#moves) with O(1) work per move; recompute O(squares).

## Key Insights & Edge Cases

verify_incremental is True: XOR-ing the key at square 4 in and then out cancels it, leaving exactly the keys for the pieces still on the board — identical to a full recompute. returns_to_zero is True only when the moves pair up (place then remove the same key); placing two *different* keys leaves a non-zero XOR, so the last call is False.
