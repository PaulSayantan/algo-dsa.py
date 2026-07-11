# Solution — 01 Matrix

## Brute Force

For every cell run an independent BFS (or scan) to find its nearest `0`.

- **Time:** O((m·n)²) — a full traversal per cell.
- **Space:** O(m·n) per BFS.

Correct but quadratic in the number of cells; too slow at the upper limits.

## Optimal Approach — Multi-Source Lee Algorithm (BFS)

The trick is to invert the question. Rather than asking "from this `1`, where is
the nearest `0`?", start the wave **from all the `0`s simultaneously** and let it
ripple outward. The first wave to touch a `1` carries its shortest distance,
because BFS expands in distance order.

### Why it is correct

Seeding the queue with every `0` at distance `0` is equivalent to adding a
virtual "super source" connected to all zeros with zero-cost edges. BFS from that
super source visits each cell in non-decreasing distance order, so the first time
any cell is reached, it is via a shortest path to *some* zero — which is exactly
the nearest zero. Marking a cell the moment it is enqueued ensures it keeps its
first (smallest) distance and is never overwritten.

### Step by step

1. Create a `dist` matrix. Set `dist[i][j] = 0` for every `0` cell and push all
   those cells into the queue. Mark the `1` cells as unvisited (e.g. `-1` or
   `inf`).
2. Pop `(r, c)`. For each 4-directional neighbour that is still unvisited:
   set `dist[nr][nc] = dist[r][c] + 1`, mark it visited, and enqueue it.
3. When the queue empties, `dist` holds every nearest-zero distance.

```python
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist
```

- **Time:** O(m·n) — each cell is enqueued and dequeued exactly once.
- **Space:** O(m·n) for the distance matrix and queue.

## Key Insights & Edge Cases

- **Multi-source seeding is the whole idea:** enqueue *all* zeros first so a
  single BFS handles every query at once.
- **Use `dist == -1` (or a sentinel) as the visited flag** so you never revisit
  a cell and never overwrite a smaller distance.
- **Direction matters:** a naive single-pass "look up and left" DP is wrong; you
  need either two DP sweeps (down-right then up-left) or this BFS.
- **All-zero or all-one-with-one-zero inputs** are handled uniformly — the seed
  step just adds more or fewer starting cells.
