# Reverse a String Using a Stack — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverse(self, s):
        stack = list(s)
        out = []
        while stack:
            out.append(stack.pop())
        return ''.join(out)
```
