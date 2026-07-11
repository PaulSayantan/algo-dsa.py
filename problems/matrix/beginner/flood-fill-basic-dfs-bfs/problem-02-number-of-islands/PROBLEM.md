# Number of Islands

**Difficulty:** Medium

**Source:** LeetCode 200 — Number of Islands

## Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land)
and `'0'`s (water), return **the number of islands**.

An **island** is surrounded by water and is formed by connecting adjacent lands
**horizontally or vertically** (not diagonally). You may assume all four edges of
the grid are surrounded by water.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Examples

### Example 1

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Explanation:** All the `'1'`s are connected 4-directionally into a single
landmass, so there is exactly one island.

### Example 2

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Explanation:** There are three separate groups of connected land: the 2x2
block in the top-left, the single cell at `(2,2)`, and the two connected cells
at `(3,3)`–`(3,4)`. None of these groups touch each other 4-directionally.

## Hint

Use **Flood Fill (basic DFS/BFS)**: scan the grid; each time you find an unvisited
land cell, that is a new island — increment the counter and flood-fill the entire
connected landmass so its cells are not counted again.
