# Max Area of Island

**Difficulty:** Medium

**Source:** LeetCode 695 — Max Area of Island

## Description

You are given an `m x n` binary matrix `grid`. An **island** is a group of `1`s
(land) connected **4-directionally** (horizontal or vertical). You may assume all
four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return the **maximum area** of an island in `grid`. If there is no island,
return `0`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
```

**Explanation:** The largest island is the connected block of `1`s in the
top-right/center around rows 3–5 and columns 8–10, which has area `6`. No other
connected group of `1`s has more cells.

### Example 2

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Explanation:** There is no land in the grid, so the maximum island area is `0`.

## Hint

Use **Flood Fill (basic DFS/BFS)**: for each unvisited land cell, flood-fill its
connected component and have the fill **return the number of cells it visited**.
Track the maximum returned area across all fills.
