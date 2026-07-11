# Solution — Escape the Grid (Vertex-Disjoint Paths)

## Brute Force

Enumerate paths for each person and search for a combination that shares no cell. With `k`
people and grids of size `RC`, the number of simple paths is exponential and the joint
search is `O(paths^k)`. Even backtracking that routes one person at a time and rolls back
on collisions is exponential in the worst case.

- **Time:** exponential.
- **Space:** `O(RC)` per path.

Correct but infeasible beyond tiny grids.

## Optimal Approach — Node-Splitting Max-Flow / Min-Cut on Grid

### Why plain edge-flow is wrong

The constraint "no cell used twice" is a **vertex capacity**. A naive flow with edges
between adjacent cells only limits how much crosses each *edge*, so two paths could still
cross through the same cell using different edges. We must cap **cells**.

### Node-splitting

Replace each non-wall cell `v` with two nodes:

- `v_in` — everything entering the cell arrives here,
- `v_out` — everything leaving the cell departs here,
- an internal edge `v_in → v_out` with **capacity 1**.

Now any flow through the cell must traverse that single capacity-1 edge, so at most one
path uses the cell. This is the canonical way to convert vertex capacities into edge
capacities.

### Full network

- Super source `S`, super sink `T`.
- For every open cell `v` (`'S'`, `'E'`, or `'.'`): edge `v_in → v_out` (cap 1).
- For every pair of orthogonally adjacent non-wall cells `u, v`: edges
  `u_out → v_in` and `v_out → u_in` (cap 1 each — actually `∞` is fine, since the cell caps
  already bound everything, but 1 suffices).
- `S → v_in` (cap 1) for every `'S'` cell.
- `v_out → T` (cap 1) for every `'E'` cell.

**Max flow from `S` to `T` = maximum number of cell-disjoint escape routes = the answer.**

### Why it is correct

- **Menger's theorem (vertex form):** the maximum number of internally vertex-disjoint
  `S–T` paths equals the minimum vertex cut. Node-splitting encodes vertex disjointness as
  edge capacity 1, so integral max flow decomposes into that many vertex-disjoint paths.
- **Integrality:** integer capacities ⇒ integral flow ⇒ each cell edge carries 0 or 1,
  i.e. genuine non-overlapping routes.
- Attaching `S → 'S'` and `'E' → T` with capacity 1 makes each start/exit serve at most one
  path, matching the problem's "start and exit cells count as used".

### Step by step

1. Assign each non-wall cell an index; give it two flow nodes `2*idx` (`in`) and
   `2*idx+1` (`out`).
2. Add `in → out` cap 1 for each cell.
3. For adjacency `u–v`, add `u_out → v_in` and `v_out → u_in`.
4. Add `S → in` for `'S'` cells and `out → T` for `'E'` cells.
5. Run **Dinic's** algorithm; return the flow value.

### Reference sketch (Dinic, cell-split)

```python
from collections import deque
from typing import List

class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]
    def add(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])
    def bfs(self, s, t):
        self.level = [-1] * len(self.g); self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _ in self.g[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1; q.append(v)
        return self.level[t] >= 0
    def dfs(self, u, t, f):
        if u == t: return f
        while self.it[u] < len(self.g[u]):
            e = self.g[u][self.it[u]]
            v, cap, rev = e
            if cap > 0 and self.level[v] == self.level[u] + 1:
                d = self.dfs(v, t, min(f, cap))
                if d > 0:
                    e[1] -= d; self.g[v][rev][1] += d; return d
            self.it[u] += 1
        return 0
    def maxflow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0] * len(self.g)
            while True:
                f = self.dfs(s, t, float('inf'))
                if f == 0: break
                flow += f
        return flow

class Solution:
    def max_escape(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        idx = {}
        for r in range(R):
            for c in range(C):
                if grid[r][c] != '#':
                    idx[(r, c)] = len(idx)
        n = 2 * len(idx)
        S, T = n, n + 1
        din = Dinic(n + 2)
        IN = lambda k: 2 * k
        OUT = lambda k: 2 * k + 1
        for (r, c), k in idx.items():
            din.add(IN(k), OUT(k), 1)          # cell capacity 1
            if grid[r][c] == 'S':
                din.add(S, IN(k), 1)
            if grid[r][c] == 'E':
                din.add(OUT(k), T, 1)
            for dr, dc in ((1, 0), (0, 1)):    # add each undirected pair once
                nb = (r + dr, c + dc)
                if nb in idx:
                    k2 = idx[nb]
                    din.add(OUT(k), IN(k2), 1)
                    din.add(OUT(k2), IN(k), 1)
        return din.maxflow(S, T)
```

- **Time:** unit-capacity Dinic runs in `O(E · √V)`. With `V = O(RC)` and `E = O(RC)`, that
  is `O((RC)^1.5)` — fine for `100 × 100`.
- **Space:** `O(V + E) = O(RC)`.

## Key Insights & Edge Cases

- **Node-splitting is mandatory** here: without it you would be solving edge-disjoint
  paths, which can overcount because two paths may legally cross a shared cell on different
  edges.
- Give **start and exit cells capacity 1** too (via the `in → out` edge), matching "each
  such cell serves at most one path." If the problem instead let many paths share exits, use
  `∞` on `out → T`.
- **Answer bounded by** `min(#S, #E)` and by the min vertex cut (a bottleneck cell forces a
  small answer, as in Example 2 where cell `(0,1)` is the sole passage).
- **Edge cases:** no `'S'` or no `'E'` ⇒ 0; a wall fully separating starts from exits ⇒ 0
  (Example 3); a start cell that is itself an exit could count as an immediate escape if the
  grid allows `S`/`E` to coincide (here they are distinct characters).
- If you also want the routes, decompose the residual flow into `S → T` paths.
