# Redundant Connection

**Difficulty:** Medium

**Source:** LeetCode 684 — Redundant Connection

## Description

In this problem, a tree is an **undirected** graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one
additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and
was not an edge that already existed. The graph is represented as an array `edges` of length `n`
where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in
the graph.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there
are multiple answers, return the answer that occurs **last** in the input.

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= a_i < b_i <= n`
- `a_i != b_i`
- There are no repeated edges.
- The given graph is connected.

## Examples

### Example 1

```
Input:  edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

Explanation: Adding edges `[1,2]` and `[1,3]` builds a valid tree over nodes `1, 2, 3`. The edge
`[2,3]` connects two nodes (`2` and `3`) that are already joined through node `1`, so it closes a
cycle. Removing it restores a tree, and it is the last such edge.

### Example 2

```
Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

Explanation: Edges `[1,2]`, `[2,3]`, `[3,4]` form the path `1-2-3-4`. The edge `[1,4]` connects
`1` and `4`, which are already connected via `1-2-3-4`, closing a cycle — so it is redundant.
Edge `[1,5]` attaches a new leaf and is not redundant. The answer is `[1,4]`.

## Hint

Process the edges in order. The redundant edge is the first one whose two endpoints are already
in the same set — detect that with **Union-Find (Disjoint Set Union)** and return it.
