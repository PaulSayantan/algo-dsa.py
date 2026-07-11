# Unique Paths II

**Difficulty:** Medium

**Source:** LeetCode 63 — Unique Paths II

## Description

You are given an `m x n` integer array `grid`. There is a robot initially located
at the top-left corner (cell `(0, 0)`). The robot tries to move to the bottom-right
corner (cell `(m - 1, n - 1)`). The robot can only move **either down or right** at
any point in time.

An obstacle and space are marked as `1` and `0` respectively in `grid`. A path that
the robot takes **cannot include any square that is an obstacle**.

Return *the number of possible unique paths that the robot can take to reach the
bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to
`2 * 10^9`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: grid = [[0,0,0],
               [0,1,0],
               [0,0,0]]
Output: 2
```

**Explanation:** There is one obstacle in the middle of the 3x3 grid. The two paths
that avoid it are:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

### Example 2

```
Input: grid = [[0,1],
               [0,0]]
Output: 1
```

**Explanation:** The only path is Down -> Right, because the cell to the immediate
right of the start is an obstacle.

### Example 3

```
Input: grid = [[1]]
Output: 0
```

**Explanation:** The start cell itself is an obstacle, so there are no valid paths.

## Hint

Use **Dynamic Programming on Grid**, just like counting unrestricted paths, but
force the count of any obstacle cell to `0` so no path is allowed to pass through
it. Be careful seeding the first row and first column.
