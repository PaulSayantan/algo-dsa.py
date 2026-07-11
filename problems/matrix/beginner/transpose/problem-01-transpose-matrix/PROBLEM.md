# Transpose Matrix

**Difficulty:** Easy

**Source:** LeetCode 867 — Transpose Matrix

## Description

Given a 2-D integer array `matrix`, return the **transpose** of `matrix`.

The transpose of a matrix is the matrix flipped over its main diagonal,
switching the row and column indices. Concretely, if `matrix` has `m` rows and
`n` columns, the transpose is an `n x m` matrix `result` where
`result[i][j] == matrix[j][i]` for every valid `i` and `j`.

The input matrix need **not** be square — this is the whole point of the
problem, since a rectangular `m x n` matrix transposes into an `n x m` matrix.

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

**Explanation:** The matrix is square (3x3). The first column `[1,4,7]` of the
input becomes the first row of the output, and so on. Element `matrix[0][1] = 2`
lands at `result[1][0]`.

### Example 2

```
Input:  matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

**Explanation:** The input is `2x3`, so the transpose is `3x2`. Row `i`,
column `j` of the output equals row `j`, column `i` of the input:
`result[2][1] = matrix[1][2] = 6`.

### Example 3

```
Input:  matrix = [[7]]
Output: [[7]]
```

**Explanation:** A single-element matrix is its own transpose.

## Hint

Build a new matrix with the dimensions swapped and copy each element across the
main diagonal — this is a direct application of the **Transpose** technique.
