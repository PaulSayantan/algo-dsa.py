# Maximum Sum Rectangle in a 2D Matrix

**Difficulty:** Medium

**Source:** GeeksforGeeks — "Maximum sum rectangle in a 2D matrix" (classic
Kadane-2D interview problem)

## Description

Given a 2D integer matrix `matrix` of size `n × m` that may contain negative
numbers, find the contiguous **rectangular submatrix** whose element sum is the
largest, and return that sum.

A rectangular submatrix is defined by choosing a top row, a bottom row
(`top <= bottom`), a left column, and a right column (`left <= right`), and
summing all cells inside that rectangle. The rectangle must be non-empty (it
contains at least one cell).

This is the canonical problem the Kadane 2D technique was designed for.

## Constraints

- `1 <= n, m <= 300`
- `-10^5 <= matrix[i][j] <= 10^5`
- The matrix contains at least one cell.

## Examples

### Example 1

```
Input:
matrix = [
  [ 1,  2, -1, -4, -20],
  [-8, -3,  4,  2,   1],
  [ 3,  8, 10,  1,   3],
  [-4, -1,  1,  7,  -6]
]
Output: 29
```

**Explanation:** The best rectangle spans rows 1..3 and columns 1..3:

```
[-3,  4,  2]
[ 8, 10,  1]
[-1,  1,  7]
```

Its sum is `-3 + 4 + 2 + 8 + 10 + 1 - 1 + 1 + 7 = 29`. No other rectangle sums
higher.

### Example 2

```
Input:
matrix = [
  [-1, -2],
  [-3, -4]
]
Output: -1
```

**Explanation:** Every cell is negative, so the largest rectangle is the single
cell `-1`. As with 1D Kadane, an empty rectangle is not allowed.

## Hint

Use **Kadane 2D (max sum submatrix)**. Fix a pair of rows `(top, bottom)`,
compress each column between them into a single value (accumulate as `bottom`
descends), then run 1D Kadane over that compressed row to find the best column
band.
