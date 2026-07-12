# Nearest Smaller Values on Both Sides — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def nearestSmaller(self, nums):
        n = len(nums)
        left = [-1] * n
        right = [-1] * n
        stack = []
        for i in range(n):
            while stack and stack[-1] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return [[left[i], right[i]] for i in range(n)]
```
