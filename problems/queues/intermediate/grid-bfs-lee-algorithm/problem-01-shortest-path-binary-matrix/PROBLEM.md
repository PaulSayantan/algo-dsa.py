# Shortest Path in Binary Matrix

**Difficulty:** Medium

**Source:** LeetCode 1091 — Shortest Path in Binary Matrix

## Description

Given an `n × n` binary matrix `grid`, return the length of the shortest **8-directional** path of `0`-cells from the top-left to the bottom-right (path length = number of cells visited), or `-1` if none exists. Start/end must be `0`.

## Examples

### Example 1

```
Input:  grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

## Hint

8-neighbor BFS from (0,0) counting cells; the first arrival at the corner is the answer.
