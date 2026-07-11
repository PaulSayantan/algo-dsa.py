# Solution — Number of Islands II

## Brute Force

After each add-land operation, recompute the island count from scratch by scanning the whole grid
and running BFS/DFS flood fill over all land cells.

```python
def numIslands2(m, n, positions):
    grid = [[0] * n for _ in range(m)]
    res = []
    for r, c in positions:
        grid[r][c] = 1
        # full flood-fill count over the entire grid
        seen = [[False] * n for _ in range(m)]
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not seen[i][j]:
                    islands += 1
                    # BFS/DFS marking the whole component as seen
                    ...
        res.append(islands)
    return res
```

- **Time:** `O(P · m · n)` where `P = len(positions)` — a full grid scan per operation. With
  `m·n` and `P` both up to `10^4`, this is up to `10^8`–`10^12` work and will time out.
- **Space:** `O(m · n)` for the grid and visited array.

## Optimal Approach (Union-Find / Disjoint Set Union)

This is the canonical **online / incremental** connectivity problem: land is only ever *added*,
never removed, which is exactly what DSU supports efficiently. Maintain a running `count` of
islands and update it as each cell arrives.

**Per operation `(r, c)`:**

1. If `(r, c)` is already land, the count is unchanged — append the current `count` and continue
   (handles repeated positions).
2. Otherwise mark `(r, c)` as land, initialize it as its own set, and do `count += 1` (a fresh
   island).
3. For each of the four orthogonal neighbors that is already land, `union` it with `(r, c)`. Each
   union that actually merges two distinct sets does `count -= 1` (two islands became one).
4. Append the updated `count`.

Map a cell to an integer id with `r * n + c` so the DSU can use flat arrays.

```python
class DSU:
    def __init__(self, size):
        self.parent = [-1] * size   # -1 means "not land yet"
        self.rank = [0] * size
        self.count = 0

    def add(self, x):
        if self.parent[x] == -1:
            self.parent[x] = x
            self.count += 1

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
    def numIslands2(self, m, n, positions):
        dsu = DSU(m * n)
        land = set()
        res = []
        for r, c in positions:
            if (r, c) in land:
                res.append(dsu.count)
                continue
            land.add((r, c))
            idx = r * n + c
            dsu.add(idx)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) in land:
                    dsu.union(idx, nr * n + nc)
            res.append(dsu.count)
        return res
```

**Why it is correct.** Before neighbors are considered, the new cell is provisionally its own
island (`count += 1`). Unioning with each already-land neighbor merges components; the DSU only
decrements `count` when two *different* roots merge, so a cell adjacent to two cells of the *same*
existing island decrements once (correct), and a cell bridging two *different* islands decrements
twice, netting `+1 - 2 = -1` (see Example 2, step 3: `2 → 1`).

- **Time:** `O(P · α(m·n))` ≈ `O(P)` — constant orthogonal-neighbor work per operation.
- **Space:** `O(m · n)` for the DSU arrays plus `O(P)` for the land set / output.

## Key Insights & Edge Cases

- **Only 4-directional adjacency counts.** Diagonal neighbors do not connect islands — Example 2
  step 2 keeps `(0,0)` and `(1,1)` separate.
- **Repeated positions must be a no-op** for the count. Guard with a `land` set (or check
  `parent[idx] != -1`) so you do not double-count or wrongly re-union.
- **Bridging decrements twice.** A single new cell can merge up to four neighbors; each genuine
  merge decrements `count`, which is why the "start at +1, then subtract per real union" bookkeeping
  is essential.
- Flatten `(r, c)` to `r * n + c` (use `n`, the column count, as the stride) to index flat arrays;
  a common bug is using `m` instead of `n`.
- Using `parent[x] == -1` as the "not land yet" sentinel lets a single array double as both the
  land marker and the DSU parent pointer.
