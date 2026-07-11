# Solution — Count Subtrees With Max Distance Between Cities

## Brute Force

Enumerate all `2^n` subsets of cities. For each subset, run a BFS/DFS to test connectivity, and for the diameter run a BFS from every node inside the subset to find the largest shortest-path distance.

- `O(2^n · n · (n + edges))` because of the per-subset multi-source BFS.
- With `n ≤ 15` this actually passes, but the repeated distance computations are wasteful — the pairwise distances never change.

## Optimal Approach (Floyd–Warshall + Subset Enumeration)

The tree distances between all pairs are fixed, so compute them **once** with Floyd–Warshall (`n ≤ 15`, so `n³` is trivial). Then enumerate subsets and use the precomputed matrix for instant diameter lookups.

### Steps

1. Build a `n × n` distance matrix `dist`: `0` on the diagonal, `1` for each tree edge (both directions), `INF` elsewhere. Convert the 1-indexed cities to 0-indexed.
2. Run Floyd–Warshall (`k` outermost) so `dist[i][j]` is the number of edges on the unique path between `i` and `j`.
3. Initialize `ans = [0] * (n - 1)`.
4. For each bitmask `mask` in `1 .. 2^n - 1`:
   - Let `nodes` be the set bits. Skip if `|nodes| < 2`.
   - **Connectivity test:** count how many tree edges have *both* endpoints in `mask`. The induced subgraph is a connected subtree iff `edgeCount == |nodes| - 1`. (In a tree, an induced subgraph on `k` nodes is connected exactly when it contains `k - 1` edges — no cycles are possible.)
   - If connected, compute `diameter = max(dist[i][j])` over all pairs `i, j` in `nodes`, and do `ans[diameter - 1] += 1`.
5. Return `ans`.

### Why Floyd–Warshall fits

We need **all-pairs** distances (any two cities in a subset might be the diameter endpoints), the graph is tiny and dense enough that `O(n³)` is negligible, and precomputing once removes the per-subset BFS. The distance matrix is reused across all `2^n` subsets.

### Reference implementation

```python
def countSubgraphsForEachDiameter(self, n, edges):
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    e = [(u - 1, v - 1) for u, v in edges]
    for u, v in e:
        dist[u][v] = dist[v][u] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    ans = [0] * (n - 1)
    for mask in range(1, 1 << n):
        nodes = [i for i in range(n) if mask & (1 << i)]
        if len(nodes) < 2:
            continue
        edge_count = sum(
            1 for u, v in e if (mask >> u) & 1 and (mask >> v) & 1
        )
        if edge_count != len(nodes) - 1:      # induced subgraph not connected
            continue
        diameter = max(dist[a][b] for a in nodes for b in nodes)
        ans[diameter - 1] += 1
    return ans
```

### Complexity

- Time: `O(n³)` for Floyd–Warshall, then `O(2^n · n²)` for the subset scan (each subset checks up to `n²` pairs for the diameter) → dominated by `O(2^n · n²)`. With `n = 15` that is about `15² · 32768 ≈ 7.4M` operations.
- Space: `O(n²)` for the distance matrix.

## Key Insights & Edge Cases

- **Tree connectivity shortcut.** In a tree, an induced subgraph on `k` chosen nodes is connected **iff** it contains exactly `k - 1` of the original edges. That replaces a per-subset BFS with a single edge count.
- **Diameter = max pairwise distance,** and thanks to Floyd–Warshall it's a matrix lookup, not a search.
- **1-indexed input → 0-indexed matrix.** Convert edges up front to avoid off-by-one bugs.
- **Result size is `n - 1`.** The largest possible diameter is the tree's own diameter (`≤ n - 1`), and `ans[diameter - 1]` maps a diameter of `d` to index `d - 1`.
- **Singletons and the empty set** contribute nothing (a subtree needs at least 2 cities); the `len(nodes) < 2` guard handles them.
- **Alternative:** an `O(2^n · n)` version incrementally tracks each connected subset's diameter, but the Floyd–Warshall lookup version is clearer and easily fast enough at `n ≤ 15`.
