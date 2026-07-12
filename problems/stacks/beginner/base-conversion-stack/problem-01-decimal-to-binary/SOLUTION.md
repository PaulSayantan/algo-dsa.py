# Decimal to Binary — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def toBinary(self, n):
        if n == 0:
            return '0'
        stack = []
        while n > 0:
            stack.append(n % 2)
            n //= 2
        out = []
        while stack:
            out.append(str(stack.pop()))
        return ''.join(out)
```
