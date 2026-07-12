# Baseball Game — Solution

## Optimal Approach

Every operation touches only the most recent entries, so the record behaves as a
stack. Integers push a new head; `"C"` pops the head; `"D"` peeks the top and
pushes twice its value; `"+"` peeks the top two and pushes their sum. A
linked-list stack does each of these at the head in O(1). After the whole pass,
sum the remaining entries.

### Reference implementation

```python
class Solution:
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
```
