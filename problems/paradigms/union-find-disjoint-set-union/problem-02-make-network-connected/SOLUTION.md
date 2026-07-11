# Solution — Number of Operations to Make Network Connected

## Brute Force

Build an adjacency list and run BFS/DFS to count connected components. If `len(connections) <
n - 1`, return `-1`; otherwise return `components - 1`.

```python
def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1
    adj = [[] for _ in range(n)]
    for a, b in connections:
        adj[a].append(b)
        adj[b].append(a)
    seen = [False] * n
    comps = 0
    for i in range(n):
        if not seen[i]:
            comps += 1
            stack = [i]
            seen[i] = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
    return comps - 1
```

- **Time:** `O(n + m)` where `m = len(connections)`.
- **Space:** `O(n + m)` for the adjacency list and visited array.

This is fine, but Union-Find expresses the same idea without building an adjacency list and with
`O(n)` auxiliary memory.

## Optimal Approach (Union-Find / Disjoint Set Union)

**Key observation about cables.** To connect `n` nodes you need at least `n - 1` cables. If
`len(connections) < n - 1`, it is impossible → return `-1`. Crucially, if you *do* have at least
`n - 1` cables, then whenever the network splits into `c` components there are always enough
*redundant* cables to fix it: each component that spans `k` nodes with `e` internal edges has
`e - (k - 1)` spare cables, and summing over all components the total spare count equals
`m - (n - c) >= (n - 1) - (n - c) = c - 1`, exactly the number of moves required.

So the whole problem reduces to **counting connected components**:

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
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
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        dsu = DSU(n)
        for a, b in connections:
            dsu.union(a, b)
        return dsu.count - 1
```

**Why `components - 1`.** A forest of `c` connected trees needs exactly `c - 1` extra edges to
become a single tree (each new edge can reduce the component count by at most one, and one spare
cable is always available as argued above). DSU gives `c` directly.

- **Time:** `O((n + m) · α(n))` ≈ `O(n + m)`.
- **Space:** `O(n)` for `parent` and `rank`.

## Key Insights & Edge Cases

- The impossibility test `m < n - 1` must come **first**; it is the only case that returns `-1`.
- You never actually need to know *which* cables are redundant — the counting argument guarantees
  they exist once the cable-count check passes.
- Duplicate `union` calls (a and b already in the same set) are safely ignored and correctly do
  **not** decrement the component count.
- Edge case `n == 1`: `m >= 0 >= n - 1 = 0`, one component, answer `0` (nothing to connect).
