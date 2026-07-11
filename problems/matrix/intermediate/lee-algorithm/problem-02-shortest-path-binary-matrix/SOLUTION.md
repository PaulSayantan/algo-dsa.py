# Solution — Shortest Path in Binary Matrix

## Brute Force

Enumerate every clear path from `(0,0)` to `(n-1,n-1)` via DFS/backtracking and
keep the minimum cell count. With 8 directions and revisits allowed along
different routes, the number of paths explodes exponentially.

- **Time:** Exponential, up to O(8^(n²)) without memoization.
- **Space:** O(n²) recursion depth.

Impractical for `n` up to 100.

## Optimal Approach — Lee Algorithm (8-directional BFS)

Each move costs 1 cell regardless of direction (including diagonals), so the
grid is unweighted and BFS yields shortest distances. The only twist versus the
standard 4-direction template is the **neighbour set of 8 offsets**.

### Why it is correct

BFS explores cells in non-decreasing distance order. The first time it reaches
`(n-1, n-1)`, that distance (in cells) is minimal. Marking cells visited on
enqueue keeps each cell in the queue at most once, so the search is O(n²).

### Step by step

1. **Guard the endpoints:** if `grid[0][0] == 1` or `grid[n-1][n-1] == 1`,
   return `-1` immediately — no clear path can start or finish.
2. Enqueue `(0, 0)` with a path length of `1` (we count cells, so the start
   already counts as one). Mark it visited.
3. Pop `(r, c, dist)`. If `(r, c)` is the bottom-right cell, return `dist`.
4. For each of the 8 neighbours that are in bounds, equal to `0`, and unvisited:
   mark visited and enqueue with `dist + 1`.
5. If the queue empties, return `-1`.

```python
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        q = deque([(0, 0, 1)])
        grid[0][0] = 1  # mark visited
        while q:
            r, c, dist = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, dist + 1))
        return -1
```

- **Time:** O(n²) — every cell is enqueued once, each visiting 8 neighbours.
- **Space:** O(n²) for the queue / visited marks.

## Key Insights & Edge Cases

- **Count cells, not edges:** the start cell contributes 1, so a 1×1 grid of
  `[[0]]` returns `1`, not `0`.
- **8 directions**, not 4 — diagonals are allowed and are what make many paths
  shorter than a Manhattan route.
- **Blocked endpoints:** an early check for `grid[0][0]` and the target avoids
  subtle bugs.
- **Mark on enqueue** to keep the O(n²) guarantee; marking on dequeue can queue
  the same cell many times through diagonal overlaps.
