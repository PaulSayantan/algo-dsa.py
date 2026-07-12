# Open the Lock — Solution

## Optimal Approach

Treat each 4-digit combination as a node in an implicit graph. From any state, the
eight neighbors turn one of the four wheels up or down by one slot (with `9`/`0`
wrap-around). BFS from `"0000"` finds the fewest moves to `target`; a `visited` set
plus the `deadends` set keep us off forbidden or repeated states. Guard the start:
if `"0000"` is itself a deadend the lock is jammed.

### Reference implementation

```python
class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            state, turns = q.popleft()
            for i in range(4):
                d = int(state[i])
                for nd in ((d + 1) % 10, (d - 1) % 10):
                    nxt = state[:i] + str(nd) + state[i + 1:]
                    if nxt in dead or nxt in seen:
                        continue
                    if nxt == target:
                        return turns + 1
                    seen.add(nxt)
                    q.append((nxt, turns + 1))
        return -1
```
