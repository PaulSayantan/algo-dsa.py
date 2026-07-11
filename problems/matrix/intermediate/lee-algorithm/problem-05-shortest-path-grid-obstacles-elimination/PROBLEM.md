# Shortest Path in a Grid with Obstacles Elimination

**Difficulty:** Hard

**Source:** LeetCode 1293 — Shortest Path in a Grid with Obstacles Elimination

## Description

You are given an `m x n` integer matrix `grid` where each cell is either `0`
(empty) or `1` (obstacle). You can move up, down, left, or right from and to an
empty cell in **one step**.

Return the **minimum number of steps** to walk from the upper-left corner
`(0, 0)` to the lower-right corner `(m - 1, n - 1)` given that you can eliminate
**at most** `k` obstacles. If it is not possible to find such a walk, return
`-1`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 40`
- `1 <= k <= m * n`
- `grid[i][j]` is either `0` or `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`

## Examples

### Example 1

```
Input: grid = [[0,0,0],
               [1,1,0],
               [0,0,0],
               [0,1,1],
               [0,0,0]], k = 1
Output: 6
```

**Explanation:** The shortest path without eliminating any obstacle is 10 steps
(snaking around the walls). With `k = 1` elimination we can break through one
obstacle and reach the target in 6 steps. One such path eliminates the obstacle
at `(3, 2)`.

### Example 2

```
Input: grid = [[0,1,1],
               [1,1,1],
               [1,0,0]], k = 1
Output: -1
```

**Explanation:** To reach the target we would have to pass through at least two
obstacles, but we may only remove one, so no valid path exists.

## Hint

Plain BFS on `(row, col)` is not enough because *how many eliminations remain*
changes what is reachable. Extend each BFS state to `(row, col, k_remaining)` and
run the **Lee Algorithm** over this augmented state space, visiting each
`(cell, remaining)` combination at most once.

## Follow-up Notes

Because all moves cost 1, the first time BFS pops the target it has the minimum
step count. The state space has size `m × n × (k + 1)`, so the search stays
polynomial.
