# Solution — Image Segmentation Min-Cut

## Brute Force

Enumerate all `2^(R*C)` foreground/background labelings, compute each one's data cost plus
separation penalty, and keep the minimum.

- **Time:** `O(2^(RC) · RC)`.
- **Space:** `O(RC)`.

Correct (and how the examples were verified) but only usable for tiny images. Note that
this energy is **not** separable pixel-by-pixel: the smoothness term couples neighbors, so
you cannot simply pick each pixel's cheaper label independently — Example 2 shows the
independent choice (cost 4 in data) still pays 4 in separation.

## Optimal Approach — Minimum Cut via Max-Flow / Min-Cut on Grid

### The energy is a graph cut

We minimize

```
E(labeling) = Σ_pixels data(pixel, label) + sep · #{adjacent pairs with different labels}.
```

This is exactly the energy that an `S–T` **minimum cut** minimizes. Build:

- Source `S` = the **foreground** terminal, sink `T` = the **background** terminal.
- For each pixel `p`: edge `S → p` with capacity `bg[p]`, and edge `p → T` with capacity
  `fg[p]`.
- For each orthogonally adjacent pixel pair `(p, q)`: an **undirected** edge of capacity
  `sep` (in a directed max-flow implementation, add `p → q` and `q → p` each with capacity
  `sep`).

**Interpretation of a cut.** Put `p` on the `S`-side ⇒ label `p` **foreground**; on the
`T`-side ⇒ **background**.

- If `p` is foreground, the cut must sever `p → T` (cost `fg[p]`). ✔ matches the FG penalty.
- If `p` is background, the cut severs `S → p` (cost `bg[p]`). ✔ matches the BG penalty.
- If adjacent `p, q` end up on different sides, exactly one of the two `sep` edges crosses
  the cut, contributing `sep`. ✔ matches the smoothness penalty. If they share a side, the
  `sep` edges do not cross.

So **cut capacity = total labeling cost**, and the **minimum cut = minimum energy**. By the
Max-Flow Min-Cut theorem, `min cut = max flow`, which we compute directly.

### Why it is correct

- The construction is the standard Kleinberg–Tardos image-segmentation reduction. Each of
  the three cost terms maps onto disjoint cut edges, so the total capacity of any cut equals
  the energy of the corresponding labeling, and every labeling corresponds to some `S–T`
  cut. Minimizing over cuts therefore minimizes over labelings.
- The energy is **submodular** (the pairwise term `sep · [ℓ_p ≠ ℓ_q]` satisfies
  `θ(0,0) + θ(1,1) ≤ θ(0,1) + θ(1,0)`, i.e. `0 + 0 ≤ sep + sep`), which is precisely the
  condition under which a two-label energy is exactly minimizable by a single graph cut.
- Integer capacities ⇒ integral max flow ⇒ a well-defined cut / labeling.

### Step by step

1. Index the pixels `0 … RC-1`; add two extra node ids for `S` and `T`.
2. For each pixel `p`: `add(S, p, bg[p])` and `add(p, T, fg[p])`.
3. For each right/down neighbor pair, `add(p, q, sep)` and `add(q, p, sep)`.
4. Run Dinic's max flow from `S` to `T`.
5. Return the flow value = min cut = minimum total cost.

### Reference sketch (Dinic)

```python
from collections import deque
from typing import List

class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]
    def add(self, u, v, cap):                 # undirected sep edge: call add(u,v,sep) twice? no:
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
                f = self.dfs(s, t, float('inf'))
                if f == 0: break
                flow += f
        return flow

class Solution:
    def min_segmentation_cost(self, fg, bg, sep):
        R, C = len(fg), len(fg[0])
        pid = lambda r, c: r * C + c
        S, T = R * C, R * C + 1
        din = Dinic(R * C + 2)
        for r in range(R):
            for c in range(C):
                p = pid(r, c)
                din.add(S, p, bg[r][c])       # S-side => foreground
                din.add(p, T, fg[r][c])       # T-side => background
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if nr < R and nc < C:      # undirected sep edge: both directions
                        q = pid(nr, nc)
                        din.add(p, q, sep)
                        din.add(q, p, sep)
        return din.maxflow(S, T)
```

Note the undirected `sep` edge is modeled as two directed capacity-`sep` edges (one each
way); do **not** rely on the residual back-edge for the reverse direction, because both
directions of the smoothness edge carry real capacity `sep`.

- **Time:** Dinic is `O(V^2 · E)` in the worst case; here `V, E = O(RC)`, and in practice
  grid graphs solve far faster (specialized solvers like Boykov–Kolmogorov are near-linear
  on such graphs). Comfortable for `100 × 100`.
- **Space:** `O(V + E) = O(RC)`.

## Key Insights & Edge Cases

- **S-side = foreground, T-side = background**, so the `S → p` edge carries the *background*
  penalty and `p → T` the *foreground* penalty. Swapping these is the most common bug.
- **The smoothness edge is undirected** — implement it as two directed `sep` edges so a
  differing pair pays exactly `sep` regardless of orientation.
- **Submodularity** (`sep ≥ 0`) is what makes a single min cut exact; if the pairwise term
  rewarded disagreement (`sep < 0`), the energy would be non-submodular and not solvable by
  one cut.
- **Edge cases:** `sep = 0` decouples pixels, so each picks its cheaper label independently;
  a `1 × 1` image (Example 3) has no edges, so the answer is just `min(fg, bg)`; if a
  pixel's `fg` and `bg` are equal, either side is fine.
- To output the actual segmentation, take the min cut: pixels reachable from `S` in the
  residual graph are foreground, the rest are background.
