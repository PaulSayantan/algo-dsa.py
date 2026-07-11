# Rotting Oranges — Solution

## Brute Force

Simulate minute by minute with repeated full-grid scans: on each pass, find
every fresh orange adjacent to a rotten one and mark it to rot *after* the pass;
apply the changes; repeat until a pass changes nothing. Then check whether any
fresh orange remains.

- **Time:** `O((R * C) * T)` where `T` is the number of minutes (up to `R * C`),
  i.e. `O((R * C)^2)` worst case.
- **Space:** `O(R * C)` to buffer the cells rotting this pass.

Correct but repeatedly rescans cells that are already settled.

## Optimal Approach (Multi-source Grid BFS)

The rot spreads outward from *all* currently-rotten oranges simultaneously, one
ring per minute — this is exactly **multi-source BFS**, where the number of
minutes equals the BFS depth.

1. Scan the grid once: enqueue the coordinates of **every** rotten orange (these
   are the level-0 sources) and count the `fresh` oranges.
2. Run BFS in **level order**. For each minute, process all oranges currently in
   the queue; each rots its fresh neighbors, decrements `fresh`, marks them
   rotten (value `2`), and enqueues them for the next level.
3. Increment the minute counter for each level that actually rots something.
4. At the end, if `fresh == 0` return the elapsed minutes; otherwise return `-1`.

**Why it is correct:** BFS explores nodes in nondecreasing distance from the
source set. With multiple sources seeded at distance 0, the level at which a cell
is first dequeued equals the minimum number of "spread" steps from the nearest
initially-rotten orange — precisely the minute it rots. Any fresh orange never
reached by BFS is in a component with no rotten orange, so it can never rot →
`-1`.

### Step by step / reference implementation

```python
from collections import deque

def orangesRotting(grid):
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
        minutes += 1
        for _ in range(len(q)):          # process one whole level
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

    return minutes if fresh == 0 else -1
```

- **Time:** `O(R * C)` — one setup scan plus each cell enqueued/dequeued once.
- **Space:** `O(R * C)` — the queue in the worst case (grid full of rotten
  oranges at start).

## Key Insights & Edge Cases

- **Process one full BFS level per minute** using `for _ in range(len(q))`. This
  "level-size snapshot" is the crux — do not let next-level cells inflate the
  current minute.
- **No fresh oranges initially** → answer `0`, even if there are zero or many
  rotten ones. Handle this before the loop (or the loop naturally leaves
  `minutes = 0`).
- **Unreachable fresh orange** → `fresh > 0` after BFS drains → return `-1`.
- Guard the loop with `fresh > 0` so you do not add a spurious extra minute after
  the last orange rots.
- A single-source version is just this algorithm with one seed; multi-source is
  the natural generalization and costs nothing extra.
