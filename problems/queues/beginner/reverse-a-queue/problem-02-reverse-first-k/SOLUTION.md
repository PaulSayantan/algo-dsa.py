# Reverse First K Elements of a Queue — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverseFirstK(self, q, k):
        stack = []
        for i in range(k):
            stack.append(q[i])
        out = []
        while stack:
            out.append(stack.pop())
        for i in range(k, len(q)):
            out.append(q[i])
        return out
```
