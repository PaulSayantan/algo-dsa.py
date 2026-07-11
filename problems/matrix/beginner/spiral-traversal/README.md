# Spiral Traversal

**Spiral traversal** means visiting the cells of a 2D matrix in a spiral order:
walk along the top row left-to-right, down the right column, along the bottom
row right-to-left, up the left column, then repeat on the inner sub-matrix that
remains. Each full loop peels off the outermost "ring" of the matrix, so the
region you still have to visit keeps shrinking until nothing is left.

## When to reach for it

Reach for spiral traversal whenever a problem asks you to **read, fill, or
generate** the entries of a matrix in a rotating, layer-by-layer order rather
than a plain row-major scan. Typical signals:

- "Return all elements of the matrix in spiral order."
- "Fill an `n x n` matrix with `1..n^2` in a spiral."
- "Populate the grid from a stream/list following a spiral path."
- "Walk outward in a spiral from a starting cell."

The core mechanism is the **four shrinking boundaries** `top`, `bottom`,
`left`, `right`. You always move in the fixed cycle
`right -> down -> left -> up`, and after finishing an edge you move the
corresponding boundary inward by one. A guard (`top <= bottom` and
`left <= right`) prevents re-visiting cells when the matrix is non-square.

A second, related variant is the **outward-growing spiral** (used by "Spiral
Matrix III"): instead of shrinking boundaries you start at a cell and take
`1, 1, 2, 2, 3, 3, ...` steps in the directions East, South, West, North,
skipping any step that leaves the grid. Both are "spiral traversal"; the
boundary-shrinking form is by far the most common.

## Complexity

For an `m x n` matrix, every cell is visited exactly once, giving:

- **Time:** `O(m * n)`
- **Space:** `O(1)` extra (excluding the output). The outward-growing variant
  is `O(max(m, n)^2)` steps because some steps fall outside the grid, but still
  produces `m * n` cells.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Spiral Matrix](problem-01-spiral-matrix/PROBLEM.md) | Return all elements of a matrix in clockwise spiral order. | Easy/Medium |
| 2 | [Anti-clockwise Spiral Traversal](problem-02-anticlockwise-spiral-traversal/PROBLEM.md) | Return all elements in counter-clockwise spiral order (down the first column first). | Easy |
| 3 | [Spiral Matrix II](problem-03-spiral-matrix-ii/PROBLEM.md) | Generate an `n x n` matrix filled with `1..n^2` in spiral order. | Medium |
| 4 | [Spiral Matrix IV](problem-04-spiral-matrix-iv/PROBLEM.md) | Fill an `m x n` grid from a linked list along a spiral path, padding with `-1`. | Medium |
| 5 | [Spiral Matrix III](problem-05-spiral-matrix-iii/PROBLEM.md) | Visit every cell walking an outward-growing spiral from a start cell. | Medium/Hard |
