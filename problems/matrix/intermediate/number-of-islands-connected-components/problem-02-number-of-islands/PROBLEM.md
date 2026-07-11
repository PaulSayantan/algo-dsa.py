# Number of Islands

**Difficulty:** Medium

**Source:** LeetCode 200 (Number of Islands)

## Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land)
and `'0'`s (water), return the **number of islands**.

An island is a maximal group of land cells connected **4-directionally**
(horizontally or vertically). You may assume all four edges of the grid are
surrounded by water. Diagonal connections do **not** join two land cells into
the same island.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'` (character values, not integers).

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

**Explanation:** All the `'1'`s in the top-left are 4-directionally connected
into a single blob, so there is exactly one island.

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

**Explanation:** The top-left `2x2` block is one island. The lone `'1'` at
`(2,2)` is a second island. The two `'1'`s at `(3,3)` and `(3,4)` form a third.
Note that `(2,2)` and `(3,3)` are only diagonally adjacent, so they are
separate islands.

### Example 3

```
Input: grid = [["0","0","0"],["0","0","0"]]
Output: 0
```

**Explanation:** There is no land, so there are no islands.

## Hint

This is the archetypal **Number of Islands / Connected Components** problem.
Scan the grid; each time you find an unvisited land cell, that is a brand-new
island — flood the whole connected region so you do not count it again.
