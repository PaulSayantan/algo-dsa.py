# Remove Duplicate Letters — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def removeDuplicateLetters(self, s):
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.discard(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
```
