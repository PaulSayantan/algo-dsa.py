# Generate All Binary Strings of Length N — Solution

## Optimal Approach

Treat the queue as a BFS frontier over prefixes. Seed it with the empty string. Each dequeued prefix is either complete (length `n`, so record it) or extended by appending `"0"` and `"1"` and re-enqueued. Enqueuing `"0"` before `"1"` keeps the finished strings in ascending order.

### Reference implementation

```python
class Solution:
    def binaryStrings(self, n):
        q = deque([""])
        out = []
        while q:
            s = q.popleft()
            if len(s) == n:
                out.append(s)
            else:
                q.append(s + "0")
                q.append(s + "1")
        return out
```
