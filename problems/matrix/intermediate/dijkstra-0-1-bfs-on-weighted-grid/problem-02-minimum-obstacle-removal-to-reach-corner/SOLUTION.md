# Solution — Minimum Obstacle Removal to Reach Corner

## Brute Force

Try every subset of obstacles to remove and test reachability with BFS, or DFS
over all paths tracking the count of obstacles crossed. Both blow up: there are
up to `2^(#obstacles)` subsets, and the number of grid paths is exponential.

- **Time:** Exponential.
- **Space:** O(m·n).

## Optimal Approach — 0-1 BFS

Model each move as a weighted edge: the weight of stepping into neighbour `nb`
is `grid[nb]` — `0` if `nb` is empty, `1` if `nb` is an obstacle you must
remove. We want the minimum-weight path from `(0,0)` to `(m-1,n-1)`. Since every
edge weight is `0` or `1`, this is the textbook case for **0-1 BFS**.

0-1 BFS is Dijkstra where the priority queue is replaced by a **double-ended
queue**. The deque stays sorted by distance if we always:

- push a **0-weight** relaxation to the **front** (same distance as current), and
- push a **1-weight** relaxation to the **back** (distance + 1).

This gives the same optimal answer as Dijkstra but in **O(m·n)** time — no `log`
factor — because each cell is finalized when first popped.

### Why it is correct

At any moment the deque holds cells with distances taking at most two values,
`d` at the front and `d+1` at the back (the "0-1 invariant"). Popping from the
front therefore always yields a minimum-distance unsettled cell, exactly as a
Dijkstra heap would. With non-negative weights, the first pop of a cell is
optimal.

### Step by step

1. `dist[0][0] = 0` (its edge weight in, if any, is already paid; the start is
   guaranteed empty), all others `= ∞`. Deque starts with `(0, 0)`.
2. Pop the **front** cell `(r, c)`. If it is the target, return `dist[r][c]`.
3. For each in-bounds neighbour `(nr, nc)`, weight `w = grid[nr][nc]`. If
   `dist[r][c] + w < dist[nr][nc]`, update it; push to the **front** if `w == 0`,
   else to the **back**.
4. Continue until the target is popped (guaranteed reachable since obstacles can
   always be removed).

```python
from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        while dq:
            r, c = dq.popleft()
            if r == m - 1 and c == n - 1:
                return dist[r][c]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    w = grid[nr][nc]
                    if dist[r][c] + w < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + w
                        if w == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        return dist[m - 1][n - 1]
```

- **Time:** O(m·n) — linear thanks to the deque.
- **Space:** O(m·n) for `dist` and the deque.

## Key Insights & Edge Cases

- **Weights are 0/1**, which is what makes the deque trick valid; if entering an
  obstacle could cost more than 1, you would fall back to a Dijkstra heap.
- **Front vs. back is the whole algorithm.** Pushing a 0-cost move to the back
  (or a 1-cost move to the front) breaks the sorted-deque invariant and yields
  wrong answers.
- Because we may relax a cell more than once, either guard with the `dist`
  comparison shown or skip a popped cell whose recorded distance improved after
  it was enqueued.
- A pure Dijkstra with a min-heap is also accepted and is easier to remember;
  0-1 BFS is the specialized, faster version worth recognizing.
- The corners are guaranteed empty, so the answer is `0` whenever an all-empty
  path already exists (Example 2).
