# Swim in Rising Water — Solution

## Brute Force

Binary search on the answer `t` in `[0, n*n-1]`. For each candidate `t`, run a BFS/DFS from
`(0,0)` that may only step onto cells with elevation `<= t`, and check whether `(n-1,n-1)` is
reachable. Keep the smallest feasible `t`.

- **Time:** `O(n^2 · log(n^2)) = O(n^2 log n)` — a `O(n^2)` BFS per binary-search step.
- **Space:** `O(n^2)` for the visited grid.

This is already efficient and passes, but it re-runs a full BFS `log(n^2)` times. The
union-find percolation sweep computes the same answer with a single monotone pass.

## Optimal Approach (Union–Find on Grid — percolation sweep)

**Idea.** As the water level `t` rises, cells "open" one at a time in increasing elevation
order (elevations are a permutation, so the order is total and unique). Once a cell opens, it
connects to any adjacent cell that is already open. The first moment the top-left and
bottom-right cells share a component is the answer.

**Algorithm:**
1. Build a list of all cells sorted by elevation (or, since values are `0..n*n-1`, an array
   `pos` where `pos[v] = (r, c)` lets you iterate `v = 0, 1, 2, ...`).
2. Keep an `active` grid and a DSU over `n*n` cells.
3. For `t = 0, 1, 2, ...`:
   - Open the cell with elevation `t`: mark it active.
   - `union` it with each in-bounds neighbor that is already active.
   - After processing, if `find(source) == find(target)`, return `t`.

Because we open exactly one new cell per `t` and only union it with already-open neighbors, the
components at "time `t`" are precisely the sets of cells mutually reachable using elevations
`<= t`. The first `t` that connects the two corners is the minimum feasible water level.

**Why it is correct.** Connectivity is **monotone** in `t`: opening more cells can only add
edges, never remove them, so once source and target are connected they stay connected. Thus the
first `t` achieving connection is exactly the minimum. Opening in elevation order guarantees
that when we test connectivity at level `t`, exactly the cells with elevation `<= t` are active
— matching the problem's "water level `t`" rule.

- **Time:** `O(n^2 · α(n^2))` ≈ `O(n^2)` when values are a dense permutation (bucket by value,
  no sort needed). With an explicit sort it is `O(n^2 log n)`.
- **Space:** `O(n^2)` for the DSU and `active` arrays.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        pos = [None] * (n * n)             # elevation -> (r, c)
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)

        dsu = DSU(n * n)
        active = [False] * (n * n)
        source, target = 0, n * n - 1
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for t in range(n * n):
            r, c = pos[t]
            idx = r * n + c
            active[idx] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and active[nr * n + nc]:
                    dsu.union(idx, nr * n + nc)
            if dsu.find(source) == dsu.find(target):
                return t
        return n * n - 1
```

## Key Insights & Edge Cases

- **Percolation framing.** "Does the source connect to the target once all cells ≤ `t` are
  open?" is the percolation question DSU answers naturally by sweeping thresholds upward.
- **Values are a permutation**, so bucket by elevation (`pos[v]`) and iterate `v` — no sort,
  giving near-`O(n^2)`. If values could repeat or be sparse, sort the cells by value instead.
- **Answer is at least `max(grid[0][0], grid[n-1][n-1])`.** The destination's own elevation must
  be under water to stand on it — the sweep enforces this automatically because the target only
  becomes active at `t = grid[n-1][n-1]`.
- **`n == 1`:** source and target are the same cell; it activates at `t = grid[0][0]` (which is
  `0`), so the loop returns `0`.
- **Only union with already-active neighbors**, exactly as in Number of Islands II; unioning
  with a not-yet-open cell would let you traverse elevations above the current level.
- **Monotonicity** is the property that makes both binary search *and* the incremental sweep
  valid; the sweep just avoids recomputation.
- Alternative optimal solution: a **Dijkstra / min-heap** that expands the frontier by smallest
  max-elevation-so-far, `O(n^2 log n)`. The union-find sweep is often simpler to reason about
  for the "when does it first connect" phrasing.
