# Zobrist Hashing (Board State)

**Zobrist hashing** gives O(1) *incremental* hashing of board positions. Precompute one random 64-bit key per (piece, square); a board's hash is the XOR of the keys for its occupied squares. Because XOR is its own inverse, moving a piece is just two XORs — remove the key at the old square, add it at the new one — so you never rehash the whole board. It is the standard trick behind transposition tables and threefold-repetition detection in game engines. A FIXED RNG seed makes the key table reproducible across runs.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Detect Repeated Board Positions](problem-01-incremental-repeat-detection/PROBLEM.md) | Board hash into a set | Medium |
| 2 | [XOR-In / XOR-Out Consistency](problem-02-xor-in-xor-out/PROBLEM.md) | XOR self-inverse | Medium |
