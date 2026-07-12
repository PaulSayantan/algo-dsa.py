# Minimum Jumps to Reach Home — Solution

## Optimal Approach

Treat the number line as an implicit board graph. A plain "position" is not enough
state, because whether a backward jump is legal depends on how you arrived: you may
not jump backward twice in a row. So a node is the pair `(position, came_by_backward)`.

From `(0, False)` run BFS. Every edge (a jump) has unit cost, so the first time BFS
reaches any state with `position == x` it has used the fewest jumps.

Transitions from `(pos, backed)`:

- Forward `pos + a` is always allowed (it lands with `backed = False`).
- Backward `pos - b` is only allowed when `backed` is `False` (it lands with
  `backed = True`), and only when `pos - b >= 0`.

A jump is valid only if the target square is not forbidden and not negative. The
board is unbounded forward, but forward exploration must be capped or BFS never
terminates. A safe cap is `max(x, max(forbidden)) + a + b`: any home reachable at
all is reachable without ever exceeding it, because going further only to come back
never helps beyond one backward step past the furthest relevant square.

Mark states seen on enqueue so each `(position, backed)` is expanded once. If the
queue empties without reaching `x`, return `-1`.

### Reference implementation

```python
class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        blocked = set(forbidden)
        limit = max([x] + list(forbidden)) + a + b
        start = (0, 0)  # (position, came_by_backward flag)
        seen = {start}
        q = deque([start])
        steps = 0
        while q:
            for _ in range(len(q)):
                pos, backed = q.popleft()
                if pos == x:
                    return steps
                nxt = pos + a
                if nxt <= limit and nxt not in blocked and (nxt, 0) not in seen:
                    seen.add((nxt, 0))
                    q.append((nxt, 0))
                if not backed:
                    prev = pos - b
                    if prev >= 0 and prev not in blocked and (prev, 1) not in seen:
                        seen.add((prev, 1))
                        q.append((prev, 1))
            steps += 1
        return -1
```
