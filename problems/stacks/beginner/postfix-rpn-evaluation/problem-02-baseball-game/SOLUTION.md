# Baseball Game — Solution

## Optimal Approach

The record behaves exactly like the stack used to evaluate a postfix stream: an
integer is an operand to push, while `+`, `D`, and `C` are operators that combine
or discard the top-of-stack scores in one left-to-right pass. Push `int(op)` for
numbers; for `+` push the sum of the top two, for `D` push double the top, and for
`C` pop the top. The answer is the sum of whatever remains. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def calPoints(self, operations):
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
```
