# Minimum Obstacle Removal to Reach Corner

**Difficulty:** Medium (LeetCode marks it Hard; conceptually a clean 0-1 BFS)

**Source:** LeetCode 2290 — Minimum Obstacle Removal to Reach Corner

## Description

You are given a `0`-indexed 2-D integer array `grid` of size `m x n`. Each cell
has one of two values:

- `0` — an **empty** cell you can travel through freely, and
- `1` — an **obstacle** that may be removed.

You can move up, down, left, or right from and to an empty cell. Return the
**minimum number of obstacles to remove** so that you can travel from the
top-left corner `(0, 0)` to the bottom-right corner `(m - 1, n - 1)`.

Moving into an empty cell is free; moving into an obstacle cell costs `1`
(because you had to remove that obstacle). You want the route whose total number
of removed obstacles is smallest.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `grid[i][j]` is either `0` or `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`

## Examples

### Example 1

```
Input: grid = [[0, 1, 1],
               [1, 1, 0],
               [1, 1, 0]]
Output: 2
```

**Explanation:** Start at `(0,0)`. Any route to `(2,2)` must break through the
band of `1`s. The cheapest plan removes the obstacles at `(0,1)` and `(0,2)`,
then walks down the free cells of column 2: `(0,0) -> (0,1)* -> (0,2)* ->
(1,2) -> (2,2)`, where `*` marks a removed obstacle. That is 2 removals, and no
route removes fewer.

### Example 2

```
Input: grid = [[0, 1, 0, 0, 0],
               [0, 1, 0, 1, 0],
               [0, 0, 0, 1, 0]]
Output: 0
```

**Explanation:** There is already a clear path of empty cells: go down column 0
to `(2,0)`, then right to `(2,2)`, up to `(0,2)`, right to `(0,4)`, and down to
`(2,4)`. No obstacle needs to be removed, so the answer is `0`.

## Hint

Entering an empty cell costs `0` and entering an obstacle costs `1` — every edge
weight is `0` or `1`. That is the exact setting for **0-1 BFS**: use a deque,
push `0`-cost moves to the **front** and `1`-cost moves to the **back**. (A
regular Dijkstra min-heap also works but is a log factor slower.)
