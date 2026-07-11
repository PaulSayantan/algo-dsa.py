# Number of Islands — Solution

## Brute Force

A "brute force" reading is to compute connected components with a **Union-Find
(Disjoint Set Union)** structure: union every land cell with its right and down
land neighbor, then count distinct roots among land cells.

- **Time:** `O(R * C * α(R * C))`, effectively near-linear.
- **Space:** `O(R * C)` for the parent array.

This is correct and competitive, but a plain traversal is simpler to write and
reason about.

## Optimal Approach (Grid DFS / BFS)

Scan every cell. When you hit a land cell (`'1'`) that has not been visited, you
have found a new island — increment the counter and launch a DFS/BFS that
**sinks** the entire connected landmass (mark every reachable land cell as
visited, e.g. by flipping it to `'0'` or adding it to a `visited` set). Because
the flood consumes the whole island, no other cell of it will ever trigger the
counter again.

**Why it is correct:** Islands are exactly the connected components of the
"land" subgraph under 4-directional adjacency. A graph's component count equals
the number of times you start a fresh traversal from an unvisited node when
sweeping all nodes. Sinking guarantees each component is counted once and only
once.

### Step by step

1. Initialize `count = 0`.
2. For each cell `(r, c)`:
   - If it is land and not yet visited: `count += 1`, then DFS/BFS to mark all
     connected land as visited.
3. Return `count`.

### Reference implementation (iterative BFS)

```python
from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                grid[r][c] = "0"  # sink
                q = deque([(r, c)])
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
    return count
```

- **Time:** `O(R * C)` — every cell is visited once by the outer scan and at
  most once by a flood.
- **Space:** `O(R * C)` — the queue/recursion in the worst case (a grid that is
  entirely land). Use a separate `visited` set instead of mutating if the input
  must be preserved.

## Key Insights & Edge Cases

- **Sink on visit** (or mark visited) so a single island is not double-counted.
- Mutating the grid to `'0'` is `O(1)` extra space; keep a `visited` set instead
  if the caller needs the grid intact.
- Recursive DFS can overflow the stack on a 300x300 all-land grid (up to 90,000
  deep); prefer BFS or an explicit stack there.
- Empty grid → `0` islands.
- Grid values are **strings** `'0'`/`'1'` in this LeetCode problem, not ints —
  compare accordingly.
