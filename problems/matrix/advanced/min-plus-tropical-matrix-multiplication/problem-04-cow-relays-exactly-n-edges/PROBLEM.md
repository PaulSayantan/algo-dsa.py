# Cow Relays (Shortest Path Using Exactly N Edges)

**Difficulty:** Hard

**Source:** USACO December 2007, Gold — "Cow Relays" (also POJ 3613 / SPOJ). A
textbook application of min-plus matrix exponentiation with vertex compression.

## Description

You are given an undirected connected weighted graph with `T` edges (each edge
`i` connects endpoints `u_i` and `v_i` with weight `w_i`). Vertex identifiers can
be arbitrary integers in a large range (e.g. up to `1000`), and only vertices
that appear on some edge exist.

Given an integer `N`, a start vertex `S`, and an end vertex `E`, find the
**length of the shortest path from `S` to `E` that traverses exactly `N`
edges**. Edges and vertices may be reused; each traversal of an edge counts
toward the `N` total, and each edge may be walked in either direction (the graph
is undirected).

Because the labels are sparse, first **compress** the at-most `2T` distinct
endpoints to indices `0 .. m-1`. Build the `m × m` weight matrix `W` (undirected,
so `W[a][b] = W[b][a] = w`), and raise it to the `N`-th tropical power under
**min-plus (tropical) matrix multiplication**. The answer is `(W^{⊙N})[S][E]`.

## Constraints

- `1 <= N <= 10^6`
- `2 <= T <= 100`
- `1 <= w_i <= 1000`
- Vertex labels are integers in `[1, 1000]`; at most `2T` distinct vertices
  actually appear (so the compressed size `m <= 200`).
- The graph is connected; a path of exactly `N` edges from `S` to `E` is
  guaranteed to exist.
- `S` and `E` appear among the edge endpoints.

## Examples

### Example 1

```
Input:
  N = 2, T = 6, S = 6, E = 4
  edges (weight, endpoint, endpoint):
    (11, 4, 6)
    ( 4, 4, 8)
    ( 8, 4, 9)
    ( 6, 6, 8)
    ( 2, 6, 9)
    ( 3, 8, 9)
Output: 10
Explanation:
  Among all 2-edge walks from 6 to 4, the cheapest is
    6 -> 8 -> 4  with cost 6 + 4 = 10.
  (The direct edge 6 -> 4 has cost 11 but uses only 1 edge, which is not
  allowed.)
```

### Example 2

```
Input:
  N = 4, T = 6, S = 6, E = 4
  edges: same six edges as Example 1
Output: 14
Explanation:
  Among all 4-edge walks from 6 to 4, the cheapest is
    6 -> 9 -> 6 -> 8 -> 4  with cost 2 + 2 + 6 + 4 = 14.
  No 4-edge walk from 6 to 4 is cheaper.
```

## Hint

Two obstacles: the hop count `N` can be up to `10^6` (too many for a linear
chain, so square the matrix), and the vertex labels are sparse (compress them
first). Both are handled by **Min-Plus (Tropical) Matrix Multiplication** with
fast exponentiation on the compressed `m × m` weight matrix — the answer is entry
`(S, E)` of its `N`-th tropical power.
