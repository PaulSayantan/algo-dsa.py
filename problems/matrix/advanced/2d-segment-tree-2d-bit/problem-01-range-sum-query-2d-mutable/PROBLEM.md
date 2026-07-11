# Range Sum Query 2D - Mutable

**Difficulty:** Medium

**Source:** LeetCode 308 — Range Sum Query 2D - Mutable

## Description

Given a 2D matrix `matrix`, handle multiple queries of the following two types:

1. **Update** the value of a cell in `matrix`.
2. Calculate the **sum of the elements** of `matrix` inside the rectangle
   defined by its upper-left corner `(row1, col1)` and lower-right corner
   `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` — initializes the object with the integer matrix
  `matrix`.
- `void update(int row, int col, int val)` — updates the value of
  `matrix[row][col]` to be `val`.
- `int sumRegion(int row1, int col1, int row2, int col2)` — returns the sum of
  the elements of `matrix` inside the rectangle defined by its upper-left corner
  `(row1, col1)` and lower-right corner `(row2, col2)`.

There are many `update` and `sumRegion` calls interleaved, so precomputing a
single static prefix-sum matrix is not enough — each `update` would force an
`O(nm)` rebuild.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^5 <= matrix[i][j] <= 10^5`
- `0 <= row < m`, `0 <= col < n`
- `-10^5 <= val <= 10^5`
- `0 <= row1 <= row2 < m`, `0 <= col1 <= col2 < n`
- At most `5000` calls to `update` and `sumRegion` combined.

## Examples

### Example 1

```
Input:
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2],
   [5, 6, 3, 2, 1],
   [1, 2, 0, 1, 5],
   [4, 1, 0, 1, 7],
   [1, 0, 3, 0, 5]]],
 [2, 1, 4, 3],
 [3, 2, 2],
 [2, 1, 4, 3]]

Output:
[null, 8, null, 10]
```

**Explanation:**
- `sumRegion(2, 1, 4, 3)` sums rows 2..4, cols 1..3 →
  `(2+0+1) + (1+0+1) + (0+3+0) = 8`.
- `update(3, 2, 2)` sets `matrix[3][2]` from `0` to `2`.
- `sumRegion(2, 1, 4, 3)` now → `(2+0+1) + (1+2+1) + (0+3+0) = 10`.

### Example 2

```
Input:
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[1, 2],
   [3, 4]]],
 [0, 0, 1, 1],
 [0, 0, 10],
 [0, 0, 1, 1]]

Output:
[null, 10, null, 19]
```

**Explanation:**
- `sumRegion(0, 0, 1, 1)` sums the whole matrix → `1 + 2 + 3 + 4 = 10`.
- `update(0, 0, 10)` sets `matrix[0][0]` from `1` to `10`.
- `sumRegion(0, 0, 1, 1)` now → `10 + 2 + 3 + 4 = 19`.

## Hint

Use a **2D Binary Indexed Tree (2D BIT / Fenwick Tree)**. It supports point
updates and rectangle-sum queries, each in `O(log m · log n)`.
