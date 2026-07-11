# Increment Submatrices by One

**Difficulty:** Medium

**Source:** LeetCode 2536 — Increment Submatrices by One

## Description

You are given a positive integer `n`, indicating that we initially have an
`n x n` 0-indexed integer matrix `mat` filled with zeroes.

You are also given a 2D integer array `queries`. For each
`queries[i] = [row1, col1, row2, col2]`, you should do the following operation:

- Add `1` to **every element** in the submatrix with the top-left corner
  `(row1, col1)` and the bottom-right corner `(row2, col2)`. That is, add `1` to
  `mat[x][y]` for all `row1 <= x <= row2` and `col1 <= y <= col2`.

Return the matrix `mat` after performing every query.

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
- The first query adds 1 to every cell in the rectangle rows 1..2, cols 1..2.
- The second query adds 1 to every cell in the rectangle rows 0..1, cols 0..1.
- Cell `(1,1)` is covered by both queries, so it ends at `2`; every other
  covered cell is covered once and equals `1`.

### Example 2

```
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
```

**Explanation:**
- The single query adds 1 to the whole `2 x 2` matrix, so every cell becomes 1.

## Hint

This is the **range-update / point-query** mode of a **2D Binary Indexed
Tree**: add `+1` to a rectangle by updating the four corners of a 2D difference
decomposition, then read each cell as a prefix query. (A plain 2D difference
array is the classic linear-time variant of the same idea.)
