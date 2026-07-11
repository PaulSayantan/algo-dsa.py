# Submatrix Value Spread

**Difficulty:** Medium

*Source: Classic competitive-programming exercise (2D range max − min).*

## Description

You are given a fixed `n x m` integer matrix `grid`. Answer `q` independent
queries. Each query gives a rectangle `(r1, c1, r2, c2)` with inclusive,
0-indexed top-left corner `(r1, c1)` and bottom-right corner `(r2, c2)`.

The **spread** of a rectangle is `(maximum value in it) − (minimum value in it)`.
For each query return the spread of the requested rectangle.

The matrix is static and there are many queries, so preprocess once and answer
each query in constant time.

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
queries = [[0, 0, 1, 1], [1, 1, 3, 3], [2, 2, 2, 2]]

Output: [5, 9, 0]
```

Explanation:
- Rectangle `(0,0)-(1,1)` covers `{7,2,4,6}`; max `7`, min `2`, spread `5`.
- Rectangle `(1,1)-(3,3)` covers `{6,3,8,0,2,7,9,4,6}`; max `9`, min `0`,
  spread `9`.
- Rectangle `(2,2)-(2,2)` is the single cell `2`; max = min = `2`, spread `0`.

### Example 2

```
Input:
grid = [[3, 3],
        [3, 3]]
queries = [[0, 0, 1, 1], [0, 0, 0, 1]]

Output: [0, 0]
```

Explanation: Every value equals `3`, so max and min coincide and the spread is
`0` for any rectangle.

## Hint

Both `max` and `min` are idempotent. Build **two 2D Sparse Tables** — one for
`max`, one for `min` — and subtract their O(1) query results.
