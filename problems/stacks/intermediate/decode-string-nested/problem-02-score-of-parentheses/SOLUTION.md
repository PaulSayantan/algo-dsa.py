# Score of Parentheses — Solution

## Optimal Approach

Treat the stack top as the running score of the frame we are currently inside.
A `(` opens a new frame (push `0`); a `)` closes the current frame: pop its
inner score `v` and add `max(2 * v, 1)` back into the parent — the `max` turns a
bare `()` (inner score `0`) into `1` while doubling any non-empty frame.

### Reference implementation

```python
class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]  # stack[-1] = score accumulated in the current frame
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += max(2 * inner, 1)
        return stack[0]
```
