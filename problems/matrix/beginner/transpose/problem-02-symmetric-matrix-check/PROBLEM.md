# Symmetric Matrix Check

**Difficulty:** Easy

**Source:** Classic linear-algebra exercise (GeeksforGeeks — "Program to check if a matrix is symmetric")

## Description

A square matrix `M` is called **symmetric** if it is equal to its own
transpose, i.e. `M[i][j] == M[j][i]` for every pair of indices `i, j`.
Equivalently, the matrix is unchanged when flipped over its main diagonal.

Given an `n x n` integer matrix, return `true` if it is symmetric and `false`
otherwise.

## Constraints

- `n == matrix.length == matrix[i].length` (the matrix is square)
- `1 <= n <= 1000`
- `-10^9 <= matrix[i][j] <= 10^9`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],[2,4,5],[3,5,6]]
Output: true
```

**Explanation:** Reflecting across the diagonal leaves the matrix unchanged:
`M[0][1]=2=M[1][0]`, `M[0][2]=3=M[2][0]`, `M[1][2]=5=M[2][1]`. It equals its
transpose, so it is symmetric.

### Example 2

```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: false
```

**Explanation:** `M[0][1]=2` but `M[1][0]=4`, so the matrix differs from its
transpose. Not symmetric.

### Example 3

```
Input:  matrix = [[9]]
Output: true
```

**Explanation:** A 1x1 matrix trivially equals its transpose.

## Hint

A matrix is symmetric exactly when it equals its **Transpose**. You only need
to compare each off-diagonal pair `M[i][j]` and `M[j][i]` once.
