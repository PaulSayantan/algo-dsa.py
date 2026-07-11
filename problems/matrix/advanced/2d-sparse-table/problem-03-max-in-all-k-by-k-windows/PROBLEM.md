# Maximum in Every k×k Window

**Difficulty:** Medium

*Source: Classic sliding-window-over-matrix exercise (2D range maximum).*

## Description

Given an `n x m` matrix `grid` and an integer `k` with `1 <= k <= min(n, m)`,
consider every axis-aligned `k x k` square window that fits entirely inside the
grid. There are `(n - k + 1)` such windows vertically and `(m - k + 1)`
horizontally.

Return a matrix `result` of size `(n - k + 1) x (m - k + 1)` where
`result[i][j]` is the **maximum value** in the `k x k` window whose top-left
corner is `(i, j)`.

## Constraints

- `1 <= n, m <= 500`
- `1 <= k <= min(n, m)`
- `-10^9 <= grid[i][j] <= 10^9`

## Examples

### Example 1

```
Input:
grid = [[1, 5, 2, 9],
        [4, 3, 8, 1],
        [7, 2, 6, 3],
        [2, 9, 4, 5]]
k = 2

Output: [[5, 8, 9],
         [7, 8, 8],
         [9, 9, 6]]
```

Explanation: Each entry is the max of a `2 x 2` window. For example the
top-left window `{1,5,4,3}` has max `5`; the window at `(0,1)` `{5,2,3,8}` has
max `8`; the window at `(2,0)` `{7,2,2,9}` has max `9`.

### Example 2

```
Input:
grid = [[1, 5, 2, 9],
        [4, 3, 8, 1],
        [7, 2, 6, 3],
        [2, 9, 4, 5]]
k = 3

Output: [[8, 9],
         [9, 9]]
```

Explanation: The top-left `3 x 3` window `{1,5,2,4,3,8,7,2,6}` has max `8`; the
window at `(0,1)` `{5,2,9,3,8,1,2,6,3}` has max `9`; and both bottom windows
contain the `9` at `(3,1)`.

## Hint

Every window is a square submatrix, so build a **2D Sparse Table** for `max`
once and query each window's top-left corner in O(1). All windows share the same
side length `k`, so `kr = kc = floor(log2(k))` is fixed for every query.
