# Transpose Matrix

**Difficulty:** Easy

**Source:** LeetCode 867 — Transpose Matrix

## Description

Given a 2D integer array `matrix` with `m` rows and `n` columns, return the
**transpose** of `matrix`.

The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices. Formally, if the input matrix has
dimensions `m × n`, the output matrix has dimensions `n × m`, and
`transpose[j][i] == matrix[i][j]` for every valid `i` and `j`.

Transpose is the first of the two passes in the Rotate 90° technique, so this
problem is a clean place to practice getting the index swap exactly right — note
that the matrix here is **not** required to be square.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10^5`
- `-10^9 <= matrix[i][j] <= 10^9`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

Explanation: Element `matrix[0][1] = 2` moves to `transpose[1][0]`, and in
general `(i, j)` swaps with `(j, i)`. The main diagonal `1, 5, 9` stays fixed.

### Example 2

```
Input:  matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

Explanation: The input is `2 × 3`, so the transpose is `3 × 2`. Column `0`
(`1, 4`) of the input becomes row `0` of the output, and so on.

## Hint

Use the transpose half of Rotate 90° (transpose + reverse): allocate an `n × m`
result and place `matrix[i][j]` at position `[j][i]`. Because the matrix is not
guaranteed to be square, you cannot swap in place here.
