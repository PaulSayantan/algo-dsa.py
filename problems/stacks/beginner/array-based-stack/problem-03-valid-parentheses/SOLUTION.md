# Valid Parentheses — Solution

## Optimal Approach

Scan left to right. Push every opening bracket. When you meet a closing bracket,
the stack must be non-empty and its top must be the matching opener; pop it.
At the end the stack must be empty. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def isValid(self, s):
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
```
