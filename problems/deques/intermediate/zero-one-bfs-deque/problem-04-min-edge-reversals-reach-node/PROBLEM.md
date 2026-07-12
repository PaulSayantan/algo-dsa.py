# Minimum Edge Reversals to Reach a Node

**Difficulty:** Medium

**Source:** Classic — minimum edge reversals on a directed graph (0-1 BFS)

## Description

You are given a directed graph with `n` nodes labeled `0..n-1` and a list of directed `edges`, where `[u, v]` is an arc from `u` to `v`. You may **reverse** the direction of any edge, and reversing one edge costs `1`. Return the minimum total number of reversals needed to travel from `src` to `dst`, or `-1` if `dst` cannot be reached even with reversals. Traversing an edge along its direction is free (weight `0`); traversing it against its direction requires a reversal (weight `1`), so build an undirected adjacency with 0/1 weights and run 0-1 BFS.

## Examples

### Example 1

```
Input:  n=4, edges=[[0,1],[1,2],[3,2]], src=0, dst=3
Output: 1
```

**Explanation:** Go `0->1->2` for free, then reverse `3->2` into `2->3` (cost 1) to reach node 3.

### Example 2

```
Input:  n=4, edges=[[0,1],[1,2],[2,3]], src=0, dst=3
Output: 0
```

**Explanation:** The directed path `0->1->2->3` already exists, so no reversals are needed.

## Hint

Add each edge twice: forward as a weight-0 arc (appendleft) and backward as a weight-1 arc (append). Then 0-1 BFS gives the fewest reversals.
