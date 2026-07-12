# 0-1 Weighted Shortest Path

**Difficulty:** Hard

**Source:** Classic — 0-1 BFS

## Description

Given `n` nodes and a directed edge list `edges` where each entry is `[u, v, w]` with `w` either 0 or 1, return the shortest distance from node `0` to node `n-1`, or `-1` if unreachable.

## Hint

Use a deque; for a 0-weight edge appendleft the neighbor, for a 1-weight edge append it.
