# Making a Large Island — Solution

## Brute Force

For every `0` in the grid, flip it to `1`, run a full flood fill to find the largest island,
then flip it back. Track the maximum over all flips (and handle the all-`1`s case).

- **Time:** `O((n^2)^2) = O(n^4)` — up to `n^2` candidate zeros, each costing an `O(n^2)`
  flood fill. For `n = 500` that is `~6.25 · 10^10` operations — far too slow.
- **Space:** `O(n^2)` for the visited set.

The repeated full scans are the problem: each flip only affects the components touching one
cell, yet we recompute the entire grid.

## Optimal Approach (Union–Find on Grid)

**Idea — precompute components once, then test each flip in O(1) neighbors.**

**Phase 1 — build components.** Run Union–Find over the whole grid, unioning every pair of
adjacent `1`s (right + down covers each edge once). The DSU's `size[find(root)]` now gives the
size of each existing island. Also record the current best island size `best` (it may already
be the answer if there is no `0` to flip, or the grid is all land).

**Phase 2 — try every flip.** For each cell `(r, c)` with value `0`:
- Collect the **roots** of its in-bounds `1` neighbors into a set (dedup is essential — two
  neighbors can belong to the *same* island; counting it twice overstates the size).
- Candidate size = `1` (the flipped cell) + the sum of `size[root]` over the **distinct**
  roots.
- Update the answer with this candidate.

Return the maximum of `best` and all candidate sizes.

**Why it is correct.** Flipping a single `0` at `(r, c)` to `1` connects exactly the islands
that touch `(r, c)`; the resulting island is the flipped cell plus each *distinct* adjacent
island exactly once. Precomputed component sizes make each evaluation `O(1)` in the number of
neighbors (≤ 4). The all-`1`s / no-zero case is covered by seeding the answer with the largest
existing component.

- **Time:** `O(n^2 · α(n^2))` ≈ `O(n^2)` — one pass to union, one pass over the zeros.
- **Space:** `O(n^2)` for the DSU arrays.

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
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n * n)

        def idx(r, c):
            return r * n + c

        # Phase 1: union adjacent land, right + down.
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                if c + 1 < n and grid[r][c + 1] == 1:
                    dsu.union(idx(r, c), idx(r, c + 1))
                if r + 1 < n and grid[r + 1][c] == 1:
                    dsu.union(idx(r, c), idx(r + 1, c))

        # Best existing island (covers the all-1s / no-zero case).
        best = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    best = max(best, dsu.size[dsu.find(idx(r, c))])

        # Phase 2: try flipping each 0.
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0:
                    continue
                roots = set()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        roots.add(dsu.find(idx(nr, nc)))
                candidate = 1 + sum(dsu.size[root] for root in roots)
                best = max(best, candidate)
        return best
```

## Key Insights & Edge Cases

- **Dedup neighbor roots.** The single most common bug: if two of the four neighbors are part of
  the same island, adding both sizes double-counts. Use a `set` of roots.
- **Seed the answer with the largest existing island.** If the grid is all `1`s there is no `0`
  to flip, so the loop over zeros never runs — the answer must come from `best` (Example 3
  returns `n*n`).
- **The flipped cell counts as `+1`.** Do not forget it, especially for an isolated `0` with no
  land neighbors (its best contribution is size `1`, still valid if `best` was `0`).
- **`size` is only meaningful at a root.** Always index `size[dsu.find(x)]`, never `size[x]`.
- Flatten with `r * n + c` (square grid, so rows == cols == `n`).
- Two passes only; the `O(1)`-per-zero evaluation is what turns the `O(n^4)` brute force into
  `O(n^2)`.
