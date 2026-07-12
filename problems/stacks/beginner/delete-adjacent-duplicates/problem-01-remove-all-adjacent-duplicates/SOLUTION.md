# Remove All Adjacent Duplicates In String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def removeDuplicates(self, s):
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
```
