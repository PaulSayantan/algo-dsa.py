# Evaluate Boolean Postfix Expression — Solution

## Optimal Approach

Identical to numeric RPN evaluation, but the stack holds booleans and the
operators are logical. Scan left to right: push `True` for `T` and `False` for
`F`. The binary operators `&` and `|` pop the top two operands and push their
AND / OR. The unary `!` is the one twist — it pops a **single** operand and
pushes its negation. After one pass the lone remaining stack entry is the
answer. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def evalBoolPostfix(self, tokens):
        stack = []
        for ch in tokens:
            if ch == 'T':
                stack.append(True)
            elif ch == 'F':
                stack.append(False)
            elif ch == '!':
                stack.append(not stack.pop())
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a and b if ch == '&' else a or b)
        return stack[-1]
```
