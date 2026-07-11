# Rotting Oranges — Solution

## Brute Force

Simulate minute by minute. On each pass, scan the entire grid, find every fresh
orange adjacent to a rotten one, and mark them to rot **after** the scan finishes (to
avoid a fresh orange rotting and then infecting neighbors in the same minute). Repeat
until a full scan produces no new rot. Then check whether any fresh orange remains.

- **Time:** `O((m * n) * T)` where `T` is the number of minutes. In the worst case
  `T = O(m * n)`, giving `O((m * n)^2)`.
- **Space:** `O(m * n)` for the "to rot this minute" list (or `O(1)` extra if you use
  a sentinel value and re-scan, still costly in time).

The repeated full-grid scans re-examine cells that will never change again, which is
wasteful.

## Optimal Approach (Multi-Source BFS)

The rot spreads outward from **all** rotten oranges at the same time, one ring per
minute. That is precisely a breadth-first search seeded with multiple sources.

**Algorithm:**

1. Scan the grid once. Push every rotten orange `(r, c)` into a queue (these are the
   BFS sources at time 0). Count the number of `fresh` oranges.
2. If `fresh == 0`, return `0` immediately (nothing to rot).
3. Run BFS **level by level**. For each level (minute), pop every cell currently in
   the queue; for each fresh 4-neighbor, mark it rotten (set grid to `2`), decrement
   `fresh`, and enqueue it. After finishing a level in which at least one orange
   rotted, increment `minutes`.
4. When the queue empties, if `fresh == 0` return `minutes`, else return `-1`.

**Why it is correct:** BFS dequeues cells in non-decreasing distance order. Because
all sources start at distance `0`, the first time a fresh orange is reached is via the
shortest path from the *nearest* rotten orange — i.e. the earliest minute it can
possibly rot. Counting completed levels therefore yields the minute at which the last
orange rots. Any fresh orange in a component containing no rotten orange is never
enqueued, so `fresh` stays positive and we correctly return `-1`.

**Reference implementation:**

```python
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q and fresh > 0:
            for _ in range(len(q)):          # process exactly one minute's frontier
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
```

- **Time:** `O(m * n)` — each cell is enqueued and dequeued at most once.
- **Space:** `O(m * n)` for the queue in the worst case (whole grid rotten at start).

## Key Insights & Edge Cases

- **Seed all sources before expanding.** Enqueuing every rotten orange first is what
  makes the levels line up with minutes; if you searched from one orange at a time you
  would have to take a min over separate searches.
- **Level-by-level counting.** Use `for _ in range(len(q))` to drain exactly one
  minute's frontier per outer iteration. Only increment `minutes` for levels where the
  queue was non-empty at the start.
- **No fresh oranges:** return `0`, not `-1`. Guard this before the loop so an
  all-empty or all-rotten grid returns `0`.
- **Unreachable fresh oranges:** a fresh orange with no path to any rotten one leaves
  `fresh > 0` at the end → return `-1`.
- **Off-by-one guard:** incrementing `minutes` unconditionally inside the loop (even on
  a level where nothing new rots) can overcount. Gating on `fresh > 0` in the `while`
  condition avoids an extra phantom minute after the last orange rots.
