# Submatrix Maximum with Point Updates

**Difficulty:** Hard

**Source:** Classic 2D Segment Tree exercise (SPOJ MATSUM / KQUERY-style,
Codeforces gym problems). This variant queries **maximum** to force a segment
tree rather than a BIT.

## Description

You are given an `n x m` integer matrix. Process `q` operations of two kinds:

- `update r c v` — set the cell at row `r`, column `c` to value `v`.
- `query r1 c1 r2 c2` — report the **maximum** value among all cells `(x, y)`
  with `r1 <= x <= r2` and `c1 <= y <= c2` (an inclusive submatrix).

Return the answer to every `query` operation, in order.

The `max` aggregate is **not invertible**: knowing the maximum over a big region
does not let you "subtract off" a sub-part, so the four-corner prefix trick used
for sums does **not** apply. This is what distinguishes the problem from a
sum-based BIT question.

## Constraints

- `1 <= n, m <= 1000`
- `1 <= q <= 10^5`
- `0 <= r < n`, `0 <= c < m` (0-indexed)
- `-10^9 <= v <= 10^9` and `-10^9 <= initial cell value <= 10^9`
- For every query, `0 <= r1 <= r2 < n` and `0 <= c1 <= c2 < m`.

## Examples

### Example 1

```
Input:
matrix =
[[1, 3, 2],
 [4, 0, 5],
 [7, 6, 1]]
operations =
query 0 0 1 1
update 0 1 9
query 0 0 1 1
query 1 1 2 2

Output:
4
9
6
```

**Explanation:**
- `query 0 0 1 1` — the submatrix `{1,3,4,0}` has max `4`.
- `update 0 1 9` — cell `(0,1)` becomes `9`.
- `query 0 0 1 1` — the submatrix is now `{1,9,4,0}`, max `9`.
- `query 1 1 2 2` — the submatrix `{0,5,6,1}` has max `6`.

### Example 2

```
Input:
matrix =
[[-5, -2],
 [-8, -1]]
operations =
query 0 0 1 1
update 1 0 -3
query 0 0 0 0

Output:
-1
-5
```

**Explanation:**
- `query 0 0 1 1` — over all four (negative) cells the max is `-1`.
- `update 1 0 -3` — cell `(1,0)` goes from `-8` to `-3` (still not the largest).
- `query 0 0 0 0` — a single cell `(0,0)` = `-5`.

## Hint

Use a **2D Segment Tree**: an outer segment tree over rows, where each node
stores an inner segment tree over columns holding the **max** of that row-band.
A BIT cannot answer range-max with arbitrary point updates because `max` is not
invertible.
