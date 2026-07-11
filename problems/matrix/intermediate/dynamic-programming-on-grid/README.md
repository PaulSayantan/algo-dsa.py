# Dynamic Programming on Grid

**Dynamic Programming on Grid** is a family of techniques where we solve a problem
defined over a 2D matrix by filling in a table `dp[i][j]` whose value depends on a
small, fixed set of neighboring cells (typically the cell above, to the left, and/or
the upper-left diagonal). Because each cell's answer is built from already-computed
neighbors, we can process the grid in a single sweep (usually top-left to
bottom-right, or bottom-right to top-left) and never recompute anything.

## When to reach for it

Reach for grid DP when the problem has all of these traits:

- The state naturally lives on cell coordinates `(row, col)`.
- The answer for a cell can be expressed as a recurrence over a **constant number**
  of adjacent cells (e.g. `dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`).
- Movement or dependency is **monotone / acyclic** (e.g. you may only move right and
  down), so there are no circular dependencies between cells.

Classic signals: "count the number of paths", "minimum / maximum cost path",
"largest all-ones square/rectangle", and "fill-in from a corner" problems.

## Typical complexity

For an `m x n` grid, the standard approach visits every cell once and does O(1) work
per cell:

- **Time:** `O(m * n)`
- **Space:** `O(m * n)` for a full table, reducible to `O(n)` (or `O(min(m, n))`)
  because each row depends only on the previous row (and sometimes the current row).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Unique Paths](problem-01-unique-paths/PROBLEM.md) | Count monotone paths from top-left to bottom-right moving only right/down. | Medium |
| 2 | [Minimum Path Sum](problem-02-minimum-path-sum/PROBLEM.md) | Find the minimum-cost path summing cell values, moving only right/down. | Medium |
| 3 | [Unique Paths II](problem-03-unique-paths-ii/PROBLEM.md) | Count right/down paths on a grid where some cells are blocked obstacles. | Medium |
| 4 | [Maximal Square](problem-04-maximal-square/PROBLEM.md) | Find the area of the largest all-ones square submatrix. | Medium |
| 5 | [Dungeon Game](problem-05-dungeon-game/PROBLEM.md) | Minimum starting health to reach the princess, solved bottom-right to top-left. | Hard |
