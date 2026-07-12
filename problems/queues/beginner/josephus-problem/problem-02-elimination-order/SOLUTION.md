# Josephus Elimination Order — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def eliminationOrder(self, n, k):
        q = deque(range(1, n + 1))
        order = []
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            order.append(q.popleft())
        return order
```
