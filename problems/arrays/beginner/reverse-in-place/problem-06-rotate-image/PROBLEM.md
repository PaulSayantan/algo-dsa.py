# Rotate Image

**Difficulty:** Medium

**Source:** LeetCode 48 — Rotate Image

## Description

You are given an `n x n` 2D `matrix` representing an image. Rotate the image by **90
degrees clockwise**.

You have to rotate the image **in place**, which means you have to modify the input 2D
matrix directly. **Do not** allocate another 2D matrix and do the rotation.

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
Output:          [[7,4,1],
                  [8,5,2],
                  [9,6,3]]
```

Explanation: A 90-degree clockwise rotation makes the first column (`7,4,1` bottom-to-
top) become the first row. Equivalently, transpose the matrix to
`[[1,4,7],[2,5,8],[3,6,9]]`, then reverse each row to get
`[[7,4,1],[8,5,2],[9,6,3]]`.

### Example 2

```
Input:  matrix = [[5, 1, 9,11],
                  [2, 4, 8,10],
                  [13,3, 6, 7],
                  [15,14,12,16]]
Output:          [[15,13, 2, 5],
                  [14, 3, 4, 1],
                  [12, 6, 8, 9],
                  [16, 7,10,11]]
```

Explanation: Transpose to
`[[5,2,13,15],[1,4,3,14],[9,8,6,12],[11,10,7,16]]`, then reverse each row to obtain the
output above.

## Hint

Use **Reverse In-Place**: transpose the matrix (swap `matrix[i][j]` with
`matrix[j][i]`), then apply the reverse-in-place two-pointer swap to each row.
