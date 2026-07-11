# Rotting Oranges

**Difficulty:** Medium

**Source:** LeetCode 994 — Rotting Oranges

## Description

You are given an `m x n` grid where each cell can have one of three values:

- `0` — an empty cell,
- `1` — a fresh orange,
- `2` — a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten
orange becomes rotten.

Return the **minimum number of minutes** that must elapse until no cell has a
fresh orange. If this is impossible (some fresh orange can never rot), return
`-1`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Examples

### Example 1

```
Input:  grid = [[2,1,1],
                [1,1,0],
                [0,1,1]]
Output: 4
```

**Explanation:** Minute 1: `(0,1)` and `(1,0)` rot. Minute 2: `(0,2)` and `(1,1)`
rot. Minute 3: `(2,1)` rots. Minute 4: `(2,2)` rots. After 4 minutes every orange
is rotten.

### Example 2

```
Input:  grid = [[2,1,1],
                [0,1,1],
                [1,0,1]]
Output: -1
```

**Explanation:** The fresh orange at the bottom-left corner `(2,0)` is never
adjacent to any orange that becomes rotten, so it can never rot. The answer
is `-1`.

### Example 3

```
Input:  grid = [[0,2]]
Output: 0
```

**Explanation:** There are no fresh oranges at minute `0`, so the elapsed time
needed is `0`.

## Hint

Push every initially rotten orange into a queue at once and run a
**multi-source Grid BFS**; each BFS level is one minute of spreading rot.
