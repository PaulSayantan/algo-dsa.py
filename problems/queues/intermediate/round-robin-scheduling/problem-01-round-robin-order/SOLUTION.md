# Round-Robin Completion Order — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def completionOrder(self, burst, quantum):
        q = deque((i, b) for i, b in enumerate(burst))
        order = []
        while q:
            pid, remaining = q.popleft()
            run = min(quantum, remaining)
            remaining -= run
            if remaining > 0:
                q.append((pid, remaining))
            else:
                order.append(pid)
        return order
```
