# Shortest Path in Binary Matrix

**Difficulty:** Medium

**Source:** LeetCode 1091 — Shortest Path in Binary Matrix

## Description

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear
path** from the top-left cell `(0, 0)` to the bottom-right cell `(n-1, n-1)`. If
there is no clear path, return `-1`.

A **clear path** is a path from the top-left to the bottom-right such that:

- All visited cells have value `0`.
- All movement is between cells that are connected **8-directionally** (any two
  cells sharing an edge or a corner are adjacent).

The **length of a clear path** is the number of visited cells on the path
(including the start and end cells).

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input:  grid = [[0,1],
                [1,0]]
Output: 2
```

**Explanation:** The path `(0,0) -> (1,1)` moves diagonally through two `0`
cells. Its length is `2`.

### Example 2

```
Input:  grid = [[0,0,0],
                [1,1,0],
                [1,1,0]]
Output: 4
```

**Explanation:** A shortest clear path is
`(0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)` visiting `5` cells... but a shorter
one exists using diagonals: `(0,0) -> (0,1) -> (1,2) -> (2,2)` visits `4` cells,
which is optimal.

### Example 3

```
Input:  grid = [[1,0,0],
                [1,1,0],
                [1,1,0]]
Output: -1
```

**Explanation:** The start cell `(0,0)` has value `1`, so no clear path can even
begin; the answer is `-1`.

## Hint

Every move costs one step and diagonals are allowed, so run an **8-directional
Grid BFS** from the start; the first time you dequeue the target, its distance is
the shortest path length.
