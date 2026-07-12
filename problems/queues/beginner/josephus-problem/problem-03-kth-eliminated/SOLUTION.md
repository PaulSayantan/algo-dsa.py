# Josephus K-th Eliminated — Solution

## Optimal Approach

Simulate the circle with a queue. Rotate the front `k-1` people to the back
(they are skipped), then dequeue the `k`-th (eliminated) and record it. The
`m`-th recorded value is the answer.

### Reference implementation

```python
class Solution:
    def kthEliminated(self, n, k, m):
        q = deque(range(1, n + 1))
        order = []
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            order.append(q.popleft())
        return order[m - 1]
```
