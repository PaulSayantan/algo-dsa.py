# Valid Parentheses — Solution

## Optimal Approach

Scan left to right. Openers are pushed onto a stack (a linked-list stack pushes
at the head in O(1)). Every closer must match the most recently seen opener —
exactly the value on top of the stack — so pop and compare. If the stack is
empty when a closer arrives, or a mismatch occurs, the string is invalid. A
valid string leaves the stack empty at the end.

### Reference implementation

```python
class Solution:
    def isValid(self, s):
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack
```
