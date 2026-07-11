# Solution — Rotting Oranges

## Brute Force

Simulate minute by minute with repeated full-grid scans: each minute, scan the
whole grid, collect fresh oranges adjacent to a rotten one, rot them all, and
repeat until a scan produces no change.

- **Time:** O((m·n) · T) where `T` is the number of minutes (up to O(m·n)),
  giving O((m·n)²) in the worst case.
- **Space:** O(m·n).

It works but re-scans the entire grid every minute.

## Optimal Approach — Multi-Source Level-by-Level Lee Algorithm (BFS)

Rot spreads in synchronized rings: all oranges one step from a rotten source rot
at minute 1, all oranges two steps away rot at minute 2, and so on. Those rings
are exactly BFS levels. Seed the queue with **every** initially rotten orange and
process the queue **one full level per minute**.

### Why it is correct

A fresh orange rots at time equal to its BFS distance to the *nearest* rotten
source. Seeding all rotten oranges at level 0 is a multi-source BFS from a
virtual super-source, so each fresh orange is reached at its minimum distance —
i.e. the earliest minute it could rot. The answer is the largest such distance,
which equals the number of BFS levels (minus the initial level 0).

### Step by step

1. Scan the grid: push every rotten orange `(2)` into the queue and count the
   fresh oranges `(1)`.
2. If `fresh == 0`, return `0` (nothing to rot).
3. `minutes = 0`. While the queue is non-empty **and** `fresh > 0`:
   - Process the entire current level (loop `len(queue)` times).
   - For each popped rotten orange, rot each fresh 4-neighbour: mark it `2`,
     decrement `fresh`, and enqueue it.
   - After finishing the level, `minutes += 1`.
4. Return `minutes` if `fresh == 0`, else `-1` (some orange was unreachable).

```python
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
```

- **Time:** O(m·n) — every cell is enqueued at most once.
- **Space:** O(m·n) for the queue.

## Key Insights & Edge Cases

- **Level-by-level counting:** advance `minutes` once per BFS level, not once per
  dequeued orange. Snapshot `len(q)` before the inner loop.
- **Count fresh oranges** so you can detect unreachable ones (`fresh > 0` at the
  end → `-1`) and short-circuit when done.
- **No fresh oranges initially → answer is 0**, even if there are zero rotten
  oranges.
- **Do not add an extra minute** for the final empty level; guarding the loop
  with `and fresh` prevents an off-by-one over-count.
