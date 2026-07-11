# Largest Submatrix With Rearrangements

**Difficulty:** Medium

**Source:** LeetCode 1727 — Largest Submatrix With Rearrangements

## Description

You are given a binary matrix `matrix` of size `m x n`. You are allowed to **rearrange the
columns of the matrix in any order** (any permutation of the columns).

Return the **area of the largest submatrix within `matrix` where every element is `1`**,
after reordering the columns optimally.

Because you may permute columns freely, a valid all-`1` rectangle is any set of columns that,
over some contiguous band of rows, are all `1` — the columns need not be adjacent in the
original matrix.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m * n <= 10^5`
- `matrix[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: matrix = [[0,0,1],
                 [1,1,1],
                 [1,0,1]]
Output: 4
```

**Explanation:** Column heights of consecutive `1`s ending at the last row are
`[2, 0, 3]`. Sorting these descending gives `[3, 2, 0]`; the best is width 2 at height 2,
for area `2 * 2 = 4`.

### Example 2

```
Input: matrix = [[1,0,1,0,1]]
Output: 3
```

**Explanation:** The single row has heights `[1,0,1,0,1]`. Three columns are `1`, so after
rearranging we can place them side by side for a `1 x 3` all-`1` submatrix of area `3`.

### Example 3

```
Input: matrix = [[1,1,0],
                 [1,0,1]]
Output: 2
```

**Explanation:** For the top row the best area is `1 x 2 = 2` (two `1`s brought together).
For the bottom row, heights are `[2, 0, 1]`; sorted descending `[2, 1, 0]` gives `2 x 1 = 2`.
The maximum overall is `2`.

## Hint

Build per-column **heights** of consecutive `1`s ending at each row (the same first step as
Maximal Rectangle). Because columns can be reordered, you do not need a stack — just **sort
each row's heights descending** and take `height[k] * (k + 1)`.
