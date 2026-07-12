# Simulate Queue Operations — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def runOps(self, ops):
        q = []
        out = []
        for op in ops:
            if op[0] == "enqueue":
                q.append(op[1])
            elif op[0] == "dequeue":
                out.append(q.pop(0))
            elif op[0] == "front":
                out.append(q[0])
            elif op[0] == "empty":
                out.append(len(q) == 0)
        return out
```
