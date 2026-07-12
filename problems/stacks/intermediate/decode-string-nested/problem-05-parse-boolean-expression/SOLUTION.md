# Parse Boolean Expression — Solution

## Optimal Approach

Walk the string pushing every non-comma character onto a stack. When a `)`
arrives, the current bracket frame is complete: pop operands (`t`/`f`) until the
matching `(`, discard the `(`, then read the operator sitting just beneath it.
Apply `!` / `&` / `|` to the collected operands and push the single-character
result (`t` or `f`) back so an enclosing frame can consume it. This is the same
open-frame / close-and-fold two-stack rhythm as nested string decoding, folding
booleans instead of substrings.

### Reference implementation

```python
class Solution:
    def parseBoolExpr(self, expression):
        stack = []
        for ch in expression:
            if ch == ',':
                continue
            if ch != ')':
                stack.append(ch)
                continue
            operands = []
            while stack[-1] != '(':
                operands.append(stack.pop())
            stack.pop()          # '('
            op = stack.pop()     # operator: ! & |
            if op == '!':
                res = 'f' if operands[0] == 't' else 't'
            elif op == '&':
                res = 't' if all(o == 't' for o in operands) else 'f'
            else:  # '|'
                res = 't' if any(o == 't' for o in operands) else 'f'
            stack.append(res)
        return stack[-1] == 't'
```
