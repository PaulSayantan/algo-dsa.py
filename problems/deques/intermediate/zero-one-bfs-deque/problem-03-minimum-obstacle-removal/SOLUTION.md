# Minimum Obstacle Removal to Reach Corner — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        while dq:
            r, c = dq.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    w = grid[nr][nc]  # cost to enter the neighbor: 0 or 1
                    nd = dist[r][c] + w
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if w == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        return dist[m - 1][n - 1]
```

### Complexity

O(m*n) time and space — each cell is finalized once.

## Key Insights & Edge Cases

The cost of a move depends only on the cell you enter, so the edge weight is exactly `grid[nr][nc]`, which is always in `{0, 1}` — the classic 0-1 BFS setup. The start cell is free even if it were an obstacle (you begin there), and a 1x1 grid needs zero removals. Because entering empty cells costs nothing, they are pushed to the front and explored at the current distance level before any obstacle-entering move is considered.
