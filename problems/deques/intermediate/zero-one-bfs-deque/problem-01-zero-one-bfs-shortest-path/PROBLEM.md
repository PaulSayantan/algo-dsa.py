# Shortest Path with 0/1 Edge Weights

**Difficulty:** Medium

**Source:** Classic — 0-1 BFS shortest path

## Description

You are given a directed graph with `n` nodes (labeled `0..n-1`) and a list of `edges`, where each edge is `[u, v, w]` with weight `w` in `{0, 1}`. Return the length of the shortest path from `src` to `dst`, or `-1` if `dst` is unreachable. Solve it with 0-1 BFS using a deque.

## Examples

### Example 1

```
Input:  n=6, src=0, dst=4
Output: 2
```

**Explanation:** 0->2 (0), 2->3 (1), 3->4 (1) costs 2.

## Hint

Deque frontier: on relaxation, appendleft if the edge weight is 0, append if it is 1.
