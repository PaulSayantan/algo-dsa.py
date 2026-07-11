# Swim in Rising Water

**Difficulty:** Hard

**Source:** LeetCode 778 (Swim in Rising Water)

## Description

You are given an `n x n` integer matrix `grid` where `grid[i][j]` is the **elevation** at cell
`(i, j)`. The values are a permutation of `0, 1, ..., n*n - 1`.

Rain starts to fall. At time `t`, the water level everywhere is `t`. You can swim from a cell to
an adjacent one (4-directionally) **if and only if** the water level is at least the elevation
of *both* cells — equivalently, you may stand on any cell whose elevation is `<= t`, and move
freely among such cells. Swimming takes no time; you just cannot enter a cell until the water
has risen to its elevation.

Starting at the top-left cell `(0, 0)`, return the **least time** `t` at which you can reach the
bottom-right cell `(n-1, n-1)`.

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value `grid[i][j]` is **unique** (a permutation of `0 .. n*n-1`).

## Examples

### Example 1

```
Input: grid = [[0,2],[1,3]]
Output: 3
```

**Explanation:** At `t = 3` the water level is high enough to stand on every cell (the max
elevation on any path to (1,1) is 3, its own elevation). At `t = 2` you can be on cells with
elevation ≤ 2 — that is (0,0)=0, (1,0)=1, (0,1)=2 — but the destination (1,1)=3 is still above
water, so you cannot arrive. Hence the answer is 3.

### Example 2

```
Input:
grid = [
  [ 0, 1, 2, 3, 4],
  [24,23,22,21, 5],
  [12,13,14,15,16],
  [11,17,18,19,20],
  [10, 9, 8, 7, 6]
]
Output: 16
```

**Explanation:** The final path must cross the cell with elevation 16, and there is a route
from (0,0) to (4,4) using only cells with elevation ≤ 16. No lower water level connects the two
corners, so the minimum time is 16.

## Hint

Think of it as **percolation**: activate cells in increasing order of elevation and union each
newly activated cell with its already-active neighbors using **Union–Find on Grid**. The answer
is the first elevation `t` at which the source and target land in the same set.

## Follow-up

Can you also solve it with a Dijkstra-style min-heap or with binary search + BFS? Compare their
complexities to the union-find sweep.
