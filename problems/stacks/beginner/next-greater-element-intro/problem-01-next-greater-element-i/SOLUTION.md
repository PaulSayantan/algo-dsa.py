# Next Greater Element I — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        nxt = {}
        stack = []
        for x in nums2:
            while stack and x > stack[-1]:
                nxt[stack.pop()] = x
            stack.append(x)
        return [nxt.get(x, -1) for x in nums1]
```
