# Boundary / Perimeter Traversal

**Category:** Matrix — Beginner

## What it is

Boundary (or perimeter) traversal is the technique of visiting **only the outer ring**
of a 2-D matrix — the first row, the last row, the first column, and the last column —
while skipping every interior cell. The elements are usually visited in a fixed order,
most commonly **clockwise** starting from the top-left corner:

```
top row      →   left to right
right column ↓   top to bottom
bottom row   ←   right to left
left column  ↑   bottom to top
```

For an `m x n` matrix the boundary contains `2*(m + n) - 4` elements (when both
`m > 1` and `n > 1`). A single row has `n` boundary elements and a single column has
`m` boundary elements — these degenerate cases are where most bugs live, because the
four "sides" overlap and corners get counted twice.

## When to reach for it

- The problem asks about the **edge / border / frame / outer ring** of a grid.
- You need to read, sum, rotate, sort, or rewrite only the outermost cells.
- You are peeling a matrix layer by layer (spiral order = boundary traversal applied
  to successively smaller sub-matrices).

## Complexity

- **Time:** `O(m + n)` to touch every boundary cell once (the interior is never visited).
  For layer-by-layer peeling (e.g. spiral) it becomes `O(m * n)` because every cell is
  eventually on some ring.
- **Space:** `O(1)` extra beyond the output list (we only track a handful of index
  pointers).

## The mental model — four directed sweeps

Track four boundaries: `top`, `bottom`, `left`, `right`. Walk the top row, then the
right column, then the bottom row (reversed), then the left column (reversed). Guard the
bottom row and left column with `if top != bottom` / `if left != right` so a single row
or single column is not emitted twice.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Boundary Traversal (Clockwise)](problem-01-boundary-traversal-clockwise/PROBLEM.md) | Emit the outer ring in clockwise order | Easy |
| 2 | [Sum of Boundary Elements](problem-02-sum-of-boundary-elements/PROBLEM.md) | Aggregate the ring without double-counting corners | Easy |
| 3 | [Sort the Boundary Elements](problem-03-sort-boundary-elements/PROBLEM.md) | Extract ring → sort → write ring back | Medium |
| 4 | [Rotate the Boundary by K](problem-04-rotate-boundary-by-k/PROBLEM.md) | Extract ring → cyclic-shift → write back | Medium |
| 5 | [Spiral Matrix](problem-05-spiral-matrix/PROBLEM.md) | Repeated boundary traversal of shrinking rings | Medium |
