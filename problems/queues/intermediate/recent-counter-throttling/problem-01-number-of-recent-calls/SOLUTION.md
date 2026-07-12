# Number of Recent Calls — Solution

## Optimal Approach

### Reference implementation

```python
class RecentCounter:
    def __init__(self):
        self._q = deque()

    def ping(self, t):
        self._q.append(t)
        while self._q[0] < t - 3000:
            self._q.popleft()
        return len(self._q)
```
