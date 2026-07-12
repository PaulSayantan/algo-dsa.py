# Sort a Stack Using One Auxiliary Stack — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def sortStack(self, stack):
        stack = list(stack)
        temp = []
        while stack:
            cur = stack.pop()
            while temp and temp[-1] > cur:
                stack.append(temp.pop())
            temp.append(cur)
        return temp
```
