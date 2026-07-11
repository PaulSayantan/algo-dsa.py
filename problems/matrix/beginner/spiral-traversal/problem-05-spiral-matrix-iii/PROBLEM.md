# Spiral Matrix III

**Difficulty:** Medium

**Source:** LeetCode 885 — Spiral Matrix III

## Description

You start on the cell `(rStart, cStart)` of an `rows x cols` grid, facing
**east**. The top-left corner is `(0, 0)` and the bottom-right corner is
`(rows - 1, cols - 1)`.

You walk in a **clockwise outward spiral**, visiting every cell of the grid.
Whenever you would move outside the grid, you continue the walk (still counting
the turn pattern) but you do **not** record the out-of-bounds positions. Keep
walking until you have visited all `rows * cols` cells.

Return an array of the coordinates `[r, c]` of every grid cell, **in the order
you visit them**.

## Constraints

- `1 <= rows, cols <= 100`
- `0 <= rStart < rows`
- `0 <= cStart < cols`

## Examples

### Example 1

```
Input:  rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
```

Explanation: Starting at `(0,0)` facing east, we simply walk right across the
only row, collecting all four cells.

### Example 2

```
Input:  rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],
         [3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],
         [4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],
         [4,0],[3,0],[2,0],[1,0],[0,0]]
```

Explanation: From `(1,4)` the spiral grows with step lengths `1,1,2,2,3,3,...`
in the direction cycle east, south, west, north. Positions that fall outside the
`5 x 6` grid are skipped, but the walk keeps going until all `30` cells appear.

### Example 3

```
Input:  rows = 2, cols = 2, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[1,1],[1,0]]
```

Explanation: East to `(0,1)`, south to `(1,1)`, then the spiral turns west to
`(1,0)`; all four cells collected.

## Hint

This is the **outward-growing** flavor of **Spiral Traversal**: take
`1, 1, 2, 2, 3, 3, ...` steps cycling through directions east, south, west,
north, and record only the steps that land inside the grid.
