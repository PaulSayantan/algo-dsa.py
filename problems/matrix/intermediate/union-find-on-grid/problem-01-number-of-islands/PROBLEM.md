# Number of Islands

**Difficulty:** Medium

**Source:** LeetCode 200 (Number of Islands)

## Description

You are given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and
`'0'`s (water). Return the **number of islands**.

An **island** is a maximal group of `'1'` (land) cells connected **4-directionally**
(horizontally or vertically). You may assume all four edges of the grid are surrounded by
water. Diagonal adjacency does **not** connect two land cells.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Examples

### Example 1

```
Input:
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Explanation:** All the `'1'` cells in the top-left touch each other through horizontal or
vertical neighbors, forming a single connected landmass. There is exactly one island.

### Example 2

```
Input:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Explanation:** The top-left 2x2 block of land is one island. The single `'1'` at row 2,
column 2 is a second island (its diagonal neighbors do not count). The two `'1'`s in the
bottom-right, connected horizontally, form a third island. Total = 3.

## Hint

Treat each land cell as a node and **union** it with its right and down land neighbors. The
answer is the number of distinct sets among land cells — a direct application of
**Union–Find on Grid**.
