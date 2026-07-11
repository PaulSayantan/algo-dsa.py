# Max Area of Island — Solution

## Brute Force

Union-find again works: union adjacent land cells, then take the maximum
component size (track sizes during union). It is near-linear but heavier than a
plain traversal, and computing per-component sizes requires extra bookkeeping.

- **Time:** `O(m * n * α(m*n))` ≈ near-linear.
- **Space:** `O(m * n)` for parent + size arrays.

## Optimal Approach (Flood Fill via DFS/BFS)

This is Number of Islands with a twist: instead of merely counting components,
each flood fill **returns its area** — the number of land cells it visited. Scan
the grid, and whenever you meet an unvisited land cell, run a fill that sinks the
component and returns its size; keep the running maximum.

Why it is correct: each connected component is flooded exactly once (the fill
marks all its cells visited before the outer scan reaches them again). A DFS that
returns `1 + area(neighbors)` sums to the total number of cells in the component,
so the maximum over all components is the answer.

### Step by step (DFS returning area)

1. `best = 0`.
2. For each `(r, c)` with `grid[r][c] == 1`: `best = max(best, dfs(r, c))`.
3. `dfs(r, c)`: if out of bounds or `grid[r][c] == 0`, return `0`. Otherwise set
   `grid[r][c] = 0` (sink) and return
   `1 + dfs(up) + dfs(down) + dfs(left) + dfs(right)`.
4. Return `best`.

```python
def maxAreaOfIsland(self, grid):
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # mark visited
        return (1 + dfs(r + 1, c) + dfs(r - 1, c)
                  + dfs(r, c + 1) + dfs(r, c - 1))

    best = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))
    return best
```

An iterative version increments a local counter each time it pops a fresh land
cell off the stack/queue.

- **Time:** `O(m * n)` — every cell is visited a constant number of times.
- **Space:** `O(m * n)` worst-case recursion/stack depth for one large island.

## Key Insights & Edge Cases

- **Return the count, don't just mark.** The only difference from island-counting
  is that the fill produces an area; sum `1 + children` (DFS) or count pops (BFS).
- **Sink as you go** so a cell is never double-counted; a cell contributes to
  exactly one island's area.
- **No islands:** return `0` (the initial `best`).
- **Sink before recursing** into neighbors — marking the current cell first
  prevents it from being re-added by an adjacent cell and inflating the count.
