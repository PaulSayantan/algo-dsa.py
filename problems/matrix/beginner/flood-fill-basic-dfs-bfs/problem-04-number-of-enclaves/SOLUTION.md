# Number of Enclaves — Solution

## Brute Force

For each land cell, launch an independent search to test whether it can reach any
border, then count the cells that cannot. Because you restart a full search per
land cell (and do not share work), this degrades badly.

- **Time:** `O((m * n)^2)` in the worst case.
- **Space:** `O(m * n)` per search.

## Optimal Approach (Flood Fill from the borders)

Flip the question around. Instead of asking "can this cell escape?", **remove
everything that can escape**, then count what is left. Land that can walk off the
boundary is exactly the land connected to a border land cell. So:

1. Flood-fill starting from every land cell on the four borders, marking each
   reachable land cell as "escaped" (e.g. set it to `0`).
2. After all border fills complete, every remaining `1` is an enclave. Count
   them.

Why it is correct: a land cell can walk off the boundary iff there is a path of
4-connected land cells from it to some border cell. Reachability is symmetric, so
the set of escaping cells is precisely the union of the border land cells'
connected components. The border-seeded fills mark exactly that union; anything
untouched has no land path to a border and is trapped.

### Step by step

1. For every border cell `(r, c)` with `grid[r][c] == 1`, run `dfs(r, c)`.
2. `dfs` sinks land (`grid[r][c] = 0`) and recurses into 4 neighbors that are
   land.
3. Return `sum(cell for row in grid for cell in row)` — the leftover `1`s.

```python
def numEnclaves(self, grid):
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return
        grid[r][c] = 0  # this land escapes; erase it
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            on_border = r in (0, m - 1) or c in (0, n - 1)
            if on_border and grid[r][c] == 1:
                dfs(r, c)

    return sum(sum(row) for row in grid)
```

Iterating BFS from a queue seeded with all border land cells is the standard way
to avoid recursion-depth issues on `500 x 500` grids.

- **Time:** `O(m * n)` — border seeding scans the perimeter, and the fills touch
  each cell at most once.
- **Space:** `O(m * n)` for the traversal stack/queue in the worst case.

## Key Insights & Edge Cases

- **Invert the problem.** Directly testing every cell is quadratic; erasing the
  escapers first makes it linear. This "flood from the boundary" trick recurs in
  Surrounded Regions and Pacific/Atlantic problems.
- **Seed from all four borders**, not just one corner — enclaves are defined
  relative to any edge.
- **Land touching the border counts as escaping**, even a lone border land cell
  with no interior neighbors.
- **No interior land / empty grid:** answer is `0`.
- Prefer iterative BFS/DFS for large grids to dodge recursion limits.
