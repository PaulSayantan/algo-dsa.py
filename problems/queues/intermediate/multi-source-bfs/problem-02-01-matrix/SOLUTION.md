# 01 Matrix — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist
```
