# Binary Numbers in a Range — Solution

## Optimal Approach

The queue generation emits the binary form of the integer `i` on its `i`-th dequeue. So run the generation `high` times, ignore the first `low - 1` results, and collect the rest. Each dequeue still enqueues both children (`s + "0"`, `s + "1"`) so the level-order sequence stays intact even while we skip the early positions.

### Reference implementation

```python
class Solution:
    def binaryRange(self, low, high):
        q = deque(["1"])
        out = []
        for i in range(1, high + 1):
            s = q.popleft()
            if i >= low:
                out.append(s)
            q.append(s + "0")
            q.append(s + "1")
        return out
```
