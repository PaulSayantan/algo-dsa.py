# Solution — Minimum Cost Path

## Brute Force

Do a DFS/backtracking search from `(0,0)`, trying all four moves and summing
cell values, tracking the best total that reaches `(m-1, n-1)`. Because moves in
all four directions are allowed, you must maintain a visited set on the current
path to avoid cycles, and the number of simple paths in a grid is exponential.

- **Time:** Exponential — roughly O(4^(m·n)) paths in the worst case.
- **Space:** O(m·n) recursion depth plus the visited set.

A plain DP `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])` (the LeetCode 64
recurrence) is **wrong here** because it assumes you only ever move right/down;
the four-direction version needs sideways/upward detours (see Example 2).

## Optimal Approach — Dijkstra on the Grid

Treat each cell as a node. The "edge" from a cell into a neighbour `nb` has
weight `grid[nb]` (the cost you pay to *enter* `nb`). All weights are
non-negative, so Dijkstra applies.

### Why it is correct

Dijkstra settles cells in non-decreasing order of best-known distance. When a
cell is first popped from the min-heap, no cheaper route to it can exist, because
any not-yet-explored path goes through a frontier cell whose tentative distance
is `>=` the popped value, and all remaining edges add non-negative cost. Hence
the first pop of the destination is its optimal cost.

### Step by step

1. Initialise `dist[0][0] = grid[0][0]` (the start cell's own value counts) and
   every other `dist` to infinity.
2. Push `(grid[0][0], 0, 0)` onto a min-heap keyed by accumulated cost.
3. Pop the smallest `(d, r, c)`. If `d > dist[r][c]`, it is a stale entry — skip
   it. If `(r, c)` is the destination, return `d`.
4. For each in-bounds neighbour `(nr, nc)`, compute `nd = d + grid[nr][nc]`. If
   `nd < dist[nr][nc]`, update `dist` and push `(nd, nr, nc)`.
5. The destination is returned in step 3 (it is always reachable).

```python
import heapq
from typing import List


def min_cost_path(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    INF = float("inf")
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]  # (cost so far, row, col)
    while pq:
        d, r, c = heapq.heappop(pq)
        if r == m - 1 and c == n - 1:
            return d
        if d > dist[r][c]:
            continue  # stale
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                nd = d + grid[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))
    return dist[m - 1][n - 1]
```

- **Time:** O(m·n·log(m·n)) — up to O(m·n) heap entries, each push/pop `log`.
- **Space:** O(m·n) for `dist` and the heap.

## Key Insights & Edge Cases

- **The start cell's value counts.** Seed `dist[0][0] = grid[0][0]`, not `0`.
  For a `1x1` grid the answer is that single cell's value.
- **Four directions, not two.** This is exactly why DP-by-rows fails and a true
  shortest-path search is required — the optimal path can move left and up.
- **Lazy deletion.** A cell may be pushed several times with different tentative
  costs; guard popped entries with `if d > dist[r][c]: continue` so each cell is
  *settled* only once.
- **Non-negative weights are essential.** If cells could be negative, Dijkstra's
  "first pop is final" invariant breaks and you would need Bellman-Ford.
- If all cells had equal cost, this degenerates to plain BFS — Dijkstra is the
  right tool precisely because the weights differ.
