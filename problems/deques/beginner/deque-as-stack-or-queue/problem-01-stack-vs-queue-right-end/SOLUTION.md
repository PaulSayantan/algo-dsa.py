# Deque as Stack vs Queue (Right End) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def asStack(self, values):
        dq = deque()
        for v in values:
            dq.append(v)          # push onto the top (right end)
        out = []
        while dq:
            out.append(dq.pop())  # LIFO: pop from the same (right) end
        return out

    def asQueue(self, values):
        dq = deque()
        for v in values:
            dq.append(v)              # enqueue at the right end
        out = []
        while dq:
            out.append(dq.popleft())  # FIFO: dequeue from the opposite (left) end
        return out
```
