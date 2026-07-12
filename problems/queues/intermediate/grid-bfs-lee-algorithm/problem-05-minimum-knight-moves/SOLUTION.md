# Minimum Knight Moves — Solution

## Optimal Approach

Every knight move has the same cost, so a breadth-first search from `(0, 0)`
finds the fewest moves — the same Lee shortest-path idea, just on an infinite
board with the 8 knight offsets as the neighborhood. Two tricks keep it finite
and fast: fold the target into the first quadrant via `x, y = abs(x), abs(y)`
(the move set is symmetric), and bound the frontier to `[-2, x + 2] × [-2, y + 2]`
so the search cannot wander arbitrarily far from the target. The first time BFS
dequeues `(x, y)`, its distance is the answer.

### Reference implementation

```python
class Solution:
    def minKnightMoves(self, x, y):
        x, y = abs(x), abs(y)
        moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
        q = deque([(0, 0, 0)])
        seen = {(0, 0)}
        while q:
            r, c, d = q.popleft()
            if (r, c) == (x, y):
                return d
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if -2 <= nr <= x + 2 and -2 <= nc <= y + 2 and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1
```
