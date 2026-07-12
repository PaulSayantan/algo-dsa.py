# Critical Connections in a Network (Bridges)

**Difficulty:** Hard

**Source:** LeetCode 1192 — Critical Connections in a Network

## Description

There are `n` servers `0..n-1` connected by undirected `connections`. A *critical connection* (bridge) is an edge whose removal disconnects some servers. Return all critical connections as a sorted list of sorted `[u, v]` pairs.

## Examples

### Example 1

```
Input:  n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
```

## Hint

DFS low-link: edge (u,v) is a bridge iff low[v] > disc[u]. Ignore the immediate parent edge.
