# Increment Submatrices by One

**Difficulty:** Medium

**Source:** LeetCode 2536 — Increment Submatrices by One

## Description

You are given a positive integer `n`, representing an `n x n` grid `mat` filled
entirely with `0`s (0-indexed).

You are also given a 2D integer array `queries`. For each
`queries[i] = [row1, col1, row2, col2]`, you should add `1` to **every** element
in the submatrix whose top-left corner is `(row1, col1)` and whose bottom-right
corner is `(row2, col2)`. That is, add `1` to `mat[x][y]` for every
`row1 <= x <= row2` and `col1 <= y <= col2`.

Return the matrix `mat` after processing every query.

## Constraints

- `1 <= n <= 500`
- `1 <= queries.length <= 10^4`
- `0 <= row1 <= row2 < n`
- `0 <= col1 <= col2 < n`

## Examples

### Example 1

```
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
```

**Explanation:**
The first query adds `1` to the 2x2 block at rows 1–2, cols 1–2:
```
0 0 0
0 1 1
0 1 1
```
The second query adds `1` to the 2x2 block at rows 0–1, cols 0–1:
```
1 1 0
1 2 1
0 1 1
```
Cell `(1,1)` is covered by both queries, so it ends at `2`.

### Example 2

```
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
```

**Explanation:**
The single query covers the entire 2x2 grid, so every cell becomes `1`.

## Hint

Stamping every cell of every rectangle is `O(q * n^2)` and too slow. Record each
rectangle with only four corner edits using a **2D Difference Array**, then run a
single 2D prefix sum to reconstruct the final grid.
