# Rotting Oranges

**Difficulty:** Medium

**Source:** LeetCode 994 — Rotting Oranges

## Description

You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten
orange becomes rotten.

Return the **minimum number of minutes** that must elapse until no cell has a
fresh orange. If this is impossible, return `-1`.

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

**Explanation:** The rot spreads outward one ring per minute. After minute 1
`(0,1)` and `(1,0)` rot; after minute 2 `(0,2)` and `(1,1)` rot; after minute 3
`(2,1)`; after minute 4 the last fresh orange `(2,2)` rots. Total: 4 minutes.

### Example 2

```
Input: grid = [[2,1,1],
               [0,1,1],
               [1,0,1]]
Output: -1
```

**Explanation:** The orange in the bottom-left corner `(2,0)` is never adjacent
to a rotten orange (it is walled off by empty cells), so it can never rot and the
answer is `-1`.

### Example 3

```
Input: grid = [[0,2]]
Output: 0
```

**Explanation:** There are no fresh oranges at minute 0, so no time needs to
elapse.

## Hint

The rot expands in synchronized rings — exactly the "waves" of BFS. Seed a queue
with **all rotten oranges at once** and run a level-by-level **Lee Algorithm**;
the number of levels processed is the elapsed minutes.
