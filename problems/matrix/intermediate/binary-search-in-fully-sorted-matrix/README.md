# Binary Search in a Fully-Sorted Matrix

## What it is

Some matrices are *fully sorted*: if you read them **row by row (row-major order)**,
the values form a single non-decreasing (or strictly increasing) 1-D sequence.
Concretely, for an `m x n` matrix this means every row is sorted left-to-right, and
the **first element of each row is >= the last element of the previous row**.

When that property holds, the 2-D matrix is *logically* just a sorted array of
`m * n` elements. You do **not** need to physically flatten it. Instead, you run an
ordinary binary search over the virtual index range `[0, m*n - 1]` and convert any
flat index `idx` back into a `(row, col)` coordinate on the fly:

```
row = idx // n      # n = number of columns
col = idx %  n
value = matrix[row][col]
```

This gives you all the classic sorted-array binary-search variants — membership
test, `lower_bound` / `upper_bound`, insertion position, floor/ceiling, counting
duplicates, and even rotated-array search — for free, without allocating an
`m * n` copy.

## When to reach for it

- The problem hands you a matrix and *promises* it is sorted in row-major order
  (each row sorted, and rows chained so the whole thing is monotone).
- You need `O(log(m*n))` lookups: exact search, first/last position, rank/index,
  floor/ceiling, or count of a value.
- The matrix is a row-major flattening of a rotated sorted array.

If instead each row **and** each column is sorted but rows are *not* chained
(e.g. LeetCode 240 "Search a 2D Matrix II"), this technique does **not** apply —
use the staircase / saddleback walk instead.

## Complexity

- **Time:** `O(log(m*n)) = O(log m + log n)` per query — a single binary search.
- **Space:** `O(1)` — you index into the existing matrix; no flattening copy.

The key trick that makes it all `O(1)` space is the index-mapping identity
`matrix[idx // n][idx % n]`, which lets a 1-D binary search address a 2-D grid.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Search a 2D Matrix](problem-01-search-a-2d-matrix/PROBLEM.md) | Membership test: is `target` in the fully-sorted matrix? | Medium |
| 2 | [Search Insert Position in a Sorted Matrix](problem-02-search-insert-position-in-a-sorted-matrix/PROBLEM.md) | Return the flat index where `target` is, or would be inserted (`lower_bound`). | Medium |
| 3 | [Count Occurrences in a Sorted Matrix](problem-03-count-occurrences-in-a-sorted-matrix/PROBLEM.md) | Count how many times `target` appears using `upper_bound - lower_bound`. | Medium |
| 4 | [Floor and Ceiling in a Sorted Matrix](problem-04-floor-and-ceiling-in-a-sorted-matrix/PROBLEM.md) | Find the largest value `<= target` and smallest value `>= target`. | Medium |
| 5 | [Search in a Rotated Sorted Matrix](problem-05-search-in-a-rotated-sorted-matrix/PROBLEM.md) | The matrix flattens to a rotated sorted array; locate `target`'s `(row, col)`. | Hard |
