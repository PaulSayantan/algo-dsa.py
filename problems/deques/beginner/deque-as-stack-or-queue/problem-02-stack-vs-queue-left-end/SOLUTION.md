# Deque as Stack vs Queue (Left End) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def leftEndStack(self, values):
        dq = deque()
        for v in values:
            dq.appendleft(v)          # push onto the left end
        out = []
        while dq:
            out.append(dq.popleft())  # LIFO: pop from the same (left) end
        return out

    def frontToBackQueue(self, values):
        dq = deque()
        for v in values:
            dq.appendleft(v)      # enqueue at the left end
        out = []
        while dq:
            out.append(dq.pop())  # FIFO: dequeue from the opposite (right) end
        return out
```
