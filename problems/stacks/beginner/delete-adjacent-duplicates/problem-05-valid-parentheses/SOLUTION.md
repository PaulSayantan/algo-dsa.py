# Valid Parentheses — Solution

## Optimal Approach

Push every opening bracket. On a closing bracket, the most recent unmatched
opener must be its partner — so check the stack top: if it matches, pop it (the
pair cancels, just like collapsing an adjacent duplicate); otherwise the string
is invalid. After the scan, the string is valid only if nothing is left unmatched.

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
