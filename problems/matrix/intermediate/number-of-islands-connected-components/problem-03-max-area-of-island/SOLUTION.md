# Max Area of Island — Solution

## Brute Force

For each land cell, launch an independent traversal that counts its component's
size, using a *fresh* visited set every time so components are recomputed from
scratch. Take the max over all starting cells.

- **Time:** `O((m*n)^2)` — up to `m*n` starting cells, each doing an `O(m*n)`
  traversal.
- **Space:** `O(m*n)` for the per-start visited set.

This recomputes the same component many times (once per cell it contains), so
it is quadratic and wasteful.

## Optimal Approach (Connected Components with size accumulation)

This is the Number of Islands sweep with one change: instead of just marking a
region, each flood **returns how many cells it covered**. Keep a running
maximum.

1. Initialize `best = 0`.
2. Sweep every cell. When you find an unvisited land cell, flood its component
   and get back the area.
3. `best = max(best, area)`.
4. Return `best`.

**Why it is correct:** each component is flooded exactly once (the first cell of
it encountered by the sweep triggers the flood; all its other cells are marked
visited and skipped). The flood counts every cell it visits exactly once, so
the returned area equals the true component size, and the max over all
components is the answer.

### DFS reference implementation

```python
def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 0                      # mark visited (sink it)
        return (1
                + dfs(r + 1, c) + dfs(r - 1, c)
                + dfs(r, c + 1) + dfs(r, c - 1))

    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))
    return best
```

The BFS version increments a counter each time it pops a land cell off the
queue; the Union-Find version stores a `size[root]` array and tracks the max
size after all unions.

- **Time:** `O(m*n)` — each cell is touched a constant number of times.
- **Space:** `O(m*n)` worst case for the recursion stack / queue.

## Key Insights & Edge Cases

- **The recursion returns a value.** The neat trick is `return 1 + sum(4
  recursive calls)`; out-of-bounds and water return `0`, so the arithmetic
  naturally accumulates only land cells.
- **No island** → return `0` (initialize `best = 0`; the sweep never updates
  it).
- **Values are integers** here (`0`/`1`), unlike Number of Islands which uses
  characters — a common copy-paste bug.
- **Sinking mutates the grid.** Use a `visited` matrix if the input must be
  preserved.
- **Single-cell islands** contribute area `1`; make sure your base/step counts
  the seed cell itself.
