# Previous Smaller Element — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def previousSmaller(self, nums):
        res = []
        stack = []
        for x in nums:
            while stack and stack[-1] >= x:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(x)
        return res
```
