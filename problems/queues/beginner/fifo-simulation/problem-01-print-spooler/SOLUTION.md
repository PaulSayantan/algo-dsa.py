# Round-Robin Print Spooler — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def printOrder(self, jobs, quantum):
        q = deque([[jid, pages] for jid, pages in jobs])
        order = []
        while q:
            jid, pages = q.popleft()
            printed = min(quantum, pages)
            remaining = pages - printed
            if remaining > 0:
                q.append([jid, remaining])
            else:
                order.append(jid)
        return order
```
