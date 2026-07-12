# Next Greater Element II (Circular) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []  # indices, decreasing values
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and nums[stack[-1]] < cur:
                res[stack.pop()] = cur
            if i < n:
                stack.append(i)
        return res
```
