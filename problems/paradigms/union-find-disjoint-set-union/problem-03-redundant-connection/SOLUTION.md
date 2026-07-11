# Solution — Redundant Connection

## Brute Force

For each edge (processed from last to first), remove it and check whether the remaining `n - 1`
edges still connect all `n` nodes (a tree). Return the first removable edge found. Connectivity
is verified with a BFS/DFS or a fresh DSU each time.

```python
def findRedundantConnection(edges):
    n = len(edges)
    for i in range(n - 1, -1, -1):
        adj = {}
        for j, (a, b) in enumerate(edges):
            if j == i:
                continue
            adj.setdefault(a, []).append(b)
            adj.setdefault(b, []).append(a)
        # BFS from node 1, count reachable nodes == n  => still a tree
        ...
```

- **Time:** `O(n^2)` — `n` candidate edges, each connectivity check is `O(n)`.
- **Space:** `O(n)` per check.

## Optimal Approach (Union-Find / Disjoint Set Union)

A tree on `n` nodes has exactly `n - 1` edges and no cycles. The input is a tree plus one extra
edge, so there is exactly one cycle. Adding edges one at a time, the edge that *creates* the
cycle is the first edge `[a, b]` for which `a` and `b` are **already in the same component**.

Because the graph is a tree plus a single edge, that first cycle-closing edge is also the unique
redundant edge — and since we scan left to right, it is automatically the last valid answer
required by the problem (there is only one candidate).

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))   # 1-indexed nodes
        self.rank = [0] * (n + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        """Return False if a, b were already connected (edge is redundant)."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges))
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        return []   # constraints guarantee this is never reached
```

**Why it is correct.** `union` merges two components and returns `True`; if it returns `False`
the endpoints already shared a root, meaning a path between them existed, so this edge completes
a cycle. The first such edge is exactly the redundant one.

- **Time:** `O(n · α(n))` ≈ `O(n)`.
- **Space:** `O(n)` for `parent` and `rank`.

## Key Insights & Edge Cases

- Nodes are labeled `1 .. n`, so size the arrays as `n + 1` (or offset by one) to avoid an
  off-by-one bug on index `0`.
- The "return the last such edge" wording only matters conceptually; since the graph is a tree
  plus exactly one edge, there is a single cycle and a single cycle-closing edge. A left-to-right
  scan returns it directly.
- This cycle-detection trick works for **undirected** graphs. For the directed variant (LeetCode
  685, Redundant Connection II) you must additionally handle a node with two parents — plain DSU
  is not enough on its own.
- Do not sort or reorder `edges`; the input order defines which edge is "redundant."
