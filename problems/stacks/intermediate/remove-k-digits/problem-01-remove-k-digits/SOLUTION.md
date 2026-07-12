# Remove K Digits — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def removeKdigits(self, num, k):
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
```
