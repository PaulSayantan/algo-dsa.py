# Minimum Cells to Block a Path

**Difficulty:** Hard

**Source:** Classic (minimum vertex cut on a grid — Menger's theorem; "disconnect the maze" family)

## Description

You are given an `R × C` grid where each cell is open (`'.'`) or a wall (`'#'`). Movement is
allowed between orthogonally adjacent (up/down/left/right) open cells. The **source** is the
top-left cell `(0, 0)` and the **sink** is the bottom-right cell `(R-1, C-1)`; both are
guaranteed to be open, and neither may be removed.

You want to make it **impossible to travel from the source to the sink** by converting some
open cells into walls. You may convert any open cells **except the source and the sink**.

Return the **minimum number of cells** you must convert to walls to disconnect the source
from the sink. If it is impossible to disconnect them (for example, the source and sink are
orthogonally adjacent), return `-1`.

This is a **minimum vertex cut** problem. By **Menger's theorem**, the minimum number of
vertices whose removal disconnects source from sink equals the maximum number of
**vertex-disjoint** source→sink paths — a single max-flow computation after
**node-splitting** (each removable cell gets an `in → out` edge of capacity 1; the
non-removable source and sink get capacity `∞`).

## Constraints

- `1 <= R, C <= 100`
- Each cell is `'.'` (open) or `'#'` (wall).
- `grid[0][0] == '.'` and `grid[R-1][C-1] == '.'`.
- The source and sink are different cells.
- Return `-1` when disconnection is impossible.

## Examples

### Example 1

```
Input:
grid = [
  "..",
  ".."
]
Output: 2
Explanation: Source (0,0) and sink (1,1). There are two vertex-disjoint routes:
(0,0)->(0,1)->(1,1) and (0,0)->(1,0)->(1,1). They share only the endpoints, so you must
wall off both interior cells (0,1) and (1,0) — removing just one leaves the other route.
Minimum cut = 2.
```

### Example 2

```
Input:
grid = [
  "..."
]
Output: 1
Explanation: The only route is (0,0)->(0,1)->(0,2). Converting the single interior cell
(0,1) into a wall disconnects source from sink. Minimum cut = 1.
```

### Example 3

```
Input:
grid = [
  ".#",
  "#."
]
Output: 0
Explanation: Source (0,0)'s only neighbors (0,1) and (1,0) are both walls, so the source
is already isolated from the sink. No cells need to be removed; the answer is 0.
```

## Hint

The cells you remove are vertices, so the answer is a minimum vertex cut. Split each
removable cell into `in → out` (capacity 1), give the source and sink capacity `∞`, and
compute the max flow — **Max-Flow / Min-Cut on Grid** with Menger's theorem gives the
number of cells to remove.
