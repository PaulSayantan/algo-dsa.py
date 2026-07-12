# Clone Graph

**Difficulty:** Medium

**Source:** LeetCode 133 — Clone Graph

## Description

Given an undirected graph on nodes `1..n` described by an edge list, produce a deep copy. To make the result checkable, return a deterministic summary of the clone: `[node_count, sorted_unique_edges]` where each edge is `[min, max]`.

## Examples

### Example 1

```
Input:  n=4 square graph
Output: [4, [[1,2],[1,4],[2,3],[3,4]]]
```

## Hint

Build an adjacency map, map each original node to a copy, then read the clone's edges.
