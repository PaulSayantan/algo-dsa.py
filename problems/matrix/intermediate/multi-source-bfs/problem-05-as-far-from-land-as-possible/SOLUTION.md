# As Far from Land as Possible — Solution

## Brute Force

For each water cell, compute its distance to the nearest land cell (by BFS or by
scanning all land cells and taking the minimum Manhattan distance), then take the
maximum of those nearest-land distances over all water cells.

- **Time:** `O((n^2)^2) = O(n^4)` — up to `n^2` water cells, each compared against up to
  `n^2` land cells (or a BFS of `O(n^2)`).
- **Space:** `O(n^2)`.

For `n = 100` this is up to `10^8` operations and needlessly repeats overlapping work.

## Optimal Approach (Multi-Source BFS)

We want `max over water cells of (distance to nearest land)`. Seed a single BFS with
**all land cells** at distance `0`. As the frontier expands ring by ring, each water
cell is first reached at exactly its nearest-land distance. The **deepest** ring — the
distance of the *last* cell filled — is the answer.

**Algorithm:**

1. Push **every land cell** into the queue and mark it visited. Count land cells.
2. If there are `0` land cells or `0` water cells, return `-1` (no meaningful pair).
3. BFS level by level. Track the current level number `dist`. Each time you expand from
   the current frontier into unvisited water cells, they belong to level `dist + 1`.
4. The maximum level at which any water cell is reached is the answer. Equivalently,
   store distances and return the max; or track `dist` as you drain each level and
   return the final `dist`.

**Why it is correct:** Multi-Source BFS labels every water cell with the shortest
distance to *some* land cell (the nearest one), because all land starts at `0` and BFS
processes cells in non-decreasing distance order. Taking the maximum over those
shortest distances directly answers "the water cell whose nearest land is farthest."
The last cell dequeued sits at the largest such distance.

**Reference implementation:**

```python
from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))          # seed every land cell

        # No land or all land (no water) -> no valid answer.
        if not q or len(q) == n * n:
            return -1

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dist = -1
        while q:
            dist += 1                          # completed one more ring
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1        # mark visited
                        q.append((nr, nc))
        return dist
```

- **Time:** `O(n^2)` — each cell enqueued and dequeued once.
- **Space:** `O(n^2)` for the queue in the worst case.

## Key Insights & Edge Cases

- **Max of nearest distances = deepest BFS ring.** Because BFS fills in
  non-decreasing distance order, the final level processed is the maximum nearest-land
  distance. No explicit distance grid is required if you just track the level counter.
- **Level counting detail:** initialize `dist = -1` and increment it once per ring
  *before* draining the frontier. Land cells occupy ring `0`; the last water ring gives
  the answer. (If you increment on empty expansions you can overcount — the loop
  naturally stops once no new water is added.)
- **Return `-1`** when the grid is all land or all water: with no water there is no cell
  to measure, and with no land there is no source. The check `not q or len(q) == n*n`
  covers both.
- **In-place visited marking:** reusing `grid[nr][nc] = 1` avoids a separate visited
  structure since land is also `1`.
- **Single land cell:** works fine; the farthest water corner yields the max Manhattan
  distance.
