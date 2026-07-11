# Max Area of Island

**Difficulty:** Medium

**Source:** LeetCode 695 — Max Area of Island

## Description

You are given an `m x n` binary matrix `grid`. An **island** is a group of `1`s
(land) connected **4-directionally** (horizontal or vertical). You may assume all
four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with value `1` in the island.

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
Input:  grid = [
  [0,0,1,0,0],
  [0,1,1,0,0],
  [0,0,0,1,1],
  [0,0,0,1,1]
]
Output: 4
```

**Explanation:** The top-left island `{(0,2),(1,1),(1,2)}` has area 3. The
bottom-right island `{(2,3),(2,4),(3,3),(3,4)}` has area 4, which is the largest.

### Example 2

```
Input:  grid = [
  [0,0,0,0],
  [0,0,0,0]
]
Output: 0
```

**Explanation:** There is no land at all, so the maximum island area is `0`.

## Hint

Run a **Grid DFS / BFS** from each unvisited land cell and have the traversal
*return the size* of the region it floods; track the maximum across all regions.
