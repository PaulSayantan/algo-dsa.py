# Increment Submatrices by One

**Difficulty:** Medium

**Source:** LeetCode 2536 — Increment Submatrices by One

## Description

You are given a positive integer `n`, indicating that we initially have an
`n x n` 0-indexed integer matrix `mat` filled with zeros.

You are also given a 2D integer array `queries` where
`queries[i] = [row1_i, col1_i, row2_i, col2_i]`.

For each query, you should perform the following operation:

- Add `1` to **every** element in the submatrix with the **top-left** corner
  `(row1_i, col1_i)` and the **bottom-right** corner `(row2_i, col2_i)`. That is,
  add `1` to `mat[x][y]` for all `row1_i <= x <= row2_i` and
  `col1_i <= y <= col2_i`.

Return the matrix `mat` after performing every query.

## Constraints

- `1 <= n <= 500`
- `1 <= queries.length <= 10^4`
- `0 <= row1_i <= row2_i < n`
- `0 <= col1_i <= col2_i < n`

## Examples

### Example 1

```
Input:  n = 3, queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
Output: [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
```

**Explanation:** Start with a 3x3 zero matrix.
- Query `[1, 1, 2, 2]` adds 1 to the bottom-right 2x2 block (rows 1..2,
  cols 1..2), giving `[[0,0,0],[0,1,1],[0,1,1]]`.
- Query `[0, 0, 1, 1]` adds 1 to the top-left 2x2 block (rows 0..1, cols 0..1),
  giving `[[1,1,0],[1,2,1],[0,1,1]]`.

The overlap cell `(1, 1)` is incremented by both queries, so it ends at 2.

### Example 2

```
Input:  n = 2, queries = [[0, 0, 1, 1]]
Output: [[1, 1], [1, 1]]
```

**Explanation:** The single query adds 1 to the entire 2x2 matrix, turning the
all-zero matrix into all ones.

## Hint

Extend the 1D range-update trick to two dimensions: for each query, place four
corner markers (`+1`, `-1`, `-1`, `+1`) in a **2D Difference Array**, then take a
2D prefix sum to materialize the matrix.
