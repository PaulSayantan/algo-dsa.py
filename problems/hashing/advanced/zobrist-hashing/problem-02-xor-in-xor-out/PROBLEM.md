# XOR-In / XOR-Out Consistency

**Difficulty:** Medium

**Source:** Classic — Zobrist incremental update

## Description

Verify Zobrist's incremental-update invariant. `verify_incremental(moves)` applies a sequence of `(op, square, piece)` moves — `place` sets a square, `remove` clears it — maintaining the hash by XOR-ing the relevant key each time, and returns whether that running hash equals a full recompute of the final board. `returns_to_zero(moves)` returns whether XOR-ing all the move keys cancels back to 0 (as it must when every placement is later removed). Both exploit XOR being its own inverse.

## Hint

Placing and removing the SAME (square,piece) XORs the same key twice, cancelling it.
