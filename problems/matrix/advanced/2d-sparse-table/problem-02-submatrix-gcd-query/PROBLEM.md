# Submatrix GCD Query

**Difficulty:** Medium

*Source: Classic competitive-programming exercise (2D Range GCD Query).*

## Description

You are given a fixed `n x m` matrix `grid` of positive integers. Answer `q`
independent queries. Each query gives a rectangle `(r1, c1, r2, c2)` with
inclusive, 0-indexed top-left corner `(r1, c1)` and bottom-right corner
`(r2, c2)`. For each query return the **greatest common divisor (gcd)** of all
values inside that rectangle.

The matrix is static and the number of queries is large, so preprocess once and
answer each query in constant time.

Return a list holding the answer to each query, in order.

## Constraints

- `1 <= n, m <= 400`
- `1 <= q <= 2 * 10^5`
- `1 <= grid[i][j] <= 10^9`
- `0 <= r1 <= r2 < n`
- `0 <= c1 <= c2 < m`

## Examples

### Example 1

```
Input:
grid = [[12, 18,  6, 24],
        [ 9, 15, 30,  3],
        [ 8, 16, 12, 20],
        [21,  7, 14, 28]]
queries = [[0, 0, 1, 1], [3, 0, 3, 3], [0, 2, 1, 3], [0, 0, 3, 3]]

Output: [3, 7, 3, 1]
```

Explanation:
- Rectangle `(0,0)-(1,1)` covers `{12,18,9,15}`; `gcd = 3`.
- Rectangle `(3,0)-(3,3)` covers `{21,7,14,28}`; `gcd = 7`.
- Rectangle `(0,2)-(1,3)` covers `{6,24,30,3}`; `gcd = 3`.
- Rectangle `(0,0)-(3,3)` covers the whole grid; `gcd = 1`.

### Example 2

```
Input:
grid = [[10, 20],
        [30, 40]]
queries = [[0, 0, 0, 1], [0, 0, 1, 1]]

Output: [10, 10]
```

Explanation:
- Rectangle `(0,0)-(0,1)` covers `{10,20}`; `gcd = 10`.
- The full matrix `{10,20,30,40}` has `gcd = 10`.

## Hint

`gcd` is idempotent (`gcd(x, x) = x`) and associative, so a **2D Sparse Table**
answers each rectangle query in O(1) after the precompute — just swap the merge
function from `min` to `gcd`.
