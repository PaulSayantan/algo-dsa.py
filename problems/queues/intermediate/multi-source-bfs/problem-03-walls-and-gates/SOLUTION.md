# Walls and Gates — Solution

## Optimal Approach

Enqueue every gate at distance 0 and run a single BFS from all of them at once.
Because BFS expands in distance-ordered waves, the first time a room is popped
into it is guaranteed to be via its nearest gate. Rooms never reached stay `INF`.

### Reference implementation

```python
class Solution:
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return rooms
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
        return rooms
```
