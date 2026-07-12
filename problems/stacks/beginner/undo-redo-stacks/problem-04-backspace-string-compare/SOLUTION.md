# Backspace String Compare — Solution

## Optimal Approach

Typing into an editor is a stack: a letter pushes, and a backspace `'#'` is an
**undo** that pops the most recently typed character (or does nothing if the
buffer is already empty). Rebuild each string by replaying its keystrokes onto a
stack, then compare the two resulting stacks for equality.

### Reference implementation

```python
class Solution:
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []
            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        return build(s) == build(t)
```
