# Min-Cost Walk of Exactly K Edges (Huge K)

**Difficulty:** Medium

**Source:** Classic competitive-programming pattern (matrix exponentiation over
the min-plus semiring). Appears on Codeforces / AtCoder as "minimum weight walk
of length exactly K" with K up to `10^18`.

## Description

You are given a directed weighted graph on `n` vertices given by an `n × n`
matrix `W`, where `W[i][j]` is the weight of edge `i → j` (or `INF` if there is
no such edge). Given a source `u`, a destination `v`, and an integer `k`
(possibly astronomically large), return the **minimum total weight of a walk
from `u` to `v` that uses exactly `k` edges**, or `-1` if no such walk exists.

Edges and vertices may be reused. The catch versus Problem 1 is scale: `k` can be
as large as `10^18`, so you cannot chain `k` matrix products. You must use
**fast (binary) exponentiation** of the weight matrix under **min-plus (tropical)
matrix multiplication**, computing `W^{⊙k}` in `O(n³ · log k)`.

The identity element for repeated squaring is the tropical identity matrix
`I` with `0` on the diagonal and `INF` elsewhere (adding a length-0 walk of cost
0 to a vertex, and no other transitions).

## Constraints

- `1 <= n <= 80`
- `1 <= k <= 10^18`
- Edge weights are non-negative integers, `0 <= W[i][j] <= 10^6` (with `INF`
  denoting "no edge").
- The answer, if finite, fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:
  n = 2
  W = [[5, 2],
       [3, 1]]        # W[i][j] = weight of edge i -> j; all edges present
  u = 0, v = 0, k = 4
Output: 7
Explanation:
  The cheapest 4-edge walk from 0 back to 0 is
    0 -> 1 -> 1 -> 1 -> 0  with cost 2 + 1 + 1 + 3 = 7.
  Looping on vertex 1 (self-edge cost 1) is cheaper than staying on 0 (cost 5).
```

### Example 2

```
Input:
  n = 2
  W = [[5, 2],
       [3, 1]]
  u = 1, v = 1, k = 10
Output: 10
Explanation:
  The self-edge 1 -> 1 costs 1. Taking it 10 times gives a 10-edge walk of cost
  1 * 10 = 10, which is optimal.
```

### Example 3

```
Input:
  n = 2
  W = [[5, 2],
       [3, 1]]
  u = 0, v = 1, k = 4
Output: 5
Explanation:
  0 -> 1 -> 1 -> 1 -> 1 costs 2 + 1 + 1 + 1 = 5. No cheaper 4-edge walk ends at
  vertex 1.
```

## Hint

`k` is far too large for a linear chain of `k` products, but the tropical
semiring is associative, so `W^{⊙k}` can be found by **binary exponentiation**:
square the matrix and multiply selectively per bit of `k`. This is
**Min-Plus (Tropical) Matrix Multiplication** combined with fast exponentiation
— `O(n³ · log k)`. Remember the tropical identity: `0` on the diagonal, `INF`
elsewhere.
