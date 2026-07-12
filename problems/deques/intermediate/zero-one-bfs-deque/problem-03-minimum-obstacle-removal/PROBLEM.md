# Minimum Obstacle Removal to Reach Corner

**Difficulty:** Medium

**Source:** LeetCode 2290 — Minimum Obstacle Removal to Reach Corner

## Description

You are given a 0-indexed `m x n` integer `grid` where each cell is either `0` (empty) or `1` (an obstacle). You can move up, down, left, or right between adjacent cells. Return the **minimum number of obstacles to remove** so you can travel from the top-left cell `(0, 0)` to the bottom-right cell `(m-1, n-1)`. Model each move as an edge whose weight is the value of the cell you step **into** (`0` for empty, `1` for an obstacle) and run 0-1 BFS.

## Examples

### Example 1

```
Input:  grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
```

**Explanation:** Removing the obstacles at `(0,1)` and `(0,2)` lets you reach the corner; no route removes fewer.

### Example 2

```
Input:  grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
```

**Explanation:** A path of empty cells already exists, so nothing needs to be removed.

## Hint

Stepping into an empty cell is a weight-0 edge (appendleft); stepping into an obstacle is a weight-1 edge (append). Run 0-1 BFS from the corner.
