# Minimum Knight Moves — Solution

## Optimal Approach

Knight moves are symmetric across both axes, so first take `abs(x), abs(y)` to fold the
target into the first quadrant. Then run BFS from both `(0, 0)` and the target, expanding
the smaller frontier each round (swapping the two visited sets alongside the frontiers).
A light bounding box (a couple squares beyond the origin/target) keeps the infinite board
finite without cutting any optimal path. When a generated square is already in the opposite
search's frontier, the two meet and the accumulated distance is the answer.

### Reference implementation

```python
class Solution:
    def minKnightMoves(self, x, y):
        x, y = abs(x), abs(y)
        start, target = (0, 0), (x, y)
        if start == target:
            return 0
        moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                 (1, -2), (2, -1), (-1, -2), (-2, -1)]
        front, back = {start}, {target}
        visited_f, visited_b = {start}, {target}
        dist = 0
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                visited_f, visited_b = visited_b, visited_f
            dist += 1
            nxt = set()
            for cx, cy in front:
                for dx, dy in moves:
                    nb = (cx + dx, cy + dy)
                    if nb[0] < -2 or nb[1] < -2 or nb[0] > x + 2 or nb[1] > y + 2:
                        continue
                    if nb in back:
                        return dist
                    if nb not in visited_f:
                        visited_f.add(nb)
                        nxt.add(nb)
            front = nxt
        return -1
```
