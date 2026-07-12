# Jump Game III — Solution

## Optimal Approach

The indices form a graph where index `i` connects to `i + arr[i]` and
`i - arr[i]` (when in bounds). BFS from `start`, marking indices seen so each is
processed once; if any dequeued index holds a `0`, return `True`. If the queue
drains without hitting a zero, no zero is reachable, so return `False`. This runs
in `O(n)` time and space.

### Reference implementation

```python
class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        seen = {start}
        q = deque([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < n and nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        return False
```
