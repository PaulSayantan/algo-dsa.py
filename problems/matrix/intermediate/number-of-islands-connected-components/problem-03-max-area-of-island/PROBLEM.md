# Max Area of Island

**Difficulty:** Medium

**Source:** LeetCode 695 (Max Area of Island)

## Description

You are given an `m x n` binary matrix `grid`. An **island** is a group of `1`s
(land) connected **4-directionally** (horizontal or vertical). You may assume
all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with value `1` in that island.

Return the maximum area of an island in `grid`. If there is no island, return
`0`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1` (integer values).

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

**Explanation:** The largest island is the cluster on the right side of rows
3-5 (cells `(3,8)`, `(4,8)`, `(4,9)`, `(3,10)`, `(4,10)`, `(5,10)`), which has
area `6`. No other connected region contains more than 6 land cells.

### Example 2

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Explanation:** There is no land, so the maximum island area is `0`.

### Example 3

```
Input: grid = [[1,1,0,0,1],[1,0,0,1,1]]
Output: 3
```

**Explanation:** The top-left island covers `(0,0)`, `(0,1)`, `(1,0)` for area
`3`. The right-side island covers `(0,4)`, `(1,3)`, `(1,4)` for area `3` as
well. The maximum is `3`.

## Hint

Same **Number of Islands / Connected Components** sweep, but instead of just
counting regions, have each flood return the *size* of the region it explored,
and track the running maximum.
