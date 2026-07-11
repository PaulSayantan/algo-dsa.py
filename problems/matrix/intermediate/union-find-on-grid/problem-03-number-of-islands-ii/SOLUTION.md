# Number of Islands II — Solution

## Brute Force

After each `addLand`, run a full flood-fill count of islands over the whole grid (as in
LeetCode 200). With `k = positions.length` operations, each scan is `O(m · n)`.

- **Time:** `O(k · m · n)` — up to `10^4 · 10^4 = 10^8`… and `m·n` can be `10^4`, so this is
  `10^8` in the worst case and blows up when both are large.
- **Space:** `O(m · n)`.

The waste is obvious: each step changes only one cell, yet we recompute everything. Union–Find
updates the answer incrementally.

## Optimal Approach (Union–Find on Grid)

**Idea.** Maintain a DSU over all `m · n` cells plus a boolean `active` grid and a running
`count` of islands. Cells are "inactive" (water) until an `addLand` turns them on.

For each `positions[i] = (r, c)`:
1. If `(r, c)` is already active, append the current `count` (no-op) and continue.
2. Mark it active; `count += 1` (a fresh singleton island).
3. For each of the 4 neighbors that is **in bounds and active**: `union(cur, neighbor)`. If the
   union merges two different sets, `count -= 1`.
4. Append `count` to the result.

**Why it is correct.** At every moment the active cells' DSU sets are exactly the current
islands (same argument as LeetCode 200, applied incrementally). Turning on a new cell tentatively
creates one new island; each merge with an already-active neighbor joins two components into
one, reducing the count by one. Because we only touch the new cell and its ≤ 4 neighbors, each
step is `O(α)` amortized. Handling the duplicate case in step 1 keeps the count correct when the
same cell is added twice.

- **Time:** `O(k · α(m·n))` ≈ `O(k)` — near-linear in the number of operations.
- **Space:** `O(m · n)` for the DSU and `active` arrays.

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
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


class Solution:
    def numIslands2(self, m, n, positions):
        dsu = DSU(m * n)
        active = [False] * (m * n)
        count = 0
        res = []
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r, c in positions:
            idx = r * n + c
            if active[idx]:
                res.append(count)
                continue
            active[idx] = True
            count += 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nidx = nr * n + nc
                    if active[nidx] and dsu.union(idx, nidx):
                        count -= 1
            res.append(count)
        return res
```

## Key Insights & Edge Cases

- **Only union with active neighbors.** A water cell is not part of any island; unioning to it
  would corrupt the count.
- **Handle duplicate positions.** Re-adding an active cell must not increment `count`. Skipping
  early (step 1) is the clean guard; forgetting it is the most common bug (see Example 3).
- **Check all four directions here** (not just right/down). Unlike a full static scan, the
  cells arrive in arbitrary order, so any of the four neighbors may already be active.
- **A merge only counts once per neighbor pair.** Using `union`'s boolean return (`True` only on
  a real merge) prevents double-decrementing when two neighbors already belong to the same
  island.
- Flatten with `r * n + c` where `n` is the number of **columns**; mixing up `m` and `n` is an
  easy indexing error.
- With `m · n` up to `10^4`, allocating a full `m·n` DSU array is fine; if it were much larger
  and sparse you could switch to a hash-map-backed DSU keyed only on activated cells.
