# Insert an Element into a Sorted Stack — Solution

## Optimal Approach

Recurse until the top is at most `x` (or the stack is empty), push `x` there,
then push each held element back as the recursion unwinds. This keeps the stack
non-decreasing bottom-to-top. Time O(n), space O(n) recursion depth. It is the
inner primitive used by recursive stack sorting.

### Reference implementation

```python
class Solution:
    def sortedInsert(self, stack, x):
        stack = list(stack)
        self._insert(stack, x)
        return stack

    def _insert(self, stack, x):
        if not stack or stack[-1] <= x:
            stack.append(x)
            return
        top = stack.pop()
        self._insert(stack, x)
        stack.append(top)
```
