# Nearest Exit from Entrance in Maze — Solution

## Optimal Approach

Run a standard Lee-algorithm BFS from `entrance`, expanding to the 4 empty
neighbors. The first time BFS reaches an empty cell that lies on the border and
is not the entrance, the accumulated distance is the shortest number of steps.
Because BFS explores cells in non-decreasing distance order, that first border
hit is guaranteed minimal. If the queue empties without reaching a border, no
exit is reachable and the answer is `-1`. Runs in O(m × n).

### Reference implementation

```python
class Solution:
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        er, ec = entrance
        q = deque([(er, ec, 0)])
        seen = {(er, ec)}
        while q:
            r, c, d = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in seen:
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return d + 1
                    seen.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1
```
