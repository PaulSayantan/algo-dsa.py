# 01 Matrix

**Difficulty:** Medium

**Source:** LeetCode 542 — 01 Matrix

## Description

Given a binary matrix `mat`, return a matrix where each cell holds its distance to the nearest `0` (4-directional steps).

## Examples

### Example 1

```
Input:  mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

## Hint

Seed the queue with every 0 cell at distance 0; BFS outward filling distances to 1 cells.
