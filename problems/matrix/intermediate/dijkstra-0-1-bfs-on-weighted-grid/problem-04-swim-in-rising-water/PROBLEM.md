# Swim in Rising Water

**Difficulty:** Hard

**Source:** LeetCode 778 — Swim in Rising Water

## Description

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]`
represents the **elevation** at that point `(i, j)`.

It starts raining, and water fills the grid over time. At time `t`, the depth of
the water everywhere is `t`. You can swim from a square to another 4-directionally
adjacent square **if and only if** the elevation of both squares individually is
at most `t` (you can swim infinitely far in zero time as long as the water level
permits). You must stay within the boundaries of the grid during your swim.

Return the **least time** until you can reach the bottom-right square
`(n - 1, n - 1)` starting from the top-left square `(0, 0)`.

Equivalently: over all paths from the top-left to the bottom-right, find the one
whose **maximum cell elevation** is smallest. That maximum elevation is the
earliest time you can complete the swim (you simply wait until the water is high
enough to clear the worst cell, then swim through).

## Constraints

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value `grid[i][j]` is **unique** (a permutation of `0 .. n^2 - 1`).

## Examples

### Example 1

```
Input: grid = [[0, 2],
               [1, 3]]
Output: 3
```

**Explanation:** The destination `(1,1)` has elevation `3`, so you cannot arrive
before `t = 3` no matter which route you take. At `t = 3` the whole grid is
submerged and you can swim `(0,0) -> (1,0) -> (1,1)` (elevations `0, 1, 3`). The
maximum elevation on that path is `3`, so the answer is `3`.

### Example 2

```
Input: grid = [[ 0,  1,  2,  3,  4],
               [24, 23, 22, 21,  5],
               [12, 13, 14, 15, 16],
               [11, 17, 18, 19, 20],
               [10,  9,  8,  7,  6]]
Output: 16
```

**Explanation:** The optimal route runs across the top row, drops down the right
column to cell `16`, then snakes down the left/bottom to the exit — visiting
elevations `0, 1, 2, 3, 4, 5, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6` and ending
at `(4, 4) = 6`. Its maximum elevation is `16`. Any route into the bottom-right
region must cross a cell of elevation at least `16`, so you cannot finish before
`t = 16`, making `16` optimal.

## Hint

This is a **minimax path** on cell elevations: minimise the largest elevation you
step on. Run **Dijkstra on the grid** but relax with `time[nb] =
min(time[nb], max(time[cur], grid[nb]))` — use `max` instead of `+`. (Binary
search on `t` plus BFS, or a Union-Find that adds cells in elevation order, also
solve it.)
