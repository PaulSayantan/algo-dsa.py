# Score of Parentheses — Solution

## Optimal Approach

This is the calculator's context stack applied to a scoring rule. Keep a stack
whose top frame accumulates the score of the current depth. A `(` opens a deeper
context (push a fresh `0`); a `)` closes it, so pop the inner score `v` and fold
`max(2 * v, 1)` into the enclosing frame — the `max` encodes both base rules at
once (`()` scores 1 when `v == 0`, and `(A)` scores `2 * A` otherwise). The
bottom frame ends holding the total.

### Reference implementation

```python
class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[0]
```
