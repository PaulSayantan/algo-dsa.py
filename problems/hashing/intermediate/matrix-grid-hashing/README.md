# Matrix / Grid Hashing

In grids, a Hash Set or Map keyed by a canonical signature answers structural questions cheaply: `(value, row/col/box)` keys detect Sudoku duplicates, row/column tuples find matching pairs, `r-c` or `r+c` groups cells by diagonal, and a shape normalized to its top-left corner identifies congruent islands. The signature must be an exact, hashable value (a tuple), never a salted `hash()`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Valid Sudoku](problem-01-valid-sudoku/PROBLEM.md) | (value, region) key set | Medium |
| 2 | [Equal Row and Column Pairs](problem-02-equal-row-and-column-pairs/PROBLEM.md) | Row-tuple frequency map | Medium |
| 3 | [Number of Distinct Islands](problem-03-number-of-distinct-islands/PROBLEM.md) | Translation-normalized shape | Medium |
| 4 | [Toeplitz Matrix](problem-04-toeplitz-matrix/PROBLEM.md) | Diagonal (r-c) map | Easy |
| 5 | [Number of Equivalent Domino Pairs](problem-05-equivalent-domino-pairs/PROBLEM.md) | Canonical (min,max) key | Easy |
