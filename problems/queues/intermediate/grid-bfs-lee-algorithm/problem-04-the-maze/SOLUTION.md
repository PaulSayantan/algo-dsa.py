# The Maze — Solution

## Optimal Approach

Model the maze as a graph whose nodes are *stopping cells*. From any cell, for
each of the four directions, keep sliding while the next cell is in bounds and
empty; the last cell before a wall is where the ball stops. Run BFS from
`start`, enqueuing each newly reached stopping cell (tracked in a `seen` set to
avoid revisits). If the ball ever stops on `destination`, return `True`;
if the queue drains first, return `False`. Each cell is enqueued at most once,
so the work is O(m × n × max(m, n)) including the rolls.

### Reference implementation

```python
class Solution:
    def hasPath(self, maze, start, destination):
        rows, cols = len(maze), len(maze[0])
        start, dest = tuple(start), tuple(destination)
        q = deque([start])
        seen = {start}
        while q:
            r, c = q.popleft()
            if (r, c) == dest:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r, c
                while 0 <= nr + dr < rows and 0 <= nc + dc < cols and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))
        return False
```
