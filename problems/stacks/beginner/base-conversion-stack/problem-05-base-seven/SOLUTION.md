# Base 7 — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return '0'
        negative = num < 0
        n = abs(num)
        stack = []
        while n > 0:
            stack.append(str(n % 7))
            n //= 7
        digits = ''.join(reversed(stack))
        return '-' + digits if negative else digits
```
