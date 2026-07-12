# Sort a Stack Using Recursion — Solution

## Optimal Approach

Pop the entire stack recursively down to empty. As the recursion unwinds, each
held value is re-inserted with a recursive `sortedInsert` that pushes deeper
elements aside until the correct slot is found. No explicit auxiliary container
is used — only the call stack. Time O(n²), space O(n) recursion depth.

### Reference implementation

```python
class Solution:
    def sortStack(self, stack):
        stack = list(stack)
        self._sort(stack)
        return stack

    def _sort(self, stack):
        if stack:
            top = stack.pop()
            self._sort(stack)
            self._insert(stack, top)

    def _insert(self, stack, x):
        # Insert x keeping the stack non-decreasing bottom-to-top.
        if not stack or stack[-1] <= x:
            stack.append(x)
            return
        top = stack.pop()
        self._insert(stack, x)
        stack.append(top)
```
