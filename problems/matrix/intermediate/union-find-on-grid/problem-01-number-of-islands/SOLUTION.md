# Number of Islands — Solution

## Brute Force

The most common "brute force" here is actually a flood fill: scan every cell; when you find
an unvisited `'1'`, start a DFS/BFS that marks every land cell reachable from it, then
increment the island counter. Each cell is visited once.

- **Time:** `O(m · n)` — every cell is pushed/popped at most once.
- **Space:** `O(m · n)` worst case for the recursion stack / queue (a grid that is all land).

This is optimal in complexity, but it is *destructive or requires a visited set*, and it does
not generalize to incremental updates. Union–Find gives the same complexity while modeling
connectivity explicitly.

## Optimal Approach (Union–Find on Grid)

**Idea.** Map each cell `(r, c)` to a flat id `r * cols + c`. Initialize the DSU with one set
per land cell (water cells are ignored / never become roots). Sweep the grid once; for each
land cell, `union` it with its **right** and **down** neighbors if those are also land. Looking
only right and down is enough because left/up neighbors were already processed when they were
the "current" cell — every adjacency is covered exactly once.

Maintain a running `count` of land sets: start it at the number of `'1'`s, and decrement it
each time a `union` actually merges two previously-separate sets. The final `count` is the
number of islands.

**Why it is correct.** Two land cells end up in the same DSU set iff there is a path of
4-directional land steps between them (union is transitive and we union every adjacent land
pair). Thus DSU sets are exactly the connected components = islands. Counting merges is a
standard identity: starting from `k` singletons, each successful union reduces the number of
components by exactly one.

**Step by step:**
1. Count land cells; set `count` to that number. Build a `DSU`.
2. For each cell `(r, c)` with `grid[r][c] == '1'`:
   - If `(r, c+1)` is land, `union(id(r,c), id(r,c+1))`; if it merged, `count -= 1`.
   - If `(r+1, c)` is land, `union(id(r,c), id(r+1,c))`; if it merged, `count -= 1`.
3. Return `count`.

- **Time:** `O(m · n · α(m·n))` ≈ `O(m · n)` with path compression + union by size.
- **Space:** `O(m · n)` for the `parent` / `size` arrays.

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
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                count += 1
                idx = r * cols + c
                if c + 1 < cols and grid[r][c + 1] == "1":
                    if dsu.union(idx, idx + 1):
                        count -= 1
                if r + 1 < rows and grid[r + 1][c] == "1":
                    if dsu.union(idx, idx + cols):
                        count -= 1
        return count
```

## Key Insights & Edge Cases

- **Only union right and down.** Unioning all four directions still works but does redundant
  find calls; right+down covers every edge exactly once.
- **Grid values are characters** (`'1'`/`'0'`), not integers — a classic off-by-type bug.
- **All water** → answer `0`; **all land** → answer `1`. Both fall out naturally because
  `count` starts at the land total and merges bring it down.
- **Single row or single column** grids are handled the same way; the neighbor bounds checks
  prevent out-of-range access.
- **Diagonal cells are not connected** — do not add diagonal unions.
- Use **path compression + union by size/rank**; without them, worst-case find is `O(n)` and a
  300×300 grid can time out.
