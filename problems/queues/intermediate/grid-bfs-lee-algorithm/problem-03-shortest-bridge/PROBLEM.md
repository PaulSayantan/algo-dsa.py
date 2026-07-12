# Shortest Bridge

**Difficulty:** Medium

**Source:** LeetCode 934 — Shortest Bridge

## Description

You are given an `n × n` binary matrix `grid` containing **exactly two** islands (maximal 4-connected groups of `1`-cells). You may flip `0`-cells to `1` to connect the two islands into one.

Return the **smallest number of `0`-cells** that must be flipped so the two islands become connected 4-directionally.

Constraints: `2 <= n <= 100`; `grid[i][j]` is `0` or `1`; exactly two islands exist.

## Examples

### Example 1

```
Input:  grid = [[0,1],[1,0]]
Output: 1
```

**Explanation:** The two single-cell islands are diagonal neighbors; flipping one `0` between them connects them.

### Example 2

```
Input:  grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

**Explanation:** The islands at `(0,1)` and `(2,2)` are two flips apart along a shortest path.

## Hint

Flood-fill one island and seed every one of its cells into a BFS queue at distance `0`; expand outward (multi-source Lee BFS) until you first touch the other island — that distance is the bridge length.
