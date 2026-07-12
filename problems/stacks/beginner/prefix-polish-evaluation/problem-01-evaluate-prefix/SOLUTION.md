# Evaluate a Prefix Expression — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def evalPrefix(self, tokens):
        stack = []
        ops = {'+', '-', '*', '/'}
        for t in reversed(tokens):
            if t in ops:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[-1]
```
