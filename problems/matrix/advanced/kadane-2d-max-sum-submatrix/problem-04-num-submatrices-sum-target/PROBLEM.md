# Number of Submatrices That Sum to Target

**Difficulty:** Hard

**Source:** LeetCode 1074 — Number of Submatrices That Sum to Target

## Description

Given a `matrix` of integers and an integer `target`, return the number of
non-empty submatrices whose sum equals `target`.

A submatrix `(x1, y1, x2, y2)` is the set of all cells `matrix[x][y]` with
`x1 <= x <= x2` and `y1 <= y <= y2`.

Two submatrices `(x1, y1, x2, y2)` and `(x1', y1', x2', y2')` are counted as
different if they differ in any coordinate — even if the two submatrices have
identical values.

This is a *counting* twist on Kadane 2D: you keep the "fix rows, compress
columns" reduction, but the 1D subroutine changes from "max subarray" to "count
subarrays with a given sum."

## Constraints

- `1 <= matrix.length <= 100`
- `1 <= matrix[0].length <= 100`
- `-1000 <= matrix[i][j] <= 1000`
- `-10^8 <= target <= 10^8`

## Examples

### Example 1

```
Input:  matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
```

**Explanation:** The four submatrices summing to `0` are the four `1 × 1` cells
that contain a `0` (positions `(0,0)`, `(0,2)`, `(2,0)`, `(2,2)`). Every larger
submatrix here includes at least one `1` and cannot cancel back to `0`.

### Example 2

```
Input:  matrix = [[1,-1],[-1,1]], target = 0
Output: 5
```

**Explanation:** Five submatrices sum to `0`: the top row `[1, -1]`, the bottom
row `[-1, 1]`, the left column `[1, -1]ᵀ`, the right column `[-1, 1]ᵀ`, and the
entire `2 × 2` matrix `1 - 1 - 1 + 1 = 0`.

### Example 3

```
Input:  matrix = [[904]], target = 0
Output: 0
```

**Explanation:** The only submatrix is the single cell `904`, which does not
equal the target `0`.

## Hint

Use **Kadane 2D (max sum submatrix)** — but replace the 1D Kadane step with a
prefix-sum hash map that counts how many contiguous column bands in the
compressed row sum to `target`.
