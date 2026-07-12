# Minimum Remove to Make Valid Parentheses — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minRemoveToMakeValid(self, s):
        chars = list(s)
        stack = []
        for i, c in enumerate(chars):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''
        for i in stack:
            chars[i] = ''
        return ''.join(chars)
```
