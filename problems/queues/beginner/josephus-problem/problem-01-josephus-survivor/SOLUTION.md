# Josephus Survivor — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def josephus(self, n, k):
        q = deque(range(1, n + 1))
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q[0]
```
