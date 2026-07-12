# Valid Parentheses — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isValid(self, s):
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in match:
                if not stack or stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)
        return not stack
```
