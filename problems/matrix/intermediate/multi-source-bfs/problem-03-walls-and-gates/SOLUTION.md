# Walls and Gates — Solution

## Brute Force

Run a separate BFS from **each empty room**, stopping at the first gate it reaches, and
write that distance back into the room. Walls block movement in every search.

- **Time:** `O((m * n)^2)` — up to `m * n` empty rooms, each launching a BFS over up to
  `m * n` cells.
- **Space:** `O(m * n)` for the per-room visited structure.

Because every room re-explores overlapping territory, this is far more work than
necessary on a 250 x 250 grid.

## Optimal Approach (Multi-Source BFS)

Flip the search direction: start from **all the gates at once**. Distances then radiate
outward, and the first time an empty room is popped it is reached via the shortest path
from the nearest gate.

**Algorithm:**

1. Enqueue **every gate** (`0`) as the initial multi-source frontier. Gates already
   hold their correct value, `0`.
2. Run BFS. Pop `(r, c)`; for each 4-neighbor `(nr, nc)` that is currently `INF` (an
   untouched empty room — walls are `-1` and already-labeled rooms are `< INF`), set
   `rooms[nr][nc] = rooms[r][c] + 1` and enqueue it.
3. Walls are never enqueued, so they are skipped automatically. Rooms with no path to
   a gate are never reached and keep `INF`.

**Why it is correct:** All gates begin at distance `0`, so BFS visits cells in
non-decreasing distance order. The first assignment to a room is thus its true minimum
distance to any gate, and the `== INF` guard prevents any later, longer path from
overwriting it. Walls act as impassable cells because they never satisfy the `== INF`
condition and are never enqueued.

**Reference implementation:**

```python
from collections import deque
from typing import List

INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return
        rows, cols = len(rooms), len(rooms[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))          # seed every gate

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
```

- **Time:** `O(m * n)` — each room enqueued and dequeued at most once.
- **Space:** `O(m * n)` for the queue in the worst case.

## Key Insights & Edge Cases

- **BFS from gates, not rooms.** This single reversal collapses one search per room
  into one search total.
- **The `== INF` test doubles as the visited check.** Since gates are `0` and walls are
  `-1`, only untouched empty rooms equal `INF`; once written they no longer match, so
  they are not revisited.
- **Walls need no special handling** beyond the `== INF` guard — they simply never
  qualify to be enqueued.
- **No gates:** the queue starts empty, the loop never runs, and every `INF` stays
  `INF` (correct).
- **Unreachable rooms** (walled off from all gates) correctly keep `INF`.
- **In-place mutation:** the function returns `None`; write results back into `rooms`.
