# Submatrix Minimum Query

**Difficulty:** Easy

*Source: Classic competitive-programming exercise (2D Range Minimum Query).*

## Description

You are given a fixed `n x m` integer matrix `grid` that never changes. You must
answer `q` independent queries. Each query gives the coordinates of a rectangle
`(r1, c1, r2, c2)` where `(r1, c1)` is the top-left corner and `(r2, c2)` is the
bottom-right corner (all 0-indexed, inclusive). For each query return the
**minimum value** among all cells inside that rectangle.

Because the number of queries can be very large while the matrix stays constant,
you should preprocess the matrix once and then answer every query in constant
time.

Return a list holding the answer to each query, in order.

## Constraints

- `1 <= n, m <= 500`
- `1 <= q <= 2 * 10^5`
- `-10^9 <= grid[i][j] <= 10^9`
- `0 <= r1 <= r2 < n`
- `0 <= c1 <= c2 < m`

## Examples

### Example 1

```
Input:
grid = [[7, 2, 9, 1],
        [4, 6, 3, 8],
        [5, 0, 2, 7],
        [1, 9, 4, 6]]
queries = [[0, 0, 1, 1], [1, 1, 3, 3], [0, 2, 2, 3]]

Output: [2, 0, 1]
```

Explanation:
- Rectangle `(0,0)-(1,1)` covers `{7,2,4,6}`; the minimum is `2`.
- Rectangle `(1,1)-(3,3)` covers `{6,3,8,0,2,7,9,4,6}`; the minimum is `0`.
- Rectangle `(0,2)-(2,3)` covers `{9,1,3,8,2,7}`; the minimum is `1`.

### Example 2

```
Input:
grid = [[5]]
queries = [[0, 0, 0, 0]]

Output: [5]
```

Explanation: The only rectangle is the single cell `5`, so the minimum is `5`.

## Hint

Sums use a prefix-sum array, but `min` is idempotent, so a **2D Sparse Table**
lets you answer every rectangle query in O(1) after an
O(n·m·log n·log m) precompute.
