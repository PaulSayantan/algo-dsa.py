# Map of Highest Peak — Solution

## Brute Force

For each land cell, run an independent BFS to find its distance to the nearest water
cell, and use that distance as the cell's height.

- **Time:** `O((m * n)^2)` — up to `m * n` land cells, each triggering a BFS over up to
  `m * n` cells.
- **Space:** `O(m * n)` per search for visited bookkeeping.

On a `1000 x 1000` grid (`10^6` cells) this is hopeless — `10^12` operations.

## Optimal Approach (Multi-Source BFS)

**Key reduction:** The rules force `height(water) = 0` and `|height(a) - height(b)| <= 1`
for adjacent `a, b`. Walking any path from a cell to the nearest water cell, the height
can drop by at most 1 per step, so a cell `d` steps from water can be **at most** `d`.
Setting each cell's height to *exactly* its distance to the nearest water cell both
satisfies all constraints (adjacent BFS distances differ by at most 1) and attains that
per-cell upper bound simultaneously, so it maximizes the global maximum. Computing
"distance to nearest water for every cell" is exactly Multi-Source BFS seeded from the
water cells — structurally identical to *01 Matrix*.

**Algorithm:**

1. Initialize `height` to `-1` everywhere (unvisited marker).
2. For every water cell, set `height = 0` and enqueue it (the multi-source frontier).
3. BFS: pop `(r, c)`; for each unvisited (`-1`) 4-neighbor, set its height to
   `height[r][c] + 1`, mark it, and enqueue it.
4. Return `height`.

**Why it is correct:** Because all water cells start at `0`, BFS assigns each cell its
true shortest distance to water. That assignment respects the adjacency constraint
(neighbors in a BFS tree differ by exactly 1; other neighbors differ by at most 1) and
matches the proven per-cell maximum, so no other valid assignment can produce a taller
peak.

**Reference implementation:**

```python
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    q.append((r, c))          # seed every water cell

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))

        return height
```

- **Time:** `O(m * n)` — each cell enqueued and dequeued once.
- **Space:** `O(m * n)` for `height` and the queue.

## Key Insights & Edge Cases

- **Recognize the reduction.** The "adjacent differ by at most 1, water is 0, maximize
  the max" phrasing is a disguised "distance to nearest source" problem — the same core
  as *01 Matrix*.
- **Multiple valid answers.** Any assignment achieving the maximum peak is accepted; the
  distance-to-nearest-water assignment is one canonical optimum.
- **At least one water cell** is guaranteed, so the queue is non-empty and every cell is
  reachable — no `-1` survives in the output.
- **All water:** every cell is a source at height `0`; the output is all zeros.
- **Use `height` itself as the visited marker** (`-1`) to avoid a separate visited set.
