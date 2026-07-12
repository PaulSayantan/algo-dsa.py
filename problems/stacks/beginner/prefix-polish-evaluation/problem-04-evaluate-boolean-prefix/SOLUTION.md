# Evaluate a Boolean Prefix Expression — Solution

## Optimal Approach

Scan the expression right to left. Map operand `T` to `True` and `F` to `False`
and push them. On an operator pop the top two booleans and push `a & b` for `&`
or `a | b` for `|` (AND/OR are commutative, so operand order does not matter
here). The last value on the stack is the result.

- **Time:** `O(n)` — one pass over the characters.
- **Space:** `O(n)` for the stack.

### Reference implementation

```python
class Solution:
    def evalBoolPrefix(self, expr):
        stack = []
        for ch in reversed(expr):
            if ch == 'T':
                stack.append(True)
            elif ch == 'F':
                stack.append(False)
            else:  # ch is '&' or '|'
                a = stack.pop()
                b = stack.pop()
                stack.append(a and b if ch == '&' else a or b)
        return stack[-1]
```
