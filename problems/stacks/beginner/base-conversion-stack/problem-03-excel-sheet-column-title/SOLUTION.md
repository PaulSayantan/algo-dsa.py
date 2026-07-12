# Excel Sheet Column Title — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def convertToTitle(self, columnNumber):
        stack = []
        while columnNumber > 0:
            columnNumber -= 1
            stack.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(stack))
```
