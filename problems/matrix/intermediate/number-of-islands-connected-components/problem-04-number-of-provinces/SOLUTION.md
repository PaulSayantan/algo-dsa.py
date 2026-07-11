# Number of Provinces — Solution

## Brute Force

Repeatedly perform transitive-closure passes: for every pair `(i, j)` that is
connected, mark them same-group, and keep re-scanning until no group labels
change (Floyd-Warshall-style reachability). This is `O(n^3)` for the closure
plus a final pass to count distinct groups.

- **Time:** `O(n^3)`.
- **Space:** `O(n^2)` (the reachability matrix) or `O(n)` for group labels.

Correct but cubic — a single traversal or Union-Find is far better.

## Optimal Approach (Connected Components on an adjacency matrix)

The key mental shift from Number of Islands: the graph is given as an
**adjacency matrix**, not a grid. Node `i`'s neighbours are all `j` with
`isConnected[i][j] == 1`. The number of provinces is the number of connected
components. Two idiomatic solutions:

### Option A — DFS/BFS over cities

1. Keep a `visited` array of size `n`, `count = 0`.
2. For each city `i` not yet visited: increment `count`, then DFS/BFS to visit
   every city reachable from `i` (following `isConnected[i][j] == 1` edges).
3. Return `count`.

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    visited = [False] * n
    count = 0

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if isConnected[i][j] == 1 and not visited[j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count
```

- **Time:** `O(n^2)` — the DFS scans a full row (`n` entries) for each of the
  `n` cities.
- **Space:** `O(n)` for `visited` plus recursion stack.

### Option B — Union-Find (often the cleanest here)

Because the relation is symmetric and given as pairs, DSU fits naturally:

1. Initialize `parent[i] = i` for all `i`; `components = n`.
2. For every pair `i < j` with `isConnected[i][j] == 1`, `union(i, j)`. Each
   successful union (two different roots merged) decrements `components`.
3. Return `components`.

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path halving
            x = parent[x]
        return x

    components = n
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
                    components -= 1
    return components
```

**Why it is correct:** cities in the same province are exactly those in the
same DSU set (unions connect directly-linked cities, and `find` collapses
transitive chains). Starting from `n` singletons, each merge of two distinct
sets reduces the component count by one, so the final `components` equals the
number of provinces.

- **Time:** `O(n^2 * α(n))` — scan the upper triangle, near-constant per union.
- **Space:** `O(n)` for the parent array.

## Key Insights & Edge Cases

- **Adjacency matrix, not a grid.** Neighbours come from row scans, not from
  `(r±1, c)` / `(r, c±1)` offsets.
- **The diagonal is all 1s** (self-loops) — harmless; skip `i == j` or just let
  `union(i, i)` be a no-op.
- **Symmetry** means you only need the upper triangle (`j > i`) for Union-Find.
- **Fully disconnected** input → `n` provinces (Example 2); **fully connected**
  → `1`.
- Union-Find is preferred when edges could arrive incrementally, but for a
  static matrix DFS/BFS is equally valid and just as fast asymptotically.
