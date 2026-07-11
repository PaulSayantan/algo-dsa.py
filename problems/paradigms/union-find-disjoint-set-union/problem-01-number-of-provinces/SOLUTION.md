# Solution — Number of Provinces

## Brute Force

Treat the matrix as an adjacency matrix and run a graph traversal (BFS or DFS). Start a fresh
traversal from every unvisited city, marking everything reachable as visited, and increment a
counter once per traversal.

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    seen = [False] * n
    provinces = 0

    def dfs(u):
        seen[u] = True
        for v in range(n):
            if isConnected[u][v] == 1 and not seen[v]:
                dfs(v)

    for i in range(n):
        if not seen[i]:
            provinces += 1
            dfs(i)
    return provinces
```

- **Time:** `O(n^2)` — every one of the `n^2` matrix cells is inspected once across all
  traversals.
- **Space:** `O(n)` for the visited array plus up to `O(n)` recursion depth.

This is already asymptotically optimal for a dense adjacency matrix (you must read all `n^2`
cells). Union-Find is presented below because it generalizes cleanly to the streaming/online
variants in later problems and avoids recursion depth issues.

## Optimal Approach (Union-Find / Disjoint Set Union)

Give each city an id `0..n-1`. Scan the upper triangle of the matrix; whenever
`isConnected[i][j] == 1`, `union(i, j)`. Because "connected" is an equivalence relation
(reflexive, symmetric, transitive), the DSU groups are exactly the provinces.

Maintain a running component count that starts at `n` and decrements by one every time a
`union` actually merges two *different* roots. That count is the answer — no final pass needed.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n            # number of disjoint sets

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)
        return dsu.count
```

**Why it is correct.** Two cities end up with the same root iff there is a chain of direct
connections between them (each `union` merges the transitive closure incrementally). Distinct
roots therefore correspond one-to-one with provinces. `count` tracks exactly the number of
distinct roots because it starts at `n` and drops by one on each genuine merge.

- **Time:** `O(n^2 · α(n))` to scan the matrix, effectively `O(n^2)`.
- **Space:** `O(n)` for `parent` and `rank`.

## Key Insights & Edge Cases

- Only scan `j > i`: the matrix is symmetric and the diagonal is all 1s (self-loops that must
  be ignored — unioning `i` with itself is a no-op anyway).
- Tracking `count` inside the DSU avoids a second pass over all roots; alternatively count the
  fixed points `find(i) == i` at the end.
- Path compression via the "halving" trick (`parent[x] = parent[parent[x]]`) keeps `find`
  iterative, sidestepping the recursion-depth risk that the DFS approach has for large `n`.
- Edge case `n == 1`: the single city is its own province, answer `1` — handled naturally since
  `count` starts at `n`.
