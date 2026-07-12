# Minimum Cost to Make at Least One Valid Path in a Grid — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        # 1..4 -> right, left, down, up (matches LC 1368 arrow encoding)
        moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        while dq:
            r, c = dq.popleft()
            for d, (dr, dc) in moves.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    w = 0 if grid[r][c] == d else 1
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

O(m*n) time and space.
