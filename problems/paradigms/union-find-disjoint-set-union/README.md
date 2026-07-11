# Union-Find (Disjoint Set Union)

**Union-Find**, also known as the **Disjoint Set Union (DSU)** data structure, maintains a
collection of disjoint sets and supports two near-constant-time operations:

- **`find(x)`** — return a canonical representative ("root") for the set that contains `x`.
- **`union(x, y)`** — merge the two sets that contain `x` and `y`.

Two elements are in the same set if and only if `find(x) == find(y)`. This makes DSU the
natural tool for answering *connectivity* / *grouping* questions on an evolving graph.

## When to reach for it

Reach for Union-Find when a problem involves any of the following:

- Grouping elements into equivalence classes (connected components).
- A stream of "merge these two things" operations, interleaved with "are these two connected?"
  queries.
- Incrementally adding edges/nodes and tracking how many components remain.
- Cycle detection in an **undirected** graph (an edge whose endpoints already share a root
  closes a cycle).
- Kruskal's minimum-spanning-tree algorithm.

If instead you must *remove* edges, or you need actual paths between nodes, prefer BFS/DFS —
plain DSU does not support deletion.

## The two optimizations that make it fast

1. **Path compression** — during `find`, re-point every node visited directly at the root.
2. **Union by rank / size** — always attach the smaller (shallower) tree under the larger one.

Applying **both** gives an amortized cost of `O(α(n))` per operation, where `α` is the inverse
Ackermann function. For every input that fits in the observable universe, `α(n) <= 4`, so each
operation is effectively **O(1)**.

## Complexity

| Aspect | Cost |
|--------|------|
| Space | `O(n)` for the `parent` (and `rank`/`size`) arrays |
| `find` / `union` (both optimizations) | `O(α(n))` amortized ≈ `O(1)` |
| `find` / `union` (only one optimization) | `O(log n)` amortized |
| Building components from `m` edges over `n` nodes | `O((n + m) · α(n))` |

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Number of Provinces](problem-01-number-of-provinces/PROBLEM.md) | Medium | Count connected components in an adjacency matrix of cities. |
| 2 | [Number of Operations to Make Network Connected](problem-02-make-network-connected/PROBLEM.md) | Medium | Reconnect a network by moving spare cables between components. |
| 3 | [Redundant Connection](problem-03-redundant-connection/PROBLEM.md) | Medium | Find the one extra edge that turns a tree into a graph with a cycle. |
| 4 | [Satisfiability of Equality Equations](problem-04-satisfiability-of-equality-equations/PROBLEM.md) | Medium | Decide if `==` / `!=` variable constraints can all hold at once. |
| 5 | [Accounts Merge](problem-05-accounts-merge/PROBLEM.md) | Medium | Merge user accounts that share any email address. |
| 6 | [Number of Islands II](problem-06-number-of-islands-ii/PROBLEM.md) | Hard | Report the island count after each cell is turned to land online. |

Work through them top to bottom — each one adds a new twist (weighted DSU, string keys,
online updates) on top of the core template.
