# Reverse a Queue in Groups of K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverseInGroups(self, q, k):
        out = []
        n = len(q)
        for start in range(0, n, k):
            stack = []
            for i in range(start, min(start + k, n)):
                stack.append(q[i])
            while stack:
                out.append(stack.pop())
        return out
```
