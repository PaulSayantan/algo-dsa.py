# Number of Islands — Solution

## Brute Force

A union-find (disjoint set union) over all land cells is a common alternative:
union each land cell with its right and down land neighbors, then count distinct
roots. It works and is near-linear, but it introduces extra data structures and
is overkill for a one-pass counting task.

- **Time:** `O(m * n * α(m*n))` ≈ near-linear with path compression + union by
  rank.
- **Space:** `O(m * n)` for the parent/rank arrays.

## Optimal Approach (Flood Fill via DFS/BFS)

Scan every cell. When you hit a land cell (`'1'`) that has not yet been claimed,
you have found a new island: increment the count and **flood fill** the whole
connected landmass, marking each reached land cell as visited (either by mutating
it to `'0'` or using a separate visited matrix). Because the fill consumes the
entire component, the outer scan will never start a second island inside the same
landmass.

Why it is correct: the outer loop starts a fill exactly once per connected
component — on the first land cell of that component it encounters — because every
other cell of the component is already marked visited by that fill before the scan
reaches it. Thus the count equals the number of connected components.

### Step by step (DFS, sinking islands in place)

1. `count = 0`.
2. For each `(r, c)`: if `grid[r][c] == '1'`, do `count += 1` and `dfs(r, c)`.
3. `dfs(r, c)`: if out of bounds or `grid[r][c] != '1'`, return. Otherwise set
   `grid[r][c] = '0'` (sink it) and recurse into the four neighbors.
4. Return `count`.

```python
def numIslands(self, grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark visited by sinking
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

- **Time:** `O(m * n)` — the outer scan touches each cell once, and across all
  fills each cell is sunk at most once.
- **Space:** `O(m * n)` worst case for recursion depth (a grid that is entirely
  land). Use an explicit stack / BFS queue to avoid deep recursion on `300 x 300`
  inputs.

## Key Insights & Edge Cases

- **Sinking vs. visited set:** mutating `'1'` to `'0'` avoids allocating a
  visited matrix. If you must preserve the input, use a separate `visited` set
  and check it in the guard.
- **Recursion depth:** with `m, n <= 300`, a single all-land grid gives a
  component of 90,000 cells; Python's default recursion limit (~1000) will
  overflow. Prefer iterative BFS/DFS, or raise the limit.
- **Empty grid** or all water: return `0`.
- **Diagonals never connect** — only orthogonal neighbors form an island.
