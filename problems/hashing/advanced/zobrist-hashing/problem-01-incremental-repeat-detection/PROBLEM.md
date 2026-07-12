# Detect Repeated Board Positions

**Difficulty:** Medium

**Source:** Classic — Zobrist (1970) hashing

## Description

Represent a 3x3 board as a length-9 list where 0 is empty and 1 or 2 is a piece type. Seed the RNG with a **fixed** integer and build a random key table `table[square][piece]`. `full_hash(board)` XORs the keys of all occupied squares. Implement `num_distinct(boards)` (count of distinct position hashes) and `has_repeat(boards)` (True iff any position recurs) — the core of repetition detection.

## Hint

Hash each board by XOR of its occupied (square,piece) keys; feed hashes into a set.
