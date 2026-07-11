# Rotting Oranges

**Difficulty:** Medium

**Source:** LeetCode 994 — Rotting Oranges

## Description

You are given an `m x n` grid where each cell can have one of three values:

- `0` — an empty cell,
- `1` — a **fresh** orange, or
- `2` — a **rotten** orange.

Every minute, any fresh orange that is **4-directionally adjacent** (up, down, left,
right) to a rotten orange becomes rotten.

Return the **minimum number of minutes** that must elapse until no cell has a fresh
orange. If this is impossible (some fresh orange can never rot), return `-1`.

All currently rotten oranges start rotting **at the same time** (minute 0). This
"many things spreading at once" structure is exactly what Multi-Source BFS models:
the set of rotten oranges is the multi-source frontier, and each BFS level is one
minute.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Examples

### Example 1

```
Input: grid = [[2,1,1],
               [1,1,0],
               [0,1,1]]
Output: 4
```

**Explanation:** Starting from the rotten orange at `(0,0)`, the rot spreads one ring
per minute. After minute 1 the cells `(0,1)` and `(1,0)` rot; minute 2 `(0,2)` and
`(1,1)`; minute 3 `(2,1)`; minute 4 the last fresh orange at `(2,2)`. No fresh orange
remains after 4 minutes.

### Example 2

```
Input: grid = [[2,1,1],
               [0,1,1],
               [1,0,1]]
Output: -1
```

**Explanation:** The orange in the bottom-left corner `(2,0)` is surrounded only by
empty cells (`(1,0)=0` above and `(2,1)=0` to its right), so it can never rot. Since
a fresh orange always remains, the answer is `-1`.

### Example 3

```
Input: grid = [[0,2]]
Output: 0
```

**Explanation:** There are no fresh oranges at all, so zero minutes are required.

## Hint

Seed a queue with **all** rotten oranges at once and run **Multi-Source BFS**. Each
full level of the BFS corresponds to one elapsed minute; the answer is the number of
levels, and any fresh orange never dequeued means the answer is `-1`.
