# Evaluate Reverse Polish Notation — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
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
