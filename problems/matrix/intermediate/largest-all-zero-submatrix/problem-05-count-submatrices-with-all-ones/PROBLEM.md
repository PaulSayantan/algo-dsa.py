# Count Submatrices With All Ones

**Difficulty:** Medium / Hard

**Source:** LeetCode 1504 — Count Submatrices With All Ones

## Description

Given an `m x n` binary matrix `mat`, return the **number of submatrices that
contain only `1`s**. A submatrix is any axis-aligned rectangle defined by a
contiguous range of rows and a contiguous range of columns; two submatrices are
different if they occupy a different set of cells.

This is the *counting* cousin of the largest-all-one-submatrix problem: rather
than the single biggest rectangle, you tally **every** all-`1` rectangle. The
same per-row height histogram drives it, but the monotonic stack now accumulates
a running **sum** of how many rectangles end in each column.

## Constraints

- `1 <= m, n <= 150`
- `mat[i][j]` is either `0` or `1`.

## Examples

### Example 1

```
Input:
mat = [[1, 0, 1],
       [1, 1, 0],
       [1, 1, 0]]
Output: 13
Explanation: There are 6 single-cell (1x1) all-1 submatrices, 4 submatrices of
size 1x2/2x1, 2 of size 2x1 in the tall left block ... summing all all-1
rectangles gives 13.
```

### Example 2

```
Input:
mat = [[0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 1, 1, 0]]
Output: 24
Explanation: Counting every all-1 rectangle (1x1 up to the largest blocks in the
central all-1 region) totals 24.
```

### Example 3

```
Input:
mat = [[1, 1, 1, 1, 1, 1]]
Output: 21
Explanation: A single row of 6 ones has C(7,2) = 21 contiguous subarrays, each a
distinct all-1 submatrix (6 of length 1, 5 of length 2, ..., 1 of length 6:
6+5+4+3+2+1 = 21).
```

## Hint

Use the **Largest All-Zero Submatrix** machinery for counting: build per-column
heights of consecutive `1`s ending at each row, then for each row count the
rectangles whose bottom edge lies on it. A monotonic stack lets you carry a
running sum `f[j]` = number of all-1 rectangles ending at column `j` in the
current row's histogram, reusing the previous shorter bar's count.
