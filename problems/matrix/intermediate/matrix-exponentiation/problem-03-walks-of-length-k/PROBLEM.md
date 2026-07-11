# Number of Walks of Length K in a Graph

**Difficulty:** Medium

Classic graph-theory result (CLRS-style adjacency-matrix powers; a staple of competitive
programming).

## Description

You are given a directed graph on `V` nodes labeled `0 .. V-1`, described by a `V × V`
adjacency matrix `adj`, where `adj[i][j] = 1` if there is an edge from node `i` to node `j`
and `0` otherwise (there may be self-loops; the graph may be directed).

Given a source node `src`, a destination node `dst`, and an integer `k`, return the number of
**distinct walks of length exactly `k`** from `src` to `dst`, **modulo `10^9 + 7`**. A *walk*
of length `k` is a sequence of `k` edges `src = u_0 -> u_1 -> ... -> u_k = dst` where each
consecutive pair is connected by an edge; nodes and edges **may repeat**.

`k` can be as large as `10^18`, so enumerating walks or doing an `O(k · V^2)` step-by-step DP
is too slow.

## Constraints

- `1 <= V <= 100`
- `adj[i][j]` is `0` or `1`; `adj` has shape `V × V`.
- `0 <= src, dst < V`
- `1 <= k <= 10^18`
- Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  adj = [[0,1,1],
               [1,0,1],
               [1,1,0]],
        src = 0, dst = 0, k = 2
Output: 2
Explanation: The graph is the triangle 0-1-2 (each pair connected). Length-2 walks from 0
back to 0 are 0->1->0 and 0->2->0, so there are 2.
```

### Example 2

```
Input:  adj = [[0,1,1],
               [1,0,1],
               [1,1,0]],
        src = 0, dst = 1, k = 3
Output: 3
Explanation: Length-3 walks from 0 to 1: 0->1->0->1, 0->2->0->1, and 0->1->2->1. That is 3.
```

## Hint

The `(i, j)` entry of the `k`-th power of the adjacency matrix counts walks of length exactly
`k` from `i` to `j`. Compute that power with **Matrix Exponentiation** in `O(V^3 log k)`.
