# Next Greater Element II — Solution

## Optimal Approach

Treat the array as circular by iterating over `2 * n` positions and indexing with
`i % n`. Keep a monotonic **decreasing** stack of indices whose answers are still
pending. When the current value is strictly greater than the value at the stack
top, that current value is the top's next greater element, so pop and record it.
Only push real indices on the first pass (`i < n`); the second pass merely resolves
elements that need to wrap around. Anything still on the stack at the end has no
greater value and stays `-1`.

### Reference implementation

```python
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []  # indices, values decreasing
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and nums[stack[-1]] < cur:
                res[stack.pop()] = cur
            if i < n:
                stack.append(i)
        return res
```
