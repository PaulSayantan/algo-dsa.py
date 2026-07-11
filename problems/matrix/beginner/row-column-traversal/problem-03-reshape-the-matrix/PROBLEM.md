# Reshape the Matrix

**Difficulty:** Easy

**Source:** LeetCode 566 — Reshape the Matrix

## Description

In MATLAB, there is a handy function called `reshape` which can reshape an `m x n`
matrix into a new one with a different size `r x c` while keeping its original data.

You are given an `m x n` matrix `mat` and two integers `r` and `c` representing the
number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with **all** the elements of the original matrix
in the **same row-traversing order** as they were originally (read left to right, top
to bottom).

If the reshape operation with given parameters is possible and legal, output the new
reshaped matrix; otherwise, output the original matrix.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `-1000 <= mat[i][j] <= 1000`
- `1 <= r, c <= 300`

## Examples

### Example 1

```
Input:  mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
```

**Explanation:** The original elements read in row order are `1, 2, 3, 4`. Since
`1 * 4 == 2 * 2`, the reshape is legal, and they refill a `1 x 4` matrix.

### Example 2

```
Input:  mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
```

**Explanation:** `2 * 4 = 8 != 2 * 2 = 4`, so the reshape is impossible. The original
matrix is returned unchanged.

### Example 3

```
Input:  mat = [[1,2,3],[4,5,6]], r = 3, c = 2
Output: [[1,2],[3,4],[5,6]]
```

**Explanation:** The elements in row order are `1, 2, 3, 4, 5, 6`. Because
`3 * 2 == 2 * 3`, they refill a `3 x 2` matrix row by row.

## Hint

Use **Row/Column Traversal**: walk the source matrix in row-major order to produce a
flat sequence of values, then place them one by one into the destination `r x c` grid,
also in row-major order. A running index `k` maps cleanly to `(k // c, k % c)`.
