# Backspace String Compare — Solution

## Optimal Approach

Type each string into a stack: append a letter, and on a `'#'` pop the top if
the stack is non-empty (a backspace on empty text is a no-op). The two typed
results are equal exactly when the stacks match.

### Reference implementation

```python
class Solution:
    def backspaceCompare(self, s, t):
        def typed(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        return typed(s) == typed(t)
```
