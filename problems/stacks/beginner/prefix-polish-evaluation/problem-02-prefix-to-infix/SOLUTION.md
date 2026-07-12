# Prefix to Infix Conversion — Solution

## Optimal Approach

Scan right to left. Push each operand. On an operator, pop the top two values
(the first popped is the left operand, the second is the right operand), wrap
them as `(left op right)`, and push the combined string back. After consuming
every token exactly one string remains — the infix expression.

- **Time:** `O(n)` — one pass, each token pushed/popped a constant number of times.
- **Space:** `O(n)` for the stack.

### Reference implementation

```python
class Solution:
    def prefixToInfix(self, expr):
        ops = set('+-*/')
        stack = []
        for ch in reversed(expr):
            if ch in ops:
                a = stack.pop()   # left operand
                b = stack.pop()   # right operand
                stack.append('(' + a + ch + b + ')')
            else:
                stack.append(ch)
        return stack[-1]
```
