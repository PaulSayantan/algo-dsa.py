# Postfix to Infix Conversion — Solution

## Optimal Approach

This is the same stack sweep as evaluating RPN, except the stack holds infix
**strings** rather than numbers. Scan left to right: an operand is pushed as-is;
an operator pops the top two partial expressions (the top is the right operand
`b`, the next is the left operand `a`) and pushes the combined string
`"(" + a + op + b + ")"`. Because operands come off the stack in reverse order,
popping `b` before `a` preserves the original operand order. After one pass the
single remaining stack entry is the full infix expression. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def postfixToInfix(self, expression):
        ops = {'+', '-', '*', '/'}
        stack = []
        for ch in expression:
            if ch in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append('(' + a + ch + b + ')')
            else:
                stack.append(ch)
        return stack[-1]
```
