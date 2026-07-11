# Making A Large Island — Solution

## Brute Force

Try every `0` cell: flip it to `1`, run a full Number-of-Islands-style flood to
find the largest island in the modified grid, then flip it back. Track the best
result over all flips. Also handle the all-`1` grid (answer `n*n`).

- **Time:** `O((n^2)^2) = O(n^4)` — up to `n^2` candidate flips, each followed
  by an `O(n^2)` scan. For `n = 500` that is ~`6.25 x 10^10` operations, far
  too slow.
- **Space:** `O(n^2)`.

The redundancy: every flip recomputes island sizes from scratch, even though
the islands themselves do not change — only the bridge between them does.

## Optimal Approach (Label components, then merge across one flip)

Compute each island's size **once**, then answer every candidate flip in `O(1)`.

### Phase 1 — Label islands with unique ids and record sizes

Sweep the grid. Each time you hit an unvisited `1`, assign a fresh island id
(start ids at `2` so they never collide with the `0`/`1` values already in the
grid) and flood the whole component, stamping every cell with that id and
counting its size. Store `size[id] = area` in a dictionary.

### Phase 2 — Evaluate each 0

For every `0` cell, look at its 4 neighbours. Collect the **set of distinct
island ids** among them (a set is essential — two neighbours may belong to the
*same* island, and you must not double-count it). The island formed by flipping
this `0` has size:

```
1 + sum(size[id] for id in distinct_neighbor_ids)
```

Track the maximum over all `0` cells.

### Edge case — no zeros

If the grid contains no `0`, no flip is possible; the answer is the largest
existing island size (which, when the grid is all `1`s, equals `n*n`).
Initialize `best` to the max island size seen in Phase 1 so this is handled for
free.

```python
def largestIsland(grid):
    n = len(grid)
    size = {}                      # island id -> area
    next_id = 2

    def dfs(r, c, island_id):
        if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
            return 0
        grid[r][c] = island_id     # stamp + mark visited
        return (1
                + dfs(r + 1, c, island_id) + dfs(r - 1, c, island_id)
                + dfs(r, c + 1, island_id) + dfs(r, c - 1, island_id))

    # Phase 1: label every island.
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                size[next_id] = dfs(r, c, next_id)
                next_id += 1

    # Handles the all-land / no-zero case: best starts as the biggest island.
    best = max(size.values(), default=0)

    # Phase 2: try flipping each 0.
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                seen = set()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        seen.add(grid[nr][nc])
                total = 1 + sum(size[i] for i in seen)
                best = max(best, total)

    return best
```

**Why it is correct:** flipping a single `0` can only merge islands that are
directly adjacent to that cell. Every cell of those adjacent islands is already
counted in their precomputed sizes, and adding the distinct sizes (via a set)
plus one for the flipped cell gives the exact size of the merged island. Taking
the max over all flips — and seeding `best` with the largest untouched island —
covers every possibility, including flipping no cell.

- **Time:** `O(n^2)` — Phase 1 visits each cell once; Phase 2 does `O(1)` work
  (at most 4 neighbours) per `0`.
- **Space:** `O(n^2)` for the size map / recursion stack in the worst case.

## Key Insights & Edge Cases

- **Use a `set` of neighbour ids.** Two of a cell's neighbours can belong to the
  same island; summing without dedup double-counts and overshoots the answer.
- **Stamp island ids starting at `2`.** Reusing `1` would clash with as-yet
  unvisited land during Phase 1; starting at `2` keeps `0` (water) and `1`
  (unvisited land) distinguishable, and lets Phase 2 test `grid[nr][nc] > 1`.
- **No zeros to flip** → answer is the largest existing island; seeding `best`
  with `max(size.values(), default=0)` handles both the all-`1` grid (`n*n`) and
  an all-`0` grid (`0`).
- **All-water grid:** every flip yields an island of size `1`, so the answer is
  `1` (unless the grid is empty).
- This "precompute components once, then answer queries in O(1)" pattern
  generalizes: whenever you would otherwise re-flood per query, label first.
