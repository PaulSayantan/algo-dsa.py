# Convert a Number to Hexadecimal — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def toHex(self, num):
        if num == 0:
            return '0'
        digits = '0123456789abcdef'
        num &= 0xffffffff
        stack = []
        while num > 0:
            stack.append(digits[num % 16])
            num //= 16
        return ''.join(reversed(stack))
```
