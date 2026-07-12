# Next Greater Element II — Solution

## Optimal Approach

Use a monotonic decreasing stack of indices and iterate `2n` times, indexing
with `i % n` to simulate the circular wrap-around. Whenever the current value is
greater than the value at the stack's top index, that top has found its next
greater element — pop and record it. Only push real indices during the first `n`
iterations; the second pass just resolves entries that wrap around. Each index
is pushed once and popped at most once, so the pass is O(n) time and O(n) space.

### Reference implementation

```python
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []  # indices with strictly decreasing values
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)
        return res
```
