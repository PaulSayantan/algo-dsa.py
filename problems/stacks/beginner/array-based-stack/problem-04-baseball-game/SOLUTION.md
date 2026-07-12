# Baseball Game — Solution

## Optimal Approach

Walk the operations, keeping a stack of the currently-valid scores. `"C"` pops
the last score, `"D"` pushes double the top, `"+"` pushes the sum of the top two,
and anything else is an integer literal to push. The answer is the sum of the
stack. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def calPoints(self, ops):
        stack = []
        for op in ops:
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
