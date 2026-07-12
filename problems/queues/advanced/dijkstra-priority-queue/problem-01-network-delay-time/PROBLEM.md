# Network Delay Time

**Difficulty:** Medium

**Source:** LeetCode 743 — Network Delay Time

## Description

You are given `times` as directed edges `[u, v, w]` (travel time), a node count `n` (labeled `1..n`), and a start node `k`. Return the time for a signal from `k` to reach *all* nodes, or `-1` if some node is unreachable.

## Examples

### Example 1

```
Input:  times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
Output: 2
```

## Hint

Dijkstra from k with a min-heap; the answer is the maximum finalized distance (or -1 if any is infinite).
