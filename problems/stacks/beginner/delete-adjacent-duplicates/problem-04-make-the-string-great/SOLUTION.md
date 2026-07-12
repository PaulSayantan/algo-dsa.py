# Make The String Great — Solution

## Optimal Approach

Scan left to right with a stack. Before pushing the current character, check the
top: if they are the same letter in opposite cases (`abs(ord(a) - ord(b)) == 32`,
the ASCII gap between a letter's lower and upper forms), pop the top instead of
pushing — that removes the bad pair. What remains on the stack is the good string.

### Reference implementation

```python
class Solution:
    def makeGood(self, s):
        stack = []
        for c in s:
            if stack and stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
```
