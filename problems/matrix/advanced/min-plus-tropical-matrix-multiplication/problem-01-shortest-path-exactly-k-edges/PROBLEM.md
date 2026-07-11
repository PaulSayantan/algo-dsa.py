# Shortest Path with Exactly K Edges

**Difficulty:** Easy

**Source:** Classic (GeeksforGeeks "Shortest path with exactly k edges in a directed and weighted graph"); a canonical introduction to min-plus matrix powers.

## Description

You are given a directed, weighted graph with `n` vertices labeled `0 .. n-1`,
described by an adjacency matrix `graph`, where `graph[i][j]` is the weight of
the edge `i → j`, or `None`/`INF` if that edge does not exist. Given a source
`u`, a destination `v`, and an integer `k`, return the **minimum total weight of
a walk that starts at `u`, ends at `v`, and uses exactly `k` edges**.

A *walk* may revisit vertices and reuse edges — the only requirement is that the
number of edges traversed is exactly `k`. If no such walk exists, return `-1`.

The intended solution builds the weighted adjacency matrix `W` and raises it to
the `k`-th power under **min-plus (tropical) matrix multiplication**: replace the
usual `(×, +)` with `(+, min)`. Then `(W^{⊙k})[u][v]` is precisely the answer.

## Constraints

- `1 <= n <= 100`
- `1 <= k <= 20`
- Edge weights are integers with `0 <= weight <= 1000`.
- `graph[i][j]` is `INF` (no edge) when there is no direct edge `i → j`.
- There may be no walk of exactly `k` edges from `u` to `v`.

## Examples

### Example 1

```
Input:
  n = 4
  edges = [[0,1,2], [0,2,1], [1,3,3], [2,1,1], [2,3,5]]   # (from, to, weight)
  u = 0, v = 3, k = 2
Output: 5
Explanation:
  Walks of exactly 2 edges from 0 to 3:
    0 -> 1 -> 3 costs 2 + 3 = 5
    0 -> 2 -> 3 costs 1 + 5 = 6
  The minimum is 5.
```

### Example 2

```
Input:
  n = 4
  edges = [[0,1,2], [0,2,1], [1,3,3], [2,1,1], [2,3,5]]
  u = 0, v = 3, k = 3
Output: 5
Explanation:
  A 3-edge walk 0 -> 2 -> 1 -> 3 costs 1 + 1 + 3 = 5.
  No cheaper 3-edge walk to vertex 3 exists, so the answer is 5.
```

### Example 3

```
Input:
  n = 4
  edges = [[0,1,2], [0,2,1], [1,3,3], [2,1,1], [2,3,5]]
  u = 0, v = 3, k = 1
Output: -1
Explanation:
  There is no direct edge 0 -> 3, so no walk of exactly 1 edge reaches 3.
  Return -1.
```

## Hint

Model each edge as a weighted transition and think of "one more edge" as one
matrix multiplication — but under **Min-Plus (Tropical) Matrix Multiplication**
`(+, min)` instead of `(×, +)`. The exactly-`k`-edge answer is entry `(u, v)` of
the `k`-th tropical power of the weight matrix.
