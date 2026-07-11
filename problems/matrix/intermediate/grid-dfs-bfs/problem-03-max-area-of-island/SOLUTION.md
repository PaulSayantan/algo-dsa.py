# Max Area of Island — Solution

## Brute Force

As with Number of Islands, a Union-Find alternative works: union adjacent land
cells, then tally the size of each component and take the max.

- **Time:** `O(R * C * α(R * C))`.
- **Space:** `O(R * C)` for parent + size arrays.

Correct, but heavier than a direct traversal that already knows each region's
size as it explores.

## Optimal Approach (Grid DFS / BFS)

This is Number of Islands with one twist: instead of counting *how many* islands
there are, we measure *how big* each one is and keep the maximum.

Sweep every cell. When you reach an unvisited land cell, run a DFS/BFS that
floods the whole connected landmass and **returns the number of cells it
visited**. Update `best = max(best, area)`.

**Why it is correct:** The traversal visits precisely the connected component of
land containing the seed cell (4-directional adjacency defines the edges), so the
count it returns is exactly that island's area. Marking cells visited (sinking to
`0` or a `visited` set) ensures every island is measured once and no cell is
counted twice.

### Step by step

1. `best = 0`.
2. For each cell `(r, c)` that is land and unvisited:
   - `area = flood(r, c)` — mark and count every connected land cell.
   - `best = max(best, area)`.
3. Return `best`.

### Reference implementation (recursive DFS returning area)

```python
def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # sink to mark visited
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))
    return best
```

- **Time:** `O(R * C)` — each cell contributes O(1) work across the whole sweep.
- **Space:** `O(R * C)` — recursion stack / queue in the worst case.

## Key Insights & Edge Cases

- The DFS **accumulates and returns** a size: `1 + sum(children)`. Sinking before
  recursing keeps the count exact.
- No land anywhere → the loop never floods, `best` stays `0`.
- A single land cell is an island of area `1`.
- Grid bounds `1 <= m, n <= 50` are small enough that recursive DFS is safe here,
  but BFS is equally valid.
