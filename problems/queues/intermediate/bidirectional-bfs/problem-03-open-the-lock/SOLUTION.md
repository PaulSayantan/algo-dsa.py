# Open the Lock — Solution

## Optimal Approach

Treat every 4-digit state as a graph node with 8 neighbors (each of 4 wheels turned up or
down, digits wrapping mod 10). Run BFS from `"0000"` and `target` at once, expanding the
smaller frontier each round. Guard against deadends up front (if `"0000"` or `target` is a
deadend the answer is `-1`) and never expand into a deadend or an already-seen state. When a
neighbor appears in the opposite frontier, the two searches have met and the current round
count is the shortest distance.

### Reference implementation

```python
class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead or target in dead:
            return -1
        if target == "0000":
            return 0
        front, back = {"0000"}, {target}
        visited = {"0000", target}
        turns = 0

        def neighbors(node):
            res = []
            for i in range(4):
                d = int(node[i])
                for nd in ((d + 1) % 10, (d - 1) % 10):
                    res.append(node[:i] + str(nd) + node[i + 1:])
            return res

        while front and back:
            if len(front) > len(back):
                front, back = back, front
            turns += 1
            nxt = set()
            for node in front:
                for nb in neighbors(node):
                    if nb in back:
                        return turns
                    if nb not in dead and nb not in visited:
                        visited.add(nb)
                        nxt.add(nb)
            front = nxt
        return -1
```
