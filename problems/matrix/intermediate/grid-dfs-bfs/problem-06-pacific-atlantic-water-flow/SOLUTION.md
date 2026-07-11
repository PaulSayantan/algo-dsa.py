# Pacific Atlantic Water Flow — Solution

## Brute Force

For every cell, launch a separate DFS/BFS that follows non-increasing-height
paths and checks whether it can reach a Pacific border cell *and* an Atlantic
border cell.

- **Time:** `O((R * C)^2)` — a full traversal (`O(R * C)`) from each of the
  `R * C` starting cells.
- **Space:** `O(R * C)` per traversal for the visited set.

Correct, but it redundantly re-explores the same downhill paths from many
sources.

## Optimal Approach (Reverse multi-source Grid DFS / BFS)

The key inversion: rather than asking "from cell X, can water flow *down* to the
ocean?", ask "starting *at* the ocean border, which cells can water climb *up*
to reach?". Reverse every edge — water flows downhill (to `<=` height), so the
reverse edge goes to neighbors of **greater or equal** height.

Run two multi-source traversals:

1. **Pacific:** seed all top-row and left-column cells; DFS/BFS inward, only
   stepping to a neighbor whose height is `>=` the current cell's height. Mark
   every reachable cell as `pacific`.
2. **Atlantic:** seed all bottom-row and right-column cells; traverse the same
   way, marking `atlantic`.

The answer is every cell that is in **both** sets.

**Why it is correct:** A cell drains to the Pacific iff there is a
non-increasing-height path from it to some Pacific-border cell. Reversing that
path gives a non-decreasing-height walk from the border to the cell — exactly
what the reverse traversal explores. So `pacific` is precisely the set of cells
that drain to the Pacific, and likewise for `atlantic`; the intersection is the
set draining to both. Seeding all border cells at once (multi-source) captures
"any" border entry point in a single traversal.

### Step by step / reference implementation

```python
def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    rows, cols = len(heights), len(heights[0])
    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]

    def dfs(r, c, seen):
        seen[r][c] = True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and not seen[nr][nc]
                    and heights[nr][nc] >= heights[r][c]):  # climb up on reverse
                dfs(nr, nc, seen)

    for r in range(rows):
        dfs(r, 0, pacific)            # left edge  -> Pacific
        dfs(r, cols - 1, atlantic)    # right edge -> Atlantic
    for c in range(cols):
        dfs(0, c, pacific)            # top edge    -> Pacific
        dfs(rows - 1, c, atlantic)    # bottom edge -> Atlantic

    return [[r, c] for r in range(rows) for c in range(cols)
            if pacific[r][c] and atlantic[r][c]]
```

- **Time:** `O(R * C)` — two traversals, each visiting every cell at most once.
- **Space:** `O(R * C)` — the two boolean matrices plus recursion/queue.

## Key Insights & Edge Cases

- **Traverse from the oceans inward**, not from each cell outward — this collapses
  `O((R*C)^2)` into `O(R*C)`.
- **Reverse the comparison:** downhill flow is `<=`, so climbing on the reverse
  traversal uses `>=`.
- **Two separate visited matrices**, one per ocean; answer = their intersection.
- Border cells trivially reach their own ocean, which is why they are seeds.
- **Single cell / single row / single column** grids: every cell touches both
  ocean groups, so all cells are returned (e.g. `[[1]] -> [[0,0]]`).
- Equal-height plateaus are reachable in both directions since the condition is
  `>=` (non-strict), which is required for water to sit and still drain.
