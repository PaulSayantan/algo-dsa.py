# Removing Stars From a String — Solution

## Optimal Approach

Scan left to right pushing letters onto a stack. Each `'*'` is a left-moving
annihilator that destroys the survivor on top, so it pops one letter. What
remains on the stack, read bottom-to-top, is the answer.

### Reference implementation

```python
class Solution:
    def removeStars(self, s):
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
```
