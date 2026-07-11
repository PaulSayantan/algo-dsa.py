# Shortest Path in a Grid with Obstacles Elimination

**Difficulty:** Hard

**Source:** LeetCode 1293 — Shortest Path in a Grid with Obstacles Elimination

## Description

You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or
`1` (obstacle). You can move up, down, left, or right from and to an empty cell **in one
step**.

Return the **minimum number of steps** to walk from the upper-left corner `(0, 0)` to
the lower-right corner `(m-1, n-1)`, given that you may eliminate **at most `k`
obstacles**. If it is not possible to reach the corner, return `-1`.

Stepping onto an obstacle cell consumes one of your `k` eliminations; stepping onto an
empty cell consumes none.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 40`
- `1 <= k <= m * n`
- `grid[i][j]` is either `0` or `1`.
- `grid[0][0] == grid[m-1][n-1] == 0`

## Examples

### Example 1

```
Input: grid = [[0,0,0],
               [1,1,0],
               [0,0,0],
               [0,1,1],
               [0,0,0]],
       k = 1
Output: 6
```

**Explanation:** The shortest path without eliminating any obstacle is `10` steps. With
`k = 1` we may break through one obstacle; the path
`(0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2*) -> (4,2)` breaks the obstacle at
`(3,2)` and reaches the goal in `6` steps.

### Example 2

```
Input: grid = [[0,1,1],
               [1,1,1],
               [1,0,0]],
       k = 1
Output: -1
```

**Explanation:** To go from `(0,0)` to `(2,2)` you must pass through at least two
obstacles, but `k = 1` only lets you remove one, so the corner is unreachable.

## Constraints recap on the state

Two visits to the same cell are **not** equivalent if they arrive with different numbers
of remaining eliminations — arriving with more budget left is strictly at least as good.

## Hint

The state is not just the cell; it is the triple `(row, col, eliminations_left)`. Run
**A\* Search** over that augmented state graph, ordering the queue by `g + h` where `g`
is steps taken and `h` is the **Manhattan distance** `|m-1-r| + |n-1-c|` to the goal —
a valid lower bound because you must take at least that many orthogonal steps regardless
of obstacles.
