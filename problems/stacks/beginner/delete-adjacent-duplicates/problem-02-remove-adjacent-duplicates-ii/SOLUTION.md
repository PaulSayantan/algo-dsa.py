# Remove All Adjacent Duplicates in String II — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def removeDuplicates(self, s, k):
        stack = []  # [char, count]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * cnt for c, cnt in stack)
```
