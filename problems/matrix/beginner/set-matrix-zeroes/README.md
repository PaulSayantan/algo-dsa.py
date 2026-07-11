# Set Matrix Zeroes — In-Place Marking Technique

**Set Matrix Zeroes** is the flagship problem of a broader, extremely useful
family of techniques: **using the input array/matrix itself as auxiliary
storage so that no extra space is needed**. Instead of allocating a separate
`seen[]` set, a `rowZero[]`/`colZero[]` boolean array, or a copy of the grid,
you encode the "flags" you need directly inside the data you were given.

The three most common flavours are:

1. **First row / first column as flags** (the literal *Set Matrix Zeroes*
   trick). Reserve row 0 and column 0 to record which rows/columns must be
   zeroed, handle those two lines separately, then rewrite the interior.
2. **Sign / negation marking.** When values are known to be positive (e.g. in
   `[1, n]`), flip the sign of `nums[index]` to record "index was visited"
   without destroying the magnitude (`abs()` recovers it).
3. **Index placement / value encoding.** Store *two* states in one cell by
   encoding them numerically — e.g. `old + new*2` for a 0/1 grid, or by
   swapping each value into the slot that matches it (cyclic sort).

## When to reach for it

- The problem explicitly asks for an **in-place, O(1) extra space** solution.
- The values live in a **bounded, predictable range** (often `1..n` or `0/1`)
  so the data itself can double as an index or a flag.
- You would otherwise allocate a hash set / auxiliary matrix that is the same
  size as the input.

## Typical complexity

| Aspect | Cost |
|--------|------|
| Time   | `O(m·n)` for grids, `O(n)` for 1-D arrays (a constant number of passes) |
| Space  | `O(1)` extra — only a handful of scalar flags |

The catch is **ordering and correctness**: because you are overwriting the data
you still need to read, you must carefully sequence the passes so a written
"marker" is never mistaken for real data. Getting that ordering right is the
whole skill this section trains.

## Problems

| # | Problem | Technique flavour | Difficulty |
|---|---------|-------------------|------------|
| 1 | [Find All Numbers Disappeared in an Array](problem-01-find-disappeared-numbers/PROBLEM.md) | Sign / negation marking to record which values appear | Easy |
| 2 | [Set Matrix Zeroes](problem-02-set-matrix-zeroes/PROBLEM.md) | First row/column reused as zero flags | Medium |
| 3 | [Find All Duplicates in an Array](problem-03-find-all-duplicates/PROBLEM.md) | Sign marking; a second hit on an index reveals a duplicate | Medium |
| 4 | [Game of Life](problem-04-game-of-life/PROBLEM.md) | Encode old + new state in one cell (bit/value packing) | Medium |
| 5 | [First Missing Positive](problem-05-first-missing-positive/PROBLEM.md) | Index placement (cyclic sort) using the array as a hash | Hard |
