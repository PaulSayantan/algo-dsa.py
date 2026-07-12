# Open the Lock — Solution

## Optimal Approach

Model each 4-digit state as a node. From any state you can turn one of the four
wheels up or down, giving 8 neighbors. BFS from `'0000'` finds the fewest moves
to `target`; deadends (and already-seen states) are never enqueued. Guard the
start itself being a deadend up front.

### Reference implementation

```python
class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        seen = {"0000"}
        q = deque([("0000", 0)])
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            for i in range(4):
                d = int(state[i])
                for nd in ((d + 1) % 10, (d - 1) % 10):
                    nxt = state[:i] + str(nd) + state[i + 1:]
                    if nxt not in seen and nxt not in dead:
                        seen.add(nxt)
                        q.append((nxt, turns + 1))
        return -1
```
