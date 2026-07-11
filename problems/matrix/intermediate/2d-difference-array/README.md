# 2D Difference Array

**Range-update rectangular regions in O(1), then recover the final grid with a 2D prefix sum.**

## What it is

A 2D difference array is the two-dimensional analogue of the 1D difference
trick. Given a matrix `M`, its difference matrix `D` stores values such that
running a **2D prefix sum** over `D` reconstructs `M`. The magic is the reverse
direction: to add a constant `v` to every cell inside an axis-aligned rectangle
`(r1, c1)`–`(r2, c2)`, you only touch **four corner cells** of `D`:

```
D[r1  ][c1  ] += v
D[r2+1][c1  ] -= v
D[r1  ][c2+1] -= v
D[r2+1][c2+1] += v
```

Each rectangle update is therefore `O(1)` regardless of the rectangle's size.
After all updates are recorded, a single 2D prefix-sum pass "spreads" each
corner contribution across the grid, giving the final matrix.

Think of it as inclusion–exclusion: `+v` at the top-left corner floods the
entire lower-right quadrant; the two `-v` terms cancel the flood past the right
and bottom edges; the `+v` at the bottom-right corner adds back the
double-subtracted quadrant.

## When to reach for it

- You must apply **many** rectangle/subgrid range-add updates and only need the
  final grid once (offline, no interleaved point queries during updates).
- You want to test **feasibility of placing stamps/tiles** in a grid using a
  coverage count.
- You need the **union area** of many rectangles (paired with coordinate
  compression).
- Any problem phrased as "add X to every cell in this rectangle, repeat Q
  times, then read the result."

If you instead need to *query* arbitrary rectangle **sums** of a static matrix,
you want a plain 2D **prefix sum**; the difference array is its inverse and is
about *building* a matrix from range updates.

## Complexity

For an `m x n` grid with `q` rectangle updates:

| Phase | Time | Space |
|-------|------|-------|
| Apply all updates | `O(q)` | `O(m*n)` for the diff matrix |
| Reconstruct via prefix sum | `O(m*n)` | in-place |
| **Total** | **`O(m*n + q)`** | **`O(m*n)`** |

Compare with the naive approach of stamping each rectangle cell-by-cell, which
is `O(q * m * n)` in the worst case.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Increment Submatrices by One](problem-01-increment-submatrices-by-one/PROBLEM.md) | Apply many `+1` rectangle updates to a zero grid and return the result | Medium |
| 2 | [Maximum Rectangle Overlap](problem-02-maximum-rectangle-overlap/PROBLEM.md) | Find the highest number of rectangles covering any single cell | Medium |
| 3 | [Batch Updates and Region Sums](problem-03-batch-updates-region-sums/PROBLEM.md) | Add values over rectangles, then answer rectangle-sum queries | Medium |
| 4 | [Rectangle Area II](problem-04-rectangle-area-ii/PROBLEM.md) | Total area of the union of rectangles via coordinate compression + diff | Hard |
| 5 | [Stamping the Grid](problem-05-stamping-the-grid/PROBLEM.md) | Decide whether stamps can cover every empty cell without overlapping occupied cells | Hard |
