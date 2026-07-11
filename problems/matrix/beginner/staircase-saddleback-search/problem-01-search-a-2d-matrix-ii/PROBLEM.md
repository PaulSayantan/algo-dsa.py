# Search a 2D Matrix II

**Difficulty:** Medium

**Source:** LeetCode 240 — Search a 2D Matrix II

## Description

Write an efficient algorithm that searches for a target value `target` in an
`m x n` integer matrix `matrix`. The matrix has the following properties:

- Integers in each **row** are sorted in ascending order from left to right.
- Integers in each **column** are sorted in ascending order from top to bottom.

Note that the matrix is **not** globally sorted when flattened (the first element
of a row can be smaller than the last element of the previous row), so you cannot
simply binary-search a flattened view.

Return `true` if `target` is found in the matrix, and `false` otherwise.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All integers in each row are sorted in ascending order.
- All integers in each column are sorted in ascending order.
- `-10^9 <= target <= 10^9`

## Examples

### Example 1

```
Input:
matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 5

Output: true
```

**Explanation:** `5` sits at row 1, column 1. Starting from the top-right value
`15`, we step left past `11`, `7`, `4` (each larger than 5 until 4), then step
down and land on `5`.

### Example 2

```
Input:
matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 20

Output: false
```

**Explanation:** No cell holds `20`. The staircase walk steps down through `15,
19, 22`, left across the bottom rows, and eventually walks off the grid without a
match.

### Example 3

```
Input:
matrix = [[-5]]
target = -5

Output: true
```

**Explanation:** A single-cell matrix that contains the target.

## Hint

The matrix is sorted along both dimensions, so use **Staircase / Saddleback
Search**: begin at the top-right (or bottom-left) corner where the two sort
orders disagree, and eliminate one full row or one full column with every
comparison.
