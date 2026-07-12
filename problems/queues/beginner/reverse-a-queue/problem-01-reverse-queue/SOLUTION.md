# Reverse a Queue — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverse(self, q):
        stack = []
        for x in q:
            stack.append(x)
        out = []
        while stack:
            out.append(stack.pop())
        return out
```
