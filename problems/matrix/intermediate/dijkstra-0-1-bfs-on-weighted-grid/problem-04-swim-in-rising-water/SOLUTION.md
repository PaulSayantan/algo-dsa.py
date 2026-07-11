# Solution — Swim in Rising Water

## Brute Force

Binary search or linearly scan `t` from `0` upward; for each `t`, run a BFS/DFS
using only cells with elevation `<= t` and check whether `(n-1, n-1)` is
reachable from `(0, 0)`. The first `t` that connects them is the answer.

- **Time:** O(n² · log(n²)) with binary search over `t` and an O(n²) reachability
  test per guess — already efficient, but a plain linear scan of `t` costs
  O(n⁴).
- **Space:** O(n²).

This works and is a perfectly good solution; the Dijkstra formulation below
finds the same value in one pass without an outer search.

## Optimal Approach — Dijkstra with a Minimax Relaxation

The answer is the **minimum over all paths of the maximum elevation** on the
path (the bottleneck elevation). Define `time[cell]` = the smallest achievable
"maximum elevation" to reach that cell. The relaxation uses `max`:

```
candidate = max(time[cur], grid[nb])
if candidate < time[nb]:
    time[nb] = candidate
```

which reads: to stand on `nb` you must have waited long enough both for your
route so far (`time[cur]`) and for `nb` itself (`grid[nb]`).

### Why it is correct

As with Path With Minimum Effort, the path cost is a **non-decreasing** function
of the prefix — taking `max` with another elevation never lowers it. That
monotonicity is exactly what Dijkstra needs, so the first time the min-heap pops
a cell, its `time` value is final and optimal. The heap always expands the cell
reachable at the earliest time.

### Step by step

1. `time[0][0] = grid[0][0]` (you cannot start before the start cell is
   passable); all others `= ∞`. Push `(grid[0][0], 0, 0)`.
2. Pop the smallest `(t, r, c)`. If it is the bottom-right cell, return `t`. Skip
   if `t > time[r][c]` (stale).
3. For each in-bounds neighbour, compute `cand = max(t, grid[nr][nc])`. If
   `cand < time[nr][nc]`, update and push `(cand, nr, nc)`.
4. Continue until the destination is popped.

```python
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float("inf")
        time = [[INF] * n for _ in range(n)]
        time[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]  # (max elevation so far, row, col)
        while pq:
            t, r, c = heapq.heappop(pq)
            if r == n - 1 and c == n - 1:
                return t
            if t > time[r][c]:
                continue  # stale
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    cand = max(t, grid[nr][nc])
                    if cand < time[nr][nc]:
                        time[nr][nc] = cand
                        heapq.heappush(pq, (cand, nr, nc))
        return time[n - 1][n - 1]
```

- **Time:** O(n²·log(n²)) — O(n²) cells, each with O(1) neighbours, heap ops
  `log`.
- **Space:** O(n²).

### Alternative: Union-Find by elevation

Because elevations are a permutation of `0..n²-1`, you can "flood" cells in
increasing elevation order, union each newly flooded cell with already-flooded
neighbours, and return the elevation at which `(0,0)` and `(n-1,n-1)` first join
the same component. This is O(n²·α(n²)) and is a classic offline alternative.

## Key Insights & Edge Cases

- **Minimax over cells**, not edges: the weight lives on the destination cell
  (`grid[nb]`), unlike Path With Minimum Effort where it is a difference between
  two cells.
- **Seed with `grid[0][0]`.** You cannot enter the grid before the start itself
  is submerged, so the answer is at least `max(grid[0][0], grid[n-1][n-1])`.
- **`max`, not `+`.** Summing elevations would answer a different question.
- **Lazy deletion** with `t > time[r][c]` keeps each cell settled once.
- The uniqueness of elevations is what makes the Union-Find variant clean, but
  Dijkstra does not rely on it.
