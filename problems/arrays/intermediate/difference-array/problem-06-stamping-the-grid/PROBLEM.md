# Stamping the Grid

**Difficulty:** Hard

**Source:** LeetCode 2132 — Stamping the Grid

## Description

You are given an `m x n` binary matrix `grid` where each cell is either `0`
(empty) or `1` (occupied). You are also given two integers `stampHeight` and
`stampWidth`.

You want to fit the stamps such that they cover **all** the empty cells while
satisfying the following restrictions:

1. Cover all the **empty** cells.
2. Do **not** cover any of the **occupied** cells.
3. Each stamp must be placed fully inside the grid, aligned to the grid, exactly
   `stampHeight x stampWidth` in size, with no rotation.
4. Stamps **can overlap** each other, and you may use an unlimited number of
   stamps.

Return `true` if it is possible to fit the stamps such that every empty cell is
covered, and `false` otherwise.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 2 * 10^5`
- `grid[i][j]` is either `0` or `1`.
- `1 <= stampHeight, stampWidth <= 10^5`

## Examples

### Example 1

```
Input:  grid = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]], stampHeight = 2, stampWidth = 2
Output: true
```

**Explanation:** The grid is completely empty. Placing 2x2 stamps at the four
top-left positions `(0,0)`, `(0,1)`, `(1,0)`, `(1,1)` covers every cell without
overlapping any occupied cell (there are none). So the answer is `true`.

### Example 2

```
Input:  grid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]], stampHeight = 2, stampWidth = 2
Output: false
```

**Explanation:** The only occupied cell is the center `(1, 1)`. Every possible
2x2 stamp placement (top-left at `(0,0)`, `(0,1)`, `(1,0)`, or `(1,1)`) overlaps
the center cell, so **no** stamp can be placed at all. The eight empty cells
therefore cannot be covered, and the answer is `false`.

## Hint

Two layers of prefix-sum thinking. First, use a 2D **prefix sum** of occupied
cells to check, in O(1), whether a stamp anchored at `(r, c)` would land on any
`1`. For every valid placement, record the covered rectangle in a 2D
**Difference Array**, then materialize the coverage and confirm every empty cell
is covered at least once.
