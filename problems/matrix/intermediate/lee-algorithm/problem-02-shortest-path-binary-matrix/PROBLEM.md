# Shortest Path in Binary Matrix

**Difficulty:** Medium

**Source:** LeetCode 1091 — Shortest Path in Binary Matrix

## Description

Given an `n x n` binary matrix `grid`, return the length of the **shortest clear
path** in the matrix. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the top-left cell
(i.e., `(0, 0)`) to the bottom-right cell (i.e., `(n - 1, n - 1)`) such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally connected** (they are
  different and share an edge **or a corner**).

The **length of a clear path** is the number of visited cells of this path
(counting both the start and end cells).

## Constraints

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: grid = [[0,1],
               [1,0]]
Output: 2
```

**Explanation:** The path goes from `(0,0)` diagonally to `(1,1)`. Both cells
are `0` and they are connected corner-to-corner, so 2 cells are visited.

### Example 2

```
Input: grid = [[0,0,0],
               [1,1,0],
               [1,1,0]]
Output: 4
```

**Explanation:** One shortest path visits `(0,0) -> (0,1) -> (1,2) -> (2,2)`,
using diagonal moves where useful. That is 4 cells.

### Example 3

```
Input: grid = [[1,0,0],
               [1,1,0],
               [1,1,0]]
Output: -1
```

**Explanation:** The start cell `(0,0)` is a `1`, so no clear path can even
begin, and the answer is `-1`.

## Hint

This is a shortest-path count on an unweighted grid with **8 directions**. Use
the **Lee Algorithm** (BFS) starting from `(0,0)`; count cells rather than edges
and remember to reject the start/end cells if they are blocked.
