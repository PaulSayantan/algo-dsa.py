# Open the Lock — Solution

## Optimal Approach

Each 4-digit state is a node; from a state you can turn any one of the 4 wheels
up or down, giving 8 neighbors. Every move has cost one, so the fewest moves to
reach `target` is the BFS shortest-path length from `"0000"`. Seed a `visited`
set with the deadends so those states are never expanded, and short-circuit if
`"0000"` itself is a deadend. BFS layer by layer; the layer at which `target`
first appears is the answer, and exhausting the queue without finding it means
`-1`. There are at most `10^4` states, so this is O(10^4) time.

### Reference implementation

```python
class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        def neighbors(state):
            for i in range(4):
                d = int(state[i])
                for nd in ((d + 1) % 10, (d - 1) % 10):
                    yield state[:i] + str(nd) + state[i + 1:]

        visited = {"0000"}
        q = deque([("0000", 0)])
        while q:
            state, steps = q.popleft()
            for nb in neighbors(state):
                if nb in visited or nb in dead:
                    continue
                if nb == target:
                    return steps + 1
                visited.add(nb)
                q.append((nb, steps + 1))
        return -1
```
