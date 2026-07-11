# Maximum Sum Rectangle with Coordinates

**Difficulty:** Hard

**Source:** Classic competitive-programming variant of the max-sum-rectangle
problem (extends GeeksforGeeks "Maximum sum rectangle in a 2D matrix")

## Description

Given a 2D integer matrix `matrix` of size `n × m` that may contain negative
numbers, find the contiguous rectangular submatrix with the largest sum and
return **both the sum and the bounding rectangle**.

Return the rectangle as `(top, left, bottom, right)`, all inclusive 0-based
indices, where the chosen rectangle covers rows `top..bottom` and columns
`left..right`. If multiple rectangles tie for the maximum sum, return any one of
them (the reference implementation returns the first found when scanning row
bands top-to-bottom and, within a band, the Kadane window that improves the
best strictly first).

Reporting boundaries — not just the sum — is a common follow-up in interviews.
It forces you to thread index bookkeeping through both the 1D Kadane subroutine
(which must return `left`/`right`) and the outer row-band loop (which supplies
`top`/`bottom`).

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
Output: sum = 29, rectangle = (top=1, left=1, bottom=3, right=3)
```

**Explanation:** The maximum-sum rectangle covers rows 1..3 and columns 1..3:

```
[-3,  4,  2]
[ 8, 10,  1]
[-1,  1,  7]
```

which sums to `29`. The bounding box is therefore `top=1, left=1, bottom=3,
right=3`.

### Example 2

```
Input:
matrix = [
  [-1, -2],
  [-3, -4]
]
Output: sum = -1, rectangle = (top=0, left=0, bottom=0, right=0)
```

**Explanation:** All cells are negative, so the best rectangle is the single
top-left cell `-1`, i.e. the `1 × 1` box at `(0, 0)`.

## Hint

Use **Kadane 2D (max sum submatrix)**. Extend the 1D Kadane subroutine so it
also reports the start/end column of its best window; combine those with the
current `(top, bottom)` row band whenever you improve the global maximum.
