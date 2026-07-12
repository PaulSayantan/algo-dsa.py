# Build a Cartesian Tree (Parent Array) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def cartesianParents(self, nums):
        n = len(nums)
        parent = [-1] * n
        stack = []  # indices, increasing values
        for i in range(n):
            last = -1
            while stack and nums[stack[-1]] > nums[i]:
                last = stack.pop()
            if last != -1:
                parent[last] = i
            if stack:
                parent[i] = stack[-1]
            stack.append(i)
        return parent
```
