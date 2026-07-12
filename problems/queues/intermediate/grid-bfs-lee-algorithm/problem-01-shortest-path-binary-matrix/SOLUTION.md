# Shortest Path in Binary Matrix — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        q = deque([(0, 0, 1)])
        seen = {(0, 0)}
        while q:
            r, c, d = q.popleft()
            if r == n - 1 and c == n - 1:
                return d
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc, d + 1))
        return -1
```
