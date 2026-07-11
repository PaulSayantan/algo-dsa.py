# Stamping the Grid

**Difficulty:** Hard

**Source:** LeetCode 2132 — Stamping the Grid

## Description

You are given an `m x n` binary matrix `grid` where each cell is either `0`
(empty) or `1` (occupied). You are also given the dimensions of a stamp:
`stampHeight x stampWidth`.

You want to fit the stamps such that **all** of the following are satisfied:

1. Cover **all the empty cells**.
2. Do **not** cover any of the occupied cells.
3. Place stamps fully **inside the grid** (no part may lie outside).
4. Stamps may **not** be rotated.
5. Stamps **may overlap** each other, and you may use as many stamps as you want.

Return `true` if it is possible to fit the stamps under these rules, or `false`
otherwise.

## Constraints

- `m == grid.length`
- `n == grid[r].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 2 * 10^5`
- `grid[r][c]` is either `0` or `1`.
- `1 <= stampHeight, stampWidth <= 10^5`

## Examples

### Example 1

```
Input:
  grid = [[1,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,1]],
  stampHeight = 2, stampWidth = 2
Output: true
```

**Explanation:**
Every empty cell can be covered by at least one 2x2 stamp that avoids the two
occupied corners. For instance, stamps placed with top-left corners at `(0,1)`,
`(1,0)`, `(1,2)`, and `(2,1)` together cover all zeros without touching a `1`.

### Example 2

```
Input:
  grid = [[1,0,0],
          [0,1,0],
          [0,0,1]],
  stampHeight = 1, stampWidth = 2
Output: false
```

**Explanation:**
No horizontal `1x2` stamp fits without covering a `1` in a position that would
also cover the empty cell `(0,1)` (its only fitting stamps overlap an occupied
cell). Some empty cells cannot be covered, so the answer is `false`.

## Hint

Two layers of matrix tricks. First use a **2D prefix sum** of occupied cells to
test, in `O(1)`, whether a stamp placed at each top-left corner would be free of
`1`s. For every valid placement, mark its rectangle with a **2D Difference
Array**; a final prefix sum tells you the stamp-coverage count of each cell, and
every empty cell must have coverage `>= 1`.
