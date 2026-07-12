# Reverse Digits of an Integer via Stack — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverseDigits(self, n):
        stack = list(str(n))
        out = []
        while stack:
            out.append(stack.pop())
        return int(''.join(out))
```
