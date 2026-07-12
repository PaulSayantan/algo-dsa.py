# Prefix to Postfix Conversion — Solution

## Optimal Approach

Scan right to left. Push each operand. On an operator, pop the top two values
(the first popped is the left operand, the second is the right operand) and push
the concatenation `left + right + op` — the operator trails both operands, which
is exactly postfix order. One string remains at the end.

- **Time:** `O(n)` — a single pass over the tokens.
- **Space:** `O(n)` for the stack.

### Reference implementation

```python
class Solution:
    def prefixToPostfix(self, expr):
        ops = set('+-*/')
        stack = []
        for ch in reversed(expr):
            if ch in ops:
                a = stack.pop()   # left operand
                b = stack.pop()   # right operand
                stack.append(a + b + ch)
            else:
                stack.append(ch)
        return stack[-1]
```
