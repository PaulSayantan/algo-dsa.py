# Solution — Minimum Cells to Block a Path

## Brute Force

Try every subset of removable open cells, mark them as walls, and BFS to check whether the
sink is still reachable; keep the smallest disconnecting subset. With `m` removable cells
this is `O(2^m · RC)` — exponential and hopeless for real grids.

- **Time:** `O(2^(RC) · RC)`.
- **Space:** `O(RC)`.

## Optimal Approach — Minimum Vertex Cut via Max-Flow / Min-Cut on Grid

### The reduction

We must delete **vertices** (cells) to disconnect source `s = (0,0)` from sink
`t = (R-1, C-1)`. The fewest such vertices is the **minimum vertex cut**. By **Menger's
theorem** (vertex version):

> minimum s–t vertex cut = maximum number of internally vertex-disjoint s–t paths.

Compute that maximum with a max flow, using **node-splitting** to turn "delete a cell" into
"cut a capacity-1 edge."

### Building the network

For each open cell `v` split it into `v_in → v_out`:

- If `v` is the **source or sink** (not removable): capacity `∞`.
- Otherwise (removable): capacity `1`.

For each pair of orthogonally adjacent open cells `u, v`, add `u_out → v_in` and
`v_out → u_in` with capacity `∞` (edges are never cut — only cells are).

Source of the flow = `s_out`; sink of the flow = `t_in`. (Equivalently connect a super
source to `s_in` and a super sink from `t_out`.)

**Max flow = minimum vertex cut = minimum cells to remove.**

### Handling "impossible" (return -1)

The only way disconnection is impossible is when the source and sink are **orthogonally
adjacent** — then there is an edge `s_out → t_in` of capacity `∞` that no vertex removal can
sever, so the max flow is infinite. Detect this: if the computed flow is `≥ ∞` (or simply
if `s` and `t` are adjacent), return `-1`. In this problem `s` and `t` are distinct and, for
grids larger than the `1×2`/`2×1` cases, are generally not adjacent; still guard for it.

### Why it is correct

- **Menger's theorem** gives the exact equality between the disjoint-path count (max flow)
  and the vertex cut size, so the flow value is precisely the minimum number of cells to
  remove.
- **Node-splitting** makes each cell removal cost exactly 1 unit of flow, and infinite
  edge/endpoint capacities ensure the min cut only ever slices `in → out` cell edges —
  i.e. corresponds to removing cells, never edges or the protected endpoints.
- **Integrality** of max flow guarantees the cut is a set of whole cells.

### Step by step

1. If `grid[0][0]` and `grid[R-1][C-1]` are orthogonally adjacent, return `-1`.
2. Split every open cell; capacity `1` for removable cells, `∞` for `s` and `t`.
3. Add `∞` adjacency edges between neighboring open cells (both directions).
4. Run Dinic from `s_out` to `t_in`.
5. Return the flow value (which is finite once step 1 passes).

### Reference sketch

```python
from collections import deque
from typing import List

INF = float('inf')

class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]
    def add(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])
    def bfs(self, s, t):
        self.lv = [-1] * len(self.g); self.lv[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _ in self.g[u]:
                if cap > 0 and self.lv[v] < 0:
                    self.lv[v] = self.lv[u] + 1; q.append(v)
        return self.lv[t] >= 0
    def dfs(self, u, t, f):
        if u == t: return f
        while self.it[u] < len(self.g[u]):
            e = self.g[u][self.it[u]]; v, cap, rev = e
            if cap > 0 and self.lv[v] == self.lv[u] + 1:
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
                f = self.dfs(s, t, INF)
                if f == 0: break
                flow += f
        return flow

class Solution:
    def min_cells_to_block(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        s, t = (0, 0), (R - 1, C - 1)
        if abs(s[0] - t[0]) + abs(s[1] - t[1]) == 1:   # adjacent -> impossible
            return -1
        idx = {}
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    idx[(r, c)] = len(idx)
        n = 2 * len(idx)
        din = Dinic(n)
        IN = lambda k: 2 * k
        OUT = lambda k: 2 * k + 1
        for (r, c), k in idx.items():
            cap = INF if (r, c) in (s, t) else 1
            din.add(IN(k), OUT(k), cap)
            for dr, dc in ((1, 0), (0, 1)):
                nb = (r + dr, c + dc)
                if nb in idx:
                    k2 = idx[nb]
                    din.add(OUT(k), IN(k2), INF)
                    din.add(OUT(k2), IN(k), INF)
        flow = din.maxflow(OUT(idx[s]), IN(idx[t]))
        return -1 if flow >= INF else flow
```

- **Time:** Dinic in `O(V^2 · E)` in general, but the removable cells are unit-capacity, so
  the flow value is `O(RC)` bounded and augmentation is fast in practice; with `V,E = O(RC)`
  it is comfortably within limits for `100 × 100`.
- **Space:** `O(V + E) = O(RC)`.

## Key Insights & Edge Cases

- **Delete vertices ⇒ min vertex cut ⇒ node-splitting.** The classic min-cut-on-edges model
  would answer the wrong question (fewest *edges* to cut).
- **Protect the endpoints** by giving `s`/`t` capacity `∞`; otherwise the algorithm might
  "remove" the source or sink itself.
- **Adjacent s and t ⇒ -1** (Example: a `1×2` grid). The infinite direct edge cannot be
  cut by removing cells.
- **Already disconnected ⇒ 0** (Example 3): if BFS cannot reach `t`, the max flow is 0,
  which is the correct answer.
- Walls are simply absent nodes; only open cells enter the network.
- To recover *which* cells to remove, find the min cut: BFS from `s_out` in the residual
  graph; a cell `v` whose `v_in` is reachable but `v_out` is not is a cut cell.
