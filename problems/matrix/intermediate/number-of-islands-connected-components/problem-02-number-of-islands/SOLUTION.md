# Number of Islands — Solution

## Brute Force

A tempting "brute" idea is Union-Find without the smart optimizations, or
repeatedly scanning to merge adjacent land cells. Even simpler-minded: for
every land cell, run a full traversal from it and try to deduplicate regions by
comparing membership sets. Comparing/merging sets naively is `O((m*n)^2)` or
worse and needs `O(m*n)` extra memory per region — clearly overkill.

The real insight is that **a single linear sweep + one flood per island** is
already optimal, so the "brute force" and "optimal" collapse to the same
traversal; the only thing that varies is *how* you flood (DFS vs BFS vs
Union-Find) and whether you overcomplicate the bookkeeping.

## Optimal Approach (Connected Components via DFS/BFS)

Model land cells as graph nodes with edges between 4-directionally adjacent
land cells. The number of islands is exactly the number of connected
components. Count them with one sweep:

1. Initialize `count = 0`.
2. Scan every cell `(r, c)`.
3. When you hit an **unvisited land cell**, increment `count` and flood the
   entire connected region (DFS or BFS), marking every reached land cell as
   visited so it is never counted again.
4. Return `count`.

**Why it is correct:** the sweep guarantees you start a flood exactly once per
component — the first time you encounter any of its cells. Every later cell of
that same component is already marked visited, so it never triggers a new
count. Thus `count` equals the number of components.

### DFS reference implementation

```python
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != "1":
            return
        grid[r][c] = "0"          # mark visited by sinking the land
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
```

### BFS variant (avoids deep recursion)

Use a queue seeded with the newly found land cell; pop, and for each in-bounds
land neighbour, mark it visited (`'0'`) and enqueue it. BFS is safer when the
grid is up to `300 x 300 = 90,000` cells and a pathological snake shape could
blow the recursion limit.

### Union-Find variant

Give each land cell an id; union it with its right and down land neighbours.
The answer is the number of distinct roots among land cells. With path
compression + union by rank this is `O(m*n * α(m*n))`.

- **Time:** `O(m*n)` — each cell is visited a constant number of times.
- **Space:** `O(m*n)` worst case (recursion stack / BFS queue / DSU arrays). If
  you may not mutate the grid, add a separate `visited` matrix of the same size.

## Key Insights & Edge Cases

- **"Sinking" land to `'0'` is the cheapest visited marker** and avoids extra
  memory — but it destroys the input. If the caller needs the grid intact, use
  a `visited` set/matrix instead.
- **Values are characters** `'0'`/`'1'`, not integers — compare against the
  string literals.
- **Empty grid or all-water grid** returns `0`; guard against `grid` or
  `grid[0]` being empty.
- **Only 4 directions** — diagonally touching land cells are distinct islands
  (see Example 2).
- **Recursion depth:** on the maximum `300 x 300` grid a single-component snake
  can require ~90,000 nested frames; prefer BFS or an explicit stack if you hit
  a `RecursionError`.
