# Maximum Rectangle Overlap

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (grid overlap counting; a
2D generalization of the "maximum number of overlapping intervals" problem).

## Description

You are given a list of axis-aligned rectangles on an integer grid. Each
rectangle is described as `[x1, y1, x2, y2]`, where `(x1, y1)` is its bottom-left
corner and `(x2, y2)` is its top-right corner. A rectangle **covers** every
integer lattice cell `(x, y)` with `x1 <= x <= x2` and `y1 <= y <= y2`
(both corners inclusive).

Return the **maximum number of rectangles that cover any single cell** — i.e. the
largest overlap depth anywhere on the grid.

All coordinates are non-negative and bounded, so you may allocate a grid of size
`(MAX_COORD + 2) x (MAX_COORD + 2)`.

## Constraints

- `1 <= rectangles.length <= 10^5`
- `0 <= x1 <= x2 <= 1000`
- `0 <= y1 <= y2 <= 1000`

## Examples

### Example 1

```
Input: rectangles = [[0,0,2,2],[1,1,3,3],[1,1,2,2]]
Output: 3
```

**Explanation:**
Cell `(1,1)` lies inside all three rectangles: `[0,0,2,2]` (0–2 in both axes),
`[1,1,3,3]`, and `[1,1,2,2]`. No cell is covered more than three times, so the
answer is `3`.

### Example 2

```
Input: rectangles = [[0,0,1,1],[2,2,3,3]]
Output: 1
```

**Explanation:**
The two rectangles are disjoint, so every covered cell is covered exactly once.
The maximum overlap depth is `1`.

## Hint

Do not scan each rectangle's interior. Add `+1` over each rectangle using a
**2D Difference Array**, run a 2D prefix sum to obtain the coverage count of
every cell, and take the maximum entry.
