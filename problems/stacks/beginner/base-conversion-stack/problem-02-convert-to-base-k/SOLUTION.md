# Convert to Base K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def toBaseK(self, n, k):
        digits = '0123456789abcdef'
        if n == 0:
            return '0'
        stack = []
        while n > 0:
            stack.append(digits[n % k])
            n //= k
        return ''.join(reversed(stack))
```
