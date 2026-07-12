# Baseball Game — Solution

## Optimal Approach

The record behaves exactly like a stack. Walk the operations left to right:

- `"C"` is an **undo** — pop the most recent score off the stack.
- `"D"` pushes double the current top.
- `"+"` pushes the sum of the top two scores.
- otherwise the token is an integer — push it.

Because every score derived by `"D"`/`"+"` and every `"C"` only ever touches the
top of the stack, LIFO ordering keeps "the previous score(s)" correct. Sum the
stack at the end.

### Reference implementation

```python
class Solution:
    def calPoints(self, operations):
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
```
