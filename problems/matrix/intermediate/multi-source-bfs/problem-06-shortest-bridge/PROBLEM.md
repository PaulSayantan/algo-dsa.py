# Shortest Bridge

**Difficulty:** Medium (leans Hard — combines flood fill with Multi-Source BFS)

**Source:** LeetCode 934 — Shortest Bridge

## Description

You are given an `n x n` binary matrix `grid` where `1` represents **land** and `0`
represents **water**. An **island** is a 4-directionally connected group of `1`s. The
grid contains **exactly two** islands.

You may change `0`s to `1`s to connect the two islands to form **one** island. Return
the **smallest number of `0`s** you must flip to connect the two islands.

Equivalently, you are finding the shortest 4-directional distance between the two
islands (the number of water cells strictly between them along the closest path).

## Constraints

- `n == grid.length == grid[i].length`
- `2 <= n <= 100`
- `grid[i][j]` is `0` or `1`.
- There are **exactly two** islands in `grid`.

## Examples

### Example 1

```
Input:  grid = [[0, 1],
                [1, 0]]
Output: 1
```

**Explanation:** The two single-cell islands are at `(0,1)` and `(1,0)`. Flipping one
water cell (either `(0,0)` or `(1,1)`) connects them, so the answer is `1`.

### Example 2

```
Input:  grid = [[0, 1, 0],
                [0, 0, 0],
                [0, 0, 1]]
Output: 2
```

**Explanation:** One island is the single cell `(0,1)`, the other is `(2,2)`. The
shortest connection flips two water cells (for example `(1,1)` and `(2,1)`, or `(1,1)`
and `(1,2)`), so the answer is `2`.

### Example 3

```
Input:  grid = [[1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]]
Output: 1
```

**Explanation:** The outer ring is one island and the single center cell `(2,2)` is the
other. They are separated by one layer of water, so flipping a single `0` (e.g.
`(2,1)`) bridges them; the answer is `1`.

## Hint

First use DFS/BFS **flood fill** to find and mark *all* cells of the **first** island.
Then push **every cell of that island** into a queue and run **Multi-Source BFS**
outward across water; the number of BFS levels expanded before you first touch the
second island is the answer.
