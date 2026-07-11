# Solution — Shortest Path in a Grid with Obstacles Elimination

## Brute Force

DFS/backtracking that tries every route, decrementing the elimination budget
whenever it steps onto an obstacle, and records the shortest arrival. Without
memoization the same `(cell, remaining)` state is re-explored along countless
paths.

- **Time:** Exponential in the number of cells.
- **Space:** O(m·n) recursion depth.

Even memoized DFS is fiddly here because the shortest path can revisit a cell
with a *different* remaining budget; plain BFS on `(row, col)` is simply wrong.

## Optimal Approach — Lee Algorithm over an Augmented State

The classic pitfall: a cell alone is not a complete BFS state. Arriving at a cell
with more eliminations left may unlock shorter continuations than arriving with
fewer. So the state must include the remaining budget: **`(row, col, k_left)`**.

Because every move still costs exactly 1, BFS over this augmented graph gives the
shortest step count — the Lee Algorithm applied to a 3-dimensional state space.

### Why it is correct

Each move has unit cost, so BFS over states expands in non-decreasing distance.
The first time a state `(m-1, n-1, *)` is dequeued, its step count is minimal.
We mark a state visited the first (hence shortest-distance) time we reach it;
revisiting the same `(row, col)` with an **equal or smaller** budget can never
help, so recording the *best remaining budget* seen per cell prunes the search
while preserving correctness.

### Step by step

1. **Early exit:** the shortest *possible* path length is `m + n - 2` (a
   monotone staircase). If `k >= m + n - 2`, you can always bulldoze straight
   through, so return `m + n - 2`.
2. State = `(row, col, k_remaining)`. Start at `(0, 0, k)` with distance `0`.
3. Track the best remaining budget seen at each cell in `seen[r][c]`; initialise
   the start.
4. BFS: pop `(r, c, rem)`. If `(r, c)` is the target, return its distance.
   For each 4-neighbour `(nr, nc)`:
   - Compute `nrem = rem - grid[nr][nc]` (spend one elimination on an obstacle).
   - If `nrem >= 0` and `nrem > seen[nr][nc]`, update `seen[nr][nc] = nrem` and
     enqueue `(nr, nc, nrem)` with `distance + 1`.
5. If the queue empties, return `-1`.

```python
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        # seen[r][c] = the largest remaining budget with which we've reached (r, c)
        seen = [[-1] * n for _ in range(m)]
        seen[0][0] = k
        q = deque([(0, 0, k, 0)])  # row, col, remaining, distance
        while q:
            r, c, rem, dist = q.popleft()
            if r == m - 1 and c == n - 1:
                return dist
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nrem = rem - grid[nr][nc]
                    if nrem > seen[nr][nc]:
                        seen[nr][nc] = nrem
                        q.append((nr, nc, nrem, dist + 1))
        return -1
```

- **Time:** O(m · n · k) — each `(cell, remaining)` state is processed once; the
  `seen`-budget pruning collapses many of them.
- **Space:** O(m · n) for `seen` plus the queue (O(m · n · k) in the worst case
  before pruning).

## Key Insights & Edge Cases

- **Budget belongs in the state:** BFS on `(row, col)` alone fails because two
  arrivals at the same cell with different remaining budgets are genuinely
  different situations.
- **Keep the best budget per cell** (`seen[r][c]`) rather than a plain visited
  flag — a later arrival with *more* eliminations left is worth exploring.
- **`k >= m + n - 2` shortcut** answers instantly and also bounds memory when
  `k` is large.
- **Manhattan lower bound:** no path is shorter than `m + n - 2`, useful for an
  optional A*/greedy-BFS optimisation.
- **Blocked target region:** if every route needs more than `k` eliminations,
  the queue drains and the answer is `-1` (as in Example 2).
