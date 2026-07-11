# Solution — Path With Minimum Effort

## Brute Force

Enumerate all paths from `(0,0)` to the corner with DFS, computing each path's
effort (its maximum consecutive height difference) and keeping the minimum. Grid
paths are exponential in `rows·columns`.

- **Time:** Exponential.
- **Space:** O(rows·columns) recursion depth plus a visited set.

## Optimal Approach — Dijkstra with a Minimax Relaxation

The twist versus ordinary Dijkstra is the **objective**: we minimise the
*largest* edge along a path (a bottleneck path), not the *sum* of edges. Define
`effort[cell]` = the smallest possible value of "maximum step" over all paths
from the start to that cell. The relaxation replaces `+` with `max`:

```
candidate = max(effort[cur], abs(height[cur] - height[nb]))
if candidate < effort[nb]:
    effort[nb] = candidate
```

Everything else — the min-heap, settling the smallest-key cell first — is
identical to standard Dijkstra.

### Why it is correct

The key that Dijkstra relies on is **monotonicity**: extending a path never
*decreases* its cost. For the sum objective, adding a non-negative edge keeps the
cost non-decreasing. For the minimax objective, taking `max` with a
non-negative difference likewise never decreases the running effort. Because the
cost of a path is a non-decreasing function of its prefix, the "first pop is
optimal" argument carries over unchanged: when a cell is first removed from the
heap, its `effort` value is final.

### Step by step

1. `effort[0][0] = 0`; all other cells `= ∞`. Push `(0, 0, 0)` onto a min-heap
   keyed by effort.
2. Pop the smallest `(e, r, c)`. If it is the bottom-right cell, return `e`. Skip
   the entry if `e > effort[r][c]` (stale).
3. For each in-bounds neighbour, compute `cand = max(e, abs(h[r][c] -
   h[nr][nc]))`. If `cand < effort[nr][nc]`, update and push `(cand, nr, nc)`.
4. Continue until the target is popped.

```python
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        INF = float("inf")
        effort = [[INF] * n for _ in range(m)]
        effort[0][0] = 0
        pq = [(0, 0, 0)]  # (effort so far, row, col)
        while pq:
            e, r, c = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return e
            if e > effort[r][c]:
                continue  # stale
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cand = max(e, abs(heights[r][c] - heights[nr][nc]))
                    if cand < effort[nr][nc]:
                        effort[nr][nc] = cand
                        heapq.heappush(pq, (cand, nr, nc))
        return 0
```

- **Time:** O(rows·columns·log(rows·columns)).
- **Space:** O(rows·columns).

### Alternative: binary search + BFS/DFS

Binary search the answer `k` over `[0, 10^6]`; for each `k`, run BFS/DFS using
only edges whose height difference is `<= k` and test whether the corner is
reachable. This is O(rows·columns·log(maxHeight)) and is a common alternative
worth knowing — but the minimax Dijkstra is a single clean pass.

## Key Insights & Edge Cases

- **`max`, not `+`.** Recognizing "minimise the worst edge" as a minimax path is
  the whole insight; the code differs from a sum-cost Dijkstra by one operator.
- **A single cell** (`1x1` grid) has no steps, so the effort is `0`.
- **Effort `0` is possible** whenever a constant-height route exists (Example 3);
  initialise the start's effort to `0`, not to a height.
- **Lazy deletion** via the `e > effort[r][c]` guard keeps each cell settled
  once.
- Height differences are non-negative, preserving the monotonicity Dijkstra
  needs; a signed cost would break the algorithm.
