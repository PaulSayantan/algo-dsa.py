# Postfix to Prefix Conversion — Solution

## Optimal Approach

Same left-to-right stack sweep as RPN evaluation, but the stack holds partial
**prefix strings** instead of numbers. An operand is pushed unchanged. On an
operator, pop the top (right operand `b`) and the next (left operand `a`) and
push `op + a + b` — the operator goes in front, matching prefix (Polish) form.
Popping `b` before `a` keeps the operands in their original order. The final
stack entry is the complete prefix expression. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def postfixToPrefix(self, expression):
        ops = {'+', '-', '*', '/'}
        stack = []
        for ch in expression:
            if ch in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ch + a + b)
            else:
                stack.append(ch)
        return stack[-1]
```
