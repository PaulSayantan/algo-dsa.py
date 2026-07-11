# Batch Updates and Region Sums

**Difficulty:** Medium

**Source:** Classic offline matrix problem (2D difference array for updates +
2D prefix sum for queries; common in competitive programming, e.g. "Matrix
Range Update and Query").

## Description

You start with an `m x n` matrix of zeros. You are given two batches of
operations that must be processed **in order: all updates first, then all
queries** (this is an *offline* problem — no query is interleaved with an
update).

1. `updates`: each `update = [r1, c1, r2, c2, v]` adds the integer `v` to every
   cell `mat[x][y]` with `r1 <= x <= r2` and `c1 <= y <= c2` (inclusive
   rectangle). `v` may be negative.
2. `queries`: each `query = [r1, c1, r2, c2]` asks for the **sum of all cells**
   in that inclusive rectangle *after every update has been applied*.

Return a list containing the answer to each query, in order.

## Constraints

- `1 <= m, n <= 1000`
- `0 <= updates.length, queries.length <= 10^5`
- `0 <= r1 <= r2 < m`, `0 <= c1 <= c2 < n`
- `-10^4 <= v <= 10^4`

## Examples

### Example 1

```
Input:
  m = 3, n = 3
  updates = [[0,0,1,1,5],[1,1,2,2,3]]
  queries = [[0,0,2,2],[1,1,1,1]]
Output: [32, 8]
```

**Explanation:**
After the two updates the matrix is:
```
5 5 0
5 8 3
0 3 3
```
(The first update puts `5` in the top-left 2x2 block; the second adds `3` to the
bottom-right 2x2 block; cell `(1,1)` receives both.)
- Query `[0,0,2,2]` sums the whole matrix: `5+5+0+5+8+3+0+3+3 = 32`.
- Query `[1,1,1,1]` is just cell `(1,1)` = `8`.

### Example 2

```
Input:
  m = 2, n = 2
  updates = [[0,0,1,1,2],[0,0,0,1,-1]]
  queries = [[0,0,0,1],[0,0,1,1]]
Output: [2, 6]
```

**Explanation:**
After the updates the matrix is:
```
1 1
2 2
```
(The first update adds `2` everywhere; the second subtracts `1` from the top
row.)
- Query `[0,0,0,1]` sums the top row: `1 + 1 = 2`.
- Query `[0,0,1,1]` sums everything: `1 + 1 + 2 + 2 = 6`.

## Hint

Two stacked techniques: build the final matrix from the range-add updates with a
**2D Difference Array**, then build a **2D prefix-sum** table over that matrix so
each rectangle-sum query is answered in `O(1)`.
