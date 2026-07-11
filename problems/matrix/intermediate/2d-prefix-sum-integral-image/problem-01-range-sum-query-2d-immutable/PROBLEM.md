# Range Sum Query 2D - Immutable

**Difficulty:** Medium

**Source:** LeetCode 304 — Range Sum Query 2D - Immutable

## Description

Given a 2D matrix `matrix`, handle multiple queries of the following type:

- Calculate the **sum of the elements** of `matrix` inside the rectangle
  defined by its **upper-left corner** `(row1, col1)` and its **lower-right
  corner** `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` initializes the object with the integer matrix
  `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` returns the sum of the
  elements of `matrix` inside the rectangle defined by its upper-left corner
  `(row1, col1)` and lower-right corner `(row2, col2)`.

You must design an algorithm where `sumRegion` runs in **O(1)** time. The matrix
does not change between queries.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^4 <= matrix[i][j] <= 10^4`
- `0 <= row1 <= row2 < m`
- `0 <= col1 <= col2 < n`
- At most `10^4` calls will be made to `sumRegion`.

## Examples

### Example 1

```
Input:
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
sumRegion(2, 1, 4, 3)
Output: 8
Explanation: The rectangle covers rows 2..4 and columns 1..3.
Its cells are (2,0,1), (1,0,1), (0,3,0) reading each row's cols 1..3:
2+0+1 + 1+0+1 + 0+3+0 = 8.
```

### Example 2

```
Input:
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
sumRegion(1, 1, 2, 2)
Output: 11
Explanation: Rows 1..2, columns 1..2: 6+3 + 2+0 = 11.
```

### Example 3

```
Input:
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
sumRegion(1, 2, 2, 4)
Output: 12
Explanation: Rows 1..2, columns 2..4: 3+2+1 + 0+1+5 = 12.
```

## Hint

Precompute a **2D Prefix Sum (Integral Image)** table once in the constructor so
that each `sumRegion` call becomes a constant-time inclusion-exclusion lookup.
