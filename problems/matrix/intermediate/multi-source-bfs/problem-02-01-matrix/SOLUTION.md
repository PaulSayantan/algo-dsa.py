# 01 Matrix — Solution

## Brute Force

For each cell containing `1`, run an independent BFS until it hits the first `0`, and
record that distance. (A dynamic-programming double sweep also works, but the naive
per-cell search is the direct brute force.)

- **Time:** `O((m * n)^2)` in the worst case — up to `m * n` cells each triggering a
  BFS that can touch `O(m * n)` cells.
- **Space:** `O(m * n)` per BFS for the visited set.

Running one search per `1` repeats enormous amounts of work; neighboring `1`s explore
almost the same region.

## Optimal Approach (Multi-Source BFS)

Invert the direction of the search. Instead of asking each `1` "where is the closest
`0`?", start from **all** the `0`s at once and let distances propagate outward. When a
`1` is dequeued for the first time, it is being reached along a shortest path from the
nearest `0`.

**Algorithm:**

1. Create a `dist` matrix. Set `dist[r][c] = 0` for every `0` and mark those cells
   visited; set every `1` to "unvisited" (e.g. `-1` or `+inf`).
2. Enqueue **all** the `0` cells as the initial multi-source frontier.
3. Standard BFS: pop `(r, c)`; for each unvisited 4-neighbor `(nr, nc)`, set
   `dist[nr][nc] = dist[r][c] + 1`, mark visited, and enqueue it.
4. Return `dist`.

**Why it is correct:** With all zeros at distance `0` in the queue, BFS processes
cells in non-decreasing distance order (the "virtual super-source connected to every
`0`" view). The first relaxation of any `1` is therefore optimal, and because each
cell is marked visited when first reached it is never overwritten by a longer path.
Since the problem guarantees at least one `0`, every `1` is reachable.

**Reference implementation:**

```python
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))          # seed every zero

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist
```

- **Time:** `O(m * n)` — each cell enqueued and dequeued once.
- **Space:** `O(m * n)` for `dist` and the queue.

## Key Insights & Edge Cases

- **Reverse the search.** The key trick is to BFS *from the targets* (`0`s) rather than
  *toward the targets*. This turns `k` searches into one.
- **Use the distance array as the visited marker.** Initializing `1`s to `-1` lets a
  single `== -1` check serve as "not yet reached," avoiding a separate visited set.
- **Level counting is unnecessary here.** Because we store the actual distance in
  `dist[r][c] = dist[r][c] + 1`, we do not need to track BFS levels explicitly.
- **At least one `0` is guaranteed,** so there is no unreachable case; but if the
  guarantee were dropped, unreachable `1`s would keep their sentinel value.
- **All zeros:** the output equals the input (every distance is `0`); the loop simply
  never relaxes anything.
