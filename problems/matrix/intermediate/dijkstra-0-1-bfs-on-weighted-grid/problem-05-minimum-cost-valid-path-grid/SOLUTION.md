# Solution — Minimum Cost to Make at Least One Valid Path in a Grid

## Brute Force

Try every combination of sign changes (each cell either keeps or flips to one of
3 other directions) and test whether a valid path now exists. With up to
`m·n = 10^4` cells and 4 choices each, this is astronomically large.

- **Time:** Exponential — O(4^(m·n)) in the worst case.
- **Space:** O(m·n).

## Optimal Approach — 0-1 BFS over Directional Costs

Model each cell as a node with **four outgoing edges**, one per direction:

- The direction the cell's sign already points has weight `0` (free).
- Each of the other three directions has weight `1` (you change the sign once).

We want the minimum-cost path from `(0,0)` to `(m-1,n-1)`. Every edge weight is
`0` or `1`, so this is a **0-1 BFS**: a Dijkstra whose priority queue is a
double-ended queue. Free moves go to the **front** (same cost), paid moves to the
**back** (cost + 1), which keeps the deque sorted by distance and gives linear
time.

### Why it is correct

The deque always holds unsettled cells whose distances differ by at most 1 (`d`
at the front, `d+1` at the back). Popping from the front therefore yields a
globally minimum-distance unsettled cell, exactly like a Dijkstra heap. With
non-negative weights, the first pop of a cell is its optimal cost. Allowing each
cell's sign to change "at most once" is automatically respected: the cheapest
path never needs to re-enter and re-change a cell, since revisiting a settled
cell can only add cost.

### Step by step

1. Map directions to offsets, indexed by sign value: `1->(0,+1)`, `2->(0,-1)`,
   `3->(+1,0)`, `4->(-1,0)`.
2. `dist[0][0] = 0`, all others `∞`. Deque starts with `(0, 0)`.
3. Pop the **front** cell `(r, c)`. If it is the target, return `dist[r][c]`.
4. For each of the 4 directions `k` (1..4) with offset `(dr, dc)`: the move costs
   `0` if `k == grid[r][c]` else `1`. If `(nr, nc)` is in bounds and
   `dist[r][c] + cost < dist[nr][nc]`, update it and push to the **front** when
   `cost == 0`, otherwise to the **back**.
5. Continue until the target is popped.

```python
from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # direction sign -> (dr, dc): 1=right, 2=left, 3=down, 4=up
        moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        while dq:
            r, c = dq.popleft()
            if r == m - 1 and c == n - 1:
                return dist[r][c]
            for sign, (dr, dc) in moves.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = 0 if sign == grid[r][c] else 1
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        return dist[m - 1][n - 1]
```

- **Time:** O(m·n) — linear via the deque; each cell has a fixed 4 edges.
- **Space:** O(m·n) for `dist` and the deque.

## Key Insights & Edge Cases

- **The sign defines the free edge.** The one direction matching `grid[r][c]`
  costs `0`; the other three cost `1`. Getting this mapping right (1/2/3/4 ->
  right/left/down/up) is the crux.
- **Front vs. back is the algorithm.** Appending a free move to the back breaks
  the 0-1 invariant and produces wrong answers.
- **A single cell** grid returns `0`: the start already is the target.
- **Guard relaxations** with the `dist` comparison (or skip stale pops) so each
  cell settles once, even though it may be reached along several routes.
- Signs pointing outside the grid are simply out-of-bounds neighbours and are
  skipped; a plain Dijkstra min-heap solves this too, but 0-1 BFS is the natural
  linear-time fit.
