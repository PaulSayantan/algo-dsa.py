# Design a Self-Sorting Stack — Solution

## Optimal Approach

Maintain a single list kept sorted so the smallest value is on top (last). On
`push(x)`, pop every element strictly smaller than `x` onto a temporary stack,
push `x`, then restore the temp elements — the sort-a-stack insertion step
applied per operation. `pop`/`peek` then read the top in O(1), returning `None`
when empty. Each `push` is O(n); the structure is fully sorted after every op.

### Reference implementation

```python
class SortedStack:
    def __init__(self):
        self._stack = []  # sorted so the smallest element is on top (last)

    def push(self, x):
        temp = []
        while self._stack and self._stack[-1] < x:
            temp.append(self._stack.pop())
        self._stack.append(x)
        while temp:
            self._stack.append(temp.pop())

    def pop(self):
        return self._stack.pop() if self._stack else None

    def peek(self):
        return self._stack[-1] if self._stack else None

    def isEmpty(self):
        return not self._stack
```
