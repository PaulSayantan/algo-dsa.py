# Reverse Last K Elements of a Queue — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverseLastK(self, q, k):
        n = len(q)
        out = []
        for i in range(n - k):
            out.append(q[i])
        stack = []
        for i in range(n - k, n):
            stack.append(q[i])
        while stack:
            out.append(stack.pop())
        return out
```
